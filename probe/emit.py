"""Public machine-readable files, one per model, plus an index and a drift list.

    python -m probe.emit [--date YYYY-MM-DD] [--trend data/trend] [--runs data/runs]
                         [--out data/public/v1]

Writes:
- data/public/v1/or/<author>/<slug>.json  one file per probed model (schema bitdepth.or.v1)
- data/public/v1/routes/<author>/<slug>.json  the route list per model (schema bitdepth.routelist.v1)
- data/public/v1/index.json               the models, their as_of date and file paths
- data/public/v1/drift.json               every endpoint whose movement flag is set

Reads files only (the cross-night trend and the night's endpoints.json). It never
calls the network and never reads the key. The site and the MCP server read these
files; nothing here is a page.

State rule (calibrated 2026-11-10 on the fourteen-night read): an endpoint is `outside`
when either test fires. Gap test: its night-to-night self-agreement exceeds its
agreement with the reference by more than GAP_MAX points (it agrees with itself more
than with the reference). Floor test: its mean on the model's first primary column is
more than FLOOR_MAX points below the median of the endpoints with MIN_NIGHTS or more
nights (it is far from the pack and may also be inconsistent with itself, which the
gap test alone cannot see). Otherwise `within`. Fewer than MIN_NIGHTS nights is
`no_data`. A trend date more than STALE_DAYS older than the emit date is `stale`.

Numbers against a stated reference. Not a claim about intent.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date as Date
from pathlib import Path
from typing import Any

from probe.packet import load_prices, load_trend

SCHEMA = "bitdepth.or.v1"
METHOD_URL = "https://bitdepth.dev/method"
FOOTER = "Numbers against a stated reference. Not a claim about intent."
MIN_NIGHTS = 7
STALE_DAYS = 3
# Calibrated 2026-11-10: 10 was reachable by noise (V4.1 Flash stepfun/fp8 at 10.2, mid-pack).
# At 15 the four V4 Pro outliers keep a 5-point margin and no mid-pack endpoint reaches it.
GAP_MAX = 15.0
# Twice the median one-hour self-disagreement on gpt-oss-120b (4.2), above the largest
# distance any within endpoint had from its pack median (4.9).
FLOOR_MAX = 8.0
FAMILIES = ("math", "json", "string", "needle", "echo")

# Which columns separate endpoints on each model (decision of 2026-10-31).
PRIMARY_COLUMNS: dict[str, list[str]] = {
    "openai/gpt-oss-120b": ["exact"],
    "deepseek/deepseek-v4-pro": ["string", "self_agree"],
    # 2026-11-10: on V4.1 Flash only exact match separates; string and math are flat model-wide.
    "deepseek/deepseek-v4.1-flash-1017": ["exact"],
}

STATE_RULE = (
    f"outside when self-agreement exceeds agreement with the reference by more than {GAP_MAX:.0f} points, "
    f"or when the endpoint's mean on the model's first primary column is more than {FLOOR_MAX:.0f} points below "
    f"the median of endpoints with {MIN_NIGHTS}+ nights; "
    f"no_data under {MIN_NIGHTS} nights; stale when the data is more than {STALE_DAYS} days old."
)


def primary_columns(slug: str, families: dict[str, Any]) -> list[str]:
    if slug in PRIMARY_COLUMNS:
        return PRIMARY_COLUMNS[slug]
    math = families.get("math") or {}
    return ["string", "self_agree"] if math and not math.get("stable") else ["exact"]


def state_of(nights: int, exact: float | None, self_agree: float | None, as_of: str, today: str) -> str:
    if (Date.fromisoformat(today) - Date.fromisoformat(as_of)).days > STALE_DAYS:
        return "stale"
    if nights < MIN_NIGHTS or exact is None or self_agree is None:
        return "no_data"
    return "outside" if (self_agree - exact) > GAP_MAX else "within"


def _median(xs: list[float]) -> float:
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def apply_floor(rows: list[dict[str, Any]], column: str) -> None:
    """Floor test: a `within` endpoint more than FLOOR_MAX points below the median of the
    endpoints with MIN_NIGHTS+ nights on the primary column becomes `outside`."""
    vals = [r.get(column) for r in rows if (r.get("nights") or 0) >= MIN_NIGHTS and r.get(column) is not None]
    if len(vals) < 3:
        return
    med = _median([float(v) for v in vals])
    for r in rows:
        v = r.get(column)
        if r.get("state") == "within" and v is not None and float(v) < med - FLOOR_MAX:
            r["state"] = "outside"


def endpoint_row(e: dict[str, Any], prices: dict[str, tuple[float, float]], as_of: str, today: str) -> dict[str, Any]:
    p = prices.get(e["tag"])
    self_agree = e["self"]["agree_pct"]
    nightly = e.get("exact_by_night", {})
    return {
        "tag": e["tag"],
        "provider_slug": e["tag"].split("/")[0],
        "declared_quant": e["declared_quant"],
        "declared_changed": bool(e.get("declared_changed")),
        "nights": e["nights"],
        "exact": e["exact_mean"],
        "exact_sd": e["exact_sd"],
        "string": e["families"].get("string"),
        "self_agree": self_agree,
        "families": {f: e["families"].get(f) for f in FAMILIES},
        "movement": e["movement"],
        "movement_flag": bool(e["movement_flag"]),
        "price_in_per_m": p[0] if p else None,
        "price_out_per_m": p[1] if p else None,
        "state": state_of(e["nights"], e["exact_mean"], self_agree, as_of, today),
        "nightly_exact": [{"date": d, "exact": v} for d, v in sorted(nightly.items())],
    }


def model_doc(m: dict[str, Any], prices: dict[str, tuple[float, float]], as_of: str, nights: int, today: str) -> dict[str, Any]:
    fams = m.get("families", {})
    rows = [endpoint_row(e, prices, as_of, today) for e in m["endpoints"]]
    apply_floor(rows, primary_columns(m["slug"], fams)[0])
    return {
        "schema": SCHEMA,
        "model": m["slug"],
        "label": m["label"],
        "as_of": as_of,
        "nights": nights,
        "endpoint_count": len(rows),
        "reference_rule": m["rules"][-1] if m.get("rules") else None,
        "method_url": METHOD_URL,
        "primary_columns": primary_columns(m["slug"], fams),
        "state_rule": STATE_RULE,
        "noise_floor": {f: (fams.get(f) or {}).get("noise_floor") for f in FAMILIES},
        "stable_families": [f for f in FAMILIES if (fams.get(f) or {}).get("stable")],
        "endpoints": rows,
        "footer": FOOTER,
    }


ROUTE_SCHEMA = "bitdepth.routelist.v1"
MIN_ROUTE_NIGHTS = 7  # same rule as check_before_route in site/api/mcp.js
ROUTE_RULE = f"state within and {MIN_ROUTE_NIGHTS}+ nights (the check_before_route rule); allowed endpoints ordered by blended price, cheapest first"


def blended(r: dict[str, Any]) -> float | None:
    if r.get("price_in_per_m") is None or r.get("price_out_per_m") is None:
        return None
    return (3 * r["price_in_per_m"] + r["price_out_per_m"]) / 4


def routable(r: dict[str, Any]) -> bool:
    return r.get("state") == "within" and (r.get("nights") or 0) >= MIN_ROUTE_NIGHTS


def exclusion_reason(r: dict[str, Any]) -> str:
    s = r.get("state")
    if s == "outside":
        return "outside"
    if s == "stale":
        return "stale"
    return f"only {r.get('nights') or 0} nights; {MIN_ROUTE_NIGHTS} needed"


def route_doc(doc: dict[str, Any]) -> dict[str, Any]:
    """The route list for one model: endpoints to allow, in the shape OpenRouter's provider block takes."""
    ok = [r for r in doc["endpoints"] if routable(r)]
    # OpenRouter treats a slug as a prefix: "venice" matches every Venice endpoint and
    # "alibaba/fp8" matches "alibaba/fp8/us-east-1". An allowed slug that would also
    # match a left-out endpoint is left out too, so the list can never route to one.
    out_tags = [r["tag"] for r in doc["endpoints"] if not routable(r)]
    shadow = {r["tag"]: [x for x in out_tags if x.startswith(r["tag"] + "/")] for r in ok}
    ok = [r for r in ok if not shadow[r["tag"]]]
    ok.sort(key=lambda r: (blended(r) is None, blended(r) or 0.0, r["tag"]))
    allow = [r["tag"] for r in ok]
    excluded = [{"tag": r["tag"], "why": exclusion_reason(r) if not routable(r) else f"would also match {', '.join(shadow[r['tag']])}"}
                for r in sorted(doc["endpoints"], key=lambda r: r["tag"]) if r["tag"] not in allow]
    return {
        "schema": ROUTE_SCHEMA,
        "model": doc["model"],
        "label": doc["label"],
        "as_of": doc["as_of"],
        "rule": ROUTE_RULE,
        "allow": allow,
        "allowed": [{"tag": r["tag"], "declared_quant": r["declared_quant"], "nights": r["nights"],
                     "blended_price_per_m": round(blended(r), 4) if blended(r) is not None else None} for r in ok],
        "excluded": excluded,
        "openrouter": {"provider": {"only": allow, "sort": "price", "allow_fallbacks": True}} if allow else None,
        "usage": ("Put openrouter.provider in the request body. Fallbacks stay on and move only among the allowed endpoints. "
                  "An account-wide allowed providers list in OpenRouter settings also applies; if the two do not overlap, requests fail."),
        "method_url": METHOD_URL,
        "footer": FOOTER,
    }


