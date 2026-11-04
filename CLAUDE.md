# Bitdepth probe harness

Nightly probe of OpenRouter inference endpoints. The repository is public so that GitHub Actions minutes are free, but it is not a published surface: scorecards here are working data, not findings, and nothing in this repository is linked from anywhere.

## Rules

- No em dashes in any file, docstring, commit message, issue title or run record.
- No prompt text or answer copied from a public benchmark or eval set.
- No file characterises a provider's intent or conduct. Scorecards report numbers against a stated reference and nothing else.
- Spend never exceeds $7.00 in a night (raised from $5.00 on 2026-11-04 when a third model was added). The cap is code, not convention.
- `OPENROUTER_API_KEY` is read from the environment only. It never appears in a file, a log, a run record or a commit.
- OpenRouter rate limits and terms are respected. Concurrency never exceeds 4.
- Every run writes `data/runs/<date>/run.json` with a `source` marker (`live` for cron, `dispatch` for manual, `local` for a session run), the prompts dropped for budget, and the cost actually billed.
- No model-written code is executed. Graders compare strings and numbers only.

## Workflow

- Branch per change.
- Tests green before merge (`pytest`).
- Merge locally and push `main`.

## Layout

- `probe/` the package: `openrouter.py` (client), `generators.py` (prompt families and graders), `budget.py` (cost estimate and cap), `run.py` (nightly run), `score.py` (scorecard), `trend.py` (cross-night trend; reads files only), `packet.py` (private rows packet for one recipient, written to `packets/`, which git ignores; reads files only; `--attestation` adds the monthly cover, summary and the proposal page in `probe/templates/proposal.md`), `emit.py` (public JSON per model, index and drift list into `data/public/v1/`; reads files only), `badge.py` (badge SVG on request, into `packets/badges/`).
- `data/prompts/fixed.jsonl` the fixed probe set, written once, never changed during an experiment.
- `data/runs/<date>/` one folder per night: `endpoints.json`, `prompts.jsonl`, `responses.jsonl`, `run.json`, and `selfcheck.jsonl` on a self-check night.
- `data/scorecard/<date>.md` and `latest.md`.
- `data/public/v1/` the machine-readable files the site and MCP server read: `or/<author>/<slug>.json`, `index.json`, `drift.json` (schema `bitdepth.or.v1`).
- `data/trend/<date>.md`, `<date>.json` and the `latest` copies: the cross-night view, rewritten every night from every run folder.
- `actor/` and `.actor/` the Apify actor (Bitdepth Endpoint Probe): one on-demand probe of one endpoint, graded against the latest night's reference with the nightly code; `OPENROUTER_API_KEY` is an actor env secret; per-probe spend cap in `actor/probe_one.py`.
- `tasks/<slug>/` one folder per task brief with `TASK.md`, `QUESTIONS.md`, `REPORT.md`.
- `.github/workflows/nightly.yml` the schedule.
