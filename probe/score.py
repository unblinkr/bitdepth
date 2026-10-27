"""Scorecard.

    python -m probe.score --date YYYY-MM-DD

Reads one night's run folder, builds the reference per prompt per model, computes the
metrics per endpoint, and writes data/scorecard/<date>.md plus latest.md.
"""

from __future__ import annotations

import argparse
import json
import shutil
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from probe import FULL_PRECISION
from probe.generators import grade, load_jsonl

SCORECARD_DIR = Path("data/scorecard")


def norm(text: str) -> str:
    return (text or "").strip()


def first_divergence(a: str, b: str) -> int:
    wa, wb = a.split(), b.split()
    for i, (x, y) in enumerate(zip(wa, wb)):
        if x != y:
            return i
    return min(len(wa), len(wb))


def build_reference(
    endpoints: list[dict[str, Any]], rows: list[dict[str, Any]]
) -> tuple[dict[str, str], str, int, list[str]]:
    """Return (reference by prompt_id, rule applied, no_reference count, reference tags)."""
    full = [e["tag"] for e in endpoints if e["quantization"] in FULL_PRECISION]
    if len(full) >= 2:
        ref_tags = full
        rule = "plurality among endpoints declaring bf16 or fp16"
    else:
        ref_tags = [e["tag"] for e in endpoints]
        rule = "plurality across all endpoints (fewer than two declare bf16 or fp16)"
    outputs: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        if r["status"] == "ok" and r["pinned_tag"] in ref_tags:
            outputs[r["prompt_id"]].append(norm(r["output"]))
    reference: dict[str, str] = {}
    no_ref = 0
    for pid, outs in outputs.items():
        common = Counter(outs).most_common(2)
        if len(common) == 1 or common[0][1] > common[1][1]:
            reference[pid] = common[0][0]
        else:
            no_ref += 1
    return reference, rule, no_ref, ref_tags


def _pct(num: int, den: int) -> float | None:
    return round(100.0 * num / den, 1) if den else None


def _median(xs: list[float]) -> float | None:
    return round(statistics.median(xs), 2) if xs else None


