"""Private rows packet for one recipient.

    python -m probe.packet --for "Requesty" --group buyer [--providers deepinfra,together]
                           [--date YYYY-MM-DD] [--runs data/runs] [--trend data/trend]
                           [--scorecards data/scorecard] [--out packets]

    python -m probe.packet --attestation --month 2026-11 --buyer "Requesty"
                           --providers together,nebius,amazon-bedrock,azure,google-vertex

The attestation form adds a dated cover, a monthly summary line per marked
endpoint (nights inside the floor out of nights run in that month) and the
proposal page from probe/templates/proposal.md as the last section.

Cuts the cross-night trend into a one-page Markdown packet plus a CSV for one
recipient: every endpoint of every probed model, with the recipient's own
providers marked and listed first (buyer), or the recipient's own endpoints
beside the reference endpoints (provider). Reads files only. It never calls the
network and never reads the key.

Packets are private and land in a folder git ignores. Nothing here is a finding
before the fourteen-night read. Numbers against a stated reference. Not a claim
about intent.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from probe.trend import fmt

GROUPS = ("buyer", "provider")
MARK = "▸"  # small right-pointing triangle, used to mark the recipient's rows
COLUMNS = [
    "model", "endpoint", "declared_quant", "nights", "exact_mean", "exact_sd",
    "string", "self_agree", "movement", "movement_flag", "price_in_per_m",
    "price_out_per_m", "marked",
]


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "recipient"


def provider_of(tag: str) -> str:
    return tag.split("/")[0]


def load_trend(trend_dir: Path, date: str | None) -> tuple[str, dict[str, Any]]:
    path = trend_dir / (f"{date}.json" if date else "latest.json")
    t = json.loads(path.read_text())
    return (date or t["dates"][-1]), t


def load_prices(runs_dir: Path, date: str) -> dict[str, dict[str, tuple[float, float]]]:
    """model label -> tag -> (usd per million in, usd per million out) for that night."""
    path = runs_dir / date / "endpoints.json"
    out: dict[str, dict[str, tuple[float, float]]] = {}
    if not path.exists():
        return out
    e = json.loads(path.read_text())
    for label, m in e.get("models", {}).items():
        out[label] = {}
        for ep in m.get("endpoints", []):
            pi, po = ep.get("price_in"), ep.get("price_out")
            if pi is None or po is None:
                continue
            out[label][ep["tag"]] = (round(pi * 1e6, 4), round(po * 1e6, 4))
    return out


def load_references(scorecard_dir: Path, date: str) -> dict[str, list[str]]:
    """model label -> reference endpoint tags, read from the scorecard footer."""
    path = scorecard_dir / f"{date}.md"
    refs: dict[str, list[str]] = {}
    if not path.exists():
        return refs
    label = None
    for line in path.read_text().splitlines():
        h = re.match(r"^## (\S+) \(`", line)
        if h:
            label = h.group(1)
            continue
        r = re.search(r"Reference endpoints: ([^.]+)\.", line)
        if r and label:
            refs[label] = [x.strip() for x in r.group(1).split(",") if x.strip()]
    return refs


def rows_for(model: dict[str, Any], prices: dict[str, tuple[float, float]], marked: set[str]) -> list[dict[str, Any]]:
    rows = []
    for e in model["endpoints"]:
        p = prices.get(e["tag"])
        rows.append({
            "model": model["label"],
            "endpoint": e["tag"],
            "declared_quant": e["declared_quant"],
            "nights": e["nights"],
            "exact_mean": e["exact_mean"],
            "exact_sd": e["exact_sd"],
            "string": e["families"].get("string"),
            "self_agree": e["self"]["agree_pct"],
            "movement": e["movement"],
            "movement_flag": e["movement_flag"],
            "price_in_per_m": p[0] if p else None,
            "price_out_per_m": p[1] if p else None,
            "marked": provider_of(e["tag"]) in marked or e["tag"] in marked,
        })
    return rows


def order(rows: list[dict[str, Any]], group: str, refs: list[str]) -> list[dict[str, Any]]:
    key = lambda r: -(r["exact_mean"] if r["exact_mean"] is not None else -1)  # noqa: E731
    if group == "buyer":
        mine = sorted([r for r in rows if r["marked"]], key=key)
        rest = sorted([r for r in rows if not r["marked"]], key=key)
        return mine + rest
    # provider: the recipient's own rows only. Other endpoints appear as a field
    # summary (top, median, bottom) without names, so nothing publishes early.
    return sorted([r for r in rows if r["marked"]], key=key)


def field_summary(rows: list[dict[str, Any]], field: str) -> str:
    xs = sorted([r[field] for r in rows if r[field] is not None], reverse=True)
    if not xs:
        return "n/a"
    mid = xs[len(xs) // 2] if len(xs) % 2 else (xs[len(xs) // 2 - 1] + xs[len(xs) // 2]) / 2
    return f"top {xs[0]:.1f}, median {mid:.1f}, bottom {xs[-1]:.1f}"


def rank(rows: list[dict[str, Any]], field: str, endpoint: str) -> tuple[int, int] | None:
    scored = [r for r in rows if r[field] is not None]
    scored.sort(key=lambda r: -r[field])
    for i, r in enumerate(scored, 1):
        if r["endpoint"] == endpoint:
            return i, len(scored)
    return None


def _money(v: float | None) -> str:
    return "-" if v is None else f"{v:.2f}"


def _mv(r: dict[str, Any]) -> str:
    if r["movement"] is None:
        return "n/a"
    s = f"{r['movement']:+.1f}"
    return s + " *" if r["movement_flag"] else s


def _grade_col(m: dict[str, Any]) -> str:
    """The column that separates endpoints on this model, from the same rule the public table uses."""
    from probe.emit import primary_columns
    return "string" if primary_columns(m.get("slug", ""), m.get("families", {}))[0] == "string" else "exact_mean"


def _col_name(field: str) -> str:
    return "String" if field == "string" else "Exact"


def headlines(name: str, group: str, nights: int, per_model: list[dict[str, Any]]) -> list[str]:
    """Three to five sentences, computed from the rows, that say what the tables show for this recipient.

    Only ranks, spreads, prices and movement. Nothing about why.
    """
    out: list[str] = []
    for pm in per_model:
        m, all_rows = pm["model"], pm["all_rows"]
        mine = [r for r in pm["rows"] if r["marked"]]
        field = _grade_col(m)
        col = _col_name(field)
        scored = sorted([r for r in all_rows if r[field] is not None], key=lambda r: -r[field])
        if not scored:
            continue
        n = len(scored)
        label = m["label"]
        if group == "buyer":
            if not mine:
                out.append(f"{label}: none of the providers {name} lists serves this model on OpenRouter; the field of {n} runs from {scored[0]['endpoint']} {scored[0][field]:.1f} to {scored[-1]['endpoint']} {scored[-1][field]:.1f} by {col}.")
                continue
            ms = sorted([r for r in mine if r[field] is not None], key=lambda r: -r[field])
            if not ms:
                continue
            best, worst = ms[0], ms[-1]
            rb, rw = rank(all_rows, field, best["endpoint"]), rank(all_rows, field, worst["endpoint"])
            if len(ms) == 1:
                out.append(f"{label}: {best['endpoint']} scores {best[field]:.1f} by {col}, {rb[0]} of {n} in the field (top {scored[0][field]:.1f}, bottom {scored[-1][field]:.1f}).")
            else:
                spread = best[field] - worst[field]
                out.append(f"{label}: your {len(ms)} endpoints run from {best['endpoint']} {best[field]:.1f} ({rb[0]} of {n}) to {worst['endpoint']} {worst[field]:.1f} ({rw[0]} of {n}) by {col}, a {spread:.1f} point spread under one model name.")
            priced = [r for r in ms if r["price_out_per_m"] is not None]
            if len(priced) >= 2:
                dear = max(priced, key=lambda r: r["price_out_per_m"])
                cheap = min(priced, key=lambda r: r["price_out_per_m"])
                if dear is not cheap:
                    verdict = "and scores higher" if dear[field] > cheap[field] else "and scores lower" if dear[field] < cheap[field] else "and scores the same"
                    out.append(f"{label} price: {dear['endpoint']} costs ${dear['price_out_per_m']:.2f} per million output against {cheap['endpoint']} at ${cheap['price_out_per_m']:.2f} {verdict} by {col} ({dear[field]:.1f} vs {cheap[field]:.1f}).")
        else:
            for r in sorted(mine, key=lambda r: r["endpoint"]):
                re_, rs = rank(all_rows, "exact_mean", r["endpoint"]), rank(all_rows, "string", r["endpoint"])
                if re_ and rs:
                    out.append(f"{label}: {r['endpoint']} is {re_[0]} of {re_[1]} by Exact and {rs[0]} of {rs[1]} by String (field top {scored[0][field]:.1f}, bottom {scored[-1][field]:.1f} by {col}).")
        moved_mine = [r for r in mine if r["movement_flag"]]
        moved_field = [r for r in all_rows if r["movement_flag"]]
        if moved_mine:
            out.append(f"{label} movement: " + "; ".join(f"{r['endpoint']} moved {r['movement']:+.1f} points between the first and last three nights" for r in moved_mine) + ".")
        elif moved_field and group == "buyer":
            who = ", ".join(f"{r['endpoint']} {r['movement']:+.1f}" for r in moved_field)
            out.append(f"{label} movement: none of your endpoints moved more than the flag threshold in {nights} nights; {len(moved_field)} in the field did ({who}).")
    return out


def render(name: str, group: str, date: str, t: dict[str, Any], per_model: list[dict[str, Any]], providers: list[str]) -> str:
    dates = t["dates"]
    span = f"{dates[0]} to {dates[-1]}"
    L: list[str] = []
    L.append(f"# Bitdepth rows for {name}")
    L.append("")
    L.append(f"Prepared {date}. Private to {name}; please do not forward. {len(dates)} nights ({span}), read on 2026-11-10. Each endpoint's state below is the one the public table will show.")
    L.append("")
    heads = headlines(name, group, len(dates), per_model)
    if heads:
        L.append("## What the rows say")
        L.append("")
        for h in heads:
            L.append(f"- {h}")
        L.append("")
    L.append("## What the numbers are")
    L.append("")
    L.append("- Each row is one OpenRouter endpoint serving the named model, probed every night with the same prompt set (math, JSON, string, needle, echo families).")
    L.append("- Exact: mean share of prompts, over the nights listed, where the endpoint's output matched the reference output for that prompt. SD is the night-to-night standard deviation. The reference rule is stated under each table.")
    L.append("- String: graded accuracy on the string family against the generated answer. It does not depend on the reference, so it reads the same whatever the other endpoints do.")
    L.append("- Self-agree: how often the endpoint agrees with its own previous output on the fixed prompts, night to night. It is the noise floor the other columns sit on.")
    L.append(f"- Movement: mean of the last {t['window']} nights minus the first {t['window']}. An asterisk marks a move past {t['thresholds']['MOVE_MIN']:.0f} points.")
    L.append("- State: outside when the endpoint agrees with itself more than 15 points more than it agrees with the reference, or when it sits more than 8 points under the median of endpoints with seven or more nights on the model's primary column. Under seven nights is no grade yet.")
    L.append(f"- Price: OpenRouter list price on {date}, USD per million tokens, input and output.")
    L.append("- Numbers describe outputs against the stated reference and nothing else.")
    if providers:
        if group == "buyer":
            L.append(f"- Rows marked {MARK} are endpoints run by the providers {name} lists: {', '.join(providers)}. They are listed first.")
        else:
            L.append(f"- Only {name}'s own endpoints are listed. The rest of the field appears as top, median and bottom without names; every endpoint sees its own rows before any name is published.")
    L.append("")
    for pm in per_model:
        m, rows, refs, rule = pm["model"], pm["rows"], pm["refs"], pm["rule"]
        L.append(f"## {m['label']} (`{m['slug']}`)")
        L.append("")
        if not rows:
            L.append(f"No endpoint of this model matched {name}.")
            L.append("")
            continue
        L.append("| | Endpoint | Declared quant | Nights | Exact | SD | String | Self-agree | Movement | $/M in | $/M out |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            mark = MARK if r["marked"] else ""
            L.append(f"| {mark} | {r['endpoint']} | {fmt(r['declared_quant'])} | {r['nights']} | {fmt(r['exact_mean'])} | {fmt(r['exact_sd'])} | {fmt(r['string'])} | {fmt(r['self_agree'])} | {_mv(r)} | {_money(r['price_in_per_m'])} | {_money(r['price_out_per_m'])} |")
        L.append("")
        total = len(m["endpoints"])
        if group == "buyer":
            L.append(f"Reference rule: {rule}. Reference endpoints on {date}: {', '.join(refs) if refs else 'see scorecard'}. Endpoints serving this model: {total}.")
        else:
            all_rows = pm["all_rows"]
            L.append(f"Reference rule: {rule}. Endpoints serving this model: {total}. Field by Exact: {field_summary(all_rows, 'exact_mean')}. Field by String: {field_summary(all_rows, 'string')}. Field by Self-agree: {field_summary(all_rows, 'self_agree')}.")
        fam = m.get("families", {})
        unstable = [f for f in ("math", "json", "string") if fam.get(f) and not fam[f]["stable"]]
        floors = ", ".join(f"{f} {fam[f]['noise_floor']:.1f}" for f in ("math", "json", "string", "needle", "echo") if fam.get(f))
        L.append(f"Family noise floor (median self-agreement, lower quartile): {floors}.")
        if _grade_col(m) == "string":
            L.append("On this model the endpoints do not agree with themselves on math wording from night to night, so Exact mostly measures wording. Read String and Self-agree first; Exact second.")
        else:
            note = f"Families below the stability threshold on this model: {', '.join(unstable)}. " if unstable else ""
            L.append(note + "Exact is the column that separates endpoints on this model.")
        if group == "provider":
            all_rows = pm["all_rows"]
            for r in [x for x in rows if x["marked"]]:
                re_ = rank(all_rows, "exact_mean", r["endpoint"])
                rs = rank(all_rows, "string", r["endpoint"])
                st = public_state(m_label_of(pm, rows), r["endpoint"])
                if re_ and rs:
                    L.append(f"{r['endpoint']}: {re_[0]} of {re_[1]} by Exact, {rs[0]} of {rs[1]} by String."
                             + (f" State: {STATE_WORDS.get(st, st)}." if st else ""))
        L.append("")
    L.append("## Next")
    L.append("")
    if group == "buyer":
        L.append("Tell me which providers you route to and I will cut this to those rows, or name a model pair you would rather see and it joins the nightly run. The raw record behind every number is kept and hashed.")
    else:
        L.append("If any figure here is wrong, say which and I will check the raw record and correct it before publication. Publication follows the same rules for every endpoint.")
    L.append("")
    L.append("Numbers against a stated reference. Not a claim about intent.")
    L.append("")
    return "\n".join(L)


def build(name: str, group: str, providers: list[str], date: str | None, runs_dir: Path, trend_dir: Path, scorecard_dir: Path) -> tuple[str, str, list[dict[str, Any]]]:
    date, t = load_trend(trend_dir, date)
    prices = load_prices(runs_dir, date)
    refs = load_references(scorecard_dir, date)
    marked = {p.strip().lower() for p in providers if p.strip()}
    per_model = []
    csv_rows: list[dict[str, Any]] = []
    for m in t["models"]:
        all_rows = rows_for(m, prices.get(m["label"], {}), marked)
        rows = order(all_rows, group, refs.get(m["label"], []))
        per_model.append({
            "model": m,
            "rows": rows,
            "all_rows": all_rows,
            "refs": refs.get(m["label"], []),
            "rule": m["rules"][-1] if m.get("rules") else "see scorecard",
        })
        csv_rows.extend(rows)
    return date, render(name, group, date, t, per_model, providers), csv_rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r[k] is None else r[k]) for k in COLUMNS})


STATE_WORDS = {"within": "within the pack", "outside": "outside the pack", "no_data": "no grade yet (under seven nights)", "stale": "stale"}
PUBLIC_DIR = Path("data/public/v1/or")


def public_state(label: str | None, tag: str) -> str | None:
    """The state data/public/v1 gives this endpoint, or None if there is no file."""
    if not label or not PUBLIC_DIR.exists():
        return None
    for f in PUBLIC_DIR.glob("*/*.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if d.get("label") != label:
            continue
        for e in d.get("endpoints", []):
            if e.get("tag") == tag:
                return e.get("state")
    return None


def m_label_of(pm: dict[str, Any], rows: list[dict[str, Any]]) -> str | None:
    if (pm.get("model") or {}).get("label"):
        return pm["model"]["label"]
    return rows[0].get("model") if rows else None


PROPOSAL = Path(__file__).parent / "templates" / "proposal.md"


def night_within(exact: float | None, self_agree: float | None) -> bool | None:
    """One night against the endpoint's own self-agreement, by the emit state rule."""
    from probe.emit import GAP_MAX
    if exact is None or self_agree is None:
        return None
    return (self_agree - exact) <= GAP_MAX