def drift_doc(models: list[dict[str, Any]], as_of: str, window: int) -> dict[str, Any]:
    items = []
    for doc in models:
        for r in doc["endpoints"]:
            if r["movement_flag"]:
                items.append({
                    "model": doc["model"],
                    "tag": r["tag"],
                    "movement": r["movement"],
                    "compared": f"mean exact of the last {window} nights minus the first {window}",
                })
    return {"schema": SCHEMA, "as_of": as_of, "items": items, "footer": FOOTER}


def build(trend_dir: Path, runs_dir: Path, date: str | None, today: str | None = None) -> dict[str, Any]:
    as_of, t = load_trend(trend_dir, date)
    today = today or as_of
    prices = load_prices(runs_dir, as_of)
    nights = len(t["dates"])
    models = [model_doc(m, prices.get(m["label"], {}), as_of, nights, today) for m in t["models"]]
    index = {
        "schema": SCHEMA,
        "as_of": as_of,
        "nights": nights,
        "first_night": t["dates"][0],
        "method_url": METHOD_URL,
        "models": [{
            "model": d["model"],
            "label": d["label"],
            "as_of": d["as_of"],
            "endpoint_count": d["endpoint_count"],
            "path": f"or/{d['model']}.json",
            "routes_path": f"routes/{d['model']}.json",
        } for d in models],
        "drift_path": "drift.json",
        "footer": FOOTER,
    }
    return {"models": models, "routes": [route_doc(d) for d in models], "index": index, "drift": drift_doc(models, as_of, t["window"])}


def write(out: Path, built: dict[str, Any]) -> list[Path]:
    written = []
    for d in built["models"]:
        p = out / "or" / f"{d['model']}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(d, indent=2) + "\n")
        written.append(p)
    for d in built.get("routes", []):
        p = out / "routes" / f"{d['model']}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(d, indent=2) + "\n")
        written.append(p)
    for name in ("index", "drift"):
        p = out / f"{name}.json"
        p.write_text(json.dumps(built[name], indent=2) + "\n")
        written.append(p)
    return written


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=None, help="trend date; default latest")
    ap.add_argument("--trend", default="data/trend")
    ap.add_argument("--runs", default="data/runs")
    ap.add_argument("--out", default="data/public/v1")
    a = ap.parse_args(argv)
    for p in write(Path(a.out), build(Path(a.trend), Path(a.runs), a.date)):
        print(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
