# TASK: Build the nightly inference probe harness, run night one, and schedule the next thirteen

**Repository:** `unblinkr/bitdepth` (new, private, empty; the founder creates it before this session)
**Save this file to:** `tasks/probe-harness/TASK.md`
**Branch:** `task/probe-harness`
**Run with:** this brief alone. The repository is empty, so Change A writes `CLAUDE.md` first. After that: branch per change, tests green, merge locally, push `main`. Write `QUESTIONS.md` and `REPORT.md` next to this file.
**Start this task in a fresh Claude Code session.** Do not continue an existing thread; stale context burns tokens and this brief is self-contained.
**Before anything else:** `gh secret list` must show `OPENROUTER_API_KEY`. If it does not, write that one line to `QUESTIONS.md` and stop.
**Executor model:** sonnet
**Date issued:** 2026-10-26
**todoist_task:** none
**closes:** none
**mockup:** none
**PR mode:** `merge on green` : nothing in this repository is public and no figure is published; every output is a file in a private repo. After `git fetch`, confirm local `main` equals `origin/main`, merge locally, push `main`.

---

## 1. Goal

After this task the repository holds a harness that sends a fixed probe set to every OpenRouter endpoint serving two open-weight models at temperature zero, scores each endpoint against a reference, writes one scorecard per night, has done so once, and is scheduled to do so for thirteen more nights without anyone touching it.

## 2. Context (self-contained; this session has no other history)

Paddock (paddock.finance) sells pre-payment verification for AI agents: its `verify_before_pay` tool reads a seller's live HTTP 402 challenge and checks the payee, chain, token and price against a settlement record. On Oct 26, 2026 the founder decided to test the same idea one layer down: whether a buyer of inference can verify that the endpoint they paid for served the model, precision and context it advertised.

The same open-weight model is served by many providers through OpenRouter, and provider-level differences are documented. Artificial Analysis launched an Endpoint Accuracy Index in Aug 2026 and found one model scoring 52% on one provider and 100% on three others. The Token-DiFR method (Nov 2025) showed that temperature-zero outputs compared against a reference reveal quantization and serving bugs. The Token Arena paper (May 2026) separated FP8 endpoints from BF16 ones by output fingerprint alone. None of this is continuous, dated per endpoint, or sold to buyers.

This task is the cheapest possible test of the idea. It is not a product. After fourteen nights it answers three questions: (1) can a harness with no GPU and one API key tell endpoints apart on the same model; (2) what is the noise floor, meaning how much two calls to the same endpoint disagree; (3) does anything change across two weeks. The founder decides what, if anything, gets published after reading the fourteen scorecards. This brief builds the harness, runs night one, and schedules the rest. Analysis of the fourteen nights is a later brief.

If something here cannot be built as written, write it to `QUESTIONS.md` and stop that change; ship the others.

## 3. Decisions already made (do not re-ask)