def endpoint_metrics(
    endpoint: dict[str, Any], rows: list[dict[str, Any]], reference: dict[str, str], prompts: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    mine = [r for r in rows if r["pinned_tag"] == endpoint["tag"]]
    considered = [r for r in mine if r["status"] != "skipped_budget"]
    ok = [r for r in mine if r["status"] == "ok"]
    matches = 0
    compared = 0
    divergences: list[float] = []
    ratios: list[float] = []
    for r in ok:
        ref = reference.get(r["prompt_id"])
        if ref is None:
            continue
        compared += 1
        out = norm(r["output"])
        if out == ref:
            matches += 1
        else:
            divergences.append(first_divergence(out, ref))
        if ref.split():
            ratios.append(len(out.split()) / len(ref.split()))
    fam_ok: dict[str, int] = Counter()
    fam_n: dict[str, int] = Counter()
    for r in ok:
        p = prompts.get(r["prompt_id"])
        if not p:
            continue
        fam_n[p["family"]] += 1
        if grade(p["family"], r["output"], p["answer"], p.get("schema")):
            fam_ok[p["family"]] += 1
    return {
        "tag": endpoint["tag"],
        "provider": endpoint["provider_name"],
        "quantization": endpoint["quantization"],
        "seed": "seed" in endpoint["supported_parameters"],
        "rows": len(considered),
        "ok": len(ok),
        "exact_pct": _pct(matches, compared),
        "compared": compared,
        "divergence_median": _median(divergences),
        "length_ratio_median": _median(ratios),
        "math": _pct(fam_ok["math"], fam_n["math"]),
        "json": _pct(fam_ok["json"], fam_n["json"]),
        "string": _pct(fam_ok["string"], fam_n["string"]),
        "needle": _pct(fam_ok["needle"], fam_n["needle"]),
        "echo": _pct(fam_ok["echo"], fam_n["echo"]),
        "error_pct": _pct(sum(1 for r in considered if r["status"] == "error"), len(considered)),
        "misrouted": sum(1 for r in considered if r["status"] == "misrouted"),
        "truncated": sum(1 for r in ok if r.get("finish_reason") == "length"),
        "latency_ms_median": _median([float(r["latency_ms"]) for r in ok if r.get("latency_ms")]),
        "cost_usd": round(sum(r["cost_usd"] for r in considered), 4),
    }


def noise_floor(sc_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Two-pass agreement per (model, tag)."""
    by_key: dict[tuple[str, str, str], dict[str, str]] = defaultdict(dict)
    for r in sc_rows:
        if r["status"] == "ok":
            by_key[(r["model"], r["pinned_tag"], r["prompt_id"])][r.get("pass", "?")] = norm(r["output"])
    agg: dict[str, dict[str, Any]] = {}
    for (model, tag, _pid), passes in by_key.items():
        if "A" in passes and "B" in passes:
            k = f"{model}|{tag}"
            a = agg.setdefault(k, {"model": model, "tag": tag, "n": 0, "agree": 0})
            a["n"] += 1
            if passes["A"] == passes["B"]:
                a["agree"] += 1
    for a in agg.values():
        a["agree_pct"] = _pct(a["agree"], a["n"])
    return agg


def fmt(v: Any) -> str:
    if v is None:
        return "n/a"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:.1f}" if abs(v) >= 10 else f"{v:.2f}"
    return str(v)


def render(date: str, run: dict[str, Any], per_model: list[dict[str, Any]], nf: dict[str, dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append(f"# Bitdepth scorecard {date}")
    lines.append("")
    lines.append(f"Run `{run.get('run_id')}`, source `{run.get('source')}`, started {run.get('started')}, finished {run.get('finished')}.")
    lines.append("Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.")
    lines.append("")
    for m in per_model:
        lines.append(f"## {m['label']} (`{m['slug']}`)")
        lines.append("")
        lines.append("| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for e in m["endpoints"]:
            lines.append(
                f"| {e['tag']} | {e['quantization']} | {fmt(e['seed'])} | {fmt(e['exact_pct'])} | {e['compared']} | "
                f"{fmt(e['divergence_median'])} | {fmt(e['length_ratio_median'])} | {fmt(e['math'])} | {fmt(e['json'])} | "
                f"{fmt(e['string'])} | {fmt(e['needle'])} | {fmt(e['echo'])} | {fmt(e['error_pct'])} | {e['misrouted']} | "
                f"{e['truncated']} | {fmt(e['latency_ms_median'])} | {e['cost_usd']:.4f} |"
            )
        lines.append("")
        lines.append(f"Reference rule: {m['rule']}. Reference endpoints: {', '.join(m['ref_tags'])}. Prompts with no plurality (excluded from exact match): {m['no_reference']}.")
        lines.append("")
    if nf:
        lines.append("## Noise floor (self-check, two passes one hour apart)")
        lines.append("")
        lines.append("| Model | Endpoint | Prompts | Agreement % |")
        lines.append("|---|---|---|---|")
        for a in sorted(nf.values(), key=lambda x: (x["model"], -(x["agree_pct"] or 0))):
            lines.append(f"| {a['model']} | {a['tag']} | {a['n']} | {fmt(a['agree_pct'])} |")
        lines.append("")
    lines.append("## Footer")
    lines.append("")
    s = run.get("summary", {})
    lines.append(f"- Rows: {s.get('rows')}; errors {s.get('errors')}; misrouted {s.get('misrouted')}; truncated (finish_reason length) {s.get('truncated')}; skipped by runtime budget stop {s.get('skipped_budget')}.")
    lines.append(f"- Prompts kept {run.get('prompts', {}).get('kept')} of {run.get('prompts', {}).get('fixed', 0) + run.get('prompts', {}).get('fresh', 0)}; dropped for budget: {run.get('prompts', {}).get('dropped')} ({', '.join(run.get('dropped_prompt_ids', [])[:8])}{'...' if len(run.get('dropped_prompt_ids', [])) > 8 else ''}).")
    lines.append(f"- Estimate before sending: ${run.get('estimate', {}).get('usd')}; billed: ${run.get('total_billed_usd', s.get('billed_cost_usd'))}; cap ${run.get('cap_usd')}; runtime budget stop: {run.get('runtime_budget_stop')}.")
    lines.append("- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.")
    lines.append("- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.")
    lines.append("- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.")
    lines.append("- Numbers describe outputs against a stated reference and nothing else.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    args = ap.parse_args(argv)
    rd = Path("data/runs") / args.date
    if not (rd / "run.json").exists():
        print(f"no run.json for {args.date}")
        return 2
    run = json.loads((rd / "run.json").read_text(encoding="utf-8"))
    if not (rd / "responses.jsonl").exists():
        print(f"no responses for {args.date} (aborted run); writing a stub scorecard")
        per_model: list[dict[str, Any]] = []
        nf: dict[str, dict[str, Any]] = {}
    else:
        endpoints_doc = json.loads((rd / "endpoints.json").read_text(encoding="utf-8"))
        prompts = {p["id"]: p for p in load_jsonl(rd / "prompts.jsonl")}
        rows = load_jsonl(rd / "responses.jsonl")
        per_model = []
        for label, m in endpoints_doc["models"].items():
            mrows = [r for r in rows if r["model"] == label]
            reference, rule, no_ref, ref_tags = build_reference(m["endpoints"], mrows)
            eps = [endpoint_metrics(e, mrows, reference, prompts) for e in m["endpoints"]]
            eps.sort(key=lambda x: (-(x["exact_pct"] if x["exact_pct"] is not None else -1), x["tag"]))
            per_model.append({"label": label, "slug": m["slug"], "rule": rule, "no_reference": no_ref, "ref_tags": ref_tags, "endpoints": eps})
        nf = noise_floor(load_jsonl(rd / "selfcheck.jsonl")) if (rd / "selfcheck.jsonl").exists() else {}
    text = render(args.date, run, per_model, nf)
    SCORECARD_DIR.mkdir(parents=True, exist_ok=True)
    out = SCORECARD_DIR / f"{args.date}.md"
    out.write_text(text, encoding="utf-8")
    shutil.copyfile(out, SCORECARD_DIR / "latest.md")
    print(f"wrote {out} and latest.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
