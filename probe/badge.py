"""Verified by Bitdepth badge for one provider on one model, written on request only.

    python -m probe.badge --provider together --model openai/gpt-oss-120b [--month 2026-11]
                          [--trend data/trend] [--out packets/badges]

Writes packets/badges/<provider>-<model-slug>.svg, which git ignores. The badge
states the month and how many nights the provider's endpoints sat inside the
floor, by the emit state rule. It is never committed and never hosted from here.
"""

from __future__ import annotations

import argparse
import sys
from html import escape
from pathlib import Path

from probe.packet import load_trend, night_within, provider_of


def nights_inside(t: dict, provider: str, model: str, month: str) -> tuple[int, int]:
    n_in = n_all = 0
    for m in t["models"]:
        if m["slug"] != model:
            continue
        for e in m["endpoints"]:
            if provider_of(e["tag"]) != provider and e["tag"] != provider:
                continue
            for d, v in e.get("exact_by_night", {}).items():
                if not d.startswith(month):
                    continue
                n_all += 1
                if night_within(v, e["self"]["agree_pct"]):
                    n_in += 1
    return n_in, n_all


def svg(month: str, n_in: int, n_all: int) -> str:
    line2 = escape(f"{month} · inside the floor {n_in} of {n_all} nights")
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="48" role="img" '
        f'aria-label="Verified by Bitdepth, {line2}">'
        '<rect width="300" height="48" rx="6" fill="#123d2e"/>'
        '<text x="14" y="20" fill="#f6efe2" font-family="Georgia,serif" font-size="14">Verified by Bitdepth</text>'
        f'<text x="14" y="38" fill="#d4a24c" font-family="ui-monospace,monospace" font-size="11">{line2}</text>'
        "</svg>\n"
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", required=True)
    ap.add_argument("--model", required=True, help="author/slug, e.g. openai/gpt-oss-120b")
    ap.add_argument("--month", default=None)
    ap.add_argument("--trend", default="data/trend")
    ap.add_argument("--out", default="packets/badges")
    a = ap.parse_args(argv)
    date, t = load_trend(Path(a.trend), None)
    month = a.month or date[:7]
    n_in, n_all = nights_inside(t, a.provider.lower(), a.model, month)
    if n_all == 0:
        print(f"no nights for {a.provider} on {a.model} in {month}", file=sys.stderr)
        return 2
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    p = out / f"{a.provider.lower()}-{a.model.split('/')[-1]}.svg"
    p.write_text(svg(month, n_in, n_all))
    print(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
