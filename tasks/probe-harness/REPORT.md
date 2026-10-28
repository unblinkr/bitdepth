# REPORT for probe-harness

Date: 2026-10-28 (night one ran 2026-10-27, 21:11 to 23:10 UTC, in GitHub Actions)
Merge commit: `6b5f0a6` (harness) on `main`; follow-ups `6895339` (public repository note), `88d3cce` (retry backoff).
Nightly workflow: https://github.com/unblinkr/bitdepth/actions/workflows/nightly.yml (cron `17 7 * * *` UTC, active).
Night-one run: https://github.com/unblinkr/bitdepth/actions/runs/40584577962 (success; committed `2102888`).

## Resolved slugs and endpoints

- `gpt-oss-120b` = `openai/gpt-oss-120b`, 25 endpoints. Declared bf16 or fp16: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Reference rule applied: plurality among those five.
- `deepseek-v4-pro` = `deepseek/deepseek-v4-pro`, 15 endpoints. Declared bf16 or fp16: none. Reference rule applied: plurality across all endpoints.
- GLM-5.2 was not probed; see `QUESTIONS.md` item 1 (cost). DeepSeek V4 Pro took its place.

Declared quantization per endpoint is in `data/runs/2026-10-27/endpoints.json` and on the scorecard.

## Check 1: dry run

```
resolved models:
  gpt-oss-120b: openai/gpt-oss-120b with 25 endpoints; declared quantization {'fp4': 8, 'int4': 1, 'bf16': 4, 'fp8': 2, 'unknown': 9, 'fp16': 1}
  deepseek-v4-pro: deepseek/deepseek-v4-pro with 15 endpoints; declared quantization {'fp8': 9, 'fp4': 2, 'unknown': 4}
prompts: 120 fixed + 24 fresh = 144; kept 144, dropped 0
estimate: $3.3831 (cap $5.00) per model {'gpt-oss-120b': 0.4975, 'deepseek-v4-pro': 2.8857}; 99990 input and 21504 output tokens per endpoint
(per-endpoint table: deepseek-v4-pro endpoints $0.12 to $0.27 each, gpt-oss-120b endpoints $0.006 to $0.051 each)
```

Estimate $3.38, under the $5.00 cap, nothing dropped.

## Check 2: night one rows, errors, misrouted

`responses.jsonl` has 5760 rows = 40 endpoints x 144 prompts. Errors 97, misrouted 0, truncated 25, skipped by runtime budget stop 0. The response's `provider` field was present on every ok row, so misroute detection was active; no row disagreed with its pin.

| Model | Endpoint | Rows | Errors | Misrouted |
|---|---|---|---|---|
| deepseek-v4-pro | alibaba/fp8 | 144 | 0 | 0 |
| deepseek-v4-pro | alibaba/fp8/us-east-1 | 144 | 4 | 0 |
| deepseek-v4-pro | atlas-cloud/fp4 | 144 | 4 | 0 |
| deepseek-v4-pro | azure/us | 144 | 33 | 0 |
| deepseek-v4-pro | baidu/fp8 | 144 | 0 | 0 |
| deepseek-v4-pro | cloudflare | 144 | 0 | 0 |
| deepseek-v4-pro | crusoe/fp8 | 144 | 9 | 0 |
| deepseek-v4-pro | deepinfra/fp8 | 144 | 0 | 0 |
| deepseek-v4-pro | digitalocean | 144 | 0 | 0 |
| deepseek-v4-pro | gmicloud/fp8 | 144 | 0 | 0 |
| deepseek-v4-pro | novita/fp8 | 144 | 3 | 0 |
| deepseek-v4-pro | relace/fp4 | 144 | 0 | 0 |
| deepseek-v4-pro | siliconflow/fp8 | 144 | 4 | 0 |
| deepseek-v4-pro | streamlake/fp8 | 144 | 0 | 0 |
| deepseek-v4-pro | venice | 144 | 4 | 0 |
| gpt-oss-120b | akashml/bf16 | 144 | 0 | 0 |
| gpt-oss-120b | amazon-bedrock | 144 | 0 | 0 |
| gpt-oss-120b | amazon-bedrock/eu-west-1 | 144 | 0 | 0 |
| gpt-oss-120b | baseten/fp4 | 144 | 0 | 0 |
| gpt-oss-120b | baseten/fp4/us | 144 | 0 | 0 |
| gpt-oss-120b | cerebras/fp16 | 144 | 0 | 0 |
| gpt-oss-120b | coreweave/fp4 | 144 | 0 | 0 |
| gpt-oss-120b | crusoe/bf16 | 144 | 0 | 0 |
| gpt-oss-120b | deepinfra/bf16 | 144 | 0 | 0 |
| gpt-oss-120b | dekallm/bf16 | 144 | 0 | 0 |
| gpt-oss-120b | digitalocean | 144 | 0 | 0 |
| gpt-oss-120b | google-vertex/global | 144 | 1 | 0 |
| gpt-oss-120b | groq | 144 | 0 | 0 |
| gpt-oss-120b | mancer/fp8 | 144 | 0 | 0 |
| gpt-oss-120b | mara | 144 | 0 | 0 |
| gpt-oss-120b | near-ai/fp4 | 144 | 0 | 0 |
| gpt-oss-120b | nebius/fp4 | 144 | 0 | 0 |
| gpt-oss-120b | novita/fp4 | 144 | 0 | 0 |
| gpt-oss-120b | parasail/fp4 | 144 | 2 | 0 |
| gpt-oss-120b | phala | 144 | 2 | 0 |
| gpt-oss-120b | sail-research/fp4 | 144 | 31 | 0 |
| gpt-oss-120b | sambanova | 144 | 0 | 0 |
| gpt-oss-120b | siliconflow/fp8 | 144 | 0 | 0 |
| gpt-oss-120b | together | 144 | 0 | 0 |
| gpt-oss-120b | venice/int4 | 144 | 0 | 0 |

