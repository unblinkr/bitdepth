# TASK: Find savings in real OpenClaw agent logs (demo report from public DataClaw data)

**Repository:** `unblinkr/bitdepth`
**Save this file to:** `tasks/agent-log-savings/TASK.md`
**Branch:** `task/agent-log-savings`
**Run with:** this brief alone. Read `CLAUDE.md` first; its Rules section is binding. Branch per change, tests green, merge locally, push `main`. Write `QUESTIONS.md` and `REPORT.md` next to this file.
**Start this task in a fresh Claude Code session.** Do not continue an existing thread; stale context burns tokens and this brief is self-contained.
**Date issued:** 2026-11-19
**PR mode:** merge on green. The nightly workflow commits to `main`; do not merge while a run is in progress.
**Status:** stages 1 and 2 run, stage 3 built and waiting on one workflow dispatch. See `REPORT.md`.

---

## 1. Goal

A rough internal script, not a product. It reads OpenClaw session logs, groups the calls into repeating jobs, ranks them by spend, replays a sample of the top jobs on cheaper endpoints from the route list, and writes one report in the shape of bitdepth.dev/sample-report.

First input: public OpenClaw logs that users published to Hugging Face with DataClaw (tag `dataclaw`). Later input: a customer's own `~/.openclaw/agents/{id}/sessions/*.jsonl`. The same script must take both.

This is the engine for the first three hand-made customer reports. No MCP wrapper, no install flow, no public docs in this task.

## 2. Why

Mancy is doing three customer reports by hand before building the report tool. A working script makes each hand report hours instead of days. A demo report from real public logs also shows whether OpenClaw users run enough repeating, unattended work for Bitdepth to matter. Background: `claude/bitdepth-risks-and-self-serve-2026-11-19.md` in the claude.ai Project (risks 3, 4 and 14).

## 3. What to build

- `probe/agentlogs.py`, with three stages a flag can stop after:
  1. **parse**: read OpenClaw session JSONL (DataClaw export format and raw `.openclaw` format) into one row per model call: session id, timestamp, model, provider, system prompt hash, first user message, output, input and output tokens, cost if present.
  2. **group and rank**: a job is a group of calls that share a system prompt hash and a template shape (first user message with numbers, dates, ids and URLs masked). Rank jobs by token spend. Flag each job **unattended** or **interactive**. Unattended signals: the same opening message across sessions, regular time intervals, cron or heartbeat payloads, no human turn. Write `jobs.json` and a short `summary.md`: share of spend that is unattended, top 10 jobs. **This stage spends nothing.**
  3. **replay**: for the top unattended jobs (max 5 jobs, max 20 samples each), send the original messages to the cheapest 3 endpoints on the route list for one open model, using `probe/openrouter.py`. Grade against the original output with string and number checks only (exact, normalized text, same JSON keys and values, same label, length ratio). Write `report.md`: per job, monthly cost now, cost on each option, pass rate, a pass or fail at a stated bar.
- `tests/test_agentlogs.py` with small hand-written fixture logs (no DataClaw content in fixtures).
- `.github/workflows/agent-logs.yml`: manual dispatch only, typed confirmation, inputs for the Hugging Face dataset names and the stage to stop after. Estimate step before any replay. Refuses while the nightly is running. Report uploaded as an artifact.

## 4. Rules that apply

- **No DataClaw content is committed.** This repo is public and these are other people's sessions. Downloads go to a git-ignored folder (`packets/agentlogs/`) or the workflow runner. Only code, fixtures and aggregate numbers (no prompt or output text) may land in the repo. The report with any text excerpts is an artifact only.
- Graders compare strings and numbers only. No model output is executed. No LLM judge in this task (see section 6).
- Spend: replay cap is the lower of the cap input, $3.00, and the nightly cap less the night's billed cost, same logic as `probe/routine.py`. Stages 1 and 2 cost nothing and need no key.
- `OPENROUTER_API_KEY` from the environment only.
- Concurrency 4. Not while the nightly is running.
- Every replay run writes `run.json` with `source` and the cost actually billed.
- No em dashes anywhere.

## 5. Steps

1. Find 2 to 3 DataClaw datasets on Hugging Face that contain OpenClaw sessions (search the `dataclaw` tag; DataClaw marks the source). Record their names in `REPORT.md`. If huggingface.co cannot be reached from the session, do the download inside the workflow instead.
2. Build parse and group. Run stages 1 and 2 on those datasets. Put the unattended share and the top jobs (counts and token totals only) in `REPORT.md`.
3. **Stop and write `QUESTIONS.md` if unattended jobs are under 10% of spend.** That is a market finding Mancy needs before any replay money is spent.
4. Otherwise run one replay through the workflow, within the cap.

## 6. Questions for Mancy (write answers into QUESTIONS.md if blocked)

- Free-text jobs (summaries, digests) cannot be graded fairly by string checks. An LLM judge would need a change to the `CLAUDE.md` grading rule. Report how much of the top spend is free text so she can decide.

## 7. Done when

- Tests green.
- Stages 1 and 2 have run on at least 2 public OpenClaw datasets, with the unattended share in `REPORT.md`.
- Either one replay report exists as a workflow artifact with billed cost in `REPORT.md`, or `QUESTIONS.md` explains why replay was stopped.
- Nothing from DataClaw datasets is in git.
