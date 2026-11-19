"""Find savings in agent session logs.

Reads agent sessions in the DataClaw export format (one JSON object per session with
`messages`, `stats`, `model`, `source`, `start_time`). A customer can produce the same file from
their own OpenClaw, Hermes, Claude Code or Codex history with `dataclaw export --no-push`, which
also redacts secrets, so this script never reads raw agent folders.

Stages (each can be the last):

1. parse: one row per session with its job key, model, tokens and final message.
2. jobs: group sessions into jobs, flag each unattended or interactive, rank by spend, project a
   month. Sends nothing.
3. replay: for unattended jobs whose last message is a decision (the agent either stays quiet with
   NO_REPLY or writes a report), send the recorded prompt and tool results to the cheapest
   endpoints on the route list and compare the decision. Strings only. No model output is run.

Everything that holds log text or model output is written under packets/agentlogs/ (git ignores
it). Only counts, token totals and costs go to data/agentlogs/<date>/.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import random
import re
import sys
import threading
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

from probe import BUDGET_USD, openrouter
from probe import routine
from probe import run as run_mod

WORK_DIR = Path("packets/agentlogs")
OUT_DIR = Path("data/agentlogs")
HARD_CEILING = 3.00
SEED = 20261119
MAX_JOBS = 5
MAX_SAMPLES = 20
MIN_SESSIONS = 10
TOOL_OUTPUT_CHARS = 3000
REPLY_MAX_TOKENS = 1200
HOURS_PER_MONTH = 730.0
NO_REPLY = "NO_REPLY"

CRON_RE = re.compile(r"^\s*\[cron:([0-9a-fA-F-]+)\s*([^\]]*)\]")
MASKS = [
    (re.compile(r"https?://\S+"), "<url>"),
    (re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F-]{27,}\b"), "<uuid>"),
    (re.compile(r"\b\d{4}-\d{2}-\d{2}[T ]?[\d:.]*Z?\b"), "<date>"),
    (re.compile(r"(?:/[\w.~-]+){2,}"), "<path>"),
    (re.compile(r"\b[0-9a-fA-F]{12,}\b"), "<hex>"),
    (re.compile(r"\d+(?:\.\d+)?"), "<n>"),
    (re.compile(r"\s+"), " "),
]
PREFIXES = ("google-antigravity/", "openclaw/")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------------------
# Stage 1: parse
# ---------------------------------------------------------------------------

def _text(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    return json.dumps(v, ensure_ascii=False)


def _tool_uses(m: dict[str, Any]) -> list[dict[str, Any]]:
    tu = m.get("tool_uses")
    if isinstance(tu, list):
        return [t for t in tu if isinstance(t, dict)]
    return []


def mask(text: str) -> str:
    out = text
    for rx, rep in MASKS:
        out = rx.sub(rep, out)
    return out.strip()[:160]


def job_key(first_user: str) -> tuple[str, str, bool]:
    """(key, display name, is_cron) for a session's first user message."""
    m = CRON_RE.match(first_user)
    if m:
        name = m.group(2).strip() or m.group(1)[:8]
        return f"cron:{m.group(1)}", name, True
    shape = mask(first_user)
    return "tpl:" + hashlib.sha1(shape.encode("utf-8")).hexdigest()[:12], shape[:60], False


