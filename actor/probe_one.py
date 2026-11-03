"""One on-demand probe of one endpoint, graded against last night's reference.

Used by the Apify actor (actor/main.py). Reuses the nightly code unchanged:
probe.run.send_all sends the prompts, probe.score.build_reference and
probe.score.endpoint_metrics grade them. Nothing here writes to data/.

The reference comes from the latest night in the public repo: the same fixed
prompts, the reference output per prompt built from that night's endpoints by
the nightly's own rule. Fresh prompts are not used because their reference
exists only for the night they were sent.
"""

from __future__ import annotations

import ipaddress
import socket
import time
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

import httpx

from probe import MAX_TOKENS, MODELS, SEED
from probe import openrouter
from probe.run import Spend, now_iso, send_all
from probe.score import build_reference, endpoint_metrics

RAW = "https://raw.githubusercontent.com/unblinkr/bitdepth/main/data"
SPEND_CAP_USD = 1.00          # hard stop for one probe on Bitdepth's OpenRouter key
MIN_OK_SHARE = 0.5            # below this share of answered prompts the probe is not charged
FOOTER = "Numbers against a stated reference. Not a claim about intent."
METHOD_URL = "https://bitdepth.dev/method"
GRADED = {m["slug"]: m["label"] for m in MODELS}
FAMILIES = ["math", "json", "string", "needle", "echo"]


class ProbeInputError(ValueError):
    """The input cannot be probed; the run is not charged."""


# ---------- reference ----------

def _get(c: httpx.Client, path: str) -> httpx.Response:
    r = c.get(f"{RAW}/{path}", headers={"User-Agent": "bitdepth-actor"})
    r.raise_for_status()
    return r


def load_reference(slug: str, client: httpx.Client | None = None) -> dict[str, Any]:
    """Latest night's fixed prompts and reference for one graded model."""
    if slug not in GRADED:
        raise ProbeInputError(f"model must be one of {sorted(GRADED)}")
    label = GRADED[slug]
    c = client or httpx.Client(timeout=120.0)
    index = _get(c, "public/v1/index.json").json()
    night = index["as_of"]
    listed = next(m for m in index["models"] if m["model"] == slug)
    public = _get(c, f"public/v1/{listed['path']}").json()
    endpoints = _get(c, f"runs/{night}/endpoints.json").json()["models"][label]["endpoints"]
    prompts = [p for p in _jsonl(_get(c, f"runs/{night}/prompts.jsonl").text) if p["id"].startswith("fixed")]
    rows = [r for r in _jsonl(_get(c, f"runs/{night}/responses.jsonl").text) if r.get("slug") == slug]
    reference, rule, no_ref, _ = build_reference(endpoints, rows)
    fixed_ids = {p["id"] for p in prompts}
    reference = {k: v for k, v in reference.items() if k in fixed_ids}
    nightly = {}
    for e in endpoints:
        m = endpoint_metrics(e, rows, reference, {p["id"]: p for p in prompts})
        if m["compared"]:
            nightly[e["tag"]] = m
    return {
        "slug": slug, "label": label, "night": night, "rule": rule,
        "prompts": prompts, "reference": reference, "public": public, "nightly_fixed": nightly,
    }


def _jsonl(text: str) -> list[dict[str, Any]]:
    import json
    return [json.loads(line) for line in text.splitlines() if line.strip()]


# ---------- targets ----------

def openrouter_target(slug: str, tag: str, lister=openrouter.list_endpoints) -> dict[str, Any]:
    eps = lister(slug)
    match = next((e for e in eps if e["tag"] == tag), None)
    if not match:
        raise ProbeInputError(f"no OpenRouter endpoint '{tag}' for {slug}. Tags: {', '.join(sorted(e['tag'] for e in eps))}")
    return match


def _public_host(url: str) -> None:
    """Refuse non-https and private, loopback or link-local hosts."""
    u = urlparse(url)
    if u.scheme != "https" or not u.hostname:
        raise ProbeInputError("base_url must be an https URL")
    try:
        infos = socket.getaddrinfo(u.hostname, u.port or 443)
    except socket.gaierror as exc:
        raise ProbeInputError(f"cannot resolve {u.hostname}") from exc
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            raise ProbeInputError("base_url resolves to a private address")


def custom_target(base_url: str, model_name: str, declared_quant: str | None) -> dict[str, Any]:
    _public_host(base_url)
    if not model_name:
        raise ProbeInputError("model_name is required for a custom endpoint")
    host = urlparse(base_url).hostname
    return {
        "provider_name": host, "tag": f"custom/{host}", "quantization": (declared_quant or "unknown").lower(),
        "price_in": 0.0, "price_out": 0.0, "supported_parameters": ["seed"], "status": None,
    }


