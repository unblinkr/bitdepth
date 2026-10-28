"""Thin OpenRouter client.

The API key is read from the environment at call time and is never stored on an
object that gets serialised. Public listing calls need no key.
"""

from __future__ import annotations

import os
import random
import time
from typing import Any

import httpx

from probe import MAX_TOKENS, SEED

BASE = "https://openrouter.ai/api/v1"
RETRY_STATUSES = {429, 500, 502, 503, 504}
MAX_RETRIES = 5
REQUEST_TIMEOUT = 120.0

# Reasoning is turned off where the endpoint allows it so the probe measures the served
# weights, not a thinking budget. If an endpoint rejects the parameter the request is
# retried with the lowest effort, then without the parameter.
REASONING_MODES: list[tuple[str, dict[str, Any] | None]] = [
    ("disabled", {"enabled": False}),
    ("low", {"effort": "low"}),
    ("none", None),
]


def _key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is not set in the environment")
    return key


def _headers(auth: bool) -> dict[str, str]:
    h = {
        "HTTP-Referer": "https://bitdepth.dev",
        "X-Title": "Bitdepth probe",
        "Content-Type": "application/json",
    }
    if auth:
        h["Authorization"] = f"Bearer {_key()}"
    return h


def list_models(client: httpx.Client | None = None) -> list[dict[str, Any]]:
    c = client or httpx.Client(timeout=60.0)
    r = c.get(f"{BASE}/models", headers=_headers(auth=False))
    r.raise_for_status()
    return r.json()["data"]


def list_endpoints(slug: str, client: httpx.Client | None = None) -> list[dict[str, Any]]:
    """Return one dict per endpoint with the fields the harness uses.

    Pricing is USD per token as OpenRouter reports it.
    """
    c = client or httpx.Client(timeout=60.0)
    r = c.get(f"{BASE}/models/{slug}/endpoints", headers=_headers(auth=False))
    r.raise_for_status()
    data = r.json().get("data", {})
    out = []
    for e in data.get("endpoints", []):
        pricing = e.get("pricing") or {}
        out.append(
            {
                "provider_name": e.get("provider_name"),
                "tag": e.get("tag"),
                "quantization": (e.get("quantization") or "unknown"),
                "price_in": float(pricing.get("prompt") or 0.0),
                "price_out": float(pricing.get("completion") or 0.0),
                "context_length": e.get("context_length"),
                "max_completion_tokens": e.get("max_completion_tokens"),
                "supported_parameters": list(e.get("supported_parameters") or []),
                "status": e.get("status"),
            }
        )
    return out


def _sleep_backoff(attempt: int) -> None:
    # 2, 4, 8, 16, 32 seconds plus jitter; rate limits are waited out, never hammered
    time.sleep((2**(attempt + 1)) + random.uniform(0, 0.5))


def _result(status: str, mode: str, **kw: Any) -> dict[str, Any]:
    base = {
        "status": status,
        "error": "",
        "text": "",
        "provider": None,
        "usage": {},
        "latency_ms": 0,
        "finish_reason": None,
        "reasoning_mode": mode,
        "raw": None,
    }
    base.update(kw)
    return base


def _attempt(c: httpx.Client, body: dict[str, Any], mode: str) -> tuple[str, dict[str, Any] | None]:
    """One request with retries. Returns (outcome, result).

    outcome is "done" (result is final) or "next_mode" (the reasoning parameter was
    rejected and the caller should try the next mode).
    """
    last_error = ""
    for attempt in range(MAX_RETRIES + 1):
        t0 = time.perf_counter()
        try:
            r = c.post(f"{BASE}/chat/completions", headers=_headers(auth=True), json=body)
        except httpx.HTTPError as exc:
            last_error = f"transport: {type(exc).__name__}"
            if attempt < MAX_RETRIES:
                _sleep_backoff(attempt)
                continue
            return "done", _result("error", mode, error=last_error)
        latency_ms = int((time.perf_counter() - t0) * 1000)
        if r.status_code in RETRY_STATUSES:
            last_error = f"http {r.status_code}: {r.text[:200]}"
            if attempt < MAX_RETRIES:
                _sleep_backoff(attempt)
                continue
            return "done", _result("error", mode, error=last_error, latency_ms=latency_ms)
        if r.status_code == 400 and "reasoning" in body and "reason" in r.text.lower():
            return "next_mode", None
        if r.status_code != 200:
            return "done", _result("error", mode, error=f"http {r.status_code}: {r.text[:300]}", latency_ms=latency_ms)
        data = r.json()
        if "error" in data and not data.get("choices"):
            err = data["error"]
            msg = err.get("message", "") if isinstance(err, dict) else str(err)
            if "reason" in msg.lower() and "reasoning" in body:
                return "next_mode", None
            return "done", _result(
                "error", mode, error=f"api: {msg[:300]}", provider=data.get("provider"),
                usage=data.get("usage") or {}, latency_ms=latency_ms, raw=data,
            )
        choice = (data.get("choices") or [{}])[0]
        message = choice.get("message") or {}
        return "done", _result(
            "ok", mode,
            text=message.get("content") or "",
            provider=data.get("provider"),
            usage=data.get("usage") or {},
            latency_ms=latency_ms,
            finish_reason=choice.get("finish_reason") or choice.get("native_finish_reason"),
            raw=data,
        )
    return "done", _result("error", mode, error=last_error or "retries exhausted")


def complete(
    slug: str,
    tag: str,
    messages: list[dict[str, str]],
    params: dict[str, Any] | None = None,
    client: httpx.Client | None = None,
) -> dict[str, Any]:
    """Send one chat completion pinned to one endpoint tag.

    Returns a dict with: status (ok or error), text, provider, usage, latency_ms,
    finish_reason, reasoning_mode, error, raw.
    """
    c = client or httpx.Client(timeout=REQUEST_TIMEOUT)
    base_body: dict[str, Any] = {
        "model": slug,
        "messages": messages,
        "temperature": 0,
        "top_p": 1,
        "seed": SEED,
        "max_tokens": MAX_TOKENS,
        "usage": {"include": True},
        "provider": {"order": [tag], "allow_fallbacks": False},
    }
    if params:
        base_body.update(params)

    for mode, reasoning in REASONING_MODES:
        body = dict(base_body)
        if reasoning is not None:
            body["reasoning"] = reasoning
        outcome, result = _attempt(c, body, mode)
        if outcome == "done" and result is not None:
            return result
    return _result("error", "none", error="all reasoning modes rejected")