def attestation_summary(t: dict[str, Any], month: str, marked: set[str]) -> list[str]:
    out = []
    for m in t["models"]:
        for e in m["endpoints"]:
            if not (provider_of(e["tag"]) in marked or e["tag"] in marked):
                continue
            nights = {d: v for d, v in e.get("exact_by_night", {}).items() if d.startswith(month)}
            if not nights:
                continue
            ok = [night_within(v, e["self"]["agree_pct"]) for v in nights.values()]
            n_in = sum(1 for x in ok if x)
            out.append(f"| {m['label']} | {e['tag']} | {fmt(e['declared_quant'])} | {n_in} of {len(nights)} | {fmt(e['self']['agree_pct'])} |")
    return out


def render_attestation(name: str, month: str, date: str, t: dict[str, Any], marked: set[str], body: str, proposal: str | None) -> str:
    month_dates = [d for d in t["dates"] if d.startswith(month)]
    L = [
        f"# Bitdepth attestation: {name}, {month}",
        "",
        f"- Buyer: {name}",
        f"- Month: {month}",
        f"- Models: {', '.join(m['slug'] for m in t['models'])}",
        f"- Nights counted in the month: {len(month_dates)}" + (f" ({month_dates[0]} to {month_dates[-1]})" if month_dates else ""),
        f"- Generated: {date}",
        "",
        "## Monthly summary",
        "",
        "A night counts as inside the floor when the endpoint's agreement with the reference that night is within "
        "10 points of its own night-to-night self-agreement. Provisional rule; calibrated on 2026-11-10.",
        "",
        "| Model | Endpoint | Declared quant | Nights inside the floor | Self-agree |",
        "|---|---|---|---|---|",
    ]
    rows = attestation_summary(t, month, marked)
    L += rows if rows else ["| | No marked endpoint has nights in this month. | | | |"]
    L += ["", "---", ""]
    body = body.split("\n", 1)[1] if body.startswith("# ") else body  # drop the packet's own title
    L.append(body.rstrip())
    L += ["", "---", ""]
    if proposal:
        L.append(proposal.replace("{Company}", name).rstrip())
    else:
        L.append("PROPOSAL COPY PENDING")
    L.append("")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--for", "--buyer", dest="name", required=True, help="recipient name, used in the title and file name")
    ap.add_argument("--attestation", action="store_true", help="monthly dated attestation for a buyer")
    ap.add_argument("--month", default=None, help="YYYY-MM for --attestation; default the trend date's month")
    ap.add_argument("--group", choices=GROUPS, default="buyer")
    ap.add_argument("--providers", default="", help="comma list of provider slugs or endpoint tags to mark (e.g. deepinfra,together,baseten/fp4)")
    ap.add_argument("--date", default=None, help="trend date; default latest")
    ap.add_argument("--runs", default="data/runs")
    ap.add_argument("--trend", default="data/trend")
    ap.add_argument("--scorecards", default="data/scorecard")
    ap.add_argument("--out", default="packets")
    a = ap.parse_args(argv)
    providers = [p.strip() for p in a.providers.split(",") if p.strip()]
    if a.group == "provider" and not providers:
        print("a provider packet needs --providers", file=sys.stderr)
        return 2
    date, md, rows = build(a.name, a.group, providers, a.date, Path(a.runs), Path(a.trend), Path(a.scorecards))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    stem = f"{slugify(a.name)}-{a.group}-{date}"
    if a.attestation:
        if not providers:
            print("an attestation needs --providers", file=sys.stderr)
            return 2
        _, t = load_trend(Path(a.trend), a.date)
        month = a.month or date[:7]
        proposal = PROPOSAL.read_text() if PROPOSAL.exists() else None
        md = render_attestation(a.name, month, date, t, {p.lower() for p in providers}, md, proposal)
        stem = f"{slugify(a.name)}-attestation-{month}"
        md_path = out / f"{stem}.md"
        md_path.write_text(md)
        write_csv(out / f"{stem}.csv", rows)
        print(md_path)
        print(out / f"{stem}.csv")
        if shutil.which("pandoc"):
            pdf = out / f"{stem}.pdf"
            r = subprocess.run(["pandoc", str(md_path), "-o", str(pdf)], capture_output=True)
            if r.returncode == 0:
                print(pdf)
        return 0
    (out / f"{stem}.md").write_text(md)
    write_csv(out / f"{stem}.csv", rows)
    print(out / f"{stem}.md")
    print(out / f"{stem}.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