Error messages:
- 59 rows: `http 429: {"error":{"message":"Rate limit exceeded: new-account-rpm/deepseek/deepseek-v4-pro-20`
- 35 rows: `http 429: {"error":{"message":"Provider returned error","code":429,"metadata":{"raw":"openai/gp`
- 2 rows: `http 429: {"error":{"message":"Provider returned error","code":429,"metadata":{"raw":"deepseek/`
- 1 rows: `api: A Timeout Occurred`

Almost every error is a 429 rate limit (OpenRouter's new-account requests-per-minute limit on DeepSeek V4 Pro, and provider-side 429s on gpt-oss, mostly sail-research). Retries were raised from three to five with longer backoff in `88d3cce`.

## Check 3: scorecard

The whole of `data/scorecard/2026-10-27.md` follows.

---

# Bitdepth scorecard 2026-10-27

Run `2026-10-27-dispatch`, source `dispatch`, started 2026-10-27T21:11:02Z, finished 2026-10-27T23:10:26Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4/us | fp4 | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 675.0 | 0.0127 |
| together | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 851.0 | 0.0183 |
| baseten/fp4 | fp4 | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 2 | 690.5 | 0.0130 |
| crusoe/bf16 | bf16 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 471.5 | 0.0065 |
| deepinfra/bf16 | bf16 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2040.5 | 0.0047 |
| groq | unknown | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 308.0 | 0.0183 |
| near-ai/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1168.5 | 0.0038 |
| cerebras/fp16 | fp16 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 248.5 | 0.0380 |
| dekallm/bf16 | bf16 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1600.5 | 0.0042 |
| amazon-bedrock | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 348.0 | 0.0181 |
| mara | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 806.0 | 0.0192 |
| sambanova | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 603.0 | 0.0201 |
| sail-research/fp4 | fp4 | yes | 95.6 | 113 | 0 | 1.00 | 100.0 | 100.0 | 72.2 | 100.0 | 100.0 | 21.5 | 0 | 1 | 827.0 | 0.0066 |
| akashml/bf16 | bf16 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 910.0 | 0.0042 |
| mancer/fp8 | fp8 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1437.0 | 0.0064 |
| parasail/fp4 | fp4 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 1.40 | 0 | 2 | 588.5 | 0.0155 |
| digitalocean | unknown | no | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1500.5 | 0.0087 |
| google-vertex/global | unknown | yes | 94.4 | 143 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 797.0 | 0.0107 |
| coreweave/fp4 | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 684.5 | 0.0041 |
| nebius/fp4 | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 518.5 | 0.0177 |
| novita/fp4 | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 977.5 | 0.0089 |
| siliconflow/fp8 | fp8 | no | 93.1 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1983.0 | 0.0268 |
| amazon-bedrock/eu-west-1 | unknown | no | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 762.0 | 0.0180 |
| venice/int4 | int4 | no | 91.0 | 144 | 0 | 1.00 | 95.8 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1782.5 | 0.0038 |
| phala | unknown | yes | 90.8 | 142 | 0 | 1.00 | 95.7 | 100.0 | 75.0 | 100.0 | 100.0 | 1.40 | 0 | 4 | 1357.0 | 0.0243 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| streamlake/fp8 | fp8 | no | 86.2 | 130 | 6.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2239.5 | 0.0328 |
| alibaba/fp8 | fp8 | yes | 82.3 | 130 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2530.5 | 0.1283 |
| alibaba/fp8/us-east-1 | fp8 | yes | 80.3 | 127 | 4 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.7 | 2.80 | 0 | 0 | 2176.0 | 0.1363 |
| venice | unknown | no | 80.2 | 126 | 8 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 2.80 | 0 | 0 | 1657.0 | 0.0698 |
| atlas-cloud/fp4 | fp4 | yes | 78.7 | 127 | 4 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 2.80 | 0 | 0 | 2514.5 | 0.1490 |
| relace/fp4 | fp4 | no | 78.5 | 130 | 4.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 956.0 | 0.0798 |
| baidu/fp8 | fp8 | no | 75.4 | 130 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1392.5 | 0.0797 |
| siliconflow/fp8 | fp8 | no | 73.0 | 126 | 2.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.7 | 2.80 | 0 | 0 | 2199.0 | 0.1158 |
| deepinfra/fp8 | fp8 | yes | 71.5 | 130 | 1 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1450.0 | 0.1184 |
| digitalocean | unknown | no | 58.5 | 130 | 1.00 | 1.00 | 97.9 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1356.0 | 0.0948 |
| azure/us | unknown | no | 53.9 | 102 | 1 | 1.00 | 100.0 | 100.0 | 40.0 | 100.0 | 94.7 | 22.9 | 0 | 0 | 1349.0 | 0.1375 |
| crusoe/fp8 | fp8 | yes | 50.4 | 123 | 1 | 1.00 | 100.0 | 100.0 | 31.8 | 100.0 | 100.0 | 6.20 | 0 | 0 | 1131.0 | 0.1489 |
| novita/fp8 | fp8 | yes | 47.2 | 127 | 0 | 1.00 | 95.7 | 100.0 | 33.3 | 100.0 | 100.0 | 2.10 | 0 | 0 | 1782.0 | 0.1386 |
| cloudflare | unknown | yes | 45.4 | 130 | 0 | 1.00 | 91.7 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1951.0 | 0.1046 |
| gmicloud/fp8 | fp8 | yes | 44.6 | 130 | 0.00 | 1.00 | 100.0 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2403.0 | 0.0873 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, siliconflow/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 14.

## Noise floor (self-check, two passes one hour apart)

| Model | Endpoint | Prompts | Agreement % |
|---|---|---|---|
| deepseek-v4-pro | baidu/fp8 | 12 | 100.0 |
| deepseek-v4-pro | relace/fp4 | 12 | 83.3 |
| deepseek-v4-pro | alibaba/fp8/us-east-1 | 12 | 83.3 |
| deepseek-v4-pro | crusoe/fp8 | 12 | 83.3 |
| deepseek-v4-pro | streamlake/fp8 | 12 | 75.0 |
| deepseek-v4-pro | gmicloud/fp8 | 12 | 75.0 |
| deepseek-v4-pro | cloudflare | 12 | 75.0 |
| deepseek-v4-pro | alibaba/fp8 | 12 | 75.0 |
| deepseek-v4-pro | deepinfra/fp8 | 12 | 66.7 |
| deepseek-v4-pro | novita/fp8 | 12 | 66.7 |
| deepseek-v4-pro | siliconflow/fp8 | 12 | 66.7 |
| deepseek-v4-pro | venice | 12 | 66.7 |
| deepseek-v4-pro | atlas-cloud/fp4 | 12 | 58.3 |
| deepseek-v4-pro | digitalocean | 12 | 50.0 |
| deepseek-v4-pro | azure/us | 10 | 20.0 |
| gpt-oss-120b | akashml/bf16 | 12 | 100.0 |
| gpt-oss-120b | google-vertex/global | 12 | 100.0 |
| gpt-oss-120b | sambanova | 12 | 100.0 |
| gpt-oss-120b | amazon-bedrock | 12 | 100.0 |
| gpt-oss-120b | groq | 12 | 100.0 |
| gpt-oss-120b | mara | 12 | 100.0 |
| gpt-oss-120b | cerebras/fp16 | 12 | 100.0 |
| gpt-oss-120b | parasail/fp4 | 8 | 100.0 |
| gpt-oss-120b | near-ai/fp4 | 12 | 91.7 |
| gpt-oss-120b | sail-research/fp4 | 12 | 91.7 |
| gpt-oss-120b | baseten/fp4/us | 12 | 91.7 |
| gpt-oss-120b | baseten/fp4 | 12 | 91.7 |
| gpt-oss-120b | amazon-bedrock/eu-west-1 | 12 | 91.7 |
| gpt-oss-120b | nebius/fp4 | 12 | 91.7 |
| gpt-oss-120b | siliconflow/fp8 | 12 | 91.7 |
| gpt-oss-120b | venice/int4 | 11 | 90.9 |
| gpt-oss-120b | deepinfra/bf16 | 10 | 90.0 |
| gpt-oss-120b | crusoe/bf16 | 12 | 83.3 |
| gpt-oss-120b | novita/fp4 | 12 | 83.3 |
| gpt-oss-120b | mancer/fp8 | 12 | 83.3 |
| gpt-oss-120b | digitalocean | 12 | 83.3 |
| gpt-oss-120b | together | 12 | 83.3 |
| gpt-oss-120b | phala | 12 | 83.3 |
| gpt-oss-120b | dekallm/bf16 | 12 | 75.0 |
| gpt-oss-120b | coreweave/fp4 | 12 | 66.7 |

## Footer

- Rows: 5760; errors 97; misrouted 0; truncated (finish_reason length) 25; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.3829; billed: $2.2523; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.


---

## Check 4: full-precision endpoints and reference rule

See "Resolved slugs" above. gpt-oss-120b used the bf16/fp16 plurality (five endpoints, no prompt without a plurality). deepseek-v4-pro fell back to the all-endpoint plurality (fourteen prompts had no plurality and were excluded from exact match).

## Check 5: noise floor

The table is in the scorecard. Many endpoints are below 90% two-pass agreement, as the brief asked to be flagged: for deepseek-v4-pro all but one endpoint (baidu/fp8 at 100%), for gpt-oss-120b nine of twenty-five. No code was changed to raise it.

What the disagreement is made of (same endpoint, same prompt, one hour apart, exact string):

| Model | Family | Disagreeing pairs / pairs |
|---|---|---|
| deepseek-v4-pro | math | 30 / 45 |
| deepseek-v4-pro | json | 14 / 45 |
| deepseek-v4-pro | string | 9 / 30 |
| deepseek-v4-pro | needle | 0 / 30 |
| deepseek-v4-pro | echo | 0 / 28 |
| gpt-oss-120b | string | 17 / 49 |
| gpt-oss-120b | json | 11 / 73 |
| gpt-oss-120b | math | 0 / 73 |
| gpt-oss-120b | needle | 0 / 49 |
| gpt-oss-120b | echo | 0 / 49 |

DeepSeek V4 Pro's math answers are graded correct 92 to 100% of the time on every endpoint but match the reference string only 34% of the time pooled: the wording around the number changes between calls at temperature zero. Exact string match is therefore a weak instrument for that model and the graded family columns carry the signal. Needle and echo are deterministic on both models. The twelve-prompt self-check is coarse (one disagreement is 8.3 points); the fixed 120 prompts repeat every night, so night-over-night agreement per endpoint on the fixed set is the better noise floor and needs no code change.

## Check 6: billed cost

`run.json`: estimate $3.3829; billed $2.2523 (main run $1.9543, self-check passes $0.1405 and $0.1575). Under $5.00. Every ok row carried `usage.cost` from OpenRouter (estimated-cost rows: 0).

## Check 7: workflow

`workflow_dispatch` of `nightly.yml` on `main` with `date=2026-10-27`, `selfcheck=true`: https://github.com/unblinkr/bitdepth/actions/runs/40584577962, success, committed `2102888 probe: 2026-10-27 (dispatch)`. A first dispatch (run 40579738792) was refused by GitHub before any step ran because the repository was private and the account's private Actions minutes were nearly spent; the founder made the repository public and the second dispatch ran. The main probe took about 50 minutes; the job was two hours because of the one-hour self-check wait.

## Check 8: pytest

`25 passed in 0.35s`

## Checks 9, 10, 11

```
=== check 9 ===
git grep -niw cheat (excluding the brief): 0 files
git grep -niw fraud (excluding the brief): 0 files
git grep -niw lying (excluding the brief): 0 files
git grep -niw scam (excluding the brief): 0 files
sk-or- (excluding the brief): 0 files
em dash U+2014 (all tracked files incl. data): 0 files

=== check 10: git grep -n OPENROUTER_API_KEY (excluding the brief) ===
.github/workflows/nightly.yml:33:          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
.github/workflows/nightly.yml:35:          if [ -z "$OPENROUTER_API_KEY" ]; then
.github/workflows/nightly.yml:36:            echo "OPENROUTER_API_KEY is not set as a repository secret. Add it under Settings, Secrets and variables, Actions."
.github/workflows/nightly.yml:68:          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
CLAUDE.md:11:- `OPENROUTER_API_KEY` is read from the environment only. It never appears in a file, a log, a run record or a commit.
README.md:3:This repository probes every OpenRouter endpoint serving two open-weight models with a fixed set of generated prompts at temperature zero, every night. A scorecard is one Markdown table per model with one row per endpoint, scoring each endpoint's outputs against a reference built from the endpoints that declare full precision. The one secret is `OPENROUTER_API_KEY`, set as a GitHub Actions secret and read from the environment. The repository is public so the nightly job runs on free Actions minutes; the scorecards in it are working data from an experiment in progress, scored against a stated reference, and are not findings about any provider.
probe/openrouter.py:34:    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
probe/openrouter.py:36:        raise RuntimeError("OPENROUTER_API_KEY is not set in the environment")

=== check 11: git grep -n sk-or- (excluding the brief) ===
(no output above means empty)

```

## Files changed

CLAUDE.md, README.md, .gitignore, requirements.txt, pyproject.toml, .github/workflows/nightly.yml, probe/__init__.py, probe/openrouter.py, probe/generators.py, probe/budget.py, probe/run.py, probe/score.py, tests/test_generators.py, tests/test_budget.py, tests/test_run.py, tests/test_score.py, tests/fixtures/endpoints_small.json, data/prompts/fixed.jsonl, data/runs/.gitkeep, data/scorecard/.gitkeep, tasks/probe-harness/TASK.md, tasks/probe-harness/QUESTIONS.md, tasks/probe-harness/REPORT.md; night one added data/runs/2026-10-27/* and data/scorecard/2026-10-27.md, latest.md.

## QUESTIONS.md

Seven items: GLM-5.2 replaced by DeepSeek V4 Pro for cost; estimate formula per family with a runtime cost stop; reasoning switched off where allowed (gpt-oss endpoints rejected `enabled: false` and ran at `effort: low`, about 38 reasoning tokens per answer; DeepSeek accepted it, zero reasoning tokens); night one ran in Actions; misroute detection is provider-level; no substitution below six endpoints; repository made public.

## What the scorecard shows and what it does not

It shows that one key, one laptop-free harness and about two dollars can send the same 144 prompts to forty endpoints in under an hour and get back outputs that can be lined up against a stated reference. On gpt-oss-120b every endpoint lands between 91% and 98% exact match against the full-precision plurality, and the graded answers are near-identical across endpoints, so one night cannot separate those endpoints from each other or from their own noise. On DeepSeek V4 Pro the exact-match spread is wide (45% to 86%) but so is each endpoint's agreement with itself an hour later, and most of that is wording around a correct number; the string family is where endpoints differ in graded accuracy (21% to 67% on 24 prompts), which is suggestive and not yet significant. It does not show that any endpoint serves anything other than what it declares, and it is not a finding about any provider. Thirteen more nights of the same fixed prompts will say whether the string-family gap and any other gap holds up above the night-over-night noise.
