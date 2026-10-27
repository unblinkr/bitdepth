"""Nightly run.

    python -m probe.run --date YYYY-MM-DD [--dry-run] [--source live|dispatch|local] [--selfcheck]

Steps: resolve the models, list endpoints, build the prompt set, estimate cost and
apply the cap, send every kept prompt to every endpoint at concurrency 4, write rows as
they return, and write run.json. The cap is enforced twice: on the estimate before
anything is sent, and at run time from billed cost.
"""

from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from probe import BUDGET_USD, CONCURRENCY, MAX_TOKENS, MODELS, SEED
from probe import budget as budget_mod
from probe import openrouter
from probe.generators import FIXED_PATH, fresh_set, load_jsonl, write_jsonl

MIN_ENDPOINTS = 6
SELFCHECK_PROMPTS = 12
SELFCHECK_WAIT_SECONDS = 3600


def runs_dir(date: str) -> Path:
    return Path("data/runs") / date


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def resolve_models(lister=openrouter.list_endpoints) -> dict[str, dict[str, Any]]:
    """Return {label: {slug, endpoints, short}} for every configured model."""
    out: dict[str, dict[str, Any]] = {}
    for m in MODELS:
        eps = lister(m["slug"])
        out[m["label"]] = {
            "slug": m["slug"],
            "endpoints": eps,
            "short": len(eps) < MIN_ENDPOINTS,
        }
    return out


def _norm(s: str | None) -> str:
    return (s or "").strip().lower()


def row_cost(result: dict[str, Any], endpoint: dict[str, Any]) -> tuple[float, str]:
    usage = result.get("usage") or {}
    if isinstance(usage.get("cost"), (int, float)):
        return float(usage["cost"]), "usage"
    pt = usage.get("prompt_tokens") or 0
    ct = usage.get("completion_tokens") or 0
    return pt * endpoint["price_in"] + ct * endpoint["price_out"], "estimated"


def make_row(
    run_id: str, label: str, slug: str, endpoint: dict[str, Any], prompt: dict[str, Any], result: dict[str, Any]
) -> dict[str, Any]:
    cost, cost_source = row_cost(result, endpoint)
    status = result["status"]
    misrouted = False
    returned = result.get("provider")
    if status == "ok" and returned and _norm(returned) != _norm(endpoint["provider_name"]):
        misrouted = True
        status = "misrouted"
    return {
        "run_id": run_id,
        "ts": now_iso(),
        "model": label,
        "slug": slug,
        "prompt_id": prompt["id"],
        "family": prompt["family"],
        "pinned_tag": endpoint["tag"],
        "pinned_provider": endpoint["provider_name"],
        "returned_provider": returned,
        "status": status,
        "misrouted": misrouted,
        "declared_quantization": endpoint["quantization"],
        "seed_supported": "seed" in endpoint["supported_parameters"],
        "request_params": {"temperature": 0, "top_p": 1, "seed": SEED, "max_tokens": MAX_TOKENS,
                           "reasoning_mode": result.get("reasoning_mode")},
        "output": result.get("text") or "",
        "usage": result.get("usage") or {},
        "latency_ms": result.get("latency_ms"),
        "finish_reason": result.get("finish_reason"),
        "error": result.get("error") or "",
        "cost_usd": round(cost, 6),
        "cost_source": cost_source,
    }


class Spend:
    """Thread-safe running total with a hard stop."""

    def __init__(self, cap: float) -> None:
        self.cap = cap
        self.total = 0.0
        self.stopped = False
        self._lock = threading.Lock()

    def add(self, usd: float) -> None:
        with self._lock:
            self.total += usd
            if self.total >= self.cap:
                self.stopped = True

    def allow(self) -> bool:
        with self._lock:
            return not self.stopped


