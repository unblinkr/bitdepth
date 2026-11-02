# REPORT: rails-data

Run 2026-11-02 from the claude.ai session (not a fresh Code session; Mancy asked for it to run there). Merged to `main` locally and pushed, per CLAUDE.md workflow and Mancy's instruction to merge without review.

## Files

- New: `probe/emit.py`, `probe/badge.py`, `probe/templates/proposal.md`, `tests/test_emit.py`, `data/public/v1/index.json`, `data/public/v1/drift.json`, `data/public/v1/or/openai/gpt-oss-120b.json`, `data/public/v1/or/deepseek/deepseek-v4-pro.json`, this folder.
- Changed: `probe/packet.py` (`--attestation`, `--month`, `--buyer` alias), `.github/workflows/nightly.yml` (Emit step, `data/public` in the commit), `CLAUDE.md` (layout).

## Deviations from the brief

1. **State rule.** The brief said "inside the family noise floor on the primary columns" without a formula. Implemented: `outside` when an endpoint's self-agreement exceeds its agreement with the reference by more than 10 points (it agrees with itself more than with the reference). Provisional, stated in every file as `state_rule`, constant `GAP_MAX` in emit.py. On the 7-night data it marks four DeepSeek V4 Pro endpoints outside (crusoe/fp8, gmicloud/fp8, novita/fp8, cloudflare), which are also the bottom four by String. Every gpt-oss-120b endpoint with 7 nights is within. Calibrate on 2026-11-10.
2. **Nightly series.** The trend file keeps a per-night series for Exact only, not String, so the field is `nightly_exact`, not `nightly_string`. A per-night String series needs trend.py to keep it; left for the Nov 10 build.
3. **Proposal copy.** The attached file still says "draft". Mancy had seen it in chat; it is in `probe/templates/proposal.md` and is used. Packets are never sent automatically. Its first line ("This packet is one week of rows") reads oddly inside a monthly attestation; reword when she next edits it.

## Verification

1. `python -m pytest -q`: 43 passed (4 new in test_emit.py).
2. deepseek-v4-pro: `2026-11-02 7 15`. gpt-oss-120b: `2026-11-02 7 27`. Two gpt-oss endpoints are `no_data` (deepinfra/fp8 4 nights, primeintellect/fp4 2 nights).
3. `drift.json`: one item, venice/int4 on gpt-oss-120b, movement -10.2.
4. Banned terms: whole-word hits only in the older `tasks/probe-harness/REPORT.md` and `tasks/selfcheck-trend/*` records, which list the terms; zero in new files. Em dash: zero in new and changed files (the two hits in `data/runs/*/responses.jsonl` are model outputs, unchanged).
5. Sample: `python -m probe.packet --attestation --month 2026-11 --buyer Requesty --providers together,nebius,amazon-bedrock,azure,google-vertex` writes `packets/requesty-attestation-2026-11.md` (git ignored). Monthly summary: 2 nights in November so far, all six Requesty endpoints 2 of 2 inside the floor.

```
BOARD SYNC
todoist_task: Bitdepth, Rails: data emitter and attestation packet
closes: none
new issues opened: none
needs_mancy: none (proposal first line to reword at her leisure)
live: data/public/v1 on main
```
