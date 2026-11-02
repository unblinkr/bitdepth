"""Public machine-readable files, one per model, plus an index and a drift list.

    python -m probe.emit [--date YYYY-MM-DD] [--trend data/trend] [--runs data/runs]
                         [--out data/public/v1]

Writes:
- data/public/v1/or/<author>/<slug>.json  one file per probed model (schema bitdepth.or.v1)
- data/public/v1/index.json               the models, their as_of date and file paths
- data/public/v1/drift.json               every endpoint whose movement flag is set

Reads files only (the cross-night trend and the night's endpoints.json). It never
calls the network and never reads the key. The site and the MCP server read these
files; nothing here is a page.

State rule (provisional; calibrate on 2026-11-10): an endpoint is `outside` when its
night-to-night self-agreement exceeds its agreement with the reference by more than
GAP_MAX points, that is, it agrees with itself more than it agrees with the
reference. Otherwise `within`. Fewer than MIN_NIGHTS nights is `no_data`. A trend
date more than STALE_DAYS older than the emit date is `stale`.

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
GAP_MAX = 10.0  # provisional; calibrate on 2026-11-10
FAMILIES = ("math", "json", "string", "needle", "echo")

# Which columns separate endpoints on each model (decision of 2026-10-31).
PRIMARY_COLUMNS: dict[str, list[str]] = {
    "openai/gpt-oss-120b": ["exact"],
    "deepseek/deepseek-v4-pro": ["string", "self_agree"],
}

STATE_RULE = (
    f"outside when self-agreement exceeds agreement with the reference by more than {GAP_MAX:.0f} points; "
    f"no_data under {MIN_NIGHTS} nights; stale when the data is more than {STALE_DAYS} days old. Provisional."
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
        } for d in models],
        "drift_path": "drift.json",
        "footer": FOOTER,
    }
    return {"models": models, "index": index, "drift": drift_doc(models, as_of, t["window"])}


def write(out: Path, built: dict[str, Any]) -> list[Path]:
    written = []
    for d in built["models"]:
        p = out / "or" / f"{d['model']}.json"
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
