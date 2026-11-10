"""Quality-adjusted spend report for one OpenRouter account.

    python -m probe.report --activity activity.json [--for "NanoGPT"] [--out packets/reports]
    python -m probe.report --fetch [--for "Bitdepth"]          reads OPENROUTER_MGMT_KEY

Joins the account's usage (OpenRouter GET /api/v1/activity: one row per day, model and
provider endpoint, with spend and tokens, last 30 days) to the nightly grades in
data/public/v1, and writes a one-page Markdown report plus a CSV:

- how much of the spend went to endpoints within the pack, outside it, or not graded yet;
- per model and provider: spend, tokens, state, the primary column against the median;
- for spend on outside endpoints, what the same tokens would have cost on the cheapest
  endpoint within the pack for that model (the route list).

The activity file is the customer's own export. No prompt or output is read. The
management key is read from the environment only and never written anywhere. Reports
land in packets/, which git ignores.

States are as of the latest graded night, not per day of use. Numbers against a stated
reference. Not a claim about intent.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path
from typing import Any

PUBLIC = Path("data/public/v1/or")
RUNS = Path("data/runs")
ACTIVITY_URL = "https://openrouter.ai/api/v1/activity"
STATE_WORDS = {"within": "within the pack", "outside": "outside the pack", "no_data": "no grade yet", "stale": "stale"}
FOOTER = "Numbers against a stated reference. Not a claim about intent."


def fetch_activity() -> list[dict[str, Any]]:
    import httpx

    key = os.environ.get("OPENROUTER_MGMT_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENROUTER_MGMT_KEY is not set in the environment")
    r = httpx.get(ACTIVITY_URL, headers={"Authorization": f"Bearer {key}"}, timeout=60.0)
    r.raise_for_status()
    return r.json().get("data", [])


def load_activity(path: Path) -> list[dict[str, Any]]:
    """The API response ({"data": [...]}), a bare JSON list, or a CSV with the same field names."""
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8") as f:
            return list(csv.DictReader(f))
    doc = json.loads(path.read_text(encoding="utf-8"))
    return doc.get("data", doc) if isinstance(doc, dict) else doc


def _num(v: Any) -> float:
    try:
        return float(v or 0)
    except (TypeError, ValueError):
        return 0.0


def load_grades(public: Path = PUBLIC, runs: Path = RUNS) -> dict[str, dict[str, Any]]:
    """{model slug: {doc, by_provider: {endpoint tag or provider name, lower: [endpoint rows]}}}.

    The exact tag wins; a provider name or slug is the fallback and may cover several tags."""
    names: dict[tuple[str, str], str] = {}
    run_dirs = sorted(d for d in runs.glob("*") if (d / "endpoints.json").exists()) if runs.exists() else []
    if run_dirs:
        ep = json.loads((run_dirs[-1] / "endpoints.json").read_text(encoding="utf-8"))
        for m in ep.get("models", {}).values():
            for e in m.get("endpoints", []):
                names[(m["slug"], e["tag"])] = e.get("provider_name", "")
    out: dict[str, dict[str, Any]] = {}
    for f in public.glob("*/*.json") if public.exists() else []:
        doc = json.loads(f.read_text(encoding="utf-8"))
        by: dict[str, list[dict[str, Any]]] = {}
        for e in doc.get("endpoints", []):
            # OpenRouter's activity rows name the endpoint by its tag (e.g. gmicloud/fp8).
            by.setdefault(e["tag"].lower(), []).append(e)
            pname = names.get((doc["model"], e["tag"])) or e.get("provider_slug", "")
            for k in {pname.lower(), e.get("provider_slug", "").lower()} - {e["tag"].lower()}:
                if k:
                    by.setdefault(k, []).append(e)
        out[doc["model"]] = {"doc": doc, "by_provider": by}
    return out


def match_model(model: str, grades: dict[str, Any]) -> str | None:
    if model in grades:
        return model
    for slug in grades:
        if model.startswith(slug):
            return slug
    return None


def _median(xs: list[float]) -> float | None:
    xs = sorted(xs)
    if not xs:
        return None
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def cheapest_within(doc: dict[str, Any], tin: float, tout: float) -> tuple[str, float] | None:
    best = None
    for e in doc.get("endpoints", []):
        if e.get("state") != "within" or e.get("price_in_per_m") is None or e.get("price_out_per_m") is None:
            continue
        cost = (tin * e["price_in_per_m"] + tout * e["price_out_per_m"]) / 1e6
        if best is None or cost < best[1]:
            best = (e["tag"], cost)
    return best


def build(activity: list[dict[str, Any]], grades: dict[str, Any]) -> dict[str, Any]:
    groups: dict[tuple[str, str], dict[str, Any]] = {}
    dates: list[str] = []
    for a in activity:
        model = a.get("model") or a.get("model_permaslug") or ""
        prov = a.get("provider_name") or ""
        g = groups.setdefault((model, prov), {"model": model, "provider": prov, "spend": 0.0,
                                               "requests": 0.0, "tin": 0.0, "tout": 0.0})
        g["spend"] += _num(a.get("usage")) + _num(a.get("byok_usage_inference"))
        g["requests"] += _num(a.get("requests"))
        g["tin"] += _num(a.get("prompt_tokens"))
        g["tout"] += _num(a.get("completion_tokens"))
        if a.get("date"):
            dates.append(str(a["date"])[:10])

    rows = []
    for g in groups.values():
        slug = match_model(g["model"], grades)
        row = dict(g, graded_model=slug, tags=[], state="not_graded", primary=None, value=None, median=None,
                   alt_tag=None, alt_cost=None)
        if slug:
            doc = grades[slug]["doc"]
            col = (doc.get("primary_columns") or ["exact"])[0]
            key = g["provider"].lower()
            eps = grades[slug]["by_provider"].get(key, [])
            exact = [e for e in eps if e["tag"].lower() == key]
            eps = exact or eps
            row["primary"] = col
            seven = [e[col] for e in doc["endpoints"] if (e.get("nights") or 0) >= 7 and e.get(col) is not None]
            row["median"] = _median(seven)
            if eps:
                row["tags"] = [e["tag"] for e in eps]
                states = {e.get("state") for e in eps}
                row["state"] = states.pop() if len(states) == 1 else "mixed"
                vals = [e[col] for e in eps if e.get(col) is not None]
                row["value"] = sum(vals) / len(vals) if vals else None
            else:
                row["state"] = "not_probed"
            if row["state"] == "outside":
                alt = cheapest_within(doc, g["tin"], g["tout"])
                if alt:
                    row["alt_tag"], row["alt_cost"] = alt
        rows.append(row)
    rows.sort(key=lambda r: -r["spend"])

    total = sum(r["spend"] for r in rows)
    by_state: dict[str, float] = {}
    for r in rows:
        by_state[r["state"]] = by_state.get(r["state"], 0.0) + r["spend"]
    return {"rows": rows, "total": total, "by_state": by_state,
            "from": min(dates) if dates else None, "to": max(dates) if dates else None,
            "as_of": max((g["doc"].get("as_of") or "") for g in grades.values()) if grades else None}


STATE_LABEL = {**STATE_WORDS, "mixed": "mixed (several endpoints from this provider)",
               "not_probed": "provider not in the nightly run", "not_graded": "model not graded"}


def _pct(x: float, total: float) -> str:
    return f"{100 * x / total:.1f}%" if total else "0.0%"


def render(name: str, r: dict[str, Any]) -> str:
    total = r["total"]
    L = [f"# Quality-adjusted spend report for {name}", ""]
    L.append(f"Usage {r['from']} to {r['to']} (OpenRouter activity export). Grades as of the night of {r['as_of']}. "
             "Private to the recipient.")
    L += ["", "## The headline", ""]
    out = r["by_state"].get("outside", 0.0)
    L.append(f"- Total spend: ${total:,.2f}.")
    for st in ("within", "outside", "no_data", "mixed", "not_probed", "not_graded", "stale"):
        if r["by_state"].get(st):
            L.append(f"- {STATE_LABEL[st].capitalize()}: ${r['by_state'][st]:,.2f} ({_pct(r['by_state'][st], total)}).")
    moved = [x for x in r["rows"] if x["state"] == "outside" and x["alt_cost"] is not None]
    if moved:
        now = sum(x["spend"] for x in moved)
        alt = sum(x["alt_cost"] for x in moved)
        L.append(f"- The same tokens on the cheapest endpoint within the pack for each model would have cost "
                 f"${alt:,.2f} instead of ${now:,.2f}.")
    elif out == 0:
        L.append("- None of this spend went to an endpoint outside the pack.")
    L += ["", "## By model and provider", "",
          "| Model | Provider | Spend | Share | Requests | Tokens in | Tokens out | State | Primary column | Value | Median | Cheapest within the pack | Cost there |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for x in r["rows"]:
        value = "-" if x["value"] is None else f"{x['value']:.1f}"
        median = "-" if x["median"] is None else f"{x['median']:.1f}"
        alt_cost = "-" if x["alt_cost"] is None else f"${x['alt_cost']:,.2f}"
        L.append(
            f"| {x['model']} | {x['provider']} | ${x['spend']:,.2f} | {_pct(x['spend'], total)} | {x['requests']:,.0f} | "
            f"{x['tin']:,.0f} | {x['tout']:,.0f} | {STATE_LABEL.get(x['state'], x['state'])} | {x['primary'] or '-'} | "
            f"{value} | {median} | {x['alt_tag'] or '-'} | {alt_cost} |")
    L += ["", "## How to read this", "",
          "- Each row is one model and one provider your account sent traffic to, summed over the period.",
          "- State is the endpoint's grade on the public table: within the pack, outside the pack, or no grade yet "
          "(under seven nights). It is the state as of the latest graded night, not per day of use.",
          "- Primary column is the measure that separates endpoints on that model (exact match or string accuracy), "
          "against the median of endpoints with seven or more nights.",
          "- Cost there prices the same input and output tokens at the cheapest endpoint within the pack, at "
          "OpenRouter list prices on the latest graded night.",
          "- Method: https://bitdepth.dev/method", "", FOOTER, ""]
    return "\n".join(L)


def write_csv(path: Path, r: dict[str, Any]) -> None:
    cols = ["model", "provider", "spend", "requests", "tin", "tout", "state", "tags", "primary", "value", "median",
            "alt_tag", "alt_cost"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for x in r["rows"]:
            w.writerow([";".join(x[c]) if c == "tags" else ("" if x[c] is None else x[c]) for c in cols])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--activity", help="activity export: API JSON, a JSON list, or CSV")
    src.add_argument("--fetch", action="store_true", help="fetch the last 30 days with OPENROUTER_MGMT_KEY")
    ap.add_argument("--for", dest="name", default="your account")
    ap.add_argument("--out", default="packets/reports")
    ap.add_argument("--public", default=str(PUBLIC))
    ap.add_argument("--runs", default=str(RUNS))
    a = ap.parse_args(argv)
    activity = fetch_activity() if a.fetch else load_activity(Path(a.activity))
    r = build(activity, load_grades(Path(a.public), Path(a.runs)))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    slug = "".join(c if c.isalnum() else "-" for c in a.name.lower()).strip("-") or "account"
    stem = f"{slug}-spend-{r['to'] or 'none'}"
    (out / f"{stem}.md").write_text(render(a.name, r), encoding="utf-8")
    write_csv(out / f"{stem}.csv", r)
    print(f"wrote {out / (stem + '.md')} and .csv: {len(r['rows'])} rows, ${r['total']:,.2f} total, "
          f"outside ${r['by_state'].get('outside', 0.0):,.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
