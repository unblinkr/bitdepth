# Bitdepth scorecard 2026-10-31

Run `2026-10-31-live`, source `live`, started 2026-10-31T13:41:33Z, finished 2026-10-31T14:48:37Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sail-research/fp4 | fp4 | yes | 100.0 | 143 | n/a | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 532.0 | 0.0083 |
| mancer/fp8 | fp8 | yes | 99.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1512.0 | 0.0061 |
| amazon-bedrock/eu-west-1 | unknown | no | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 831.5 | 0.0179 |
| crusoe/bf16 | bf16 | yes | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 392.0 | 0.0066 |
| amazon-bedrock | unknown | no | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 425.5 | 0.0180 |
| cerebras/fp16 | fp16 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 344.0 | 0.0377 |
| nebius/fp4 | fp4 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 513.5 | 0.0174 |
| together | unknown | no | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 752.0 | 0.0178 |
| deepinfra/fp8 | fp8 | yes | 97.7 | 129 | 0 | 1.00 | 100.0 | 100.0 | 81.8 | 100.0 | 100.0 | 9.70 | 0 | 1 | 1540.0 | 0.0229 |
| baseten/fp4 | fp4 | no | 97.2 | 143 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 412.5 | 0.0129 |
| coreweave/fp4 | fp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 1 | 989.0 | 0.0041 |
| deepinfra/bf16 | bf16 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2226.5 | 0.0048 |
| dekallm/bf16 | bf16 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1745.5 | 0.0041 |
| google-vertex/global | unknown | yes | 97.2 | 142 | 0.00 | 1.00 | 95.7 | 100.0 | 83.3 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1097.0 | 0.0106 |
| groq | unknown | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 276.5 | 0.0180 |
| mara | unknown | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 908.5 | 0.0191 |
| sambanova | unknown | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 609.0 | 0.0200 |
| baseten/fp4/us | fp4 | no | 96.5 | 143 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 407.0 | 0.0127 |
| venice/int4 | int4 | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2343.5 | 0.0039 |
| akashml/bf16 | bf16 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 685.5 | 0.0041 |
| near-ai/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1739.0 | 0.0038 |
| parasail/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 634.0 | 0.0146 |
| phala | unknown | yes | 95.8 | 143 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 3 | 1538.0 | 0.0238 |
| siliconflow/fp8 | fp8 | no | 95.7 | 139 | 0.00 | 1.00 | 97.9 | 100.0 | 91.3 | 100.0 | 100.0 | 2.80 | 0 | 0 | 3608.5 | 0.0236 |
| novita/fp4 | fp4 | yes | 91.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1466.0 | 0.0092 |
| digitalocean | unknown | no | 90.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1373.5 | 0.0087 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 1.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 81.2 | 133 | 2 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2194.0 | 0.0974 |
| alibaba/fp8 | fp8 | yes | 80.5 | 133 | 3.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2315.0 | 0.1294 |
| venice | unknown | no | 80.5 | 133 | 1.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1087.5 | 0.0689 |
| streamlake/fp8 | fp8 | no | 78.9 | 133 | 1.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2080.5 | 0.0291 |
| atlas-cloud/fp4 | fp4 | yes | 76.7 | 133 | 1 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2402.5 | 0.1381 |
| deepinfra/fp8 | fp8 | yes | 73.7 | 133 | 1 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 719.5 | 0.1181 |
| relace/fp4 | fp4 | no | 71.4 | 133 | 1.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1044.5 | 0.0797 |
| siliconflow/fp8 | fp8 | no | 70.7 | 133 | 2 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2238.0 | 0.0904 |
| azure/us | unknown | no | 58.6 | 133 | 1 | 1.00 | 95.8 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1289.5 | 0.1739 |
| crusoe/fp8 | fp8 | yes | 57.9 | 133 | 0.00 | 1.00 | 100.0 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1030.0 | 0.1563 |
| digitalocean | unknown | no | 57.1 | 133 | 1 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1680.5 | 0.0955 |
| gmicloud/fp8 | fp8 | yes | 54.1 | 133 | 0 | 1.00 | 97.9 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2426.5 | 0.0784 |
| novita/fp8 | fp8 | yes | 53.4 | 133 | 0.00 | 1.00 | 97.9 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1805.0 | 0.1057 |
| baidu/fp8 | fp8 | no | 51.9 | 133 | 0.00 | 1.00 | 97.9 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1552.5 | 0.0675 |
| cloudflare | unknown | yes | 50.4 | 133 | 0.00 | 1.00 | 93.8 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2276.5 | 0.0920 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 11.

## Footer

- Rows: 5904; errors 20; misrouted 0; truncated (finish_reason length) 22; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.3372; billed: $1.8711; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
