# REPORT: Trust gate

Date: 2026-11-23. Branch `task/trust-gate`, merged locally into `main`.

## What was built

- `probe/trust.py`: `snapshot_zdr()`, `snapshot_listed()`, `delisted()`, `lost_zdr()`, `zdr_flags()` (the 7-night clearing rule), `open_incidents()`, `trust_flags(model, endpoints) -> {tag: reason}`. Reasons are `delisted <date>`, `lost ZDR <date>`, `open incident: <provider> <date> <source_url>`. When more than one applies, the incident is reported first, then lost ZDR, then delisted. A relisted endpoint is probed again but stays off route lists with `delisted <date>; listed again <date>, <n> of 7 fresh nights` until it has `MIN_ROUTE_NIGHTS` probed nights since it came back.
- ZDR matching is on tag plus a normalized model id (a trailing date or version stamp such as `-1017` or `-20261120` is dropped), so `deepseek/deepseek-v4.1-flash-1017` matches the ZDR list's `deepseek/deepseek-v4.1-flash`. Tested.
- A ZDR fetch that comes back empty or with under half the prior snapshot's entries is treated as a failed fetch and is not written, so a bad response cannot flag the whole list for seven nights. Earlier flags and incidents still apply on such a night.
- `data/trust/listed/<date>.json`: every configured model's listing, taken nightly (free, keyless). Needed so emit, which reads files only, can tell a delisting, including for the twice-weekly models on their off nights. Nights with no record for a model are never read as absences.
- `data/incidents.json`: GMICloud (opened 2026-11-21), Novita, Phala, Together (opened 2026-11-22), all `closed: null`, source the OpenRouter blog URL, note "Provider security notice; see source." Provider names match OpenRouter's `provider_name` values (`GMICloud` is one word in OpenRouter's data).
- `probe/run.py`: `apply_trust()` runs after the listing and before the estimate. Flagged endpoints are removed from the probe set (no request sent) and written to `endpoints.json` under `untrusted` with `state: "untrusted"` and the reason; the full live list is kept under `listed`. `run.json` carries a `trust` block (ZDR fetch status and every flag).
- `probe/emit.py`: flagged rows get `state: "untrusted"`, keep the grade under `graded_state`, and carry `trust_reason` and `trust_source_url`. `routable()` is False for them; `exclusion_reason()` returns the trust reason word for word. Each model file lists every flagged tag under `untrusted`; flagged tags with no graded row are also put under the route list's `excluded`. `ROUTE_RULE` gains "and no trust flag (delisted, lost ZDR, open incident)".
- `probe/site.py`: each `/m/<model>` page shows a small "Trust gate" table (endpoint, reason, source link). Untrusted rows leave the main board. The preview build drops the list (real tags). No other site change.
- `probe/watch.py`: plain words for the new state in alert emails.
- `.github/workflows/nightly.yml`: a "Trust snapshots" step before emit, and `data/trust` added to the commit.
- Tests: `tests/test_trust.py` (14 tests: delisted, relisted, lost ZDR with clearing, first night with no prior, incident open, incident closed, ZDR id normalization, collapsed ZDR fetch, route reasons word for word, prefix shadowing both ways, nightly run sends nothing to a flagged endpoint). `tests/conftest.py` keeps every test offline. `tests/route_list.test.mjs` accepts trust reasons. `tests/test_actor_probe.py` was already failing on `main` (it pinned `deepinfra/fp8`, which left the gpt-oss-120b listing on 2026-11-16); it now uses `deepinfra/bf16`.
- pytest: 142 passed. node tests: 18 passed.

## First pass (2026-11-23)

ZDR: first snapshot taken today (928 entries), so nothing is flagged lost ZDR until tomorrow's snapshot. Listing snapshot taken today. Route JSON regenerated from files with `python -m probe.emit` (as of 2026-11-22). No paid call was made.

Every endpoint flagged, by model and reason:

