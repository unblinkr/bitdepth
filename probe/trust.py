"""Trust gate: endpoints that are neither probed nor allowed on a route list.

    python -m probe.trust --date YYYY-MM-DD           ZDR and listing snapshots for the date
    python -m probe.trust --date YYYY-MM-DD --show    print every flag, by model, from files only

An endpoint is flagged when any of these holds:

1. delisted: it is in our listing history but not in OpenRouter's current
   GET /api/v1/models/{slug}/endpoints list. One that comes back is probed again and
   becomes routable only after MIN_FRESH_NIGHTS probed nights since it came back.
2. lost ZDR: it was on OpenRouter's public Zero Data Retention list
   (GET /api/v1/endpoints/zdr) on the most recent earlier snapshot and is not on it
   tonight. The flag clears after ZDR_CLEAR_NIGHTS straight snapshots back on the list.
   The first snapshot has no prior, so this check flags nothing that night.
3. open incident: its provider has an entry in data/incidents.json with no `closed`
   date. Only a person closes an incident; the code never does.

A flag only ever removes an endpoint. Nothing here adds one to an allow list, and no
history row is deleted. Both OpenRouter calls are public and need no key.

Files:
- data/trust/zdr/<date>.json     the ZDR list (model_id, tag, provider_name only)
- data/trust/listed/<date>.json  every configured model's endpoint listing (tag, provider_name)
- data/incidents.json            hand-kept, one entry per provider incident
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Callable, Iterable

import httpx

from probe import MODELS

BASE = "https://openrouter.ai/api/v1"
ZDR_URL = f"{BASE}/endpoints/zdr"
DATA = Path("data")
MIN_FRESH_NIGHTS = 7  # same as emit.MIN_ROUTE_NIGHTS
ZDR_CLEAR_NIGHTS = 7
# A ZDR fetch that returns fewer than this share of the prior snapshot's entries is
# treated as a failed fetch, not as a mass removal, and is not written.
ZDR_MIN_SHARE = 0.5

Key = tuple[str, str]  # (normalized model id, tag)


# ---------------------------------------------------------------- normalizing


_DATE_SUFFIX = re.compile(r"-(\d{4}|\d{6}|\d{8}|\d{4}-\d{2}-\d{2})$")


def norm_model(model_id: str | None) -> str:
    """Model id without a trailing date or version stamp: our slug
    deepseek/deepseek-v4.1-flash-1017 and the ZDR list's deepseek/deepseek-v4.1-flash match."""
    return _DATE_SUFFIX.sub("", (model_id or "").strip().lower())


def norm_provider(name: str | None) -> str:
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def zdr_keys(entries: Iterable[dict[str, Any]]) -> set[Key]:
    return {(norm_model(e.get("model_id")), e.get("tag") or "") for e in entries if e.get("tag")}


# ---------------------------------------------------------------- fetching and snapshots


def fetch_zdr(client: httpx.Client | None = None) -> list[dict[str, Any]]:
    """The public ZDR list, reduced to model_id, tag and provider_name."""
    c = client or httpx.Client(timeout=60.0)
    r = c.get(ZDR_URL, headers={"HTTP-Referer": "https://bitdepth.dev", "X-Title": "Bitdepth probe"})
    r.raise_for_status()
    data = r.json().get("data") or []
    out = [{"model_id": e.get("model_id"), "tag": e.get("tag"), "provider_name": e.get("provider_name")} for e in data]
    return sorted(out, key=lambda e: (e["model_id"] or "", e["tag"] or ""))


def _dated(folder: Path) -> list[tuple[str, Path]]:
    if not folder.exists():
        return []
    return sorted((p.stem, p) for p in folder.glob("*.json") if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem))


def load_zdr_snapshots(data_dir: Path = DATA) -> list[tuple[str, list[dict[str, Any]]]]:
    return [(d, json.loads(p.read_text())["entries"]) for d, p in _dated(data_dir / "trust" / "zdr")]


