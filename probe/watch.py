"""Watch plan: nightly changes per endpoint, and alerts to paying watchers.

    python -m probe.watch [--public data/public/v1] [--state data/watch/last.json]
                          [--notify] [--dry-run]

Step 1 (always): compare tonight's public model files with last night's snapshot and
write data/public/v1/changes.json: every endpoint whose state, declared quantization
or listed price changed, plus endpoints that appeared or disappeared. Then rewrite the
snapshot. Reads files only.

Step 2 (--notify): read the active Watch subscriptions from Stripe and email each
watcher the changes on the endpoints they watch, through Resend. Runs only when
STRIPE_SECRET_KEY, RESEND_API_KEY and WATCH_PAYMENT_LINK are all set; otherwise it
says so and exits 0. Keys are read from the environment only and never printed.

A watcher names endpoints in the Checkout text custom field (key containing `endpoint`, else the first text field), comma or newline
separated, as `<author/slug>:<tag>` (one model) or `<tag>` (that tag on every model).
A subscription watches at most as many endpoints as its quantity. Nobody is emailed
on a night with no change on their endpoints.

Numbers against a stated reference. Not a claim about intent.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date as Date
from pathlib import Path
from typing import Any

SCHEMA = "bitdepth.changes.v1"
FOOTER = "Numbers against a stated reference. Not a claim about intent."
PRICE_TOLERANCE = 0.005  # relative; smaller moves are rounding
FROM_ADDR = "Bitdepth <hello@bitdepth.dev>"
STRIPE_API = "https://api.stripe.com/v1"
RESEND_API = "https://api.resend.com/emails"
ACTIVE = {"active", "trialing"}


# ---------- step 1: changes ----------

def load_current(public: Path) -> tuple[str, dict[str, dict[str, Any]]]:
    """Return (as_of, {"<model>|<tag>": row}) from the public model files."""
    index = json.loads((public / "index.json").read_text())
    rows: dict[str, dict[str, Any]] = {}
    as_of = ""
    for m in index.get("models", []):
        path = public / m["path"] if "path" in m else None
        if path is None or not path.exists():
            continue
        doc = json.loads(path.read_text())
        as_of = max(as_of, doc.get("as_of", ""))
        for e in doc.get("endpoints", []):
            rows[f"{doc['model']}|{e['tag']}"] = {
                "model": doc["model"],
                "label": doc.get("label", doc["model"]),
                "tag": e["tag"],
                "state": e.get("state"),
                "declared_quant": e.get("declared_quant"),
                "price_in_per_m": e.get("price_in_per_m"),
                "price_out_per_m": e.get("price_out_per_m"),
            }
    return as_of, rows


def _price_moved(a: Any, b: Any) -> bool:
    if a is None or b is None:
        return a != b
    if a == 0:
        return b != 0
    return abs(b - a) / abs(a) > PRICE_TOLERANCE


def diff(prev: dict[str, dict[str, Any]], cur: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for key in sorted(set(prev) | set(cur)):
        p, c = prev.get(key), cur.get(key)
        base = c or p
        head = {"model": base["model"], "label": base["label"], "tag": base["tag"]}
        if p is None:
            out.append({**head, "field": "listed", "from": None, "to": "new"})
            continue
        if c is None:
            out.append({**head, "field": "listed", "from": "listed", "to": "removed"})
            continue
        for field in ("state", "declared_quant"):
            if p.get(field) != c.get(field):
                out.append({**head, "field": field, "from": p.get(field), "to": c.get(field)})
        for field in ("price_in_per_m", "price_out_per_m"):
            if _price_moved(p.get(field), c.get(field)):
                out.append({**head, "field": field, "from": p.get(field), "to": c.get(field)})
    return out


def run_changes(public: Path, state_path: Path) -> dict[str, Any]:
    as_of, cur = load_current(public)
    prev: dict[str, dict[str, Any]] = {}
    first = not state_path.exists()
    if not first:
        prev = json.loads(state_path.read_text()).get("rows", {})
    changes = [] if first else diff(prev, cur)
    doc = {
        "schema": SCHEMA,
        "as_of": as_of,
        "baseline": first,
        "count": len(changes),
        "changes": changes,
        "footer": FOOTER,
    }
    (public / "changes.json").write_text(json.dumps(doc, indent=1) + "\n")
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps({"as_of": as_of, "rows": cur}, indent=1, sort_keys=True) + "\n")
    return doc


# ---------- step 2: watchers ----------

def parse_endpoints(text: str | None) -> list[str]:
    if not text:
        return []
    items = [s.strip() for s in re.split(r"[,\n;]+", text)]
    return [s for s in items if s]


def matches(spec: str, change: dict[str, Any]) -> bool:
    if ":" in spec:
        model, tag = spec.split(":", 1)
        return model.strip().lower() == change["model"].lower() and tag.strip().lower() == change["tag"].lower()
    return spec.lower() == change["tag"].lower()


def changes_for(specs: list[str], quantity: int, changes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    watched = specs[: max(quantity, 0)]
    return [c for c in changes if any(matches(s, c) for s in watched)]


def _fmt(v: Any) -> str:
    if v is None:
        return "none"
    if isinstance(v, float):
        return f"${v:.3f}/M"
    return str(v)


FIELD_LABEL = {
    "state": "grade state",
    "declared_quant": "declared precision",
    "price_in_per_m": "input price",
    "price_out_per_m": "output price",
    "listed": "listing",
}


def email_body(as_of: str, items: list[dict[str, Any]]) -> str:
    lines = [f"Bitdepth Watch, night of {as_of}", "", "What changed on the endpoints you watch:", ""]
    for c in items:
        lines.append(f"- {c['label']} / {c['tag']}: {FIELD_LABEL.get(c['field'], c['field'])} "
                     f"{_fmt(c['from'])} -> {_fmt(c['to'])}")
    lines += [
        "",
        "Full table: https://bitdepth.dev",
        "Method: https://bitdepth.dev/method",
        "",
        FOOTER,
        "To change your endpoints, reply to this email. To cancel, use the link on your Stripe receipt.",
    ]
    return "\n".join(lines)


def list_watchers(stripe_key: str, link: str) -> list[dict[str, Any]]:
    """Active Watch subscriptions from completed Checkout sessions on the payment link."""
    import httpx

    auth = (stripe_key, "")
    out: list[dict[str, Any]] = []
    params: dict[str, Any] = {"payment_link": link, "status": "complete", "limit": 100}
    with httpx.Client(timeout=30) as client:
        while True:
            r = client.get(f"{STRIPE_API}/checkout/sessions", params=params, auth=auth)
            r.raise_for_status()
            page = r.json()
            for s in page.get("data", []):
                sub_id = s.get("subscription")
                email = (s.get("customer_details") or {}).get("email")
                if not sub_id or not email:
                    continue
                sr = client.get(f"{STRIPE_API}/subscriptions/{sub_id}", auth=auth)
                if sr.status_code != 200:
                    continue
                sub = sr.json()
                if sub.get("status") not in ACTIVE:
                    continue
                items = (sub.get("items") or {}).get("data") or [{}]
                qty = int(items[0].get("quantity") or 0)
                text = None
                fields = [f for f in (s.get("custom_fields") or []) if f.get("type") == "text"]
                named = [f for f in fields if "endpoint" in (f.get("key") or "").lower()]
                for f in (named or fields)[:1]:
                    text = (f.get("text") or {}).get("value")
                out.append({"email": email, "quantity": qty, "specs": parse_endpoints(text)})
            if not page.get("has_more"):
                break
            params["starting_after"] = page["data"][-1]["id"]
    return out


def send_email(resend_key: str, to: str, subject: str, body: str) -> None:
    import httpx

    r = httpx.post(
        RESEND_API,
        headers={"Authorization": f"Bearer {resend_key}"},
        json={"from": FROM_ADDR, "to": [to], "reply_to": "hello@bitdepth.dev", "subject": subject, "text": body},
        timeout=30,
    )
    r.raise_for_status()


def notify(doc: dict[str, Any], dry_run: bool = False) -> int:
    stripe_key = os.environ.get("STRIPE_SECRET_KEY")
    resend_key = os.environ.get("RESEND_API_KEY")
    link = os.environ.get("WATCH_PAYMENT_LINK")
    if not (stripe_key and resend_key and link):
        print("watch: notify skipped (STRIPE_SECRET_KEY, RESEND_API_KEY or WATCH_PAYMENT_LINK not set)")
        return 0
    if not doc["changes"]:
        print("watch: no changes tonight, nothing to send")
        return 0
    watchers = list_watchers(stripe_key, link)
    sent = 0
    for w in watchers:
        items = changes_for(w["specs"], w["quantity"], doc["changes"])
        if not items:
            continue
        if not dry_run:
            send_email(resend_key, w["email"], f"Bitdepth Watch: {len(items)} change(s) on {doc['as_of']}",
                       email_body(doc["as_of"], items))
        sent += 1
    print(f"watch: {len(watchers)} active watchers, {sent} emailed" + (" (dry run)" if dry_run else ""))
    return sent


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--public", default="data/public/v1")
    ap.add_argument("--state", default="data/watch/last.json")
    ap.add_argument("--notify", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    doc = run_changes(Path(a.public), Path(a.state))
    print(f"watch: {doc['count']} changes as of {doc['as_of']}" + (" (baseline night)" if doc["baseline"] else ""))
    if a.notify:
        notify(doc, dry_run=a.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
