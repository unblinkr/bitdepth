"""Cost estimate and the nightly cap.

The estimate is computed before anything is sent. Input tokens are estimated as
characters divided by four plus a small overhead. Expected output tokens are set per
family and capped by the request's max_tokens. If the estimate is over the cap the
run drops needle prompts first, then the fresh prompts, then aborts.

The cap is also enforced at run time from billed cost, so the estimate never has to
be exact for the hard rule to hold.
"""

from __future__ import annotations

from typing import Any

from probe import BUDGET_USD, MAX_TOKENS

INPUT_OVERHEAD_TOKENS = 24
EXPECTED_OUTPUT_TOKENS = {
    "math": 96,
    "string": 64,
    "needle": 64,
    "echo": 256,
    "json": 320,
}


def input_tokens(prompt: str) -> int:
    return len(prompt) // 4 + INPUT_OVERHEAD_TOKENS


def output_tokens(family: str) -> int:
    return min(EXPECTED_OUTPUT_TOKENS.get(family, MAX_TOKENS), MAX_TOKENS)


def estimate(endpoints_by_model: dict[str, list[dict[str, Any]]], prompts: list[dict[str, Any]]) -> dict[str, Any]:
    """Return the estimate in USD with a per-model and per-endpoint breakdown."""
    total_in = sum(input_tokens(p["prompt"]) for p in prompts)
    total_out = sum(output_tokens(p["family"]) for p in prompts)
    per_model: dict[str, float] = {}
    per_endpoint: list[dict[str, Any]] = []
    grand = 0.0
    for label, endpoints in endpoints_by_model.items():
        sub = 0.0
        for e in endpoints:
            cost = total_in * e["price_in"] + total_out * e["price_out"]
            per_endpoint.append({"model": label, "tag": e["tag"], "usd": round(cost, 4)})
            sub += cost
        per_model[label] = round(sub, 4)
        grand += sub
    return {
        "usd": round(grand, 4),
        "per_model": per_model,
        "per_endpoint": per_endpoint,
        "prompts": len(prompts),
        "input_tokens_per_endpoint": total_in,
        "output_tokens_per_endpoint": total_out,
    }


def apply_cap(
    endpoints_by_model: dict[str, list[dict[str, Any]]],
    prompts: list[dict[str, Any]],
    cap: float = BUDGET_USD,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any], bool]:
    """Return (kept prompts, dropped prompts, final estimate, aborted).

    Drop order: every needle prompt, then every remaining fresh prompt. If still over
    the cap, abort (kept is empty).
    """
    kept = list(prompts)
    dropped: list[dict[str, Any]] = []
    est = estimate(endpoints_by_model, kept)
    if est["usd"] <= cap:
        return kept, dropped, est, False

    needle = [p for p in kept if p["family"] == "needle"]
    kept = [p for p in kept if p["family"] != "needle"]
    dropped.extend(needle)
    est = estimate(endpoints_by_model, kept)
    if est["usd"] <= cap:
        return kept, dropped, est, False

    fresh = [p for p in kept if p["id"].startswith("fresh-")]
    kept = [p for p in kept if not p["id"].startswith("fresh-")]
    dropped.extend(fresh)
    est = estimate(endpoints_by_model, kept)
    if est["usd"] <= cap:
        return kept, dropped, est, False

    return [], dropped + kept, est, True