def check_zdr_size(entries: list[dict[str, Any]], prior: list[dict[str, Any]] | None) -> None:
    if not entries:
        raise RuntimeError("ZDR list came back empty; not treated as a snapshot")
    if prior and len(entries) < ZDR_MIN_SHARE * len(prior):
        raise RuntimeError(f"ZDR list has {len(entries)} entries against {len(prior)} on the prior snapshot; "
                           "treated as a failed fetch, not a snapshot")


def snapshot_zdr(date: str, data_dir: Path = DATA, fetcher: Callable[[], list[dict[str, Any]]] = fetch_zdr) -> Path:
    """Fetch the ZDR list and write data/trust/zdr/<date>.json."""
    entries = fetcher()
    prior = [e for d, e in load_zdr_snapshots(data_dir) if d < date]
    check_zdr_size(entries, prior[-1] if prior else None)
    p = data_dir / "trust" / "zdr" / f"{date}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"date": date, "source": ZDR_URL, "count": len(entries), "entries": entries}, indent=1) + "\n")
    return p


def snapshot_listed(date: str, data_dir: Path = DATA, lister: Callable[[str], list[dict[str, Any]]] | None = None) -> Path:
    """Every configured model's current endpoint listing, written to data/trust/listed/<date>.json.
    A model whose listing call fails is left out (no record), never written as empty."""
    if lister is None:
        from probe import openrouter
        lister = openrouter.list_endpoints
    models: dict[str, Any] = {}
    errors: dict[str, str] = {}
    for m in MODELS:
        try:
            eps = lister(m["slug"])
        except Exception as exc:  # noqa: BLE001 - recorded, the model gets no record tonight
            errors[m["slug"]] = type(exc).__name__
            continue
        models[m["slug"]] = sorted(({"tag": e["tag"], "provider_name": e.get("provider_name")} for e in eps),
                                   key=lambda e: e["tag"])
    p = data_dir / "trust" / "listed" / f"{date}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"date": date, "models": models, "errors": errors}, indent=1) + "\n")
    return p


# ---------------------------------------------------------------- listing history


def _label_of(slug: str) -> str | None:
    return next((m["label"] for m in MODELS if m["slug"] == slug), None)