**openai/gpt-oss-120b** (9)
- open incident: novita/fp4 (Novita), phala (Phala), together (Together)
- delisted: akashml/bf16 (2026-11-04), mara (2026-11-05), deepinfra/fp8 (2026-11-16), io-net/fp4 (2026-11-16), sail-research/fp4 (2026-11-21), dekallm/bf16 (2026-11-23)

**deepseek/deepseek-v4-pro** (6)
- open incident: gmicloud/fp8 (GMICloud), novita/fp8 (Novita)
- delisted: cloudflare (2026-11-04), crusoe/fp8 (2026-11-04), nebius/fp8 (2026-11-10), atlas-cloud/fp4 (2026-11-21)

**deepseek/deepseek-v4.1-flash-1017** (14 by the probe gate, 18 on the route list)
- open incident: gmicloud/fp8 (GMICloud), novita/fp8 (Novita), phala (Phala), together (Together)
- delisted: decart/fp4 (2026-11-05), cohere (2026-11-07), fireworks/ultrafast (2026-11-10), relace/fast (2026-11-10), decart/fp8 (2026-11-11), ionstream/flex (2026-11-18), nebius/fp8 (2026-11-18), atlas-cloud/fp8 (2026-11-21), stepfun/fp8 (2026-11-22), dekallm (2026-11-23)
- listed again, not yet 7 fresh nights (route list only; still probed): modelrun/fp4 (delisted 2026-11-11, back 2026-11-17, 6 of 7), reka (delisted 2026-11-16, back 2026-11-20, 3 of 7), sail-research/fp4 and sail-research/fp4/us (delisted 2026-11-19, back 2026-11-21, 2 of 7)

**mistralai/mistral-large-4-0** (0)

**z-ai/glm-5.3-flash** (10 by the probe gate, 11 on the route list)
- open incident: gmicloud/fp8 (GMICloud), novita/fp8 (Novita), phala/nvfp4 (Phala), together (Together)
- delisted: primeintellect (2026-11-14), baseten/fp8/us (2026-11-14), atlas-cloud/fp8 (2026-11-19), nextbit/fp4 (2026-11-19), parasail/fp4 (2026-11-19), dekallm (2026-11-23)
- listed again: river (delisted 2026-11-11, back 2026-11-14, 3 of 7)

**google/gemma-4-31b-it** (4 by the probe gate, 5 on the route list)
- open incident: novita/bf16 (Novita)
- delisted: io-net (2026-11-11), dekallm (2026-11-16), primeintellect/fp4 (2026-11-16)
- listed again: modelrun/fp4 (delisted 2026-11-11, back 2026-11-19, 1 of 7)

**xiaomi/mimo-v2.6-pro** (1)
- open incident: gmicloud/bf16 (GMICloud)

## Allowed per model after the gate (route lists as of 2026-11-22)

| Model | Allowed before | Allowed now |
|---|---|---|
| openai/gpt-oss-120b | 28 | 20 |
| deepseek/deepseek-v4-pro | 13 | 12 |
| deepseek/deepseek-v4.1-flash-1017 | 43 | 32 |
| mistralai/mistral-large-4-0 | 2 | 2 |
| z-ai/glm-5.3-flash | 0 | 0 |
| google/gemma-4-31b-it | 0 | 0 |
| xiaomi/mimo-v2.6-pro | 0 | 0 |

## Tonight's run

A dry check (public listing calls only, no completions) of `resolve_models` plus `apply_trust` for 2026-11-23 leaves zero GMICloud, Novita, Phala or Together endpoints in any model's probe set. The probe set is 22, 12, 48, 2, 38, 17 and 4 endpoints across the seven models.

## Not done or open

- See `QUESTIONS.md`: the MCP `check_before_route` tool and `site/api/_lib/routes.js` were left unchanged under "no other site changes".
- `CLAUDE.md` Layout does not yet mention `probe/trust.py`, `data/trust/` or `data/incidents.json`.
