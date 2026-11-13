# Routine jobs: cost and pass rate, 2026-11-13

One-off measurement. Working data, not a finding. Numbers against stated answers; nothing here says why an endpoint answers as it does.

- Baseline: `anthropic/claude-sonnet-5.5` on default routing
- Lane: the cheapest 2 allowed endpoints on the route list as of 2026-11-13, per model
- Outside: the cheapest endpoint the route list excludes as outside, where OpenRouter still lists one
- System prompt: 55818 characters (about 13954 tokens), the same on every call
- Instances per job: 5. Temperature 0. No reasoning parameter is sent, so each endpoint runs at its default.
- Output limit: 1500 to 2000 tokens. Replies cut off at the limit: 1.
- Billed: $1.2877 of a $3.50 cap. Rows skipped for budget: 0.

## Monthly cost at the stated schedule, and passes

Passes are instances answered correctly over instances that returned.

| Job | Calls a month | baseline | lane:deepseek-v4-pro | lane:gpt-oss-120b | outside:deepseek-v4-pro | outside:gpt-oss-120b |
| --- | --- | --- | --- | --- | --- | --- |
| heartbeat | 1,440 | $57.57 (5/5) | $2.65 (10/10) | $0.58 (9/10) | $7.25 (5/5) | $0.67 (5/5) |
| monitor | 2,880 | $119.52 (5/5) | $7.89 (9/10) | $1.52 (10/10) | $16.57 (5/5) | $1.60 (4/4) |
| digest | 150 | $6.06 (5/5) | $0.30 (9/10) | $0.06 (7/10) | $1.18 (5/5) | $0.07 (2/5) |
| briefing | 300 | $12.24 (5/5) | $0.53 (10/10) | $0.12 (10/10) | $0.83 (5/5) | $0.15 (5/5) |
| tagging | 1,500 | $63.14 (5/5) | $3.52 (10/10) | $0.69 (10/10) | $4.60 (5/5) | $0.81 (5/5) |
| **Total** | | $258.53 | $14.89 | $2.97 | $30.43 | $3.30 |

## Saving against the baseline

- lane:deepseek-v4-pro: $14.89 a month against $258.53, 94.2% lower. Passes: 48/50.
- lane:gpt-oss-120b: $2.97 a month against $258.53, 98.9% lower. Passes: 46/50.

## Per endpoint

| Kind | Model | Endpoint | Returned | Passed | Mean cost per call |
| --- | --- | --- | --- | --- | --- |
| baseline | claude-sonnet-5.5 | default routing | 25/25 | 25 | $0.04095 |
| lane | deepseek-v4-pro | baidu/fp8 | 25/25 | 23 | $0.00217 |
| lane | deepseek-v4-pro | streamlake/fp8 | 25/25 | 25 | $0.00211 |
| lane | gpt-oss-120b | coreweave/fp4 | 25/25 | 22 | $0.00052 |
| lane | gpt-oss-120b | near-ai/fp4 | 25/25 | 24 | $0.00037 |
| outside | deepseek-v4-pro | gmicloud/fp8 | 25/25 | 25 | $0.00490 |
| outside | gpt-oss-120b | venice/int4 | 24/25 | 21 | $0.00051 |

## Schedule assumptions

Heartbeat every 30 minutes; monitor every 15 minutes; a daily digest of 5 model calls; a daily briefing of 10 model calls; 50 tagging batches of 20 tickets a day. Each measured call stands for one model call in that schedule.

## Limits

- 5 instances per job is a small sample. Treat a pass rate as a first read.
- The jobs are synthetic and short. A real agent's jobs call tools and carry longer histories.
- Prompt caching is whatever each endpoint applied by default; cached tokens are in the rows.

Numbers against a stated reference. Not a claim about intent.
