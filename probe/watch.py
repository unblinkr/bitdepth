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
                "nights": e.get("nights"),
                "endpoint_count": doc.get("endpoint_count"),
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


STATE_WORDS = {"within": "within the pack", "outside": "outside the pack", "no_data": "no grade yet", "stale": "stale (no fresh night)"}
MIN_NIGHTS = 7


def state_words(r: dict[str, Any]) -> str:
    """Plain words for a grade state, with the reason when there is no grade yet."""
    st = r.get("state")
    if not st:
        return "not graded yet"
    words = STATE_WORDS.get(st, st)
    if st == "no_data":
        n, ec = r.get("nights"), r.get("endpoint_count")
        if isinstance(ec, int) and ec < 3:
            words += f" (only {ec} endpoint{'s' if ec != 1 else ''} serve this model, too few to compare)"
        elif isinstance(n, int) and n < MIN_NIGHTS:
            words += f" ({n} of {MIN_NIGHTS} nights so far)"
    return words


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
        if c["field"] == "state":
            frm, to = STATE_WORDS.get(c["from"] or "", _fmt(c["from"])), STATE_WORDS.get(c["to"] or "", _fmt(c["to"]))
        else:
            frm, to = _fmt(c["from"]), _fmt(c["to"])
        lines.append(f"- {c['label']} / {c['tag']}: {FIELD_LABEL.get(c['field'], c['field'])} {frm} -> {to}")
    lines += [
        "",
        "Full table: https://bitdepth.dev",
        "Method: https://bitdepth.dev/method",
        "",
        FOOTER,
        "To change your endpoints, reply to this email or pick again at https://bitdepth.dev/watch. To cancel, use the link on your Stripe receipt.",
    ]
    return "\n".join(lines)


def payment_links() -> list[str]:
    """WATCH_PAYMENT_LINK plus WATCH_TEST_PAYMENT_LINK, each comma separated."""
    raw = ",".join(os.environ.get(k, "") for k in ("WATCH_PAYMENT_LINK", "WATCH_TEST_PAYMENT_LINK"))
    return [x.strip() for x in raw.split(",") if x.strip()]


def list_watchers(stripe_key: str, link: str | list[str]) -> list[dict[str, Any]]:
    """Active Watch subscriptions: Checkout sessions on the payment link(s), plus
    sessions made by the bitdepth.dev/watch picker (metadata bitdepth_watch=1)."""
    links = [link] if isinstance(link, str) else list(link)
    out: list[dict[str, Any]] = []
    for one in links:
        if one:
            out += _list_watchers_one(stripe_key, {"payment_link": one})
    out += _list_watchers_one(stripe_key, {}, picker_only=True)
    seen: set[str] = set()
    uniq = []
    for w in out:
        k = w.get("sub") or w["email"]
        if k not in seen:
            seen.add(k)
            uniq.append(w)
    return uniq


def picker_specs(meta: dict[str, Any] | None) -> list[str]:
    """Endpoints the picker stored in session metadata as endpoints_0, endpoints_1, ..."""
    meta = meta or {}
    keys = sorted((k for k in meta if k.startswith("endpoints_")), key=lambda k: int(k.split("_")[1]) if k.split("_")[1].isdigit() else 0)
    return parse_endpoints(",".join(str(meta[k]) for k in keys))


def _list_watchers_one(stripe_key: str, extra: dict[str, Any], picker_only: bool = False) -> list[dict[str, Any]]:
    import httpx

    auth = (stripe_key, "")
    out: list[dict[str, Any]] = []
    params: dict[str, Any] = {"status": "complete", "limit": 100, **extra}
    with httpx.Client(timeout=30) as client:
        while True:
            r = client.get(f"{STRIPE_API}/checkout/sessions", params=params, auth=auth)
            r.raise_for_status()
            page = r.json()
            for s in page.get("data", []):
                is_picker = (s.get("metadata") or {}).get("bitdepth_watch") == "1"
                if picker_only and not is_picker:
                    continue
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
                specs = picker_specs(s.get("metadata")) if is_picker else parse_endpoints(text)
                out.append({"email": email, "quantity": qty, "specs": specs, "sub": sub_id})
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
    link = payment_links()
    if not (stripe_key and resend_key):
        print("watch: notify skipped (STRIPE_SECRET_KEY or RESEND_API_KEY not set)")
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


# ---------- keys: same scheme as site/api/_lib/keys.js ----------