def parse_session(row: dict[str, Any], origin: str) -> dict[str, Any] | None:
    msgs = row.get("messages") or []
    users = [m for m in msgs if m.get("role") == "user"]
    if not users:
        return None
    first = _text(users[0].get("content"))
    key, name, cron = job_key(first)
    stats = row.get("stats") or {}
    tin, tout = int(stats.get("input_tokens") or 0), int(stats.get("output_tokens") or 0)
    estimated = False
    if tin == 0 and tout == 0:
        # Some exports carry no token counts. Estimate from the visible text (chars / 4). This
        # leaves out the system prompt, so it is a floor.
        chars_in = sum(len(_text(m.get("content"))) for m in users)
        chars_out = 0
        for m in msgs:
            if m.get("role") == "assistant":
                chars_out += len(_text(m.get("content"))) + len(_text(m.get("thinking")))
                chars_in += sum(len(_text(t.get("output"))) for t in _tool_uses(m))
        tin, tout, estimated = chars_in // 4, chars_out // 4, True
    finals = [m for m in msgs if m.get("role") == "assistant" and _text(m.get("content")).strip()]
    final = _text(finals[-1].get("content")).strip() if finals else ""
    tools = [t for m in msgs if m.get("role") == "assistant" for t in _tool_uses(m)]
    return {
        "origin": origin, "session_id": row.get("session_id"), "source": row.get("source") or "unknown",
        "model": row.get("model") or "unknown", "start": row.get("start_time"), "job": key, "job_name": name,
        "cron": cron, "user_turns": len(users), "tool_calls": len(tools), "input_tokens": tin,
        "output_tokens": tout, "tokens_estimated": estimated, "final": final,
        "decision": (NO_REPLY if final == NO_REPLY else ("report" if final else "none")),
        "_first_user": first, "_tools": tools,
    }


def origin_of(path: str) -> str:
    """Dataset name for a file: the folder for dated part files (hermes/2026-04-09.jsonl), else the file."""
    p = Path(path)
    return p.parent.name if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem) else p.stem


def load(paths: list[str]) -> list[dict[str, Any]]:
    sessions: list[dict[str, Any]] = []
    for pattern in paths:
        for p in sorted(glob.glob(pattern)):
            with open(p, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    s = parse_session(json.loads(line), origin_of(p))
                    if s:
                        sessions.append(s)
    return sessions


# ---------------------------------------------------------------------------
# Stage 2: jobs
# ---------------------------------------------------------------------------

def _ts(v: str | None) -> datetime | None:
    if not v:
        return None
    try:
        d = datetime.fromisoformat(v.replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def price_table(fetch: bool = True, client: httpx.Client | None = None) -> dict[str, tuple[float, float]]:
    """OpenRouter list prices per token, keyed by model id. Empty when not fetched."""
    if not fetch:
        return {}
    c = client or httpx.Client(timeout=60.0)
    r = c.get(f"{openrouter.BASE}/models")
    r.raise_for_status()
    out = {}
    for m in r.json().get("data", []):
        p = m.get("pricing") or {}
        try:
            out[m["id"]] = (float(p.get("prompt") or 0), float(p.get("completion") or 0))
        except (TypeError, ValueError):
            continue
    return out


def _norm_model(name: str) -> str:
    n = name.lower()
    for p in PREFIXES:
        if n.startswith(p):
            n = n[len(p):]
    n = re.sub(r"-(thinking|highspeed|\d{8})$", "", n)
    n = re.sub(r"(\d)-(\d)", r"\1.\2", n)
    return n.split("/")[-1]


def match_price(model: str, prices: dict[str, tuple[float, float]]) -> tuple[str | None, tuple[float, float] | None]:
    want = _norm_model(model)
    for mid, pr in prices.items():
        if ":" in mid:
            continue
        if mid.split("/")[-1].lower() == want:
            return mid, pr
    return None, None


def build_jobs(sessions: list[dict[str, Any]], prices: dict[str, tuple[float, float]]) -> list[dict[str, Any]]:
    by_job: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for s in sessions:
        by_job[f"{s['origin']}|{s['job']}"].append(s)
    jobs = []
    for key, ss in by_job.items():
        n = len(ss)
        cron = any(s["cron"] for s in ss)
        single_turn = sum(1 for s in ss if s["user_turns"] == 1)
        unattended = cron or (n >= 3 and single_turn / n >= 0.8)
        tin = sum(s["input_tokens"] for s in ss)
        tout = sum(s["output_tokens"] for s in ss)
        cost = 0.0
        priced = True
        models = Counter(s["model"] for s in ss)
        for s in ss:
            _, pr = match_price(s["model"], prices)
            if pr is None:
                priced = False
                continue
            cost += s["input_tokens"] * pr[0] + s["output_tokens"] * pr[1]
        times = sorted(t for t in (_ts(s["start"]) for s in ss) if t)
        hours = (times[-1] - times[0]).total_seconds() / 3600 if len(times) > 1 else 0.0
        # Only scheduled jobs are projected. Batch pipelines run in bursts, so their rate over a
        # short window says nothing about a month.
        per_month = (n - 1) / hours * HOURS_PER_MONTH if hours >= 1 and cron else None
        decisions = Counter(s["decision"] for s in ss)
        jobs.append({
            "key": key, "origin": ss[0]["origin"], "job": ss[0]["job"], "name": ss[0]["job_name"],
            "kind": "unattended" if unattended else "interactive", "cron": cron, "sessions": n,
            "models": dict(models), "input_tokens": tin, "output_tokens": tout,
            "tokens_estimated": any(s["tokens_estimated"] for s in ss),
            "cost_usd": round(cost, 4) if prices else None, "all_priced": priced if prices else False,
            "window_hours": round(hours, 2), "runs_per_month": round(per_month) if per_month else None,
            "cost_per_month_usd": (round(cost / n * per_month, 2) if per_month and prices and priced else None),
            "decisions": dict(decisions),
            "gradable": unattended and decisions.get(NO_REPLY, 0) > 0 and decisions.get("report", 0) > 0,
        })
    jobs.sort(key=lambda j: (-(j["input_tokens"] + 4 * j["output_tokens"])))
    return jobs


def shares(jobs: list[dict[str, Any]]) -> dict[str, Any]:
    def w(j: dict[str, Any]) -> int:
        return j["input_tokens"] + 4 * j["output_tokens"]
    total = sum(w(j) for j in jobs) or 1
    un = sum(w(j) for j in jobs if j["kind"] == "unattended")
    by_origin: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "unattended": 0, "sessions": 0})
    for j in jobs:
        o = by_origin[j["origin"]]
        o["total"] += w(j)
        o["sessions"] += j["sessions"]
        if j["kind"] == "unattended":
            o["unattended"] += w(j)
    return {
        "weighted_tokens": total, "unattended_share": round(un / total, 4),
        "by_origin": {k: {**v, "unattended_share": round(v["unattended"] / (v["total"] or 1), 4)} for k, v in by_origin.items()},
        "note": "Spend weight is input tokens plus 4 times output tokens, so models with no price still count.",
    }


