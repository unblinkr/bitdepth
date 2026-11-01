"""Cross-night trend.

    python -m probe.trend --date YYYY-MM-DD [--runs data/runs] [--out data/trend]

Reads every night's run folder up to and including the date, and writes one trend
file per date (Markdown and JSON, plus latest copies) with, per model and endpoint:
the exact-match history and its movement, graded accuracy per family, night-to-night
agreement with itself on the fixed prompts, and the one-hour self-check agreement on
the nights it was measured. Per model and family it prints the noise floor the grade
brief defines. It reads files only. It never calls the network and never reads the key.

Numbers against a stated reference. Not a claim about intent.
"""

from __future__ import annotations

import argparse
import json
import shutil
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from probe.generators import FAMILIES, load_jsonl
from probe.score import build_reference, endpoint_metrics, noise_floor, norm

THRESHOLDS = {
    "STABLE_MIN": 95.0,  # provisional; calibrate on 2026-11-10
    "MOVE_MIN": 10.0,  # provisional; calibrate on 2026-11-10
}
WINDOW = 3  # nights in each end of the movement window
MIN_NIGHTS_FOR_FLAG = 4
FIXED_PREFIX = "fixed-"
FOOTER_LINE = "Numbers against a stated reference. Not a claim about intent."


def _pct(num: int, den: int) -> float | None:
    return round(100.0 * num / den, 1) if den else None


def _mean(xs: list[float]) -> float | None:
    return round(statistics.fmean(xs), 1) if xs else None


def _sd(xs: list[float]) -> float | None:
    return round(statistics.pstdev(xs), 1) if len(xs) > 1 else (0.0 if xs else None)


