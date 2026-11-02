# TASK: Public data rails in the probe repo (JSON emitter, drift feed, dated attestation packet)

**Repository:** `unblinkr/bitdepth`
**Save this file to:** `tasks/rails-data/TASK.md`
**Branch:** `rails-data`, merged to `main` by PR at the end. Nothing here changes the nightly probe itself.
**Run with:** this brief plus the attached `proposal-page-copy-2026-11-02.md` (only if Mancy has marked it approved; if the file is absent or says "draft", build the proposal page with the placeholder text `PROPOSAL COPY PENDING` and say so in REPORT.md). Write `QUESTIONS.md` and `REPORT.md` next to this file.
**Start this task in a fresh Claude Code session.** Do not continue an existing thread; stale context burns tokens and this brief is self-contained.
**Executor model:** sonnet
**Date issued:** 2026-11-02
**todoist_task:** Bitdepth board, "Rails: data emitter and attestation packet"
**closes:** none
**PR mode:** open PR `rails-data` into `main`; Mancy merges.

---

## 1. Goal

After this task, every nightly run also writes machine-readable public files under `data/public/v1/`, and `probe/packet.py` can produce a dated monthly attestation for a named buyer. The site brief (`tasks/rails-site/TASK.md` in `unblinkr/bitdepth-site`) reads these files. Nothing in this task publishes a web page.

## 2. Context

The probe has run nightly since 2026-10-27 on `openai/gpt-oss-120b` and `deepseek/deepseek-v4-pro`, every OpenRouter endpoint. The fourteen-night read is 2026-11-10. The repo is public. `probe/packet.py` (built 2026-11-01) already produces per-recipient row tables; see `packets/` output and the Requesty example. `data/trend/latest.md` is the cross-night trend file from the selfcheck-trend task. On DeepSeek V4 Pro the grade reads String and self-agreement first, Exact second (decision of 2026-10-31).

## 3. Decisions already made (do not re-ask)

- New module `probe/emit.py`, called at the end of the nightly workflow after the trend file is written. Pure function of files already in `data/`; no network calls.
- Output, one file per model: `data/public/v1/or/<author>/<slug>.json`, plus `data/public/v1/index.json` (list of models with `as_of` and file path) and `data/public/v1/drift.json`.
- Per-model schema (from the 2026-10-28 overlay plan, extended):

```json
{
  "schema": "bitdepth.or.v1",
  "model": "deepseek/deepseek-v4-pro",
  "as_of": "2026-11-02",
  "nights": 7,
  "reference_rule": "plurality across all endpoints (fewer than two declare bf16 or fp16)",
  "method_url": "https://bitdepth.dev/method",
  "primary_columns": ["string", "self_agree"],
  "noise_floor": {"math": 29.0, "json": 63.8, "string": 66.5, "needle": 100.0, "echo": 97.0},
  "endpoints": [
    {
      "tag": "deepinfra/fp8",
      "provider_slug": "deepinfra",
      "declared_quant": "fp8",
      "nights": 7,
      "exact": 75.1, "exact_sd": 2.6,
      "string": 63.9, "self_agree": 65.8,
      "movement": 3.0, "movement_flag": false,
      "price_in_per_m": 1.30, "price_out_per_m": 2.60,
      "state": "within",
      "nightly_string": [63.1, 64.0, 63.5, 64.4, 63.9, 64.2, 64.1]
    }
  ],
  "footer": "Numbers against a stated reference. Not a claim about intent."
}
```

  `state`: `within` (inside the family noise floor on the primary columns), `outside`, `no_data` (fewer than 7 nights), `stale` (as_of older than 3 nights). Use the same column math packet.py already uses; do not invent a new grade. `primary_columns` is `["exact"]` for gpt-oss-120b and `["string", "self_agree"]` for deepseek-v4-pro, read from a small config dict in emit.py.
- `drift.json`: every (endpoint, model) pair whose `movement_flag` is true in the latest run, with the movement value and the nights compared. Empty list is valid.
- Workflow: the nightly GitHub Actions job commits `data/public/` along with the rest of the night's data. No new secrets.
- `probe/packet.py` gains `--attestation --month YYYY-MM --buyer <name> --providers <comma list>`: a cover page (buyer, month, models, nights counted, generated date), the existing tables cut to the buyer's providers first, a monthly summary line per endpoint (nights within the floor out of nights run), and the proposal page from the attached copy as the last section. Output Markdown and, if `pandoc` is available, PDF, into the git-ignored `packets/`.
- A badge generator `probe/badge.py` writes `packets/badges/<provider>-<model-slug>.svg` (text: "Verified by Bitdepth", the month, "inside the floor N of M nights"). Generated only on request; never committed.

## 4. Hard rules (violating any fails the task)

- No em dashes in any file or commit message.
- The nightly probe's prompts, models, schedule and grading do not change.
- No file characterises a provider's intent or conduct. JSON carries numbers, states and the footer string only.
- The banned terms from `tasks/probe-harness/TASK.md` section 5 do not appear in any new file; grep before the PR, excluding `tasks/*/TASK.md`.
- No secrets in output. `OPENROUTER_API_KEY` stays a repo secret.

## 5. Build scope

### Change A: `probe/emit.py`, schema, workflow step
Emit from the existing night's data. Backfill: run once over all nights to date so `data/public/v1/` exists in the PR.

### Change B: `drift.json` and `index.json`

### Change C: `packet.py --attestation` and `badge.py`
Produce one sample: `--buyer Requesty --providers together,nebius,amazon-bedrock,azure,google-vertex --month 2026-11`. Paste its first and last 30 lines into REPORT.md.

### Change D: tests
`tests/test_emit.py`: schema keys present; `state` logic on a fixture (6 nights gives `no_data`, an out-of-floor fixture gives `outside`); drift list matches `movement_flag`.

## 6. Out of scope

- Any web page, API server, MCP server or payment code (that is the site brief).
- New models, new prompt families, cache hit rate column (Nov 10 build list).
- Publishing anything outside the repo.

## 7. Verification (run them; paste results into REPORT.md)

1. `python -m pytest tests/test_emit.py -q`
2. `ls -R data/public/v1` and `python -c "import json;d=json.load(open('data/public/v1/or/deepseek/deepseek-v4-pro.json'));print(d['as_of'],d['nights'],len(d['endpoints']))"`
3. Same for gpt-oss-120b.
4. `cat data/public/v1/drift.json`
5. Banned-terms and em-dash grep, zero, commands and output pasted.
6. The workflow file diff.

## 8. Handback

`tasks/rails-data/REPORT.md`: files created, the PR URL, the sample attestation excerpt, anything in `QUESTIONS.md`.

End the session with this block, exactly this shape:

```
BOARD SYNC
todoist_task: Bitdepth, Rails: data emitter and attestation packet
closes: none
new issues opened: <#n title> | none
needs_mancy: <merge PR #n; approve proposal copy if pending> | none
live: data/public/v1 in PR <url>
```
