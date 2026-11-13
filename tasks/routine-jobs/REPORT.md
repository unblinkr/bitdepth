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

## Results

Two passes were dispatched on 2026-11-13, both attached to that night. Together they billed $2.5486 ($1.2609 and $1.2877); with the nightly run ($2.4438) the night stands at $4.99 of $7.75.

**Pass one (`data/routine/2026-11-13/`) is not a usable read.** It sent 64 to 400 output tokens with reasoning off or low. gpt-oss-120b returned empty text at the limit on most rows, and the baseline was cut off mid-working on the monitor job. Those rows measure the output limit, not the job. Kept in the repository as the record of what was sent.

**Pass two (`data/routine/2026-11-13-pass2/`)** used 1,500 to 2,000 output tokens and no reasoning parameter. 174 of 175 calls returned (one 429 on venice/int4); one reply hit the limit.

| Group | Passes | Monthly cost at the stated schedule |
| --- | --- | --- |
| baseline: claude-sonnet-5.5, default routing | 25/25 | $258.53 |
| lane: gpt-oss-120b (near-ai/fp4, coreweave/fp4) | 46/50 | $2.97 |
| lane: deepseek-v4-pro (streamlake/fp8, baidu/fp8) | 48/50 | $14.89 |
| outside: gpt-oss-120b (venice/int4) | 21/24 | $3.30 |
| outside: deepseek-v4-pro (gmicloud/fp8) | 25/25 | $30.43 |

- Misses cluster in one job. On the inbox digest, gpt-oss-120b returned no action emails on 3 of 10 lane runs and 3 of 5 venice/int4 runs. Heartbeat, monitor, briefing and tagging passed on 39 of 40 gpt-oss-120b lane runs.
- The four quiet instances (nothing due, nothing to flag) passed on every endpoint in pass two. In pass one, with reasoning off, DeepSeek V4 Pro flagged services on both quiet monitor instances on all three of its endpoints.
- The endpoints the route list excludes did not score lower here: gmicloud/fp8 passed 25 of 25. Five instances a job cannot separate 21/24 from 46/50.
- Mean latency: baseline 2.4 s, gpt-oss-120b lane 6.2 s, DeepSeek V4 Pro lane 8.1 s, venice/int4 12.5 s.
- The baseline billed about 20,000 input tokens a call for a prompt the chars / 4 estimate puts at 14,400.

## Not done

- DeepSeek V4.1 Flash is not in the lane yet (see `QUESTIONS.md`, item 1).
- No cheap closed baseline (item 3).
- The jobs are single calls with no tools. A real agent run chains several calls; the monthly figure multiplies one measured call by a stated schedule.
