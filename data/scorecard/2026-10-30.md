# Bitdepth scorecard 2026-10-30

Run `2026-10-30-live`, source `live`, started 2026-10-30T14:15:48Z, finished 2026-10-30T15:28:27Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| parasail/fp4 | fp4 | yes | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 1 | 525.0 | 0.0148 |
| baseten/fp4 | fp4 | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 482.0 | 0.0129 |
| crusoe/bf16 | bf16 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 449.5 | 0.0064 |
| deepinfra/bf16 | bf16 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 1.40 | 0 | 1 | 2284.5 | 0.0047 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 667.5 | 0.0181 |
| baseten/fp4/us | fp4 | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.70 | 0 | 1 | 472.0 | 0.0129 |
| together | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 958.0 | 0.0177 |
| deepinfra/fp8 | fp8 | yes | 96.9 | 131 | 0.00 | 1.00 | 100.0 | 100.0 | 86.4 | 100.0 | 100.0 | 9.00 | 0 | 0 | 1489.0 | 0.0234 |
| amazon-bedrock | unknown | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 260.0 | 0.0180 |
| mara | unknown | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.70 | 0 | 0 | 839.0 | 0.0191 |
| nebius/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 425.0 | 0.0175 |
| sambanova | unknown | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 696.5 | 0.0200 |
| akashml/bf16 | bf16 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 831.0 | 0.0042 |
| cerebras/fp16 | fp16 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 213.5 | 0.0371 |
| sail-research/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 894.0 | 0.0082 |
| siliconflow/fp8 | fp8 | no | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2891.5 | 0.0254 |
| groq | unknown | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 309.0 | 0.0180 |
| novita/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1469.5 | 0.0088 |
| coreweave/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1297.5 | 0.0040 |
| dekallm/bf16 | bf16 | yes | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1454.5 | 0.0041 |
| mancer/fp8 | fp8 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1554.0 | 0.0062 |
| venice/int4 | int4 | no | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2530.0 | 0.0039 |
| google-vertex/global | unknown | yes | 93.8 | 144 | 0 | 1.00 | 87.5 | 95.8 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 798.5 | 0.0107 |
| phala | unknown | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 4 | 1865.5 | 0.0238 |
| digitalocean | unknown | no | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1262.5 | 0.0086 |
| near-ai/fp4 | fp4 | yes | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1689.0 | 0.0038 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 81.8 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2370.0 | 0.1288 |
| alibaba/fp8/us-east-1 | fp8 | yes | 81.1 | 132 | 1 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2057.5 | 0.1348 |
| atlas-cloud/fp4 | fp4 | yes | 78.8 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2343.0 | 0.1420 |
| streamlake/fp8 | fp8 | no | 78.8 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2383.0 | 0.0358 |
| deepinfra/fp8 | fp8 | yes | 77.3 | 132 | 3.50 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1199.0 | 0.1177 |
| relace/fp4 | fp4 | no | 74.8 | 131 | 3 | 1.00 | 100.0 | 100.0 | 69.6 | 100.0 | 95.8 | 0.70 | 0 | 0 | 1838.0 | 0.0794 |
| siliconflow/fp8 | fp8 | no | 68.9 | 132 | 3 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2143.0 | 0.0950 |
| venice | unknown | no | 68.9 | 132 | 1 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1553.5 | 0.0679 |
| digitalocean | unknown | no | 59.1 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1623.5 | 0.0939 |
| baidu/fp8 | fp8 | no | 53.8 | 132 | 0 | 1.00 | 97.9 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1745.5 | 0.1348 |
| gmicloud/fp8 | fp8 | yes | 53.8 | 132 | 0 | 1.00 | 97.9 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2730.5 | 0.0856 |
| crusoe/fp8 | fp8 | yes | 53.4 | 131 | 1 | 1.00 | 97.9 | 100.0 | 33.3 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1873.0 | 0.1512 |
| azure/us | unknown | no | 53.0 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1104.0 | 0.1748 |
| novita/fp8 | fp8 | yes | 50.8 | 132 | 0 | 1.00 | 93.8 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1825.0 | 0.1228 |
| cloudflare | unknown | yes | 48.5 | 132 | 0.00 | 1.00 | 93.8 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2260.5 | 0.0830 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, streamlake/fp8, gmicloud/fp8, siliconflow/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, baidu/fp8, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 12.

## Footer

- Rows: 5904; errors 20; misrouted 0; truncated (finish_reason length) 21; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.4988; billed: $1.9996; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
