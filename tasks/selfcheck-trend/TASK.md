# TASK: Measure the noise floor twice more and write the cross-night trend the Nov 10 read grades from

**Repository:** `unblinkr/bitdepth`
**Save this file to:** `tasks/selfcheck-trend/TASK.md`
**Branch:** `task/selfcheck-trend`
**Run with:** this brief alone. Read `CLAUDE.md` first; its Rules section is binding. Branch per change, tests green, merge locally, push `main`. Write `QUESTIONS.md` and `REPORT.md` next to this file.
**Start this task in a fresh Claude Code session.** Do not continue an existing thread; stale context burns tokens and this brief is self-contained.
**Before anything else:** confirm `data/runs/` holds at least five dated folders and `data/runs/2026-10-27/selfcheck.jsonl` exists. If not, write that one line to `QUESTIONS.md` and stop.
**Executor model:** fable (run from the chat session on 2026-10-31)
**Date issued:** 2026-10-31
**todoist_task:** Bitdepth board, Nov 10 read
**closes:** none
**mockup:** none
**PR mode:** `merge on green`. After `git fetch`, confirm local `main` equals `origin/main`, merge locally, push `main`. The nightly workflow commits to `main` at 07:17 and 11:17 UTC; do not merge while a run is in progress (check the Actions tab).

---

## 1. Goal

After this task the nightly pipeline measures the one-hour noise floor on two more nights (night seven and night fourteen) on three times the prompts, and writes, every night, one cross-night trend file per model that the Nov 10 read can grade from: per endpoint, the exact-match history and its movement, graded accuracy per family, night-to-night agreement with itself on the fixed prompts, and the one-hour self-check agreement where measured. Nothing else about what is sent changes.

## 2. Context

Five nights are in (Oct 27 to 31). The read on 2026-10-31 (project file `claude/interim-read-five-nights-2026-10-31.md`) found two things the night-one design does not settle:

1. The noise floor was measured once, on night one, on 12 prompts (granularity 8.3 points). On gpt-oss-120b the gap between the top and bottom of the table is five to six points, so a one-shot 12-prompt floor cannot say whether that gap is outside the noise. One more measurement, on more prompts, settles whether the floor is stable.
2. On deepseek-v4-pro the one-hour self-agreement was 50% to 83% for most endpoints, so exact match against the plurality cannot grade that model alone. The String family is graded against the generated answer, not the plurality, and it splits the endpoints into the same two tiers every night. The Nov 10 read needs the family accuracies and the self-agreement beside exact match, per endpoint, across every night, in one file. Today that takes a script written by hand.

The grade itself (letters, thresholds) stays in the grade-archive brief and the Nov 10 read. This task produces the inputs.

## 3. Decisions already made (do not re-ask)

- **Second and third self-check nights:** the nights whose UTC date is `2026-11-02` (night seven) or `2026-11-09` (night fourteen). Same mechanism as night one (`--selfcheck`: pass A, one-hour wait, pass B, same prompts), on the first 36 fixed prompts instead of 12. The first 12 of those 36 are the night-one prompts, so the night-one floor is a subset. Expected cost about $0.90 a night on top of the usual $2; the $5 runtime cap applies to the whole night as before.
- **The dates live in the workflow file** as an environment variable `SELFCHECK_DATES` (space separated). The Resolve step turns the self-check on when the resolved date is in that list, or when the dispatch input `selfcheck` is `true`. Changing the dates is a one-line edit.
- **`probe/run.py` gains one argument,** `--selfcheck-prompts N` (default 12, the night-one value), and records `prompts` and the prompt ids in `run.json` under `selfcheck`. Nothing else in the capture changes: prompts, parameters, concurrency, cap, models, reference rule are untouched.
- **New module `probe/trend.py`:** `python -m probe.trend --date YYYY-MM-DD` reads every `data/runs/<date>/` with a `run.json` and a `responses.jsonl` up to and including that date and writes `data/trend/<date>.md`, `data/trend/<date>.json`, and copies to `latest.md` and `latest.json`. Scorecards (`probe/score.py`) are untouched so the nightly record stays comparable.
- **Per model, per endpoint, the trend file prints:** nights present; exact % on every night; mean, standard deviation, min and max of exact %; movement, defined as the mean of the last three nights minus the mean of the first three nights (nights overlap when fewer than six are present, and the file says so); mean graded accuracy per family (math, json, string, needle, echo) over the nights; night-to-night self-agreement on the fixed prompts, overall and per family; and one-hour self-check agreement for every self-check night, listed by date.
- **Night-to-night self-agreement:** for one endpoint, the share of (fixed prompt, consecutive-night pair) where both nights are `ok` rows and the stripped outputs are equal word for word. Fresh prompts are excluded because they change nightly. Consecutive means consecutive among the nights the endpoint was present.
- **Per model, per family, the trend file prints the noise floor** as the grade-archive brief defines it: 100 minus the 75th percentile across endpoints of night-to-night disagreement in that family, and the median endpoint self-agreement. A family is marked stable when the median is at or above `STABLE_MIN` (provisional 95). These feed the Nov 10 calibration and are not grades.
- **Movement flag:** a row is marked in the movement column when the absolute movement is at or above `MOVE_MIN` (provisional 10 points) and the endpoint has at least four nights. The flag describes a number, nothing else.
- **Thresholds** live in one dict `THRESHOLDS` at the top of `probe/trend.py`, each with the comment `provisional; calibrate on 2026-11-10`.
- **Sorting:** within a model, rows sort by mean exact % descending, then tag. A second compact table per model sorts the same endpoints by String accuracy descending, then night-to-night self-agreement, so the family view is readable without re-sorting by hand.
- **Workflow:** after the Score step, add `python -m probe.trend --date <date>` with `continue-on-error: true`, and add `data/trend` to the commit. The key is still passed only to the Probe step.
- **Backfill:** run `probe.trend` once for `2026-10-31` in this task so the five-night trend is on `main` tonight.

