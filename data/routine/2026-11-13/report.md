# Routine jobs: cost and pass rate, 2026-11-13

One-off measurement. Working data, not a finding. Numbers against stated answers; nothing here says why an endpoint answers as it does.

- Baseline: `anthropic/claude-sonnet-5.5` on default routing
- Lane: the cheapest 2 allowed endpoints on the route list as of 2026-11-13, per model
- Outside: the cheapest endpoint the route list excludes as outside, where OpenRouter still lists one
- System prompt: 55818 characters (about 13954 tokens), the same on every call
- Instances per job: 5. Temperature 0, reasoning off where the endpoint allows it.
- Billed: $1.2609 of a $3.00 cap. Rows skipped for budget: 0.

## Monthly cost at the stated schedule, and passes

Passes are instances answered correctly over instances that returned.

| Job | Calls a month | baseline | lane:deepseek-v4-pro | lane:gpt-oss-120b | outside:deepseek-v4-pro | outside:gpt-oss-120b |
| --- | --- | --- | --- | --- | --- | --- |
| heartbeat | 1,440 | $57.49 (4/5) | $4.29 (8/10) | $0.55 (1/10) | $9.60 (4/5) | $0.64 (0/5) |
| monitor | 2,880 | $118.27 (1/5) | $6.41 (6/10) | $1.19 (0/10) | $6.24 (3/5) | $1.31 (0/5) |
| digest | 150 | $6.06 (5/5) | $0.35 (10/10) | $0.06 (0/10) | $0.67 (4/5) | $0.07 (1/5) |
| briefing | 300 | $12.10 (5/5) | $0.67 (8/10) | $0.11 (0/10) | $0.55 (2/5) | $0.14 (0/5) |
| tagging | 1,500 | $63.14 (5/5) | $3.72 (10/10) | $0.62 (7/10) | $3.77 (5/5) | $0.74 (4/5) |
| **Total** | | $257.06 | $15.44 | $2.53 | $20.83 | $2.90 |

## Saving against the baseline

- lane:deepseek-v4-pro: $15.44 a month against $257.06, 94.0% lower. Passes: 42/50.
- lane:gpt-oss-120b: $2.53 a month against $257.06, 99.0% lower. Passes: 8/50.

## Per endpoint

| Kind | Model | Endpoint | Returned | Passed | Mean cost per call |
| --- | --- | --- | --- | --- | --- |
| baseline | claude-sonnet-5.5 | default routing | 25/25 | 20 | $0.04076 |
| lane | deepseek-v4-pro | baidu/fp8 | 25/25 | 21 | $0.00181 |
| lane | deepseek-v4-pro | streamlake/fp8 | 25/25 | 21 | $0.00310 |
| lane | gpt-oss-120b | coreweave/fp4 | 25/25 | 3 | $0.00046 |
| lane | gpt-oss-120b | near-ai/fp4 | 25/25 | 5 | $0.00031 |
| outside | deepseek-v4-pro | gmicloud/fp8 | 25/25 | 18 | $0.00353 |
| outside | gpt-oss-120b | venice/int4 | 25/25 | 5 | $0.00046 |

## Schedule assumptions

Heartbeat every 30 minutes; monitor every 15 minutes; a daily digest of 5 model calls; a daily briefing of 10 model calls; 50 tagging batches of 20 tickets a day. Each measured call stands for one model call in that schedule.

## Limits

- 5 instances per job is a small sample. Treat a pass rate as a first read.
- The jobs are synthetic and short. A real agent's jobs call tools and carry longer histories.
- Prompt caching is whatever each endpoint applied by default; cached tokens are in the rows.

Numbers against a stated reference. Not a claim about intent.