def listings(slug: str, data_dir: Path = DATA, runs_dir: Path | None = None) -> list[tuple[str, dict[str, str | None]]]:
    """Every night this model has a listing record for, oldest first: (date, {tag: provider_name}).
    Sources: each run's endpoints.json (its `listed` field when present, else its endpoints)
    and data/trust/listed/<date>.json. The trust snapshot wins on a date that has both,
    because it is taken after the run. Nights with no record for the model are not
    absences (a twice-weekly model is not listed on its off nights)."""
    runs_dir = runs_dir or data_dir / "runs"
    label = _label_of(slug)
    out: dict[str, dict[str, str | None]] = {}
    if runs_dir.exists():
        for p in sorted(runs_dir.glob("*/endpoints.json")):
            d = p.parent.name
            try:
                doc = json.loads(p.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            for key, m in (doc.get("models") or {}).items():
                if m.get("slug") == slug or (not m.get("slug") and key == label):
                    eps = m.get("listed") if m.get("listed") is not None else m.get("endpoints", [])
                    out[d] = {e["tag"]: e.get("provider_name") for e in eps}
    for d, p in _dated(data_dir / "trust" / "listed"):
        models = json.loads(p.read_text()).get("models") or {}
        if slug in models:
            out[d] = {e["tag"]: e.get("provider_name") for e in models[slug]}
    return sorted(out.items())


def delisted(model: str, history_tags: Iterable[str], live_tags: Iterable[str]) -> set[str]:
    """Tags in our history for `model` that are not in tonight's listing."""
    del model
    return set(history_tags) - set(live_tags)


def delisted_dates(seq: list[tuple[str, dict[str, Any]]]) -> dict[str, str]:
    """For each tag absent from the last listing: the first night it was missing."""
    out: dict[str, str] = {}
    seen: set[str] = set()
    for d, tags in seq:
        cur = set(tags)
        for t in seen - cur:
            out.setdefault(t, d)
        for t in cur:
            out.pop(t, None)
        seen |= cur
    return out


def relisted_dates(seq: list[tuple[str, dict[str, Any]]]) -> dict[str, tuple[str, str]]:
    """For each tag in the last listing that was missing on an earlier night after first
    being listed: (the first night of its latest absence, the night it came back)."""
    out: dict[str, tuple[str, str]] = {}
    seen: set[str] = set()
    gone: dict[str, str] = {}
    for d, tags in seq:
        cur = set(tags)
        for t in seen - cur:
            gone.setdefault(t, d)
        for t in cur:
            if t in gone:
                out[t] = (gone.pop(t), d)
        seen |= cur
    last = set(seq[-1][1]) if seq else set()
    return {t: v for t, v in out.items() if t in last}


# ---------------------------------------------------------------- ZDR


def lost_zdr(today: Iterable[dict[str, Any]] | set[Key], prior: Iterable[dict[str, Any]] | set[Key] | None) -> set[Key]:
    """(model, tag) keys on the most recent earlier snapshot and missing today. No prior
    (the first night) means nothing is flagged."""
    if prior is None:
        return set()
    t = today if isinstance(today, set) else zdr_keys(today)
    p = prior if isinstance(prior, set) else zdr_keys(prior)
    return p - t


def zdr_flags(snapshots: list[tuple[str, list[dict[str, Any]] | set[Key]]], clear_nights: int = ZDR_CLEAR_NIGHTS) -> dict[Key, str]:
    """Keys flagged lost ZDR after the last snapshot, with the date each was lost. A key
    clears after `clear_nights` straight snapshots back on the list."""
    flagged: dict[Key, str] = {}
    streak: dict[Key, int] = {}
    prev: set[Key] | None = None
    for d, entries in sorted(snapshots, key=lambda x: x[0]):
        cur = entries if isinstance(entries, set) else zdr_keys(entries)
        lost = lost_zdr(cur, prev)
        for k in lost:
            flagged[k] = d
            streak[k] = 0
        for k in list(flagged):
            if k in lost:
                continue
            if k in cur:
                streak[k] = streak.get(k, 0) + 1
                if streak[k] >= clear_nights:
                    del flagged[k]
                    del streak[k]
            else:
                streak[k] = 0
        prev = cur
    return flagged


# ---------------------------------------------------------------- incidents


def load_incidents(data_dir: Path = DATA) -> list[dict[str, Any]]:
    p = data_dir / "incidents.json"
    if not p.exists():
        return []
    doc = json.loads(p.read_text())
    return doc.get("incidents", []) if isinstance(doc, dict) else doc


def open_incidents(data_dir: Path = DATA, incidents: list[dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
    """{normalized provider name: incident} for every entry with no `closed` date. When a
    provider has more than one open entry, the earliest opened is kept."""
    out: dict[str, dict[str, Any]] = {}
    for i in sorted(incidents if incidents is not None else load_incidents(data_dir), key=lambda x: x.get("opened") or ""):
        if i.get("closed"):
            continue
        out.setdefault(norm_provider(i.get("provider_name")), i)
    return out


# ---------------------------------------------------------------- the gate


def incident_reason(i: dict[str, Any]) -> str:
    return f"open incident: {i['provider_name']} {i['opened']} {i['source_url']}"


def source_url(reason: str, slug: str) -> str | None:
    """The link behind a reason: the incident's source, the ZDR list, or the model's endpoint list."""
    if reason.startswith("open incident:"):
        m = re.search(r"(https?://\S+)$", reason)
        return m.group(1) if m else None
    if reason.startswith("lost ZDR"):
        return ZDR_URL
    if reason.startswith("delisted"):
        return f"{BASE}/models/{slug}/endpoints"
    return None


def trust_flags(
    model: str,
    endpoints: list[dict[str, Any]] | None = None,
    *,
    date: str | None = None,
    data_dir: Path = DATA,
    runs_dir: Path | None = None,
    zdr_today: list[dict[str, Any]] | None = None,
    probing: bool = True,
    fresh_nights: dict[str, int] | None = None,
    incidents: list[dict[str, Any]] | None = None,
) -> dict[str, str]:
    """{tag: reason} for every endpoint of `model` (a slug) that is not to be probed or routed.

    endpoints: tonight's live listing (dicts with tag and provider_name). None means the
    latest listing on file is tonight's (emit reads files only).
    date: tonight's date; listings and ZDR snapshots on file from this date on are
    replaced by `endpoints` and `zdr_today`.
    zdr_today: tonight's ZDR list, when fetched but not yet written as a snapshot.
    probing: True for the nightly run, where an endpoint that came back after a delisting
    is probed again so it can earn fresh nights. False for route lists, where it stays
    flagged until it has MIN_FRESH_NIGHTS probed nights (counted in fresh_nights) since it came back.

    Reasons: "delisted <date>", "lost ZDR <date>", "open incident: <provider> <date> <source_url>".
    When more than one applies, an open incident is reported first, then lost ZDR, then delisted.
    """
    seq = listings(model, data_dir, runs_dir)
    if endpoints is not None:
        if date:
            seq = [(d, t) for d, t in seq if d < date]
        seq.append((date or "9999-12-31", {e["tag"]: e.get("provider_name") for e in endpoints}))
    if not seq:
        return {}
    tonight = seq[-1][1]
    provider: dict[str, str | None] = {}
    for _, tags in seq:
        provider.update({t: p for t, p in tags.items() if p})

    flags: dict[str, str] = {}
    gone = delisted_dates(seq)
    for t in delisted(model, provider.keys() | gone.keys(), tonight.keys()):
        if t in gone:
            flags[t] = f"delisted {gone[t]}"
    if not probing:
        for t, (d_gone, d_back) in relisted_dates(seq).items():
            n = (fresh_nights or {}).get(t, 0)
            if n < MIN_FRESH_NIGHTS:
                flags[t] = f"delisted {d_gone}; listed again {d_back}, {n} of {MIN_FRESH_NIGHTS} fresh nights"

    snaps: list[tuple[str, Any]] = load_zdr_snapshots(data_dir)
    if zdr_today is not None:
        snaps = [(d, e) for d, e in snaps if not date or d < date] + [(date or "9999-12-31", zdr_today)]
    lost = zdr_flags(snaps)
    nm = norm_model(model)
    for t in provider.keys() | tonight.keys():
        if (nm, t) in lost:
            flags[t] = f"lost ZDR {lost[(nm, t)]}"

    inc = open_incidents(data_dir, incidents)
    for t in provider.keys() | tonight.keys():
        i = inc.get(norm_provider(provider.get(t) or tonight.get(t)))
        if i:
            flags[t] = incident_reason(i)
    return flags


def fresh_nights_from_rows(rows: list[dict[str, Any]], slug: str, data_dir: Path = DATA, runs_dir: Path | None = None) -> dict[str, int]:
    """Probed nights per relisted tag since it came back, from emit rows' nightly_exact dates."""
    back = relisted_dates(listings(slug, data_dir, runs_dir))
    out: dict[str, int] = {}
    for r in rows:
        if r["tag"] in back:
            since = back[r["tag"]][1]
            out[r["tag"]] = sum(1 for p in r.get("nightly_exact") or [] if p.get("date", "") >= since)
    return out


# ---------------------------------------------------------------- command line


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", required=True)
    ap.add_argument("--data", default=str(DATA))
    ap.add_argument("--show", action="store_true", help="print the flags from files only; fetch nothing")
    a = ap.parse_args(argv)
    data_dir = Path(a.data)
    if not a.show:
        try:
            print(snapshot_zdr(a.date, data_dir))
        except Exception as exc:  # noqa: BLE001 - a failed fetch writes nothing; earlier flags still stand
            print(f"ZDR snapshot not written: {exc}")
        print(snapshot_listed(a.date, data_dir))
    for m in MODELS:
        flags = trust_flags(m["slug"], data_dir=data_dir, probing=True)
        print(f"{m['slug']}: {len(flags)} flagged")
        for t, why in sorted(flags.items()):
            print(f"  {t}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
