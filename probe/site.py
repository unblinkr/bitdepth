"""Static leaderboard, per-model pages, charts page, share images and badges for bitdepth.dev.

    python -m probe.site --preview      # placeholder data into site/lab/ (noindex, unlinked)
    python -m probe.site --live         # real data from data/public/v1 into site/

Reads files only (data/public/v1). Every page is plain HTML with the figures in the
markup, so a crawler or an answer engine reads the table without running script.
Charts are inline SVG drawn here. The share buttons (site/assets/share.js) turn a
chart card into a PNG in the browser; the per-model share card is a PNG written
here with Pillow so that X, Reddit and Slack previews carry the headline.

Preview mode replaces every provider name with a letter and every number with a
seeded synthetic value. Nothing in site/lab/ is a measurement.

Ranking: endpoints in state "within" with at least 7 nights, by quality-adjusted
price: blended price ((3 x input + output) / 4, per million tokens) divided by
agreement with the reference on the model's primary column. First-look endpoints
(fewer than 7 nights) carry their night count and no rank. Endpoints in state
"outside" sit below a divider. The headline is composed here from those rows, so
no sentence on a page says more than the numbers under it.
"""

from __future__ import annotations

import argparse
import copy
import json
import random
import shutil
import sys
from statistics import median
from datetime import date, timedelta
from html import escape
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path(__file__).resolve().parent / "assets" / "fonts"
MIN_NIGHTS = 7
STALE_DAYS = 3
SITE = "https://bitdepth.dev"

PINE = "#1E3B2F"
PINE_DEEP = "#14291F"
CREAM = "#F4EEE2"
PANEL = "#FBF8F1"
GOLD = "#B8902A"
BURG = "#7A2A35"
MUTED = "#4E5B53"
LINE = "#D9CFB8"
SAGE = "#BFCBC2"

STATE_LABEL = {
    "within": "Matches reference",
    "outside": "Outside reference",
    "no_data": "First look",
    "stale": "Stale",
}

# ---------------------------------------------------------------- data


def load(data_dir: Path) -> dict[str, Any]:
    index = json.loads((data_dir / "index.json").read_text())
    models = []
    for m in index["models"]:
        models.append(json.loads((data_dir / m["path"]).read_text()))
    drift_p = data_dir / "drift.json"
    drift = json.loads(drift_p.read_text()) if drift_p.exists() else {"items": []}
    return {"index": index, "models": models, "drift": drift}


def placeholder(data: dict[str, Any], seed: int = 7) -> dict[str, Any]:
    """Same shape, letters for providers, synthetic numbers. Never a measurement."""
    rnd = random.Random(seed)
    out = copy.deepcopy(data)
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    names = letters + [a + b for a in letters for b in letters]
    for m in out["models"]:
        name_of: dict[str, str] = {}
        for e in m["endpoints"]:
            p = e["provider_slug"]
            if p not in name_of:
                name_of[p] = "host-" + names[len(name_of)].lower()
            rest = e["tag"].split("/", 1)[1] if "/" in e["tag"] else ""
            e["provider_slug"] = name_of[p]
            e["tag"] = name_of[p] + ("/" + rest if rest else "")
            base = rnd.uniform(55, 97)
            e["exact"] = round(base, 1)
            e["string"] = round(base - rnd.uniform(5, 20), 1)
            e["self_agree"] = None if e.get("self_agree") is None else round(min(99.0, base + rnd.uniform(-2, 14)), 1)
            e["price_in_per_m"] = round(rnd.uniform(0.08, 1.8), 3)
            e["price_out_per_m"] = round(e["price_in_per_m"] * rnd.uniform(1.8, 4.5), 3)
            if e.get("movement") is not None:
                e["movement"] = round(rnd.uniform(-12, 12), 1)
                e["movement_flag"] = abs(e["movement"]) > 10
            if e["state"] in ("within", "outside"):
                e["state"] = "outside" if rnd.random() < 0.22 else "within"
            series = e.get("nightly_exact") or []
            for pt in series:
                pt["exact"] = round(max(30.0, min(100.0, base + rnd.uniform(-6, 6))), 1)
        m["placeholder"] = True
    for it in out["drift"].get("items", []):
        it["tag"] = "host-" + rnd.choice(letters).lower()
        it["movement"] = round(rnd.uniform(-20, -10), 1)
    out["placeholder"] = True
    return out


def slug_of(m: dict[str, Any]) -> str:
    return m["model"].split("/", 1)[1]


def nice_name(m: dict[str, Any]) -> str:
    s = slug_of(m)
    known = {
        "gpt-oss-120b": "gpt-oss-120b",
        "deepseek-v4-pro": "DeepSeek V4 Pro",
        "deepseek-v4.1-flash-1017": "DeepSeek V4.1 Flash",
        "mistral-large-4-0": "Mistral Large 4",
        "glm-5.3-flash": "GLM 5.3 Flash",
        "gemma-4-31b-it": "Gemma 4 31B",
        "mimo-v2.6-pro": "MiMo V2.6 Pro",
    }
    return known.get(s, s.replace("-", " ").title())


def primary(m: dict[str, Any]) -> str:
    cols = m.get("primary_columns") or ["exact"]
    return cols[0]


def blended(e: dict[str, Any]) -> float | None:
    pi, po = e.get("price_in_per_m"), e.get("price_out_per_m")
    if pi is None or po is None:
        return None
    return (3 * pi + po) / 4


def agreement(m: dict[str, Any], e: dict[str, Any]) -> float | None:
    v = e.get(primary(m))
    return None if v is None else float(v)


def qa_price(m: dict[str, Any], e: dict[str, Any]) -> float | None:
    b, a = blended(e), agreement(m, e)
    if b is None or not a:
        return None
    return b / (a / 100.0)


def drift_word(e: dict[str, Any]) -> str:
    mv = e.get("movement")
    if mv is None:
        return "n/a"
    if not e.get("movement_flag"):
        return "stable"
    return "improving" if mv > 0 else "worsening"


def model_nights(m: dict[str, Any]) -> int:
    return max((e.get("nights") or 0 for e in m["endpoints"]), default=0)


def is_first_look(m: dict[str, Any]) -> bool:
    return model_nights(m) < MIN_NIGHTS


