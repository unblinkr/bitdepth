# TASK: Trust gate. Stop testing and routing to endpoints that were delisted, lost ZDR, or have an open incident

**Repository:** `unblinkr/bitdepth`
**Save this file to:** `tasks/trust-gate/TASK.md`
**Branch:** `task/trust-gate`
**Run with:** this brief alone. Read `CLAUDE.md` first; its Rules section is binding. Branch per change, tests green, merge locally, push `main`. Write `QUESTIONS.md` and `REPORT.md` next to this file.
**Start this task in a fresh Claude Code session.** Do not continue an existing thread; stale context burns tokens and this brief is self-contained.
**Date issued:** 2026-11-22
**PR mode:** merge on green. The nightly workflow commits to `main`; do not merge while a run is in progress.

---

## 1. Goal

The route lists grade quality and price. They say nothing about whether a host can be trusted with a prompt. Add a trust gate so that an endpoint is neither probed nor allowed when any of these is true:

1. **Delisted.** It is in our history but no longer in OpenRouter's `GET /api/v1/models/{slug}/endpoints` list.
2. **Lost ZDR.** It was on OpenRouter's public Zero Data Retention list (`GET /api/v1/endpoints/zdr`, no auth, about 934 entries on Nov 22) on an earlier night and is not on it tonight.
3. **Open incident.** Its provider has an entry in a hand-kept `data/incidents.json` with no `closed` date.

## 2. Why

On Nov 21 OpenRouter told customers an attacker had searched GMI Cloud's stored prompts for credentials, and disabled every GMI endpoint. On Nov 22 it off-boarded three providers and removed 125 endpoints from ZDR. Our Nov 21 list still allowed `gmicloud/fp8`, `novita/fp8` and `together` on DeepSeek V4.1 Flash. A check run on Nov 22 found 11 allowed endpoints across three models no longer listed by OpenRouter, including `gmicloud/fp8`, `novita/fp4` and `phala`.

## 3. What to build

- `probe/trust.py`
  - `snapshot_zdr()`: fetch the ZDR list, write `data/trust/zdr/<date>.json` (model_id, tag, provider_name only).
  - `delisted(model, history_tags, live_tags)`.
  - `lost_zdr(today, prior)`: endpoints on the most recent earlier snapshot and missing today. First night has no prior, so nothing is flagged by this check.
  - `open_incidents()`: reads `data/incidents.json`.
  - `trust_flags(model, endpoints) -> {tag: reason}` where reason is one of `delisted <date>`, `lost ZDR <date>`, `open incident: <provider> <date> <source_url>`.
- `data/incidents.json`, seeded with:
  - GMI Cloud, opened 2026-11-21, source: OpenRouter customer notice (email) and https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/
  - Novita, Phala, Together, each opened 2026-11-22, same blog URL as source. Scope: provider-wide until closed.
  - Schema per entry: `provider_name`, `opened`, `closed` (null), `source_url`, `note`.
- Nightly run: call `trust_flags` before probing. Flagged endpoints are skipped (no requests sent) and recorded as `state: "untrusted"` with the reason.
- `probe/emit.py`: `routable()` returns False for untrusted rows; `exclusion_reason()` returns the trust reason. The reason must show in each route JSON's `excluded[].why`, word for word.
- `ROUTE_RULE` text gains: "and no trust flag (delisted, lost ZDR, open incident)".
- Site: on each model's data page, show untrusted endpoints in their own small table with the reason and source link. No other site changes.
- `tests/test_trust.py`: delisted, lost ZDR, incident open, incident closed, first night with no prior snapshot, prefix shadowing still works when a parent slug is untrusted.

## 4. Rules that apply

- Both OpenRouter calls are public and free. No new paid calls.
- A flag only ever removes an endpoint. Nothing here can add one to an allow list.
- An endpoint flagged `delisted` that reappears becomes routable again only after it earns `MIN_ROUTE_NIGHTS` fresh nights.
- An endpoint flagged `lost ZDR` clears when it is back on the ZDR list for 7 straight nights.
- Incidents clear only by a human setting `closed`. The code never closes one.
- Do not delete history rows for flagged endpoints. Past grades stay as they were.

## 5. Done when

- Tonight's run sends zero requests to GMI Cloud, Novita, Phala or Together endpoints.
- Every route JSON regenerates with those endpoints under `excluded` with a reason.
- `REPORT.md` lists every endpoint flagged on the first run, by model and reason, and the count still allowed per model.