def percentile(xs: list[float], p: float) -> float | None:
    """Linear interpolation between order statistics, p in [0, 100]."""
    if not xs:
        return None
    s = sorted(xs)
    if len(s) == 1:
        return s[0]
    k = (len(s) - 1) * p / 100.0
    lo, hi = int(k), min(int(k) + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def load_nights(runs_dir: Path, upto: str) -> list[dict[str, Any]]:
    """Every run folder with run.json and responses.jsonl, dated at or before upto, oldest first."""
    nights: list[dict[str, Any]] = []
    for d in sorted(p for p in runs_dir.iterdir() if p.is_dir()):
        if d.name > upto or not (d / "run.json").exists() or not (d / "responses.jsonl").exists():
            continue
        endpoints_doc = json.loads((d / "endpoints.json").read_text(encoding="utf-8"))
        night = {
            "date": d.name,
            "models": endpoints_doc["models"],
            "prompts": {p["id"]: p for p in load_jsonl(d / "prompts.jsonl")},
            "rows": load_jsonl(d / "responses.jsonl"),
            "selfcheck": load_jsonl(d / "selfcheck.jsonl") if (d / "selfcheck.jsonl").exists() else [],
        }
        nights.append(night)
    return nights


def movement(history: list[float]) -> tuple[float | None, bool]:
    """Mean of the last WINDOW values minus the mean of the first WINDOW. Second value says
    whether the two windows overlap (fewer than 2 * WINDOW values)."""
    if len(history) < 2:
        return None, False
    w = min(WINDOW, len(history))
    first, last = history[:w], history[-w:]
    return round(statistics.fmean(last) - statistics.fmean(first), 1), len(history) < 2 * WINDOW


def self_agreement(
    tag: str, label: str, nights: list[dict[str, Any]]
) -> dict[str, Any]:
    """Night-to-night agreement of one endpoint with itself on the fixed prompts: for each
    pair of consecutive nights the endpoint was present, each fixed prompt with an ok row on
    both nights counts once; it agrees when the stripped outputs are equal."""
    present = [n for n in nights if any(e["tag"] == tag for e in n["models"].get(label, {}).get("endpoints", []))]
    agree: dict[str, int] = defaultdict(int)
    pairs: dict[str, int] = defaultdict(int)
    for a, b in zip(present, present[1:]):
        oa = {r["prompt_id"]: norm(r["output"]) for r in a["rows"]
              if r["model"] == label and r["pinned_tag"] == tag and r["status"] == "ok" and r["prompt_id"].startswith(FIXED_PREFIX)}
        ob = {r["prompt_id"]: norm(r["output"]) for r in b["rows"]
              if r["model"] == label and r["pinned_tag"] == tag and r["status"] == "ok" and r["prompt_id"].startswith(FIXED_PREFIX)}
        for pid in oa.keys() & ob.keys():
            fam = b["prompts"].get(pid, a["prompts"].get(pid, {})).get("family", "?")
            pairs[fam] += 1
            pairs["all"] += 1
            if oa[pid] == ob[pid]:
                agree[fam] += 1
                agree["all"] += 1
    out: dict[str, Any] = {"pairs": pairs["all"], "agree_pct": _pct(agree["all"], pairs["all"]), "by_family": {}}
    for fam in FAMILIES:
        out["by_family"][fam] = {"pairs": pairs[fam], "agree_pct": _pct(agree[fam], pairs[fam])}
    return out


def family_noise(endpoint_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Per family: median endpoint self-agreement, 75th percentile of disagreement, the noise
    floor (100 minus that percentile) and whether the family is stable at STABLE_MIN."""
    out: dict[str, dict[str, Any]] = {}
    for fam in FAMILIES:
        agrees = [e["self"]["by_family"][fam]["agree_pct"] for e in endpoint_rows
                  if e["self"]["by_family"][fam]["agree_pct"] is not None]
        if not agrees:
            out[fam] = {"endpoints": 0, "median_agree_pct": None, "p75_disagree_pct": None, "noise_floor": None, "stable": None}
            continue
        med = round(statistics.median(agrees), 1)
        p75 = round(percentile([100.0 - a for a in agrees], 75), 1)
        out[fam] = {
            "endpoints": len(agrees),
            "median_agree_pct": med,
            "p75_disagree_pct": p75,
            "noise_floor": round(100.0 - p75, 1),
            "stable": med >= THRESHOLDS["STABLE_MIN"],
        }
    return out


def build(nights: list[dict[str, Any]]) -> dict[str, Any]:
    dates = [n["date"] for n in nights]
    selfcheck_dates = [n["date"] for n in nights if n["selfcheck"]]
    # one-hour self-check agreement, keyed "model|tag", per self-check night
    sc_by_date: dict[str, dict[str, dict[str, Any]]] = {n["date"]: noise_floor(n["selfcheck"]) for n in nights if n["selfcheck"]}
    # per-night scorecard metrics, so trend numbers equal the nightly scorecards
    per_night: dict[str, dict[str, dict[str, dict[str, Any]]]] = {}  # date -> label -> tag -> metrics
    rules: dict[str, set[str]] = defaultdict(set)
    labels: dict[str, str] = {}
    for n in nights:
        per_night[n["date"]] = {}
        for label, m in n["models"].items():
            labels.setdefault(label, m["slug"])
            mrows = [r for r in n["rows"] if r["model"] == label]
            reference, rule, _no_ref, _tags = build_reference(m["endpoints"], mrows)
            rules[label].add(rule)
            per_night[n["date"]][label] = {e["tag"]: endpoint_metrics(e, mrows, reference, n["prompts"]) for e in m["endpoints"]}

    models_out: list[dict[str, Any]] = []
    for label, slug in labels.items():
        tags: list[str] = []
        for n in nights:
            for e in n["models"].get(label, {}).get("endpoints", []):
                if e["tag"] not in tags:
                    tags.append(e["tag"])
        rows_out: list[dict[str, Any]] = []
        for tag in tags:
            present = [d for d in dates if tag in per_night[d].get(label, {})]
            metrics = {d: per_night[d][label][tag] for d in present}
            exact_by_night = {d: metrics[d]["exact_pct"] for d in present}
            history = [v for v in exact_by_night.values() if v is not None]
            move, overlap = movement(history)
            declared = [metrics[d]["quantization"] for d in present]
            fam_means = {fam: _mean([metrics[d][fam] for d in present if metrics[d][fam] is not None]) for fam in FAMILIES}
            rows_out.append({
                "tag": tag,
                "declared_quant": declared[-1] if declared else None,
                "declared_changed": len(set(declared)) > 1,
                "nights": len(present),
                "exact_by_night": exact_by_night,
                "exact_mean": _mean(history),
                "exact_sd": _sd(history),
                "exact_min": min(history) if history else None,
                "exact_max": max(history) if history else None,
                "movement": move,
                "movement_overlap": overlap,
                "movement_flag": (move is not None and len(history) >= MIN_NIGHTS_FOR_FLAG and abs(move) >= THRESHOLDS["MOVE_MIN"]),
                "families": fam_means,
                "self": self_agreement(tag, label, nights),
                "selfcheck": {d: sc_by_date[d].get(f"{label}|{tag}") for d in selfcheck_dates},
            })
        rows_out.sort(key=lambda r: (-(r["exact_mean"] if r["exact_mean"] is not None else -1), r["tag"]))
        models_out.append({
            "label": label,
            "slug": slug,
            "rules": sorted(rules[label]),
            "endpoints": rows_out,
            "families": family_noise(rows_out),
        })
    return {
        "dates": dates,
        "selfcheck_dates": selfcheck_dates,
        "thresholds": THRESHOLDS,
        "window": WINDOW,
        "models": models_out,
    }


def fmt(v: Any) -> str:
    if v is None:
        return "n/a"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:.1f}"
    return str(v)


def _short(date: str) -> str:
    return date[5:]


def render(date: str, t: dict[str, Any]) -> str:
    dates, sc_dates = t["dates"], t["selfcheck_dates"]
    L: list[str] = []
    L.append(f"# Bitdepth trend through {date}")
    L.append("")
    L.append(f"Nights found: {len(dates)} ({', '.join(dates)}). Self-check nights: {', '.join(sc_dates) if sc_dates else 'none'}.")
    L.append("Each row is one OpenRouter endpoint across every night it was listed. Exact % per night is the nightly scorecard figure (match against that night's reference). Family columns are mean graded accuracy against the generated answers. Self-agree is the endpoint's night-to-night agreement with itself on the fixed prompts. Self-check columns are the one-hour two-pass agreement on the nights it was measured. All numbers are percentages unless the column says otherwise.")
    L.append("")
    for m in t["models"]:
        L.append(f"## {m['label']} (`{m['slug']}`)")
        L.append("")
        L.append("### Exact match by night")
        L.append("")
        head = "| Endpoint | Declared quant | Nights | " + " | ".join(_short(d) for d in dates) + " | Mean | SD | Min | Max | Movement |"
        L.append(head)
        L.append("|" + "---|" * (len(dates) + 8))
        for e in m["endpoints"]:
            cells = " | ".join(fmt(e["exact_by_night"].get(d)) if d in e["exact_by_night"] else "-" for d in dates)
            quant = f"{e['declared_quant']} (changed)" if e["declared_changed"] else fmt(e["declared_quant"])
            mv = fmt(e["movement"])
            if e["movement"] is not None:
                mv = f"{e['movement']:+.1f}"
                if e["movement_flag"]:
                    mv += " *"
            L.append(f"| {e['tag']} | {quant} | {e['nights']} | {cells} | {fmt(e['exact_mean'])} | {fmt(e['exact_sd'])} | {fmt(e['exact_min'])} | {fmt(e['exact_max'])} | {mv} |")
        L.append("")
        L.append("### Graded accuracy and self-agreement (sorted by String, then Self-agree)")
        L.append("")
        sc_cols = "".join(f" Self-check {_short(d)} |" for d in sc_dates)
        L.append("| Endpoint | Math | JSON | String | Needle | Echo | Self-agree | Pairs | Self-agree Math | JSON | String | Needle | Echo |" + sc_cols)
        L.append("|" + "---|" * (13 + len(sc_dates)))
        ordered = sorted(m["endpoints"], key=lambda e: (
            -(e["families"]["string"] if e["families"]["string"] is not None else -1),
            -(e["self"]["agree_pct"] if e["self"]["agree_pct"] is not None else -1),
            e["tag"],
        ))
        for e in ordered:
            f = e["families"]
            s = e["self"]
            sc = "".join(
                f" {fmt(e['selfcheck'][d]['agree_pct'])} ({e['selfcheck'][d]['n']}) |" if e["selfcheck"].get(d) else " - |"
                for d in sc_dates
            )
            L.append(
                f"| {e['tag']} | {fmt(f['math'])} | {fmt(f['json'])} | {fmt(f['string'])} | {fmt(f['needle'])} | {fmt(f['echo'])} | "
                f"{fmt(s['agree_pct'])} | {s['pairs']} | "
                + " | ".join(fmt(s["by_family"][fam]["agree_pct"]) for fam in FAMILIES)
                + " |" + sc
            )
        L.append("")
        L.append("### Noise floor by family (night-to-night)")
        L.append("")
        L.append("| Family | Endpoints | Median self-agree | P75 disagreement | Noise floor | Stable |")
        L.append("|---|---|---|---|---|---|")
        for fam in FAMILIES:
            fn = m["families"][fam]
            L.append(f"| {fam} | {fn['endpoints']} | {fmt(fn['median_agree_pct'])} | {fmt(fn['p75_disagree_pct'])} | {fmt(fn['noise_floor'])} | {fmt(fn['stable'])} |")
        L.append("")
        L.append(f"Reference rule(s) seen: {'; '.join(m['rules'])}.")
        L.append("")
    L.append("## Footer")
    L.append("")
    L.append(f"- Nights found: {len(dates)}. Self-check nights found: {len(sc_dates)} ({', '.join(sc_dates) if sc_dates else 'none'}).")
    L.append("- Self-agree: for each pair of consecutive nights the endpoint was listed, each fixed prompt with an ok row on both nights counts once, and agrees when the stripped outputs are equal word for word. Fresh prompts are excluded because they change nightly. Pairs is the count of such prompt-night pairs.")
    L.append(f"- Movement: mean exact % over the last {t['window']} nights minus the mean over the first {t['window']}; when fewer than {2 * t['window']} nights are present the two windows overlap. An asterisk marks an absolute movement at or above {t['thresholds']['MOVE_MIN']:.0f} points on at least {MIN_NIGHTS_FOR_FLAG} nights. Provisional; calibrate on 2026-11-10.")
    L.append(f"- Noise floor per family: 100 minus the 75th percentile across endpoints of night-to-night disagreement. Stable means the median endpoint self-agreement is at or above {t['thresholds']['STABLE_MIN']:.0f}. Provisional; calibrate on 2026-11-10.")
    L.append("- Self-check: two passes of the same fixed prompts one hour apart on the nights listed; the figure is the share of prompts whose two outputs were equal, with the prompt count in brackets.")
    L.append("- Declared quant is the latest night's declaration; (changed) means it differed on some night in the range.")
    L.append(f"- {FOOTER_LINE}")
    L.append("")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--runs", default="data/runs")
    ap.add_argument("--out", default="data/trend")
    args = ap.parse_args(argv)
    nights = load_nights(Path(args.runs), args.date)
    if not nights:
        print(f"no complete runs at or before {args.date}")
        return 2
    t = build(nights)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    md = out_dir / f"{args.date}.md"
    js = out_dir / f"{args.date}.json"
    md.write_text(render(args.date, t), encoding="utf-8")
    js.write_text(json.dumps(t, indent=1, ensure_ascii=False), encoding="utf-8")
    shutil.copyfile(md, out_dir / "latest.md")
    shutil.copyfile(js, out_dir / "latest.json")
    print(f"wrote {md} and {js} ({len(nights)} nights, self-check on {len(t['selfcheck_dates'])}), plus latest copies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