def _fmt_tok(n: int) -> str:
    return f"{n / 1e6:.1f}M" if n >= 1e6 else f"{n / 1e3:.0f}k"


def summary_md(jobs: list[dict[str, Any]], sh: dict[str, Any], names: bool) -> str:
    """names=False gives an aggregate view safe to commit (no job names, no text)."""
    lines = ["# Agent log savings: jobs", "", f"- Written: {now_iso()}",
             f"- Unattended share of spend weight: {sh['unattended_share']:.0%}", ""]
    lines += ["| Source file | Sessions | Unattended share |", "| --- | --- | --- |"]
    for o, v in sh["by_origin"].items():
        lines.append(f"| {o} | {v['sessions']} | {v['unattended_share']:.0%} |")
    lines += ["", "## Top 10 jobs", "",
              "| # | Job | Kind | Sessions | Input | Output | Cost seen | Runs a month | Cost a month | Gradable |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for i, j in enumerate(jobs[:10], 1):
        label = j["name"] if names else j["job"]
        cost = "n/a" if j["cost_usd"] is None or not j["all_priced"] else f"${j['cost_usd']:,.2f}"
        cpm = "n/a" if j["cost_per_month_usd"] is None else f"${j['cost_per_month_usd']:,.0f}"
        lines.append(f"| {i} | {label} | {j['kind']} | {j['sessions']} | {_fmt_tok(j['input_tokens'])}"
                     f"{' est' if j['tokens_estimated'] else ''} | {_fmt_tok(j['output_tokens'])} | {cost} | "
                     f"{j['runs_per_month'] or 'n/a'} | {cpm} | {'yes' if j['gradable'] else 'no'} |")
    lines += ["", "Cost seen uses OpenRouter list prices for the recorded model. Runs a month projects the observed "
              "rate over the observed window, for scheduled (cron) jobs only. Gradable means the job's last message is a "
              "decision (NO_REPLY or a report) that a string check can compare.", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Stage 3: replay
# ---------------------------------------------------------------------------

SYSTEM = (
    "You are an always-on assistant agent. A scheduled job has run and its tool calls have already "
    "returned. Read the job instructions and the tool results, then write the final message for the "
    "user. If the instructions say to stay quiet when nothing needs reporting and nothing needs "
    f"reporting, reply with exactly {NO_REPLY} and nothing else. Do not call tools."
)


def replay_prompt(s: dict[str, Any]) -> str:
    parts = ["Job instructions:", s["_first_user"].strip(), "", "Tool results:"]
    for i, t in enumerate(s["_tools"], 1):
        inp = _text(t.get("input"))[:600]
        out = _text(t.get("output"))[:TOOL_OUTPUT_CHARS]
        parts += [f"[{i}] {t.get('tool', 'tool')} {inp}", out, ""]
    parts.append("Write the final message now.")
    return "\n".join(parts)


def decision_of(text: str) -> str:
    t = (text or "").strip().strip("`").strip()
    return NO_REPLY if t == NO_REPLY or t.upper().startswith(NO_REPLY) else ("report" if t else "none")


def pick_samples(jobs: list[dict[str, Any]], sessions: list[dict[str, Any]],
                 max_jobs: int = MAX_JOBS, max_samples: int = MAX_SAMPLES) -> list[dict[str, Any]]:
    chosen = [j for j in jobs if j["gradable"] and j["sessions"] >= MIN_SESSIONS][:max_jobs]
    out = []
    for j in chosen:
        pool = [s for s in sessions if f"{s['origin']}|{s['job']}" == j["key"] and s["decision"] in (NO_REPLY, "report")
                and s["_tools"]]
        rng = random.Random(f"{SEED}:{j['key']}")
        # Keep both decisions in the sample so a target that always stays quiet cannot pass.
        quiet = [s for s in pool if s["decision"] == NO_REPLY]
        loud = [s for s in pool if s["decision"] == "report"]
        rng.shuffle(quiet)
        rng.shuffle(loud)
        half = max_samples // 2
        take = quiet[:half] + loud[:max_samples - min(half, len(quiet))]
        out += [{"job_key": j["key"], "job": j["job"], "session": s} for s in take[:max_samples]]
    return out


def estimate(prompt: str, target: dict[str, Any]) -> tuple[float, float]:
    tin = len(SYSTEM + prompt) // 4 + 50
    expected = tin * target["price_in"] + 300 * target["price_out"]
    worst = tin * routine.RESERVE_MARGIN * target["price_in"] + REPLY_MAX_TOKENS * target["price_out"]
    return expected, worst


def send(samples: list[dict[str, Any]], targets: list[dict[str, Any]], cap: routine.HardCap, out_path: Path,
         run_id: str, completer=openrouter.complete) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    lock = threading.Lock()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    def work(item: tuple[dict[str, Any], dict[str, Any]]) -> dict[str, Any]:
        smp, t = item
        s = smp["session"]
        prompt = replay_prompt(s)
        _, worst = estimate(prompt, t)
        row: dict[str, Any] = {"run_id": run_id, "ts": now_iso(), "job": smp["job"], "job_key": smp["job_key"],
                               "session_id": s["session_id"], "model": t["label"], "slug": t["slug"],
                               "pinned_tag": t["tag"], "expected": s["decision"]}
        if not cap.reserve(worst):
            row.update({"status": "skipped_budget", "output": "", "cost_usd": 0.0, "got": "none", "passed": False})
        else:
            res = completer(t["slug"], t["tag"], [{"role": "system", "content": SYSTEM},
                                                  {"role": "user", "content": prompt}],
                            {"max_tokens": REPLY_MAX_TOKENS}, reasoning_modes=routine.DEFAULT_REASONING)
            cost, source = run_mod.row_cost(res, t)
            cap.settle(worst, cost)
            got = decision_of(res.get("text") or "") if res["status"] == "ok" else "none"
            row.update({"status": res["status"], "output": res.get("text") or "", "usage": res.get("usage") or {},
                        "cost_usd": round(cost, 6), "cost_source": source, "returned_provider": res.get("provider"),
                        "got": got, "passed": res["status"] == "ok" and got == s["decision"]})
        with lock:
            rows.append(row)
            with out_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return row

    items = [(smp, t) for smp in samples for t in targets]
    with ThreadPoolExecutor(max_workers=min(routine.MAX_WORKERS, run_mod.concurrency())) as ex:
        for fut in as_completed([ex.submit(work, it) for it in items]):
            fut.result()
    return rows


def replay_summary(rows: list[dict[str, Any]], jobs: list[dict[str, Any]],
                   targets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key = {j["key"]: j for j in jobs}
    out = []
    for (jk, model), rs in sorted(_group(rows).items()):
        j = by_key[jk]
        t = next(x for x in targets if x["label"] == model)
        sent = [r for r in rs if r["status"] != "skipped_budget"]
        ok = [r for r in sent if r["passed"]]
        per_run = (j["input_tokens"] / j["sessions"]) * t["price_in"] + (j["output_tokens"] / j["sessions"]) * t["price_out"]
        out.append({"job": j["job"], "model": model, "tag": t["tag"], "sent": len(sent), "passed": len(ok),
                    "pass_rate": round(len(ok) / len(sent), 3) if sent else None,
                    "now_per_month_usd": j["cost_per_month_usd"],
                    "option_per_month_usd": round(per_run * j["runs_per_month"], 2) if j["runs_per_month"] else None,
                    "billed_usd": round(sum(r["cost_usd"] for r in rs), 4)})
    return out


def _group(rows: list[dict[str, Any]]) -> dict[tuple[str, str], list[dict[str, Any]]]:
    g: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        g[(r["job_key"], r["model"])].append(r)
    return g


def report_md(record: dict[str, Any], summ: list[dict[str, Any]], names: dict[str, str], bar: float) -> str:
    lines = ["# Agent log savings: replay", "", f"- Run: {record['run_id']} ({record['source']})",
             f"- Billed: ${record['total_billed_usd']:.4f} of a ${record['cap_usd']:.2f} cap. "
             f"Rows skipped for budget: {record['skipped_budget']}.",
             f"- Pass bar: {bar:.0%} of sampled runs make the same decision as the original model.", "",
             "| Job | Option | Endpoint | Sent | Same decision | Cost a month now | Cost a month on option | Verdict |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for s in summ:
        now = "n/a" if s["now_per_month_usd"] is None else f"${s['now_per_month_usd']:,.0f}"
        opt = "n/a" if s["option_per_month_usd"] is None else f"${s['option_per_month_usd']:,.0f}"
        rate = "n/a" if s["pass_rate"] is None else f"{s['passed']}/{s['sent']} ({s['pass_rate']:.0%})"
        verdict = "n/a" if s["pass_rate"] is None else ("pass" if s["pass_rate"] >= bar else "fail")
        lines.append(f"| {names.get(s['job'], s['job'])} | {s['model']} | {s['tag']} | {s['sent']} | {rate} | {now} | {opt} | {verdict} |")
    lines += ["", "The replay sends the recorded job instructions and tool results, without the agent's own system "
              "prompt, which the export does not include. The cost on an option uses the recorded token counts, "
              "so it assumes the same context is sent. The decision check is a string comparison: stay quiet "
              f"({NO_REPLY}) or write a report.", ""]
    return "\n".join(lines)


def agentlogs_billed(date: str, out_dir: Path = OUT_DIR) -> float:
    total = 0.0
    for p in sorted(out_dir.glob(f"{date}*/run.json")):
        try:
            total += float(json.loads(p.read_text(encoding="utf-8")).get("total_billed_usd") or 0.0)
        except (json.JSONDecodeError, ValueError):
            continue
    return round(total, 4)


def effective_cap(requested: float, date: str) -> float:
    night = routine.night_billed(date)
    prior = routine.routine_billed(date) + agentlogs_billed(date)
    return round(max(0.0, min(requested, HARD_CEILING - agentlogs_billed(date), BUDGET_USD - night - prior)), 4)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("inputs", nargs="+", help="DataClaw conversations.jsonl files or globs")
    ap.add_argument("--stop-after", choices=["parse", "jobs", "replay"], default="jobs")
    ap.add_argument("--date", default="", help="Night the replay is attached to (UTC). Blank: latest run record.")
    ap.add_argument("--cap", type=float, default=routine.DEFAULT_CAP)
    ap.add_argument("--bar", type=float, default=0.9)
    ap.add_argument("--source", default="local", choices=["local", "dispatch"])
    ap.add_argument("--no-prices", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="Estimate the replay and send nothing")
    a = ap.parse_args(argv)

    sessions = load(a.inputs)
    print(f"parsed {len(sessions)} sessions from {len(a.inputs)} input(s)")
    if a.stop_after == "parse" or not sessions:
        return 0

    prices = price_table(fetch=not a.no_prices)
    jobs = build_jobs(sessions, prices)
    sh = shares(jobs)
    work = WORK_DIR / "out"
    work.mkdir(parents=True, exist_ok=True)
    (work / "jobs.json").write_text(json.dumps({"shares": sh, "jobs": jobs}, indent=1, ensure_ascii=False), encoding="utf-8")
    (work / "summary.md").write_text(summary_md(jobs, sh, names=True), encoding="utf-8")
    print(summary_md(jobs, sh, names=False))
    if a.stop_after == "jobs":
        return 0

    date = a.date or max((p.parent.name for p in routine.RUNS_DIR.glob("*/run.json")), default="")
    if not date:
        print("no nightly run record found; refusing to replay")
        return 1
    samples = pick_samples(jobs, sessions)
    if not samples:
        print("no gradable unattended job with enough sessions; nothing to replay")
        return 0
    targets = routine.lane_targets(hosts=1, outside=False)
    cap_usd = effective_cap(a.cap, date)
    exp = sum(estimate(replay_prompt(s["session"]), t)[0] for s in samples for t in targets)
    print(f"replay: {len(samples)} samples x {len(targets)} targets, expected ${exp:.4f}, cap ${cap_usd:.2f} (date {date})")
    if a.dry_run:
        return 0

    run_id = f"agentlogs-{date}-{datetime.now(timezone.utc).strftime('%H%M%S')}"
    rows = send(samples, targets, routine.HardCap(cap_usd), work / "responses.jsonl", run_id)
    summ = replay_summary(rows, jobs, targets)
    billed = round(sum(r["cost_usd"] for r in rows), 4)
    record = {"run_id": run_id, "source": a.source, "date": date, "written": now_iso(), "cap_usd": cap_usd,
              "total_billed_usd": billed, "skipped_budget": sum(1 for r in rows if r["status"] == "skipped_budget"),
              "inputs": [Path(p).name for p in a.inputs], "targets": [{k: t[k] for k in ("label", "slug", "tag")} for t in targets],
              "bar": a.bar, "unattended_share": sh["unattended_share"], "results": summ}
    names = {j["job"]: j["name"] for j in jobs}
    (work / "report.md").write_text(report_md(record, summ, names, a.bar), encoding="utf-8")
    out = OUT_DIR / date
    out.mkdir(parents=True, exist_ok=True)
    (out / "run.json").write_text(json.dumps(record, indent=1), encoding="utf-8")
    print(report_md(record, summ, {}, a.bar))
    return 0


if __name__ == "__main__":
    sys.exit(main())