def rows(m: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    ranked, first, outside = [], [], []
    for e in m["endpoints"]:
        st = e.get("state")
        if st == "within" and (e.get("nights") or 0) >= MIN_NIGHTS:
            ranked.append(e)
        elif st == "outside":
            outside.append(e)
        else:
            first.append(e)
    big = float("inf")
    ranked.sort(key=lambda e: (qa_price(m, e) or big))
    first.sort(key=lambda e: (qa_price(m, e) or big))
    outside.sort(key=lambda e: (qa_price(m, e) or big))
    return {"ranked": ranked, "first": first, "outside": outside}


def last_listed(e: dict[str, Any]) -> str | None:
    ds = [p["date"] for p in (e.get("nightly_exact") or []) if p.get("date")]
    return max(ds) if ds else None


def delisted(m: dict[str, Any], e: dict[str, Any]) -> str | None:
    """Date of the last night an endpoint was listed, when it has dropped off OpenRouter's listing."""
    last, as_of = last_listed(e), m.get("as_of")
    if not last or not as_of:
        return None
    gap = (date.fromisoformat(as_of) - date.fromisoformat(last)).days
    return last if gap > STALE_DAYS else None


def lead_order(ms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Graded models first, the one with the most endpoints outside the reference leading."""
    def k(m: dict[str, Any]) -> tuple:
        return (is_first_look(m), -len(rows(m)["outside"]))
    return sorted(ms, key=k)


def drift_pick(ms: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]] | None:
    """The endpoint with the largest flagged fall that now sits outside the reference."""
    best = None
    for m in ms:
        if is_first_look(m):
            continue
        for e in m["endpoints"]:
            mv = e.get("movement")
            if e.get("state") == "outside" and e.get("movement_flag") and mv is not None and mv < 0:
                if best is None or mv < best[1].get("movement"):
                    best = (m, e)
    return best


def chart_drift(m: dict[str, Any], e: dict[str, Any], cid: str, w: int = 760, h: int = 300) -> str:
    """One endpoint's exact match each night against the median of every other endpoint on the model."""
    mine = {p["date"]: p["exact"] for p in (e.get("nightly_exact") or []) if p.get("exact") is not None}
    others: dict[str, list[float]] = {}
    for o in m["endpoints"]:
        if o is e:
            continue
        for p in o.get("nightly_exact") or []:
            if p.get("exact") is not None:
                others.setdefault(p["date"], []).append(p["exact"])
    days = sorted(set(mine) | set(others))
    if len(days) < 2:
        return '<p class="muted">No nightly series yet.</p>'
    days = _dates(days[0], days[-1])
    med = {d: median(v) for d, v in others.items() if v}
    vals = list(mine.values()) + list(med.values())
    lo = max(0, int(min(vals) // 10 * 10) - 10)
    pl, pr, pt, pb = 40, 30, 14, 34
    iw, ih = w - pl - pr, h - pt - pb

    def X(i: int) -> float:
        return pl + (iw * i / max(1, len(days) - 1))

    def Y(v: float) -> float:
        return pt + ih * (1 - (v - lo) / (100 - lo))

    g = []
    for t in range(lo, 101, 10 if 100 - lo <= 50 else 20):
        y = Y(t)
        g.append(f'<line x1="{pl}" y1="{y:.1f}" x2="{w - pr}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1"/>'
                 f'<text x="{pl - 6}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{t}</text>')
    for i in sorted({0, len(days) // 2, len(days) - 1}):
        g.append(f'<text x="{X(i):.1f}" y="{h - 12}" text-anchor="middle" font-size="11" fill="{MUTED}">{escape(_md(days[i]))}</text>')

    def line(series: dict[str, float], col: str, sw: float, label: str) -> None:
        segs, cur = [], []
        for i, d in enumerate(days):
            if d in series:
                cur.append(f"{X(i):.1f},{Y(series[d]):.1f}")
            elif cur:
                segs.append(cur)
                cur = []
        if cur:
            segs.append(cur)
        for seg in segs:
            if len(seg) == 1:
                x, y = seg[0].split(",")
                g.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{col}"><title>{escape(label)}</title></circle>')
            else:
                g.append(f'<polyline points="{" ".join(seg)}" fill="none" stroke="{col}" stroke-width="{sw}"><title>{escape(label)}</title></polyline>')
        last = max((i for i, d in enumerate(days) if d in series), default=None)
        if last is not None:
            g.append(f'<text x="{X(last) - 4:.1f}" y="{Y(series[days[last]]) - 7:.1f}" text-anchor="end" font-size="11" fill="{col}">{escape(label)}</text>')

    line(med, PINE, 1.6, f"median of the other {len(m['endpoints']) - 1} endpoints")
    line(mine, BURG, 2.4, e["tag"])
    desc = f"Exact match with the reference each night: {e['tag']} against the median of the other endpoints serving {nice_name(m)}."
    return (f'<svg id="{cid}" viewBox="0 0 {w} {h}" width="100%" role="img" aria-labelledby="{cid}-d" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">'
            f'<desc id="{cid}-d">{escape(desc)}</desc>{"".join(g)}</svg>')


def drift_sentence(m: dict[str, Any], e: dict[str, Any]) -> str:
    pts = [p for p in (e.get("nightly_exact") or []) if p.get("exact") is not None]
    first3 = [p["exact"] for p in pts[:3]]
    last3 = [p["exact"] for p in pts[-3:]]
    a, b = sum(first3) / len(first3), sum(last3) / len(last3)
    return (f"On {nice_name(m)}, {e['tag']} matched the reference on {a:.0f}% of prompts over its first three nights "
            f"and {b:.0f}% over its last three. It now sits outside the reference.")


def outside_sentence(m: dict[str, Any]) -> str:
    r = rows(m)
    pc = primary(m)
    label = {"exact": "exact match", "string": "string match"}.get(pc, pc)
    inside = [agreement(m, e) for e in r["ranked"] if agreement(m, e) is not None]
    tags = ", ".join(e["tag"] for e in r["outside"])
    s = (f"On {nice_name(m)}, {len(r['outside'])} of {len(m['endpoints'])} endpoints sit outside the reference: {tags}.")
    if inside:
        s += f" Ranked endpoints run {min(inside):.0f} to {max(inside):.0f}% on {label}."
    return s


def money(v: float | None, digits: int = 2) -> str:
    if v is None:
        return "n/a"
    if v < 0.1:
        digits = 3
    return f"${v:.{digits}f}"


def pct(v: float | None) -> str:
    return "n/a" if v is None else f"{v:.1f}%"


def headline(m: dict[str, Any]) -> str:
    """One pasteable sentence, numbers against the reference only."""
    name = nice_name(m)
    r = rows(m)
    n = len(m["endpoints"])
    if is_first_look(m) or not r["ranked"]:
        k = model_nights(m)
        return (f"First look at {name}: {n} endpoints on OpenRouter, {k} night{'s' if k != 1 else ''} measured. "
                f"Grades start at {MIN_NIGHTS} nights.")
    best = r["ranked"][0]
    priced = [e for e in r["ranked"] + r["outside"] if blended(e) is not None]
    cheapest = min(priced, key=lambda e: blended(e)) if priced else best
    s = (f"On {name}, the cheapest endpoint that matches the reference is {best['tag']} "
         f"at {money(best.get('price_out_per_m'))} per million output tokens.")
    if cheapest is not best and cheapest.get("state") == "outside":
        s += (f" The cheapest listed, {cheapest['tag']} at {money(cheapest.get('price_out_per_m'))}, "
              f"sits outside the reference.")
    elif r["outside"]:
        s += f" {len(r['outside'])} of {n} endpoints sit outside the reference."
    else:
        s += f" All {len(r['ranked'])} graded endpoints match it."
    return s


# ---------------------------------------------------------------- charts (inline SVG)


def _dates(first: str, last: str) -> list[str]:
    d0, d1 = date.fromisoformat(first), date.fromisoformat(last)
    out = []
    while d0 <= d1:
        out.append(d0.isoformat())
        d0 += timedelta(days=1)
    return out


def chart_agreement(m: dict[str, Any], cid: str, w: int = 760, h: int = 300) -> str:
    """Exact match with the reference, each night, one line per endpoint. A missing
    night breaks the line and is marked on the axis."""
    series = [(e, {p["date"]: p["exact"] for p in (e.get("nightly_exact") or []) if p.get("exact") is not None}) for e in m["endpoints"]]
    all_d = sorted({d for _, s in series for d in s})
    if not all_d:
        return '<p class="muted">No nightly series yet.</p>'
    days = _dates(all_d[0], m.get("as_of", all_d[-1]))
    vals = [v for _, s in series for v in s.values()]
    lo = max(0, int(min(vals) // 10 * 10) - 10)
    pl, pr, pt, pb = 40, 14, 14, 34
    iw, ih = w - pl - pr, h - pt - pb

    def X(i: int) -> float:
        return pl + (iw * i / max(1, len(days) - 1))

    def Y(v: float) -> float:
        return pt + ih * (1 - (v - lo) / (100 - lo))

    g = []
    for t in range(lo, 101, 10 if 100 - lo <= 50 else 20):
        y = Y(t)
        g.append(f'<line x1="{pl}" y1="{y:.1f}" x2="{w - pr}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1"/>'
                 f'<text x="{pl - 6}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{t}</text>')
    for i in sorted({0, len(days) // 2, len(days) - 1}):
        g.append(f'<text x="{X(i):.1f}" y="{h - 12}" text-anchor="middle" font-size="11" fill="{MUTED}">'
                 f'{escape(_md(days[i]))}</text>')
    gaps = set()
    order = {"within": 0, "no_data": 1, "outside": 2}
    for e, s in sorted(series, key=lambda x: order.get(x[0].get("state"), 1)):
        st = e.get("state")
        col = BURG if st == "outside" else (GOLD if st == "no_data" else PINE)
        sw = 2 if st == "outside" else 1.4
        op = 0.95 if st == "outside" else 0.5
        dash = ' stroke-dasharray="4 3"' if st == "no_data" else ""
        segs, cur = [], []
        started = False
        for i, d in enumerate(days):
            if d in s:
                cur.append(f"{X(i):.1f},{Y(s[d]):.1f}")
                started = True
            else:
                if started and any(dd > d for dd in s):
                    gaps.add(i)
                if cur:
                    segs.append(cur)
                cur = []
        if cur:
            segs.append(cur)
        for seg in segs:
            if len(seg) == 1:
                x, y = seg[0].split(",")
                g.append(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{col}" opacity="{op}"><title>{escape(e["tag"])}</title></circle>')
            else:
                g.append(f'<polyline points="{" ".join(seg)}" fill="none" stroke="{col}" stroke-width="{sw}" '
                         f'opacity="{op}"{dash}><title>{escape(e["tag"])}</title></polyline>')
    for i in sorted(gaps):
        g.append(f'<text x="{X(i):.1f}" y="{pt + ih + 13}" text-anchor="middle" font-size="11" fill="{BURG}">&#215;</text>')
    desc = f"Exact match with the reference each night for {len(series)} endpoints serving {nice_name(m)}."
    return (f'<svg id="{cid}" viewBox="0 0 {w} {h}" width="100%" role="img" aria-labelledby="{cid}-d" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">'
            f'<desc id="{cid}-d">{escape(desc)}</desc>{"".join(g)}</svg>')


def chart_scatter(m: dict[str, Any], cid: str, w: int = 760, h: int = 340) -> str:
    """Blended price against agreement with the reference. Cheap and outside sits low left."""
    pts = [(e, blended(e), agreement(m, e)) for e in m["endpoints"]]
    pts = [p for p in pts if p[1] is not None and p[2] is not None]
    if not pts:
        return '<p class="muted">No priced rows yet.</p>'
    xs = [p[1] for p in pts]
    ys = [p[2] for p in pts]
    xmax = max(xs) * 1.12
    ylo = max(0, int(min(ys) // 10 * 10) - 5)
    yhi = min(100, int(max(ys) // 10 * 10) + 10)
    pl, pr, pt, pb = 44, 18, 14, 40
    iw, ih = w - pl - pr, h - pt - pb

    def X(v: float) -> float:
        return pl + iw * v / xmax

    def Y(v: float) -> float:
        return pt + ih * (1 - (v - ylo) / max(1, yhi - ylo))

    g = []
    for t in range(ylo, yhi + 1, 10):
        g.append(f'<line x1="{pl}" y1="{Y(t):.1f}" x2="{w - pr}" y2="{Y(t):.1f}" stroke="{LINE}"/>'
                 f'<text x="{pl - 6}" y="{Y(t) + 4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{t}%</text>')
    step = _tick(xmax)
    v = 0.0
    while v <= xmax:
        g.append(f'<text x="{X(v):.1f}" y="{h - 20}" text-anchor="middle" font-size="11" fill="{MUTED}">${v:g}</text>')
        v = round(v + step, 4)
    g.append(f'<text x="{pl + iw / 2:.1f}" y="{h - 4}" text-anchor="middle" font-size="11" fill="{MUTED}">'
             f'Blended price per million tokens</text>')
    r = rows(m)
    label_tags = {e["tag"] for e in r["ranked"][:3] + r["outside"]}
    if len(pts) <= 12:
        label_tags = {p[0]["tag"] for p in pts}
    for e, x, y in sorted(pts, key=lambda p: p[0].get("state") == "outside"):
        st = e.get("state")
        col = BURG if st == "outside" else (GOLD if st == "no_data" else PINE)
        g.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="5" fill="{col}" fill-opacity=".85" stroke="{PANEL}">'
                 f'<title>{escape(e["tag"])}: {money(x)} blended, {pct(y)}</title></circle>')
        if e["tag"] in label_tags:
            g.append(f'<text x="{X(x) + 8:.1f}" y="{Y(y) + 4:.1f}" font-size="10.5" fill="{PINE_DEEP}">'
                     f'{escape(e["tag"].split("/")[0])}</text>')
    desc = f"Blended price against agreement with the reference for {len(pts)} endpoints serving {nice_name(m)}."
    return (f'<svg id="{cid}" viewBox="0 0 {w} {h}" width="100%" role="img" aria-labelledby="{cid}-d" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">'
            f'<desc id="{cid}-d">{escape(desc)}</desc>{"".join(g)}</svg>')


def chart_quant(models: list[dict[str, Any]], cid: str, w: int = 760) -> str:
    """Declared quantization against measured state, all models."""
    buckets: dict[str, dict[str, int]] = {}
    for m in models:
        for e in m["endpoints"]:
            q = e.get("declared_quant") or "unknown"
            st = e.get("state") if e.get("state") in ("within", "outside") else "no_data"
            buckets.setdefault(q, {"within": 0, "outside": 0, "no_data": 0})[st] += 1
    order = sorted(buckets, key=lambda q: -sum(buckets[q].values()))
    rh, pl = 30, 96
    h = rh * len(order) + 40
    mx = max(sum(b.values()) for b in buckets.values())
    iw = w - pl - 50
    g = []
    for i, q in enumerate(order):
        y = 10 + i * rh
        x = pl
        g.append(f'<text x="{pl - 10}" y="{y + 15}" text-anchor="end" font-size="12" fill="{PINE_DEEP}">{escape(q)}</text>')
        for st, col in (("within", PINE), ("no_data", GOLD), ("outside", BURG)):
            n = buckets[q][st]
            if not n:
                continue
            bw = iw * n / mx
            g.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="20" fill="{col}"><title>{q}: {n} {STATE_LABEL[st].lower()}</title></rect>')
            if bw > 18:
                g.append(f'<text x="{x + bw / 2:.1f}" y="{y + 14}" text-anchor="middle" font-size="11" fill="{CREAM}">{n}</text>')
            x += bw
        g.append(f'<text x="{x + 6:.1f}" y="{y + 14}" font-size="11" fill="{MUTED}">{sum(buckets[q].values())}</text>')
    return (f'<svg id="{cid}" viewBox="0 0 {w} {h}" width="100%" role="img" aria-labelledby="{cid}-d" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">'
            f'<desc id="{cid}-d">Endpoints by declared quantization, split by measured state, all models.</desc>'
            f'{"".join(g)}</svg>')


def _tick(mx: float) -> float:
    for s in (0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10):
        if mx / s <= 7:
            return s
    return 20


def _md(d: str) -> str:
    dt = date.fromisoformat(d)
    return dt.strftime("%b ") + str(dt.day)


# ---------------------------------------------------------------- HTML


def head(title: str, desc: str, url: str, og_img: str | None, preview: bool, depth: str) -> str:
    robots = "noindex,nofollow" if preview else "index,follow,max-snippet:-1,max-image-preview:large"
    card = "summary_large_image" if og_img else "summary"
    img = ""
    if og_img:
        img = (f'<meta property="og:image" content="{og_img}"><meta property="og:image:width" content="1200">'
               f'<meta property="og:image:height" content="630"><meta name="twitter:image" content="{og_img}">')
    return f"""<!doctype html>
<html lang="en">
<!-- generated by probe.site; edit probe/site.py, not this file -->
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Bitdepth">
<meta property="og:url" content="{url}"><meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta name="twitter:card" content="{card}"><meta name="twitter:site" content="@bitdepthdev">
<meta name="twitter:title" content="{escape(title)}"><meta name="twitter:description" content="{escape(desc)}">
{img}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}assets/board.css">
</head>
<body>
"""


def nav(base: str, current: str) -> str:
    def a(href: str, label: str, key: str) -> str:
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'

    return f"""<header class="top"><div class="wrap">
<div class="brand"><a class="wordmark" href="{base}/">Bitdepth</a><span class="line-tag">Independent grades for inference endpoints</span></div>
<nav aria-label="Site">{a(base + "/", "Leaderboard", "board")}{a(base + "/charts", "Charts", "charts")}{'' if base else '<a href="/compare">Compare</a>'}<a href="/market">Market</a><a href="/method">Method</a><a href="/pricing">Pricing</a><a href="/about">About</a></nav>
</div></header>
"""


def banner(preview: bool) -> str:
    if not preview:
        return ""
    return ('<div class="pvbar">Preview with placeholder data. Provider names are letters and every number is '
            'synthetic. Real grades replace this after the fourteen-night read.</div>\n')


def share(cid: str, title: str, tweet: str, url: str, png: str | None = None) -> str:
    attrs = f'data-target="{cid}" data-title="{escape(title)}" data-tweet="{escape(tweet)}" data-url="{escape(url)}"'
    if png:
        attrs += f' data-png="{escape(png)}"'
    return (f'<div class="share" {attrs}><button type="button" data-act="link">Copy link</button>'
            f'<button type="button" data-act="copyimg">Copy image</button>'
            f'<button type="button" data-act="png">PNG</button>'
            f'<button type="button" data-act="x">Share on X</button></div>')


def cite(url: str, as_of: str) -> str:
    return f'<p class="cite">Cite: Bitdepth &middot; {escape(url.replace("https://", ""))} &middot; as of {_md(as_of)}, {as_of[:4]}</p>'


def table(m: dict[str, Any], limit: int | None = None) -> str:
    r = rows(m)
    pc = primary(m)
    pc_label = {"exact": "Exact match", "string": "String match"}.get(pc, pc)
    head_ = (f'<thead><tr><th class="n">#</th><th>Endpoint</th><th>Declared</th><th class="r">{pc_label}</th>'
             f'<th class="r">Self-agree</th><th class="r">Nights</th><th>Drift</th><th class="r">$ in / out per M</th>'
             f'<th class="r">Quality-adjusted</th><th>State</th></tr></thead>')
    body = []

    def tr(e: dict[str, Any], rank: str) -> str:
        st = e.get("state", "no_data")
        label = STATE_LABEL.get(st, st)
        if st == "no_data":
            label = f"First look, {e.get('nights') or 0} night{'s' if (e.get('nights') or 0) != 1 else ''}"
        gone = delisted(m, e)
        if gone:
            label += f", not listed since {_md(gone)}"
        changed = ' <span class="chg" title="Declared quantization changed during the period">changed</span>' if e.get("declared_changed") else ""
        return (f'<tr class="s-{st}"><td class="n">{rank}</td><td class="ep">{escape(e["tag"])}</td>'
                f'<td>{escape(e.get("declared_quant") or "unknown")}{changed}</td>'
                f'<td class="r">{pct(agreement(m, e))}</td><td class="r">{pct(e.get("self_agree"))}</td>'
                f'<td class="r">{e.get("nights") or 0}</td><td>{drift_word(e)}</td>'
                f'<td class="r">{money(e.get("price_in_per_m"))} / {money(e.get("price_out_per_m"))}</td>'
                f'<td class="r b">{money(qa_price(m, e))}</td><td><span class="st st-{st}">{escape(label)}</span></td></tr>')

    ranked = r["ranked"] if limit is None else r["ranked"][:limit]
    for i, e in enumerate(ranked, 1):
        body.append(tr(e, str(i)))
    if limit is None:
        if r["first"]:
            body.append(f'<tr class="div"><td colspan="10">First look: fewer than {MIN_NIGHTS} nights, not ranked</td></tr>')
            body.extend(tr(e, "") for e in r["first"])
        if r["outside"]:
            body.append('<tr class="div out"><td colspan="10">Outside the reference</td></tr>')
            body.extend(tr(e, "") for e in r["outside"])
    return f'<div class="tw"><table class="board">{head_}<tbody>{"".join(body)}</tbody></table></div>'


def footer() -> str:
    return """<footer><div class="wrap">
<div><span class="fm">Bitdepth</span>Independent grades for AI inference endpoints.<br><br>hello@bitdepth.dev<br>Autumn Sun LLC, Sheridan, WY</div>
<div><h4>Data</h4><ul><li><a href="/">Leaderboard</a></li><li><a href="/charts">Charts</a></li><li><a href="/market">Market</a></li></ul></div>
<div><h4>Trust</h4><ul><li><a href="/method">Method</a></li><li><a href="/method#policy">Publication policy</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="/about">About</a></li><li><a href="mailto:hello@bitdepth.dev">Contact</a></li></ul></div>
</div></footer>
<div class="finelines"><div class="wrap"><span>Numbers against a stated reference. Not a claim about intent.</span><span>Listed prices from OpenRouter, read nightly; grades are Bitdepth's.</span></div></div>
"""


def method_cards() -> str:
    return f"""<div class="method">
<div class="m"><h3>The reference</h3><p>For each model, the answer most endpoints declaring full precision (bf16 or fp16) give at temperature zero. Where fewer than two declare it, the plurality answer across all endpoints. <a href="/method">Method</a>.</p></div>
<div class="m"><h3>Agreement and self-agreement</h3><p>Agreement is how often an endpoint gives the reference answer. Self-agreement is how often it gives its own answer twice. An endpoint that agrees with itself far more than with the reference is serving something different.</p></div>
<div class="m"><h3>How rank works</h3><p>Endpoints that match the reference are ranked by quality-adjusted price: the blended price, (3 &times; input + output) &divide; 4 per million tokens, divided by agreement. A cheap endpoint that misses the reference is never shown as the cheapest.</p></div>
<div class="m"><h3>First look</h3><p>An endpoint needs {MIN_NIGHTS} nights before it is ranked. Until then it shows its night count and its numbers, with no rank.</p></div>
<div class="m"><h3>Drift</h3><p>The mean of the last three nights against the first three. A move of more than 10 points reads as improving or worsening; anything smaller is stable.</p></div>
<div class="m"><h3>How to cite</h3><p>Every chart and table carries a cite line with the date. Copy it with the figure. Wrong model name or missing endpoint? <a href="mailto:hello@bitdepth.dev?subject=Leaderboard%20correction">Tell us</a>.</p></div>
</div>"""


def page_board(data: dict[str, Any], base: str, depth: str, preview: bool, abs_base: str) -> str:
    ms = lead_order(data["models"])
    as_of = data["index"]["as_of"]
    n_ep = sum(len(m["endpoints"]) for m in ms)
    n_out = sum(1 for m in ms for e in m["endpoints"] if e.get("state") == "outside")
    nights = data["index"].get("nights", max(model_nights(m) for m in ms))
    url = abs_base + "/"
    title = "Who actually serves the model: the inference endpoint leaderboard | Bitdepth"
    desc = ("Every OpenRouter endpoint for each open-weight model, graded nightly against a full-precision reference "
            "and ranked by quality-adjusted price.")
    h = [head(title, desc, url, abs_base + "/og/board.png", preview, depth), banner(preview), nav(base, "board")]
    h.append(f"""<section class="hero"><div class="wrap hero-wrap">
<div><div class="kick">Endpoint leaderboard</div><h1>Who actually serves the model.</h1>
<p class="sub">Every OpenRouter endpoint for each open-weight model, sent the same prompts at temperature zero every night, graded against a full-precision reference, and ranked by what a correct answer costs.</p></div>
<div class="asof">Last run <b>{_md(as_of)}, {as_of[:4]}</b><br>{nights} nights measured</div>
</div></section>
<div class="tiles"><div class="wrap tiles-wrap">
<div class="tile"><div class="v">{n_ep}</div><div class="l">endpoints graded</div></div>
<div class="tile"><div class="v">{len(ms)}</div><div class="l">open-weight models</div></div>
<div class="tile"><div class="v">{n_out}</div><div class="l">endpoints outside the reference</div></div>
</div></div>
<main class="wrap body">""")
    h.append(findings(ms, base, abs_base, as_of))
    # cheapest real endpoint per model
    cards = []
    for m in ms:
        r = rows(m)
        top = r["ranked"][:3]
        lis = "".join(f'<li><span>{i}</span><b>{escape(e["tag"])}</b><em>{money(qa_price(m, e))}</em></li>' for i, e in enumerate(top, 1))
        if not lis:
            lis = f'<li class="fl">First look, {model_nights(m)} night{"s" if model_nights(m) != 1 else ""}. Ranked from {MIN_NIGHTS}.</li>'
        cards.append(f'<a class="mc" href="{base}/m/{slug_of(m)}"><div class="mh"><h3>{escape(nice_name(m))}</h3>'
                     f'<span>{len(m["endpoints"])} endpoints</span></div><p class="hl">{escape(headline(m))}</p>'
                     f'<ol>{lis}</ol><div class="more">Full table and charts &rarr;</div></a>')
    h.append('<div class="sec"><div class="k">Cheapest real endpoint</div><h2>Per model, the best price for the right answer.</h2>'
             f'<div class="mcards">{"".join(cards)}</div></div>')
    # tabs
    tabs = "".join(f'<button type="button" role="tab" data-tab="t-{slug_of(m)}"{" aria-selected=\"true\"" if i == 0 else ""}>{escape(nice_name(m))}</button>' for i, m in enumerate(ms))
    panels = []
    for i, m in enumerate(ms):
        sid = f"t-{slug_of(m)}"
        murl = f"{abs_base}/m/{slug_of(m)}"
        panels.append(f'<div class="panel" id="{sid}" role="tabpanel"{"" if i == 0 else " hidden"}>'
                      f'<div class="ph"><p class="hl">{escape(headline(m))}</p>{share(sid + "-tbl", nice_name(m) + " endpoint leaderboard", headline(m), murl, f"{abs_base}/og/{slug_of(m)}.png")}</div>'
                      f'<div id="{sid}-tbl">{table(m)}</div>{cite(murl, m.get("as_of", as_of))}'
                      f'<p class="src">Reference: {escape(m.get("reference_rule", ""))}. <a href="{base}/m/{slug_of(m)}">Open the {escape(nice_name(m))} page</a>.</p></div>')
    h.append(f'<div class="sec" id="board"><div class="k">The board</div><h2>Every endpoint, named.</h2>'
             f'<div class="tabs" role="tablist">{tabs}</div>{"".join(panels)}</div>')
    h.append(f'<div class="sec"><div class="k">Method</div><h2>How this board is measured.</h2>{method_cards()}</div>')
    h.append(f"""<div class="sec two-up">
<div class="m dark"><h3>Get the data</h3><p>The same figures as JSON, one file per model, rewritten every night.</p><code>{SITE}/data/v1/index.json</code></div>
<div class="m"><h3>Serve one of these models?</h3><p>Endpoints that match the reference can carry the Graded by Bitdepth badge, linked to their row. To add an endpoint, correct a listing or ask about grades and data for your routes, <a href="mailto:hello@bitdepth.dev?subject=Endpoint%20listing">write to us</a>.</p></div>
</div>""")
    h.append("</main>")
    h.append(footer())
    h.append(f'<script src="{depth}assets/share.js" defer></script></body></html>\n')
    return "".join(h)


def findings(ms: list[dict[str, Any]], base: str, abs_base: str, as_of: str) -> str:
    """What the board found: the model with the most endpoints outside the reference, and the biggest drift."""
    out = []
    lead = next((m for m in ms if not is_first_look(m) and rows(m)["outside"]), None)
    if lead:
        r = rows(lead)
        pc = primary(lead)
        label = {"exact": "Exact match", "string": "String match"}.get(pc, pc)
        lis = "".join(
            f'<div style="display:flex;gap:12px;padding:6px 0;border-bottom:1px solid {LINE}"><b style="flex:1">{escape(e["tag"])}</b>'
            + f'<span style="width:64px;text-align:right">{pct(agreement(lead, e))}</span>'
            + f'<span class="muted" style="width:170px">{"not listed since " + _md(delisted(lead, e)) if delisted(lead, e) else "still listed"}</span></div>'
            for e in r["outside"])
        sent = outside_sentence(lead)
        murl = f"{abs_base}/m/{slug_of(lead)}"
        out.append(f'<div class="card" id="f-out"><div class="ch"><h3>{escape(nice_name(lead))}: outside the reference</h3>'
                   f'{share("f-out", nice_name(lead) + ": outside the reference", sent, murl, f"{abs_base}/og/{slug_of(lead)}.png")}</div>'
                   f'<p class="hl">{escape(sent)}</p><div style="margin:12px 0">{lis}</div><p class="muted">{label}, mean over every night listed.</p>'
                   f'{cite(murl, lead.get("as_of", as_of))}<div class="more"><a href="{base}/m/{slug_of(lead)}">Full table &rarr;</a></div></div>')
    pick = drift_pick(ms)
    if pick:
        m, e = pick
        sent = drift_sentence(m, e)
        murl = f"{abs_base}/m/{slug_of(m)}"
        out.append(f'<div class="card chart" id="f-drift"><div class="ch"><h3>{escape(e["tag"])}, night by night</h3>'
                   f'{share("f-drift-c", e["tag"] + " against the other endpoints", sent, f"{abs_base}/charts#f-drift")}</div>'
                   f'<p class="hl">{escape(sent)}</p>{chart_drift(m, e, "f-drift-c")}{cite(abs_base + "/charts", m.get("as_of", as_of))}</div>')
    if not out:
        return ""
    return ('<div class="sec" id="findings"><div class="k">What the board found</div><h2>Same model name, different answers.</h2>'
            f'<div class="grid2">{"".join(out)}</div></div>')


def page_model(data: dict[str, Any], m: dict[str, Any], base: str, depth: str, preview: bool, abs_base: str) -> str:
    s = slug_of(m)
    url = f"{abs_base}/m/{s}"
    name = nice_name(m)
    as_of = m.get("as_of", data["index"]["as_of"])
    hl = headline(m)
    title = f"{name} on OpenRouter: which endpoint serves the real model | Bitdepth"
    h = [head(title, hl, url, f"{abs_base}/og/{s}.png", preview, depth), banner(preview), nav(base, "board")]
    r = rows(m)
    h.append(f"""<section class="hero"><div class="wrap hero-wrap">
<div><div class="kick">{escape(m["model"])} &middot; {len(m["endpoints"])} endpoints</div><h1>{escape(name)}</h1>
<p class="sub big">{escape(hl)}</p>
{share("og-" + s, name + " on Bitdepth", hl, url, f"{abs_base}/og/{s}.png").replace('class="share"', 'class="share dark"')}</div>
<div class="asof">Last run <b>{_md(as_of)}, {as_of[:4]}</b><br>{model_nights(m)} nights measured</div>
</div></section>
<div class="tiles"><div class="wrap tiles-wrap">
<div class="tile"><div class="v">{len(r["ranked"])}</div><div class="l">match the reference</div></div>
<div class="tile"><div class="v">{len(r["first"])}</div><div class="l">first look, not yet ranked</div></div>
<div class="tile"><div class="v">{len(r["outside"])}</div><div class="l">outside the reference</div></div>
</div></div>
<main class="wrap body">
<div class="sec" id="table"><div class="k">The board</div><h2>Every endpoint, named.</h2>
{share("tbl-" + s, name + " endpoint leaderboard", hl, url + "#table")}
<div id="tbl-{s}">{table(m)}</div>{cite(url, as_of)}
<p class="src">Reference: {escape(m.get("reference_rule", ""))}. State rule: {escape(m.get("state_rule", ""))}</p></div>
<div class="sec" id="price"><div class="k">Price against agreement</div><h2>Cheap and wrong sits low on the left.</h2>
<div class="card chart"><div class="ch"><p class="muted">Each dot is one endpoint. Across: blended price per million tokens. Up: agreement with the reference.</p>
{share("sc-" + s, name + ": price against agreement", hl, url + "#price")}</div>
<div class="legend"><span class="lg pine"></span>Matches reference<span class="lg gold"></span>First look<span class="lg burg"></span>Outside reference</div>
{chart_scatter(m, "sc-" + s)}{cite(url + "#price", as_of)}</div></div>
<div class="sec" id="nightly"><div class="k">Night by night</div><h2>Does an endpoint change?</h2>
<div class="card chart"><div class="ch"><p class="muted">Exact match with the reference each night, one line per endpoint. &#215; marks a night with no row.</p>
{share("ag-" + s, name + ": agreement night by night", hl, url + "#nightly")}</div>
<div class="legend"><span class="lg pine"></span>Matches reference<span class="lg gold"></span>First look<span class="lg burg"></span>Outside reference</div>
{chart_agreement(m, "ag-" + s)}{cite(url + "#nightly", as_of)}</div></div>
<div class="sec" id="badge"><div class="k">For providers</div><h2>Graded by Bitdepth.</h2>
<div class="two-up"><div class="m"><p>An endpoint that matches the reference can show this badge on its docs or pricing page. It links back to its row here, and it updates every night.</p>
<img src="{base}/badge/sample.svg" height="48" alt="Graded by Bitdepth badge sample"></div>
<div class="m"><p>Badge code for a matching endpoint, after the first ranked read:</p><code>&lt;a href="{url}"&gt;&lt;img src="{abs_base}/badge/{s}/PROVIDER.svg" alt="Graded by Bitdepth"&gt;&lt;/a&gt;</code></div></div></div>
<div class="sec"><div class="k">Method</div><h2>How this page is measured.</h2>{method_cards()}</div>
</main>""")
    h.append(footer())
    h.append(f'<script src="{depth}assets/share.js" defer></script></body></html>\n')
    return "".join(h)


def page_charts(data: dict[str, Any], base: str, depth: str, preview: bool, abs_base: str) -> str:
    ms = data["models"]
    as_of = data["index"]["as_of"]
    url = abs_base + "/charts"
    title = "Inference endpoints over time, in charts | Bitdepth"
    desc = "Agreement with a full-precision reference, price and declared quantization for every OpenRouter endpoint, nightly."
    h = [head(title, desc, url, abs_base + "/og/board.png", preview, depth), banner(preview), nav(base, "charts")]
    ms = lead_order(ms)
    graded = [m for m in ms if not is_first_look(m)] or ms
    lead = next((m for m in graded if rows(m)["outside"]), graded[0])
    finding = outside_sentence(lead) if rows(lead)["outside"] else headline(lead)
    h.append(f"""<section class="hero"><div class="wrap hero-wrap">
<div><div class="kick">Charts &middot; endpoints over time</div><h1>Inference endpoints, in charts.</h1>
<p class="sub">Every chart is drawn from the nightly probe. Free to view, free to cite, free to share. Each one exports clean for X, a deck or a memo.</p></div>
<div class="thought"><div class="tk">Finding of the night &middot; {_md(as_of)}</div><p id="fon">{escape(finding)}</p>
{share("fon", "Finding of the night", finding, f"{abs_base}/m/{slug_of(lead)}", f"{abs_base}/og/{slug_of(lead)}.png")}</div>
</div></section>
<main class="wrap body">""")
    h.append(findings(ms, base, abs_base, as_of))
    for m in ms:
        s = slug_of(m)
        h.append(f'<div class="sec"><div class="k">{escape(nice_name(m))}</div>'
                 f'<div class="grid2">'
                 f'<div class="card chart" id="c-sc-{s}"><div class="ch"><h3>Price against agreement</h3>'
                 f'{share("csc-" + s, nice_name(m) + ": price against agreement", headline(m), url + "#c-sc-" + s)}</div>'
                 f'{chart_scatter(m, "csc-" + s, 560, 320)}{cite(url, m.get("as_of", as_of))}</div>'
                 f'<div class="card chart" id="c-ag-{s}"><div class="ch"><h3>Agreement night by night</h3>'
                 f'{share("cag-" + s, nice_name(m) + ": agreement night by night", headline(m), url + "#c-ag-" + s)}</div>'
                 f'{chart_agreement(m, "cag-" + s, 560, 300)}{cite(url, m.get("as_of", as_of))}</div>'
                 f'</div></div>')
    drift = data["drift"].get("items", [])
    dl = "".join(f'<li><b>{escape(it["tag"])}</b> on {escape(it["model"].split("/")[-1])}: {it["movement"]:+.1f} points</li>' for it in drift) \
        or "<li>No endpoint moved more than 10 points this period.</li>"
    h.append(f'<div class="sec"><div class="k">All models</div><div class="grid2">'
             f'<div class="card chart" id="c-quant"><div class="ch"><h3>Declared quantization against measured state</h3>'
             f'{share("cq", "Declared quantization against measured state", "What endpoints declare, against how they measure.", url + "#c-quant")}</div>'
             f'<div class="legend"><span class="lg pine"></span>Matches reference<span class="lg gold"></span>First look<span class="lg burg"></span>Outside reference</div>'
             f'{chart_quant(ms, "cq", 560)}{cite(url, as_of)}</div>'
             f'<div class="card chart" id="c-drift"><div class="ch"><h3>Moved this period</h3></div>'
             f'<p class="muted">Mean exact match of the last three nights against the first three.</p><ul class="drift">{dl}</ul>{cite(url, as_of)}</div>'
             f'</div></div>')
    h.append("""<div class="sec"><div class="k">Glossary</div><h2>Speak the language.</h2><div class="method">
<div class="m"><h3>Endpoint</h3><p>One provider serving one model at one declared precision on OpenRouter.</p></div>
<div class="m"><h3>Declared quantization</h3><p>The precision the provider lists: bf16 or fp16 is full precision; fp8, fp4 and int4 are smaller and cheaper to run.</p></div>
<div class="m"><h3>Reference</h3><p>The answer the full-precision endpoints give. What every endpoint is graded against.</p></div>
<div class="m"><h3>Agreement</h3><p>The share of prompts where an endpoint gives the reference answer.</p></div>
<div class="m"><h3>Quality-adjusted price</h3><p>Blended price divided by agreement. What a correct answer costs.</p></div>
<div class="m"><h3>Drift</h3><p>An endpoint whose answers move over the period, measured against its own first nights.</p></div>
</div></div>
</main>""")
    h.append(footer())
    h.append(f'<script src="{depth}assets/share.js" defer></script></body></html>\n')
    return "".join(h)


# ---------------------------------------------------------------- images


def _font(name: str, size: int):
    from PIL import ImageFont

    return ImageFont.truetype(str(FONTS / name), size)


def _wrap(draw, text: str, font, width: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def og_model(m: dict[str, Any], path: Path, preview: bool) -> None:
    from PIL import Image, ImageDraw

    W, H = 1200, 630
    im = Image.new("RGB", (W, H), PINE)
    d = ImageDraw.Draw(im)
    kick = _font("Inter-SemiBold.otf", 22)
    serif = _font("DejaVuSerif.ttf", 40)
    body = _font("Inter-Regular.otf", 24)
    mono = _font("Inter-SemiBold.otf", 24)
    small = _font("Inter-Regular.otf", 20)
    d.text((64, 52), ("BITDEPTH  ·  " + nice_name(m).upper()), font=kick, fill=GOLD)
    hl = headline(m)
    y = 100
    lines = _wrap(d, hl, serif, W - 128)
    if len(lines) > 4:
        serif = _font("DejaVuSerif.ttf", 32)
        lines = _wrap(d, hl, serif, W - 128)[:5]
    for ln in lines:
        d.text((64, y), ln, font=serif, fill=CREAM)
        y += serif.size + 12
    y = max(y + 18, 350)
    r = rows(m)
    top = r["ranked"][:3] or r["first"][:3]
    d.line((64, y, W - 64, y), fill="#3C5A4C", width=2)
    y += 14
    d.text((64, y), "ENDPOINT", font=small, fill=SAGE)
    d.text((640, y), "DECLARED", font=small, fill=SAGE)
    d.text((W - 64, y), "QUALITY-ADJUSTED $/M", font=small, fill=SAGE, anchor="ra")
    y += 36
    for i, e in enumerate(top, 1):
        d.text((64, y), f"{i if r['ranked'] else '·'}  {e['tag']}", font=mono, fill=CREAM)
        d.text((640, y), e.get("declared_quant") or "unknown", font=body, fill=SAGE)
        d.text((W - 64, y), money(qa_price(m, e)), font=mono, fill=GOLD, anchor="ra")
        y += 42
    as_of = m.get("as_of", "")
    foot = f"bitdepth.dev/m/{slug_of(m)}   ·   as of {_md(as_of)}, {as_of[:4]}   ·   {model_nights(m)} nights"
    if preview:
        foot = "PREVIEW · PLACEHOLDER DATA · NOT A MEASUREMENT"
    d.text((64, H - 52), foot, font=small, fill=SAGE)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, optimize=True)


def og_board(data: dict[str, Any], path: Path, preview: bool) -> None:
    from PIL import Image, ImageDraw

    W, H = 1200, 630
    im = Image.new("RGB", (W, H), PINE)
    d = ImageDraw.Draw(im)
    d.text((64, 60), "BITDEPTH  ·  ENDPOINT LEADERBOARD", font=_font("Inter-SemiBold.otf", 22), fill=GOLD)
    d.text((64, 110), "Who actually serves", font=_font("DejaVuSerif.ttf", 72), fill=CREAM)
    d.text((64, 196), "the model.", font=_font("DejaVuSerif.ttf", 72), fill=CREAM)
    ms = data["models"]
    n_ep = sum(len(m["endpoints"]) for m in ms)
    n_out = sum(1 for m in ms for e in m["endpoints"] if e.get("state") == "outside")
    stats = [(str(n_ep), "endpoints graded"), (str(len(ms)), "open-weight models"), (str(n_out), "outside the reference")]
    x = 64
    for v, l in stats:
        d.text((x, 360), v, font=_font("Inter-SemiBold.otf", 64), fill=CREAM)
        d.text((x, 440), l, font=_font("Inter-Regular.otf", 22), fill=SAGE)
        x += 360
    foot = f"bitdepth.dev   ·   graded nightly against a full-precision reference   ·   as of {data['index']['as_of']}"
    if preview:
        foot = "PREVIEW · PLACEHOLDER DATA · NOT A MEASUREMENT"
    d.text((64, H - 56), foot, font=_font("Inter-Regular.otf", 20), fill=SAGE)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, optimize=True)


def badge_svg(model_name: str, as_of: str, url: str) -> str:
    raw = f"{model_name} · matches reference · {as_of}"
    line2 = escape(raw)
    bw = max(200, int(len(raw) * 6.9) + 28)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{bw}" height="48" viewBox="0 0 {bw} 48" role="img" aria-label="Graded by Bitdepth, {line2}">'
        f'<title>Graded by Bitdepth: {line2}</title>'
        f'<rect width="{bw}" height="48" rx="6" fill="{PINE}"/>'
        f'<text x="14" y="20" fill="{CREAM}" font-family="Georgia,serif" font-size="14">Graded by Bitdepth</text>'
        f'<text x="14" y="38" fill="{GOLD}" font-family="ui-monospace,monospace" font-size="11">{line2}</text>'
        "</svg>\n"
    )


# ---------------------------------------------------------------- build


def build(data: dict[str, Any], out: Path, base: str, preview: bool, abs_base: str, home: bool) -> list[Path]:
    """Write every page and image under out. base is the URL path prefix ('' or '/lab')."""
    written: list[Path] = []

    def w(rel: str, text: str) -> None:
        p = out / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        written.append(p)

    depth_root = "../" if base else ""
    board_html = page_board(data, base, "/", preview, abs_base)
    if home or base:
        w("index.html", board_html)
    else:
        w("leaderboard/index.html", board_html)
    w("charts/index.html", page_charts(data, base, "/", preview, abs_base))
    for m in data["models"]:
        s = slug_of(m)
        w(f"m/{s}/index.html", page_model(data, m, base, "/", preview, abs_base))
        og_model(m, out / "og" / f"{s}.png", preview)
        written.append(out / "og" / f"{s}.png")
        if not preview:
            for e in rows(m)["ranked"]:
                w(f"badge/{s}/{e['provider_slug']}.svg", badge_svg(nice_name(m), m.get("as_of", ""), f"{abs_base}/m/{s}"))
    og_board(data, out / "og" / "board.png", preview)
    written.append(out / "og" / "board.png")
    w("badge/sample.svg", badge_svg("DeepSeek V4 Pro", "sample", abs_base))
    if not preview:
        dst = out / "data" / "v1"
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(ROOT / "data" / "public" / "v1", dst)
    del depth_root
    return written


MARKER = "generated by probe.site"


def sitemap(site: Path, data: dict[str, Any]) -> None:
    """Add the leaderboard, charts, compare and per-model URLs to sitemap.xml once each."""
    p = site / "sitemap.xml"
    text = p.read_text() if p.exists() else (
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n')
    as_of = data["index"]["as_of"]
    urls = [f"{SITE}/charts", f"{SITE}/compare"] + [f"{SITE}/m/{slug_of(m)}" for m in data["models"]]
    add = "".join(f"  <url><loc>{u}</loc><lastmod>{as_of}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\n"
                  for u in urls if f"<loc>{u}</loc>" not in text)
    text = text.replace(f"<loc>{SITE}/</loc><lastmod>", f"<loc>{SITE}/</loc><lastmod>{as_of}</lastmod><x>", 1)
    if "<x>" in text:
        import re
        text = re.sub(r"<x>[0-9-]+</lastmod>", "", text)
    text = text.replace("</urlset>", add + "</urlset>")
    p.write_text(text)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--preview", action="store_true", help="placeholder data into site/lab/")
    g.add_argument("--live", action="store_true", help="real data into site/ (leaderboard becomes the home page)")
    ap.add_argument("--data", default=str(ROOT / "data" / "public" / "v1"))
    ap.add_argument("--site", default=str(ROOT / "site"))
    a = ap.parse_args(argv)
    data = load(Path(a.data))
    site = Path(a.site)
    if a.preview:
        out = site / "lab"
        written = build(placeholder(data), out, "/lab", True, SITE + "/lab", home=True)
    else:
        home = site / "index.html"
        if home.exists() and MARKER not in home.read_text():
            dst = site / "compare" / "index.html"
            dst.parent.mkdir(parents=True, exist_ok=True)
            text = home.read_text().replace('<link rel="canonical" href="https://bitdepth.dev/">',
                                            '<link rel="canonical" href="https://bitdepth.dev/compare">')
            dst.write_text(text)
            home.unlink()
            print("moved the hand-written home page to site/compare/index.html")
        written = build(data, site, "", False, SITE, home=True)
        sitemap(site, data)
    print(f"wrote {len(written)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