def mint_key(sub_id: str, secret: str) -> str:
    import base64
    import hmac
    import hashlib

    sig = hmac.new(secret.encode(), sub_id.encode(), hashlib.sha256).hexdigest()[:32]
    b = base64.urlsafe_b64encode(sub_id.encode()).decode().rstrip("=")
    return f"bdw_{b}_{sig}"


def key_section(key: str, example: dict[str, Any] | None) -> list[str]:
    model, tag = (example["model"], example["tag"]) if example else ("deepseek/deepseek-v4-pro", "alibaba/fp8")
    return [
        "YOUR API KEY",
        key,
        "",
        "It unlocks the full row for any endpoint we grade, with no per-call payment: every night",
        "against the reference, self-agreement by prompt family, the self-check nights and the noise floor.",
        "Pass it in the X-Bitdepth-Key header. Try it now:",
        "",
        f'  curl -H "X-Bitdepth-Key: {key}" "https://bitdepth.dev/api/v1/row?model={model}&endpoint={tag}"',
        "",
        "Free with or without a key:",
        "  https://bitdepth.dev/v1/index.json          every model we grade",
        f"  https://bitdepth.dev/v1/or/{model}.json   every endpoint of one model, graded",
        "  https://bitdepth.dev/v1/changes.json        last night's changes",
        "",
        "In Claude or any MCP client, add the connector https://bitdepth.dev/api/mcp/mcp and ask",
        '"which DeepSeek V4 Pro endpoints match the reference, cheapest first?"',
        "",
        "The key works while your Watch plan is active. Keep it private.",
    ]


# ---------- welcome: the first email a new watcher gets ----------

