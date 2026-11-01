# Bitdepth scorecard 2026-11-01

Run `2026-11-01-live`, source `live`, started 2026-11-01T14:18:54Z, finished 2026-11-01T15:24:46Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4 | fp4 | no | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 424.5 | 0.0127 |
| baseten/fp4/us | fp4 | no | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 444.0 | 0.0125 |
| dekallm/bf16 | bf16 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1820.0 | 0.0041 |
| parasail/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 554.0 | 0.0146 |
| deepinfra/bf16 | bf16 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2144.0 | 0.0048 |
| mara | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 925.5 | 0.0196 |
| near-ai/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1179.0 | 0.0038 |
| sambanova | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 622.0 | 0.0205 |
| siliconflow/fp8 | fp8 | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 78.3 | 100.0 | 95.8 | 1.40 | 0 | 0 | 2411.5 | 0.0248 |
| deepinfra/fp8 | fp8 | yes | 97.0 | 135 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 6.20 | 0 | 0 | 1482.0 | 0.0232 |
| cerebras/fp16 | fp16 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 252.0 | 0.0374 |
| groq | unknown | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 313.5 | 0.0183 |
| amazon-bedrock/eu-west-1 | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 634.5 | 0.0181 |
| crusoe/bf16 | bf16 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 473.0 | 0.0064 |
| together | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 655.0 | 0.0181 |
| amazon-bedrock | unknown | no | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 351.5 | 0.0183 |
| mancer/fp8 | fp8 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1534.0 | 0.0062 |
| akashml/bf16 | bf16 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 687.0 | 0.0043 |
| nebius/fp4 | fp4 | yes | 93.1 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 486.0 | 0.0175 |
| primeintellect/fp4 | fp4 | yes | 93.1 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1103.5 | 0.0025 |
| sail-research/fp4 | fp4 | yes | 93.1 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 712.5 | 0.0084 |
| novita/fp4 | fp4 | yes | 92.4 | 144 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 95.8 | 95.8 | 0.00 | 0 | 4 | 1222.0 | 0.0085 |
| phala | unknown | yes | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 91.7 | 0.00 | 0 | 6 | 1612.0 | 0.0234 |
| coreweave/fp4 | fp4 | yes | 91.7 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 883.5 | 0.0040 |
| google-vertex/global | unknown | yes | 90.9 | 143 | 0 | 1.00 | 93.8 | 100.0 | 73.9 | 100.0 | 100.0 | 0.70 | 0 | 0 | 982.0 | 0.0109 |
| digitalocean | unknown | no | 88.9 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1172.0 | 0.0086 |
| venice/int4 | int4 | no | 81.9 | 144 | 0.00 | 1.00 | 81.2 | 100.0 | 75.0 | 100.0 | 79.2 | 0.00 | 0 | 13 | 1988.0 | 0.0048 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 87.6 | 137 | 8 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2162.0 | 0.1033 |
| alibaba/fp8 | fp8 | yes | 86.1 | 137 | 8 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2386.0 | 0.1356 |
| baidu/fp8 | fp8 | no | 81.0 | 137 | 2.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1463.5 | 0.0189 |
| deepinfra/fp8 | fp8 | yes | 78.8 | 137 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 95.8 | 95.8 | 0.00 | 0 | 0 | 768.5 | 0.1182 |
| venice | unknown | no | 76.6 | 137 | 4.00 | 1.00 | 100.0 | 100.0 | 70.8 | 95.8 | 95.8 | 0.00 | 0 | 0 | 1116.5 | 0.0689 |
| streamlake/fp8 | fp8 | no | 74.5 | 137 | 4 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2511.5 | 0.0079 |
| atlas-cloud/fp4 | fp4 | yes | 72.3 | 137 | 1.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2315.0 | 0.1490 |
| relace/fp4 | fp4 | no | 70.1 | 137 | 5 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 792.0 | 0.0797 |
| siliconflow/fp8 | fp8 | no | 68.6 | 137 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2189.0 | 0.0928 |
| azure/us | unknown | no | 59.9 | 137 | 1 | 1.00 | 97.9 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1378.5 | 0.1735 |
| digitalocean | unknown | no | 51.8 | 137 | 1.00 | 1.00 | 100.0 | 100.0 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1591.5 | 0.0948 |
| crusoe/fp8 | fp8 | yes | 49.6 | 137 | 1 | 1.00 | 100.0 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1132.0 | 0.1564 |
| gmicloud/fp8 | fp8 | yes | 48.2 | 137 | 1 | 1.00 | 93.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3550.0 | 0.0859 |
| novita/fp8 | fp8 | yes | 46.7 | 137 | 1 | 1.00 | 91.7 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1944.5 | 0.1015 |
| cloudflare | unknown | yes | 43.1 | 137 | 0.00 | 1.00 | 93.8 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2219.5 | 0.1048 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 7.

## Footer

- Rows: 6048; errors 12; misrouted 0; truncated (finish_reason length) 33; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.1857; billed: $1.8473; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