def custom_completer(base_url: str, api_key: str, model_name: str, client: httpx.Client | None = None) -> Callable:
    """Same request the nightly sends, to an OpenAI-compatible server. The key lives only
    in this closure for the length of the run; it is never logged or returned."""
    url = base_url.rstrip("/") + "/chat/completions"
    c = client or httpx.Client(timeout=openrouter.REQUEST_TIMEOUT)
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    def complete(_slug: str, _tag: str, messages: list[dict[str, str]]) -> dict[str, Any]:
        base = {"model": model_name, "messages": messages, "temperature": 0, "top_p": 1,
                "seed": SEED, "max_tokens": MAX_TOKENS}
        # Mirrors the nightly: lowest reasoning effort first, then none if refused.
        for mode, extra in (("low", {"reasoning_effort": "low"}), ("none", {})):
            body = {**base, **extra}
            last = ""
            for attempt in range(openrouter.MAX_RETRIES + 1):
                t0 = time.perf_counter()
                try:
                    r = c.post(url, headers=headers, json=body)
                except httpx.HTTPError as exc:
                    last = f"transport: {type(exc).__name__}"
                    if attempt < openrouter.MAX_RETRIES:
                        openrouter._sleep_backoff(attempt)
                        continue
                    return openrouter._result("error", mode, error=last)
                ms = int((time.perf_counter() - t0) * 1000)
                if r.status_code in openrouter.RETRY_STATUSES and attempt < openrouter.MAX_RETRIES:
                    openrouter._sleep_backoff(attempt)
                    continue
                if r.status_code == 400 and extra and "reason" in r.text.lower():
                    break
                if r.status_code != 200:
                    return openrouter._result("error", mode, error=f"http {r.status_code}", latency_ms=ms)
                data = r.json()
                choice = (data.get("choices") or [{}])[0]
                return openrouter._result(
                    "ok", mode, text=(choice.get("message") or {}).get("content") or "",
                    usage=data.get("usage") or {}, latency_ms=ms, finish_reason=choice.get("finish_reason"),
                )
        return openrouter._result("error", "none", error="reasoning parameter refused in every mode")

    return complete


# ---------- grading against last night ----------

def _rank(value: float | None, others: list[float]) -> str | None:
    if value is None or not others:
        return None
    better = sum(1 for o in others if o > value)
    return f"{better + 1} of {len(others) + 1}"


def compare(metrics: dict[str, Any], ref: dict[str, Any], own_tag: str | None = None) -> dict[str, Any]:
    """Place the probe against last night's endpoints on the same fixed prompts. The
    probed endpoint's own nightly row is left out of the field it is ranked against."""
    nightly = {t: m for t, m in ref["nightly_fixed"].items() if t != own_tag}
    states = {e["tag"]: e["state"] for e in ref["public"]["endpoints"]}
    within = [t for t, s in states.items() if s == "within" and t in nightly]
    cols = ["exact_pct"] + FAMILIES
    out: dict[str, Any] = {"endpoints_last_night": len(nightly), "within_last_night": len(within), "columns": {}}
    for col in cols:
        mine = metrics.get(col)
        all_vals = [m[col] for m in nightly.values() if m.get(col) is not None]
        within_vals = [nightly[t][col] for t in within if nightly[t].get(col) is not None]
        out["columns"][col.replace("_pct", "")] = {
            "probe": mine,
            "rank_among_last_night": _rank(mine, all_vals),
            "last_night_median": round(sorted(all_vals)[len(all_vals) // 2], 1) if all_vals else None,
            "lowest_within": min(within_vals) if within_vals else None,
        }
    primary = [c for c in ref["public"].get("primary_columns", ["exact"]) if c in out["columns"]]
    checks = [out["columns"][c]["probe"] is not None and out["columns"][c]["lowest_within"] is not None
              and out["columns"][c]["probe"] >= out["columns"][c]["lowest_within"] for c in primary]
    out["primary_columns_checked"] = primary
    out["at_or_above_lowest_within"] = bool(checks) and all(checks)
    out["not_checked"] = [c for c in ref["public"].get("primary_columns", []) if c not in out["columns"]]
    return out


def run_probe(
    ref: dict[str, Any],
    target: dict[str, Any],
    completer: Callable,
    workdir: Path,
    target_kind: str,
) -> dict[str, Any]:
    prompts = [p for p in ref["prompts"] if p["id"] in ref["reference"]]
    models = {ref["label"]: {"slug": ref["slug"], "endpoints": [target], "short": True}}
    spend = Spend(SPEND_CAP_USD)
    started = now_iso()
    rows = send_all(f"probe-{started}", models, prompts, workdir / "responses.jsonl", spend, completer=completer)
    metrics = endpoint_metrics(target, rows, ref["reference"], {p["id"]: p for p in prompts})
    ok_share = (metrics["ok"] / metrics["rows"]) if metrics["rows"] else 0.0
    last_night_row = next((e for e in ref["public"]["endpoints"] if e["tag"] == target["tag"]), None)
    return {
        "schema": "bitdepth.probe.v1",
        "probed_at": started,
        "finished_at": now_iso(),
        "model": ref["slug"],
        "target": {
            "kind": target_kind,
            "tag": target["tag"],
            "provider": target["provider_name"],
            "declared_quant": target["quantization"],
        },
        "reference": {
            "night": ref["night"],
            "rule": ref["rule"],
            "prompts": len(prompts),
            "note": "Fixed prompts only, graded with the nightly code against that night's reference.",
        },
        "result": {k: metrics[k] for k in (
            "exact_pct", "compared", "math", "json", "string", "needle", "echo",
            "error_pct", "misrouted", "truncated", "latency_ms_median", "ok", "rows",
        )},
        "against_last_night": compare(metrics, ref, target["tag"]),
        "last_night_row": last_night_row,
        "answered_share": round(ok_share, 3),
        "chargeable": ok_share >= MIN_OK_SHARE and not spend.stopped,
        "budget_stop": spend.stopped,
        "method_url": METHOD_URL,
        "footer": FOOTER,
    }