def resolve(specs: list[str], quantity: int, rows: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    """Return (matched rows, specs that match nothing, specs beyond the paid quantity)."""
    paid, extra = specs[: max(quantity, 0)], specs[max(quantity, 0):]
    matched: list[dict[str, Any]] = []
    unknown: list[str] = []
    for spec in paid:
        hits = [r for r in rows.values() if matches(spec, {"model": r["model"], "tag": r["tag"]})]
        if hits:
            matched += hits
        else:
            unknown.append(spec)
    return matched, unknown, extra


def welcome_body(as_of: str, matched: list[dict[str, Any]], unknown: list[str], extra: list[str], key: str | None = None) -> str:
    lines = ["Welcome to Bitdepth Watch.", "", f"Here is where your endpoints stand as of the night of {as_of}.", ""]
    for r in matched:
        lines.append(f"- {r['label']} / {r['tag']}: {state_words(r)}, "
                     f"declared precision {_fmt(r.get('declared_quant'))}, output price {_fmt(r.get('price_out_per_m'))}")
    if unknown:
        lines += ["", "We could not find these, so they are not being watched yet:"]
        lines += [f"- {u}" for u in unknown]
        lines += ["Reply with the right name and we will fix it. Every endpoint we grade is listed at https://bitdepth.dev/v1/index.json"]
    if extra:
        lines += ["", "These go past the number of endpoints on your plan, so they are not watched:"]
        lines += [f"- {x}" for x in extra]
    lines += [
        "",
        "From tonight, you get an email the morning after any of these changes its grade state, declared precision or price, and every Monday a status email on all of them.",
        "",
        *(key_section(key, matched[0] if matched else None) + [""] if key else []),
        "Full table: https://bitdepth.dev",
        "Method: https://bitdepth.dev/method",
        "",
        FOOTER,
        "To change your endpoints, reply to this email or pick again at https://bitdepth.dev/watch. To cancel, use the link on your Stripe receipt.",
    ]
    return "\n".join(lines)


def _hash(sub_id: str) -> str:
    import hashlib

    return hashlib.sha256(sub_id.encode()).hexdigest()[:16]


def welcome(public: Path, ledger: Path, dry_run: bool = False) -> int:
    """Email each new subscription once. The ledger holds short hashes only, no emails."""
    stripe_key = os.environ.get("STRIPE_SECRET_KEY")
    resend_key = os.environ.get("RESEND_API_KEY")
    links = payment_links()
    if not (stripe_key and resend_key):
        print("watch: welcome skipped (STRIPE_SECRET_KEY or RESEND_API_KEY not set)")
        return 0
    data = json.loads(ledger.read_text()) if ledger.exists() else {}
    seen = set(data.get("welcomed", []))
    keyed = set(data.get("keyed", []))
    secret = os.environ.get("WATCH_KEY_SECRET", "")
    as_of, rows = load_current(public)
    sent = 0
    for w in list_watchers(stripe_key, links):
        sub = w.get("sub") or ""
        h = _hash(sub or w["email"])
        key = mint_key(sub, secret) if (secret and sub.startswith("sub_")) else None
        matched, unknown, extra = resolve(w["specs"], w["quantity"], rows)
        if h not in seen:
            if not dry_run:
                send_email(resend_key, w["email"], "Bitdepth Watch: you are set up", welcome_body(as_of, matched, unknown, extra, key))
                seen.add(h)
                if key:
                    keyed.add(h)
            sent += 1
            print(f"watch: welcome {h}: {len(matched)} matched, {len(unknown)} not found, {len(extra)} over quantity, key {'yes' if key else 'no'}")
        elif key and h not in keyed:
            body = "\n".join(["Your Bitdepth Watch plan now comes with an API key.", ""] + key_section(key, matched[0] if matched else None) + ["", FOOTER])
            if not dry_run:
                send_email(resend_key, w["email"], "Bitdepth Watch: your API key", body)
                keyed.add(h)
            sent += 1
            print(f"watch: key email {h}")
    if not dry_run:
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text(json.dumps({"welcomed": sorted(seen), "keyed": sorted(keyed)}, indent=2) + "\n")
    print(f"watch: {sent} welcome email(s)" + (" (dry run)" if dry_run else ""))
    return sent


# ---------- weekly: the email that always arrives ----------



def weekly_body(as_of: str, matched: list[dict[str, Any]], unknown: list[str]) -> str:
    inside = sum(1 for r in matched if r.get("state") == "within")
    lines = [
        "Your week on Bitdepth Watch.",
        "",
        f"Every endpoint below was tested every night this week. As of the night of {as_of}, "
        f"{inside} of {len(matched)} are within the pack.",
        "",
    ]
    for r in matched:
        lines.append(f"- {r['label']} / {r['tag']}: {state_words(r)}, "
                     f"declared precision {_fmt(r.get('declared_quant'))}, output price {_fmt(r.get('price_out_per_m'))}")
    if unknown:
        lines += ["", "We still cannot find these, so they are not watched:"] + [f"- {u}" for u in unknown]
        lines += ["Reply with the right name, or pick again at https://bitdepth.dev/watch"]
    lines += [
        "",
        "Between Mondays, you hear from us the morning after any of these changes grade, declared precision or price.",
        "",
        "Full table: https://bitdepth.dev",
        "",
        FOOTER,
        "To change your endpoints, reply to this email or pick again at https://bitdepth.dev/watch.",
    ]
    return "\n".join(lines)


def weekly(public: Path, dry_run: bool = False) -> int:
    stripe_key = os.environ.get("STRIPE_SECRET_KEY")
    resend_key = os.environ.get("RESEND_API_KEY")
    if not (stripe_key and resend_key):
        print("watch: weekly skipped (STRIPE_SECRET_KEY or RESEND_API_KEY not set)")
        return 0
    as_of, rows = load_current(public)
    sent = 0
    for w in list_watchers(stripe_key, payment_links()):
        matched, unknown, _extra = resolve(w["specs"], w["quantity"], rows)
        if not dry_run:
            send_email(resend_key, w["email"], f"Bitdepth Watch: your endpoints this week ({as_of})", weekly_body(as_of, matched, unknown))
        sent += 1
    print(f"watch: {sent} weekly email(s)" + (" (dry run)" if dry_run else ""))
    return sent


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--public", default="data/public/v1")
    ap.add_argument("--state", default="data/watch/last.json")
    ap.add_argument("--notify", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--welcome", action="store_true", help="only send first emails to new watchers")
    ap.add_argument("--weekly", action="store_true", help="send every watcher the Monday status email")
    ap.add_argument("--ledger", default="data/watch/welcomed.json")
    a = ap.parse_args(argv)
    if a.welcome:
        welcome(Path(a.public), Path(a.ledger), dry_run=a.dry_run)
        return 0
    if a.weekly:
        weekly(Path(a.public), dry_run=a.dry_run)
        return 0
    doc = run_changes(Path(a.public), Path(a.state))
    print(f"watch: {doc['count']} changes as of {doc['as_of']}" + (" (baseline night)" if doc["baseline"] else ""))
    if a.notify:
        notify(doc, dry_run=a.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
