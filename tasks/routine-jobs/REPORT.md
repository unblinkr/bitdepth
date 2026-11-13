# Routine jobs: cost and pass rate on a frontier model against the route list

**Date:** 2026-11-13. One-off measurement, asked for by Mancy the same day.

## What changed

- `probe/routine.py` (new): five synthetic routine agent jobs, a fixed system prompt of 55,818 characters (about 13,950 tokens), targets from the route list, a hard cap with reservations, and a report.
- `probe/openrouter.py`: `complete(slug, tag, ...)` accepts `tag=None` and then sends no provider block. Pinned calls build the same body as before.
- `.github/workflows/routine-jobs.yml` (new): manual dispatch, `confirm` must be `RUN`, estimate step before the paid step, stops if the nightly is running or queued, commits `data/routine/<date>/`.
- `tests/test_routine.py` (new): 17 tests. Suite: 112 passed.
- `CLAUDE.md`: layout line for the module and the workflow.

## Targets on the 2026-11-13 route list (dry run, nothing sent)

| Kind | Model | Endpoint | In per M | Out per M |
| --- | --- | --- | --- | --- |
| baseline | anthropic/claude-sonnet-5.5 | default routing | $2.000 | $10.000 |
| lane | openai/gpt-oss-120b | near-ai/fp4 | $0.030 | $0.150 |
| lane | openai/gpt-oss-120b | coreweave/fp4 | $0.030 | $0.170 |
| outside | openai/gpt-oss-120b | venice/int4 | $0.030 | $0.150 |
| lane | deepseek/deepseek-v4-pro | streamlake/fp8 | $0.657 | $1.314 |
| lane | deepseek/deepseek-v4-pro | baidu/fp8 | $0.656 | $1.311 |
| outside | deepseek/deepseek-v4-pro | gmicloud/fp8 | $0.957 | $1.914 |

25 jobs (5 instances of 5) by 7 targets is 175 calls. Estimate $1.62, worst case $2.09, cap $3.00. The night's run billed $2.44, so the night stays under $7.75.

## How to run

Actions, "routine jobs", Run workflow, type `RUN` in confirm. Leave the date blank to attach the run to the latest night with a run record. Results land in `data/routine/<date>/report.md` and in the job summary.

Locally: `python -m probe.routine --date YYYY-MM-DD --dry-run` prints the targets and the estimate and sends nothing.

## Not done

- DeepSeek V4.1 Flash is not in the lane yet (see `QUESTIONS.md`, item 1).
- No cheap closed baseline (item 3).
- The jobs are single calls with no tools. A real agent run chains several calls; the monthly figure multiplies one measured call by a stated schedule.