def send_all(
    run_id: str,
    models: dict[str, dict[str, Any]],
    prompts: list[dict[str, Any]],
    out_path: Path,
    spend: Spend,
    completer=openrouter.complete,
    extra: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Send every prompt to every endpoint, prompts outer so a budget stop leaves every
    endpoint with the same prompts done. Rows are appended to out_path as they return."""
    jobs: list[tuple[str, str, dict[str, Any], dict[str, Any]]] = []
    for p in prompts:
        for label, m in models.items():
            for e in m["endpoints"]:
                jobs.append((label, m["slug"], e, p))

    rows: list[dict[str, Any]] = []
    write_lock = threading.Lock()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    def work(job: tuple[str, str, dict[str, Any], dict[str, Any]]) -> dict[str, Any]:
        label, slug, e, p = job
        if not spend.allow():
            result = {"status": "skipped_budget", "error": "runtime budget stop", "text": "", "provider": None,
                      "usage": {}, "latency_ms": 0, "finish_reason": None, "reasoning_mode": None}
        else:
            result = completer(slug, e["tag"], [{"role": "user", "content": p["prompt"]}])
        row = make_row(run_id, label, slug, e, p, result)
        if extra:
            row.update(extra)
        if row["status"] != "skipped_budget":
            spend.add(row["cost_usd"])
        with write_lock:
            rows.append(row)
            with out_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            n = len(rows)
            if n % 100 == 0 or n == len(jobs):
                print(f"  {n}/{len(jobs)} rows, spend ${spend.total:.4f}", flush=True)
        return row

    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futures = [ex.submit(work, j) for j in jobs]
        for fut in as_completed(futures):
            fut.result()
    return rows


def summarise(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_status: dict[str, int] = {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    truncated = sum(1 for r in rows if r["status"] == "ok" and r.get("finish_reason") == "length")
    return {
        "rows": len(rows),
        "by_status": by_status,
        "errors": by_status.get("error", 0),
        "misrouted": by_status.get("misrouted", 0),
        "skipped_budget": by_status.get("skipped_budget", 0),
        "truncated": truncated,
        "billed_cost_usd": round(sum(r["cost_usd"] for r in rows), 4),
        "estimated_cost_rows": sum(1 for r in rows if r["cost_source"] == "estimated" and r["status"] in ("ok", "misrouted")),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--source", choices=["live", "dispatch", "local"], default="local")
    ap.add_argument("--selfcheck", action="store_true")
    ap.add_argument("--selfcheck-wait", type=int, default=SELFCHECK_WAIT_SECONDS)
    args = ap.parse_args(argv)

    rd = runs_dir(args.date)
    run_json = rd / "run.json"
    if run_json.exists() and not args.dry_run:
        print(f"run exists for {args.date}, skipping")
        return 0

    started = now_iso()
    models = resolve_models()
    print("resolved models:")
    for label, m in models.items():
        quants: dict[str, int] = {}
        for e in m["endpoints"]:
            quants[e["quantization"]] = quants.get(e["quantization"], 0) + 1
        short = " (fewer than six endpoints)" if m["short"] else ""
        print(f"  {label}: {m['slug']} with {len(m['endpoints'])} endpoints{short}; declared quantization {quants}")

    if not FIXED_PATH.exists():
        print(f"{FIXED_PATH} is missing; run python -m probe.generators --write-fixed first")
        return 2
    fixed = load_jsonl(FIXED_PATH)
    fresh = fresh_set(args.date)
    prompts = fixed + fresh
    endpoints_by_model = {label: m["endpoints"] for label, m in models.items()}
    kept, dropped, est, aborted = budget_mod.apply_cap(endpoints_by_model, prompts)

    print(f"prompts: {len(fixed)} fixed + {len(fresh)} fresh = {len(prompts)}; kept {len(kept)}, dropped {len(dropped)}")
    print(f"estimate: ${est['usd']:.4f} (cap ${BUDGET_USD:.2f}) per model {est['per_model']}; "
          f"{est['input_tokens_per_endpoint']} input and {est['output_tokens_per_endpoint']} output tokens per endpoint")
    if dropped:
        fams: dict[str, int] = {}
        for p in dropped:
            fams[p["family"]] = fams.get(p["family"], 0) + 1
        print(f"dropped for budget: {fams}")

    if args.dry_run:
        print("endpoint estimate table (USD):")
        for e in sorted(est["per_endpoint"], key=lambda x: -x["usd"]):
            print(f"  {e['model']:<16} {e['tag']:<32} {e['usd']:.4f}")
        if aborted:
            print("ABORT: estimate exceeds the cap after dropping needle and fresh prompts")
        return 0

    rd.mkdir(parents=True, exist_ok=True)
    with (rd / "endpoints.json").open("w", encoding="utf-8") as f:
        json.dump({"date": args.date, "fetched": started, "models": models}, f, indent=1, ensure_ascii=False)

    run_id = f"{args.date}-{args.source}"
    record: dict[str, Any] = {
        "run_id": run_id,
        "date": args.date,
        "source": args.source,
        "started": started,
        "models": {label: {"slug": m["slug"], "endpoints": len(m["endpoints"]), "short": m["short"]} for label, m in models.items()},
        "prompts": {"fixed": len(fixed), "fresh": len(fresh), "kept": len(kept), "dropped": len(dropped)},
        "dropped_prompt_ids": [p["id"] for p in dropped],
        "estimate": {"usd": est["usd"], "per_model": est["per_model"]},
        "cap_usd": BUDGET_USD,
        "aborted_on_estimate": aborted,
    }
    if aborted:
        record["finished"] = now_iso()
        record["summary"] = {"rows": 0, "billed_cost_usd": 0.0}
        with run_json.open("w", encoding="utf-8") as f:
            json.dump(record, f, indent=1)
        print("ABORT: estimate exceeds the cap after dropping needle and fresh prompts; nothing sent")
        return 0

    write_jsonl(rd / "prompts.jsonl", kept)
    spend = Spend(BUDGET_USD)
    print(f"sending {len(kept)} prompts to {sum(len(m['endpoints']) for m in models.values())} endpoints at concurrency {CONCURRENCY}")
    rows = send_all(run_id, models, kept, rd / "responses.jsonl", spend)
    record["summary"] = summarise(rows)
    record["runtime_budget_stop"] = spend.stopped

    if args.selfcheck and not spend.stopped:
        sc_prompts = fixed[:SELFCHECK_PROMPTS]
        sc_path = rd / "selfcheck.jsonl"
        print(f"self-check pass A: {len(sc_prompts)} prompts")
        rows_a = send_all(run_id, models, sc_prompts, sc_path, spend, extra={"pass": "A"})
        print(f"waiting {args.selfcheck_wait} seconds before pass B")
        time.sleep(args.selfcheck_wait)
        print("self-check pass B")
        rows_b = send_all(run_id, models, sc_prompts, sc_path, spend, extra={"pass": "B"})
        record["selfcheck"] = {
            "prompts": len(sc_prompts),
            "wait_seconds": args.selfcheck_wait,
            "pass_a": summarise(rows_a),
            "pass_b": summarise(rows_b),
        }
        record["runtime_budget_stop"] = spend.stopped

    record["finished"] = now_iso()
    record["total_billed_usd"] = round(spend.total, 4)
    with run_json.open("w", encoding="utf-8") as f:
        json.dump(record, f, indent=1)
    print(f"done: {record['summary']['rows']} rows, billed ${spend.total:.4f}, run.json written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
