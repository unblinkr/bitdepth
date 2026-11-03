# Bitdepth scorecard 2026-11-03

Run `2026-11-03-live`, source `live`, started 2026-11-03T15:15:09Z, finished 2026-11-03T17:25:47Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 331.5 | 0.0374 |
| dekallm/bf16 | bf16 | yes | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 1 | 1873.0 | 0.0040 |
| mara | unknown | no | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 1 | 1109.0 | 0.0193 |
| sambanova | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 489.5 | 0.0202 |
| together | unknown | no | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 73.9 | 100.0 | 100.0 | 0.70 | 0 | 1 | 818.0 | 0.0181 |
| sail-research/fp4 | fp4 | yes | 97.7 | 130 | 0 | 1.00 | 100.0 | 100.0 | 81.0 | 100.0 | 100.0 | 9.70 | 0 | 0 | 692.5 | 0.0072 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 898.5 | 0.0182 |
| baseten/fp4 | fp4 | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 567.0 | 0.0128 |
| deepinfra/fp8 | fp8 | yes | 96.8 | 124 | 0.00 | 1.00 | 100.0 | 100.0 | 78.3 | 100.0 | 100.0 | 13.9 | 0 | 1 | 1594.0 | 0.0221 |
| baseten/fp4/us | fp4 | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 580.5 | 0.0128 |
| mancer/fp8 | fp8 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 82.6 | 100.0 | 100.0 | 1.40 | 0 | 0 | 1530.5 | 0.0065 |
| near-ai/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1810.0 | 0.0038 |
| primeintellect/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 69.6 | 100.0 | 100.0 | 1.40 | 0 | 0 | 995.0 | 0.0045 |
| siliconflow/fp8 | fp8 | no | 95.7 | 141 | 0.00 | 1.00 | 97.8 | 100.0 | 91.7 | 100.0 | 100.0 | 2.10 | 0 | 0 | 3349.0 | 0.0250 |
| akashml/bf16 | bf16 | yes | 95.5 | 134 | 0.00 | 1.00 | 100.0 | 100.0 | 82.6 | 100.0 | 100.0 | 6.90 | 0 | 1 | 745.5 | 0.0041 |
| crusoe/bf16 | bf16 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 82.6 | 100.0 | 100.0 | 1.40 | 0 | 0 | 585.5 | 0.0065 |
| groq | unknown | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 367.5 | 0.0182 |
| parasail/fp4 | fp4 | yes | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 497.0 | 0.0151 |
| amazon-bedrock | unknown | no | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 381.0 | 0.0181 |
| coreweave/fp4 | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1031.0 | 0.0041 |
| digitalocean | unknown | no | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1530.0 | 0.0087 |
| nebius/fp4 | fp4 | yes | 93.1 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 555.5 | 0.0178 |
| google-vertex/global | unknown | yes | 92.4 | 144 | 0 | 1.00 | 95.8 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 2 | 2175.0 | 0.0110 |
| phala | unknown | yes | 91.9 | 136 | 0 | 1.00 | 97.7 | 100.0 | 79.2 | 100.0 | 100.0 | 5.60 | 0 | 3 | 1243.0 | 0.0224 |
| deepinfra/bf16 | bf16 | yes | 85.3 | 109 | 0.00 | 1.00 | 82.8 | 95.0 | 61.9 | 94.7 | 95.0 | 24.3 | 0 | 1 | 3262.0 | 0.0035 |
| venice/int4 | int4 | no | 76.4 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 75.0 | 100.0 | 83.3 | 0.00 | 0 | 19 | 2336.0 | 0.0052 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 84.4 | 135 | 4 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2409.0 | 0.1323 |
| alibaba/fp8/us-east-1 | fp8 | yes | 83.7 | 135 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2165.5 | 0.1180 |
| atlas-cloud/fp4 | fp4 | yes | 74.8 | 135 | 1.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2209.0 | 0.1495 |
| siliconflow/fp8 | fp8 | no | 74.8 | 135 | 2.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2327.0 | 0.0906 |
| streamlake/fp8 | fp8 | no | 74.8 | 135 | 4.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2271.5 | 0.0335 |
| relace/fp4 | fp4 | no | 74.1 | 135 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1158.5 | 0.0798 |
| venice | unknown | no | 70.4 | 135 | 1.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 87.5 | 0.00 | 0 | 0 | 2402.0 | 0.0892 |
| deepinfra/fp8 | fp8 | yes | 70.1 | 117 | 1 | 1.00 | 100.0 | 100.0 | 61.9 | 100.0 | 95.0 | 13.2 | 0 | 0 | 1499.0 | 0.0940 |
| azure/us | unknown | no | 57.8 | 135 | 1 | 1.00 | 97.9 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1269.5 | 0.1745 |
| digitalocean | unknown | no | 57.0 | 135 | 1.00 | 1.00 | 97.9 | 100.0 | 33.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1731.0 | 0.0952 |
| baidu/fp8 | fp8 | no | 48.1 | 135 | 0.00 | 1.00 | 100.0 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1690.0 | 0.0764 |
| crusoe/fp8 | fp8 | yes | 48.1 | 135 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 817.5 | 0.1469 |
| gmicloud/fp8 | fp8 | yes | 47.4 | 135 | 0 | 1.00 | 97.9 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2419.0 | 0.0760 |
| novita/fp8 | fp8 | yes | 47.4 | 135 | 0 | 1.00 | 100.0 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1942.0 | 0.0968 |
| cloudflare | unknown | yes | 46.3 | 134 | 0.00 | 1.00 | 95.7 | 100.0 | 20.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2730.0 | 0.0708 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 9.

## Footer

- Rows: 5904; errors 120; misrouted 0; truncated (finish_reason length) 37; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.3728; billed: $1.8699; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
