# Bitdepth scorecard 2026-10-28

Run `2026-10-28-dispatch`, source `dispatch`, started 2026-10-28T12:40:58Z, finished 2026-10-28T13:43:59Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4/us | fp4 | no | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 611.0 | 0.0127 |
| amazon-bedrock | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 405.5 | 0.0184 |
| crusoe/bf16 | bf16 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 398.5 | 0.0065 |
| deepinfra/bf16 | bf16 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1982.5 | 0.0047 |
| parasail/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 535.5 | 0.0152 |
| cerebras/fp16 | fp16 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 781.5 | 0.0378 |
| nebius/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 484.5 | 0.0176 |
| together | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 756.0 | 0.0183 |
| akashml/bf16 | bf16 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 708.5 | 0.0043 |
| baseten/fp4 | fp4 | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 591.0 | 0.0127 |
| groq | unknown | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 353.5 | 0.0181 |
| amazon-bedrock/eu-west-1 | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 896.0 | 0.0181 |
| coreweave/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 946.0 | 0.0040 |
| dekallm/bf16 | bf16 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1621.5 | 0.0041 |
| mancer/fp8 | fp8 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1260.5 | 0.0063 |
| mara | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 887.5 | 0.0196 |
| venice/int4 | int4 | no | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2359.0 | 0.0038 |
| google-vertex/global | unknown | yes | 95.1 | 144 | 0 | 1.00 | 93.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 856.5 | 0.0111 |
| near-ai/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1877.0 | 0.0038 |
| sail-research/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 843.5 | 0.0083 |
| sambanova | unknown | no | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 546.0 | 0.0206 |
| siliconflow/fp8 | fp8 | no | 93.1 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2292.5 | 0.0260 |
| phala | unknown | yes | 91.7 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 95.8 | 100.0 | 0.00 | 0 | 3 | 1369.0 | 0.0244 |
| digitalocean | unknown | no | 91.0 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1368.0 | 0.0086 |
| novita/fp4 | fp4 | yes | 91.0 | 144 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 4 | 1077.5 | 0.0093 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 80.3 | 132 | 4.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2251.5 | 0.1418 |
| relace/fp4 | fp4 | no | 78.6 | 131 | 3.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.70 | 0 | 0 | 1305.0 | 0.0774 |
| atlas-cloud/fp4 | fp4 | yes | 78.0 | 132 | 4 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2635.5 | 0.1459 |
| streamlake/fp8 | fp8 | no | 78.0 | 132 | 3 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2527.0 | 0.0349 |
| deepinfra/fp8 | fp8 | yes | 76.5 | 132 | 3 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1405.0 | 0.1182 |
| alibaba/fp8 | fp8 | yes | 75.0 | 132 | 3 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2507.0 | 0.1283 |
| venice | unknown | no | 72.7 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1705.5 | 0.0696 |
| siliconflow/fp8 | fp8 | no | 71.2 | 132 | 2.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2792.5 | 0.0960 |
| baidu/fp8 | fp8 | no | 68.9 | 122 | 0.00 | 1.00 | 97.6 | 100.0 | 34.8 | 100.0 | 91.3 | 6.90 | 0 | 0 | 1777.5 | 0.0756 |
| azure/us | unknown | no | 59.5 | 131 | 1 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.3 | 0.70 | 0 | 0 | 1298.0 | 0.1747 |
| digitalocean | unknown | no | 55.3 | 132 | 1 | 1.00 | 100.0 | 100.0 | 37.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1494.0 | 0.0956 |
| crusoe/fp8 | fp8 | yes | 50.0 | 132 | 0.00 | 1.00 | 100.0 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1573.5 | 0.1568 |
| novita/fp8 | fp8 | yes | 48.5 | 132 | 0.00 | 1.00 | 97.9 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1994.5 | 0.1248 |
| gmicloud/fp8 | fp8 | yes | 47.7 | 132 | 0 | 1.00 | 97.9 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2636.0 | 0.0847 |
| cloudflare | unknown | yes | 44.7 | 132 | 0 | 1.00 | 93.8 | 100.0 | 16.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2350.5 | 0.0569 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 12.

## Footer

- Rows: 5760; errors 12; misrouted 0; truncated (finish_reason length) 20; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.3401; billed: $1.9157; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