- Python 3.12, `httpx`, `jsonschema`, `pytest`. No framework, no database, no local model, no GPU.
- OpenRouter is the only gateway. No direct provider accounts.
- Two models: gpt-oss-120b (expected slug `openai/gpt-oss-120b`) and GLM-5.2 (expected slug `z-ai/glm-5.2`). Resolve the exact slugs from `GET https://openrouter.ai/api/v1/models` at run time and record them in `REPORT.md`. If either model has fewer than six endpoints on OpenRouter the night this runs, substitute DeepSeek V4 Pro and say so in `REPORT.md`.
- Every endpoint of each model is probed. Each request is pinned to one provider with OpenRouter provider routing (`provider: {"order": ["<provider>"], "allow_fallbacks": false}`). Confirm the exact field names against the live endpoints response and the OpenRouter provider-routing docs, not from memory. The provider named in the response must match the pinned provider or the row is marked `misrouted` and excluded from scoring.
- Sampling: `temperature: 0`, `top_p: 1`, `seed: 42`, `max_tokens: 512`. Request usage accounting in the response. Endpoints whose `supported_parameters` lack `seed` are still probed; the scorecard marks them `no_seed`.
- Declared quantization comes from `GET https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints` and is logged every night per endpoint, so a change in declaration is captured.
- Reference per model per prompt: the output shared by the plurality of endpoints whose declared quantization is `bf16` or `fp16`. If fewer than two endpoints declare either, the reference is the plurality across all endpoints and the scorecard footer says so. A prompt with no plurality is excluded from the agreement metrics and counted under `no_reference`.
- Probe set: 120 fixed prompts generated by seeded code (seed `20261026`) and committed to `data/prompts/fixed.jsonl`, plus 24 fresh prompts each night from the same generators with seed `int(YYYYMMDD)`. The fixed set never changes during the fourteen nights.
- No prompt or answer is copied from a public benchmark. Generators produce every prompt and every answer programmatically. Identity prompts ("which model are you") are not used; they are not evidence.
- Metrics per endpoint per night: exact match vs reference (%), median word index of first divergence, output length ratio vs reference, math accuracy, JSON validity, needle recall, echo exact match, error rate, misrouted count, median latency, billed cost in USD, declared quantization.
- Self-consistency on night one only: the same 12 fixed prompts go to every endpoint twice, one hour apart. The two-run agreement per endpoint is the noise floor and prints on the scorecard.
- Budget: $5.00 per night, enforced in code. A dry run estimates cost from the endpoints pricing before anything is sent. If the estimate exceeds $5.00 the run drops needle prompts first, then fresh prompts, and records what it dropped. If still over, it aborts and writes the estimate to the run record.
- Concurrency 4. Exponential backoff on 429 and 5xx, three retries, then the row is marked `error`.
- Schedule: GitHub Actions cron `17 7 * * *` UTC (03:17 ET), starting Oct 27, 2026. The workflow commits results to `main` with a bot identity and skips when a run for that date already exists.
- Raw responses are kept. Every row stores prompt id, family, model slug, pinned provider, returned provider, request parameters, full output text, usage as returned, latency in ms, and run id.
- Scorecards are Markdown files in the repo. Nothing is rendered anywhere else.
- Repository stays private. No file in it is a public surface.

## 4. Hard rules (violating any fails the task)

- No em dashes in any file, docstring, commit message, issue title or run record.
- No prompt text or answer copied from a public benchmark or eval set.
- No file characterises a provider's intent or conduct. Scorecards report numbers against a stated reference and nothing else.
- Spend never exceeds $5.00 in a night. The cap is code, not convention.
- `OPENROUTER_API_KEY` is read from the environment only. It never appears in a file, a log, a run record or a commit.
- OpenRouter rate limits and terms are respected. Concurrency never exceeds 4.
- Every run writes `data/runs/<date>/run.json` with a `source` marker (`live` for cron, `dispatch` for manual, `local` for the night-one session run), the prompts dropped for budget, and the cost actually billed.
- No model-written code is executed. Graders compare strings and numbers only.

## 5. Banned terms

Grep every tracked file except `tasks/probe-harness/TASK.md` (this brief lists the terms); each count must be 0. The first four are whole-word and case-insensitive (`git grep -niw`), the fifth is a substring (`git grep -n`):
- `cheat`
- `fraud`
- `lying`
- `scam`
- `sk-or-`
- the em dash character, U+2014 (grep with `LC_ALL=C.UTF-8 grep -rP "\x{2014}"`)

## 6. Build scope

### Change A: repository bootstrap

Create `CLAUDE.md` containing the eight rules of section 4 verbatim under a heading `Rules`, plus three lines: branch per change; tests green before merge; merge locally and push `main`. Create `README.md` (four sentences: what the repo probes, what a scorecard is, that `OPENROUTER_API_KEY` is the one secret, that nothing here is published). Create `.gitignore` (venv, `__pycache__`, `.env`), `requirements.txt` (`httpx`, `jsonschema`, `pytest`), `pyproject.toml` with the package `probe`, and empty folders `data/prompts/`, `data/runs/`, `data/scorecard/`, `tasks/`.