## 4. Hard rules (violating any fails the task)

- Every rule in `CLAUDE.md`, Rules section. Grep the banned terms (`cheat`, `fraud`, `lying`, `scam` whole word, `sk-or-` substring, U+2014) across tracked files except `tasks/*/TASK.md` before merging; each count is 0.
- No change to `data/prompts/fixed.jsonl`, `probe/generators.py`, `probe/budget.py`, `probe/openrouter.py`, `probe/score.py`, the request parameters, the models, the concurrency or the cap.
- `probe/trend.py` never reads `OPENROUTER_API_KEY` and never makes a network request.
- The trend file footer carries, every time: the nights found, the self-check nights found, the definitions of self-agreement and movement, and the fixed line "Numbers against a stated reference. Not a claim about intent."

## 5. Build scope

### Change A: `probe/run.py`
`--selfcheck-prompts` (default 12); `run.json` `selfcheck` block records `prompts` and `prompt_ids`. `tests/test_run.py` gains one test that the self-check sends exactly N prompts per endpoint per pass and records them.

### Change B: `.github/workflows/nightly.yml`
`SELFCHECK_DATES` env; Resolve step sets `--selfcheck --selfcheck-prompts 36` when the date is listed or the input says so; trend step; `data/trend` in the commit.

### Change C: `probe/trend.py` and `tests/test_trend.py`
Everything in section 3 under trend. Tests, from a fixture of three synthetic nights in a temp directory: exact history and mean; movement with overlapping windows; night-to-night self-agreement overall and per family (one endpoint that flips one fixed prompt on one night); fresh prompts excluded; noise floor and stable-family marking at `STABLE_MIN`; self-check agreement joined from a `selfcheck.jsonl`; the footer lines present; the movement flag at `MOVE_MIN`.

### Change D: `CLAUDE.md` layout lines
Add `trend.py` to the package list and `data/trend/` to the data list. Rules section unchanged.

### Change E: backfill
`python -m probe.trend --date 2026-10-31` on the merged checkout; commit `data/trend/` and push.

## 6. Out of scope (do not do)

- Letter grades, thresholds beyond the two provisional constants here, or any calibration; that is the grade-archive brief and the Nov 10 read.
- Any public page, feed, chart or copy.
- Statistical tests. No p-values, no significance claims.
- Adding models, prompts or endpoints.

## 7. Verification checks (run them; paste results into REPORT.md)

1. `pytest` summary line, green.
2. The Resolve step logic, exercised in a shell with the three cases (listed date, unlisted date, dispatch input true), output pasted.
3. `python -m probe.trend --date 2026-10-31` output and the first table of `data/trend/2026-10-31.md` pasted; the night-one self-check column shows the night-one values for the endpoints that had them.
4. Banned-terms grep, all zero, commands and output pasted.
5. `git diff --stat main..task/selfcheck-trend -- probe/generators.py probe/budget.py probe/openrouter.py probe/score.py data/prompts/fixed.jsonl` is empty; pasted.
6. The workflow diff pasted.
7. Estimated cost of a self-check night stated from the night-one `selfcheck.jsonl` cost scaled by 3; under $5 with the nightly run.

## 8. Handback

`tasks/selfcheck-trend/REPORT.md` with: files changed, the five-night trend tables, the self-check schedule as it now stands, anything in `QUESTIONS.md`, and one paragraph in plain words on what the trend file shows and does not show. No conclusion about any provider.

End the session with this block, exactly this shape:

```
BOARD SYNC
todoist_task: Bitdepth, Nov 10 read
closes: none
new issues opened: <#n title> | none
needs_mancy: <one line> | none
live: main <merge commit>; trend data/trend/latest.md; self-check nights 2026-11-02 and 2026-11-09 at 36 prompts
```