### Change B: `probe/openrouter.py`

A thin client. `list_models()`, `list_endpoints(slug)` returning provider name, declared quantization, pricing per million input and output tokens, context length, max completion tokens, supported parameters. `complete(slug, provider, messages, params)` returning output text, returned provider, usage, latency, and the raw JSON. Backoff and retry per section 3. The key is read from `OPENROUTER_API_KEY` at call time and never stored on an object that gets serialised.

### Change C: `probe/generators.py` and the fixed set

Five families. Every generator takes a seed and returns `{"id", "family", "prompt", "answer", "schema"}` where `schema` is present only for `json`.

| Family | Count fixed | Prompt | Grade |
|---|---|---|---|
| `math` | 40 | A three-step integer word problem from templates with random integers in 2 to 999; asks for the final integer only | last integer in the output equals `answer` |
| `json` | 20 | A generated record (a name, three dates, two amounts, a list of four items) described in prose; asks for a JSON object matching a stated schema | `jsonschema` validates and every field equals the generated record |
| `string` | 20 | One of: reverse this word, count letter X in this word, apply a Caesar shift of k, sort the letters of this word | output stripped equals `answer` |
| `needle` | 20 | About 2,500 words of generated filler sentences with one planted eight-character alphanumeric code; asks for the code | output contains the code |
| `echo` | 20 | "Repeat exactly the text between the markers" with generated text containing diacritics, CJK characters, emoji and mixed punctuation | output stripped equals the text exactly |

Fresh nightly set: 24 prompts (8 `math`, 4 `json`, 4 `string`, 4 `needle`, 4 `echo`) with the date seed. `python -m probe.generators --write-fixed` writes `data/prompts/fixed.jsonl` once with seed `20261026`; running it again with the file present is a no-op that prints the existing count.

### Change D: `probe/run.py`

`python -m probe.run --date YYYY-MM-DD [--dry-run] [--source live|dispatch|local]`.

1. Resolve the two slugs; apply the substitution rule from section 3 if needed.
2. List endpoints per model; log declared quantization and pricing to `data/runs/<date>/endpoints.json`.
3. Load the fixed set and generate the fresh set.
4. Estimate cost: for each endpoint, sum input tokens (estimate as characters divided by 4) times input price plus 512 times output price, over all prompts. Apply the drop order from section 3. `--dry-run` prints the table and the estimate and exits.
5. Send every prompt to every endpoint, concurrency 4, pinned. Write rows to `data/runs/<date>/responses.jsonl` as they return.
6. On night one only (`--selfcheck` flag, used once): after the main run, send fixed prompts 1 to 12 to every endpoint, wait sixty minutes, send them again, write both to `data/runs/<date>/selfcheck.jsonl`.
7. Write `data/runs/<date>/run.json` with source, slugs, endpoint count, prompt counts, prompts dropped, rows, errors, misrouted, billed cost summed from usage.
8. If `data/runs/<date>/run.json` already exists, exit 0 with the line `run exists for <date>, skipping`.

### Change E: `probe/score.py`

`python -m probe.score --date YYYY-MM-DD` reads the run, computes the reference per prompt per model by the section 3 rule, computes every metric in section 3 per endpoint, and writes `data/scorecard/<date>.md` and copies it to `data/scorecard/latest.md`. One table per model, one row per endpoint, sorted by exact match descending. Footer: the reference rule applied per model, the `no_reference` count, the noise floor table when `selfcheck.jsonl` exists, prompts dropped for budget, billed cost. Word index of first divergence is computed on whitespace-split words; say so in the footer.

### Change F: tests (`tests/`)

- Generators are deterministic for a seed and differ across seeds.
- Each grader passes on its own generated answer and fails on a mutated one (one pass, one fail per family).
- Cost estimator against a fixed endpoints fixture matches a hand-computed value.
- Cap: an estimate over $5.00 drops needle prompts first, then fresh prompts, then aborts; the abort writes the estimate and sends nothing (mock the client).
- Misroute: a response whose provider differs from the pinned provider is marked `misrouted` and excluded from metrics.
- Reference: plurality among `bf16` endpoints wins; a tie yields `no_reference`; fewer than two `bf16` endpoints falls back to all endpoints.
- Skip: a second run for a date that has `run.json` exits 0 without sending.

### Change G: `.github/workflows/nightly.yml`

Cron `17 7 * * *` plus `workflow_dispatch`. Steps: checkout, Python 3.12, install, `python -m probe.run --date <today UTC> --source live` (`dispatch` when triggered by hand), `python -m probe.score --date <today UTC>`, commit `data/runs/<date>/` and `data/scorecard/` to `main` with a bot identity, push. The key is passed as `OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}` and nowhere else.

### Change H: night one

From the merged checkout: `python -m probe.run --date 2026-10-26 --source local --selfcheck`, then `python -m probe.score --date 2026-10-26`. Commit the results to `main` and push.

## 7. Out of scope (do not do)

- Any public page, post, chart, tweet or README claim about a provider. The founder writes any public copy from the scorecards in a later brief.
- Closed models (OpenAI, Anthropic, Google) and direct provider APIs.
- The Paddock site (`unblinkr/openclaw-news`), the Ledger (`unblinkr/paddock-ledger`), MCP, x402, MPP, pricing.
- Statistical tests beyond the metrics in section 3. No p-values, no significance claims.
- Executing model-written code.
- A dashboard or site of any kind.

## 8. Verification checks (run them; paste results into REPORT.md)

1. `python -m probe.run --date 2026-10-26 --dry-run` prints the resolved slugs, the endpoint count per model with declared quantization, the prompt count, and the estimated cost. Estimate is at or under $5.00. Paste the whole output.
2. Night one completes. Paste the row count of `responses.jsonl` (expected: endpoints times 144, less dropped prompts), errors per endpoint, misrouted per endpoint.
3. Paste `data/scorecard/2026-10-26.md` whole.
4. Paste, per model, the endpoints declaring `bf16` or `fp16` and which reference rule applied.
5. Paste the noise floor table from `selfcheck.jsonl`. If any endpoint's two-run agreement is below 90%, say so. Do not change code to raise it.
6. Paste the billed cost from `run.json`. It is at or under $5.00.
7. `gh workflow run nightly.yml` succeeds. Paste the run URL and either the commit it made or the `run exists` skip line.
8. `pytest` green. Paste the summary line.
9. Banned terms grep across tracked files, excluding `tasks/probe-harness/TASK.md`, is 0 for every term in section 5. Paste the commands and output.
10. `git grep -n "OPENROUTER_API_KEY"` shows only `nightly.yml`, `README.md`, and the two client lines that read the environment. Paste.
11. `git grep -n "sk-or-"` is empty. Paste.

## 9. Handback

Write `tasks/probe-harness/REPORT.md` with: the resolved slugs, the endpoint lists with declared quantization, the night-one scorecard, the noise floor table, the billed cost, the list of files changed, anything written to `QUESTIONS.md`, and one paragraph in plain words on what the scorecard shows and what it does not show. No conclusion about any provider.

Report the merge commit and the nightly workflow URL.

End the session with this block, exactly this shape, so the founder can paste it to chat and the board gets updated:

```
BOARD SYNC
todoist_task: none
closes: none
new issues opened: <#n title> | none
needs_mancy: <one line> | none
live: main <merge commit>; nightly workflow <URL>; next run 2026-10-27 07:17 UTC
```
