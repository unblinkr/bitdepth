# Bitdepth scorecard 2026-10-29

Run `2026-10-29-live`, source `live`, started 2026-10-29T14:25:27Z, finished 2026-10-29T15:47:32Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4 | fp4 | no | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 614.5 | 0.0129 |
| crusoe/bf16 | bf16 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 613.5 | 0.0065 |
| amazon-bedrock | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 436.5 | 0.0181 |
| baseten/fp4/us | fp4 | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 531.5 | 0.0127 |
| deepinfra/bf16 | bf16 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 95.8 | 100.0 | 0.00 | 0 | 0 | 2371.5 | 0.0046 |
| mancer/fp8 | fp8 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1733.5 | 0.0063 |
| mara | unknown | no | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 81.8 | 100.0 | 100.0 | 2.10 | 0 | 0 | 1488.0 | 0.0187 |
| parasail/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 636.5 | 0.0150 |
| groq | unknown | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 330.5 | 0.0180 |
| sambanova | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 496.5 | 0.0196 |
| together | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 818.0 | 0.0183 |
| venice/int4 | int4 | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.70 | 0 | 0 | 3326.0 | 0.0038 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 918.0 | 0.0181 |
| cerebras/fp16 | fp16 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 303.5 | 0.0380 |
| coreweave/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 1.40 | 0 | 0 | 1394.0 | 0.0039 |
| dekallm/bf16 | bf16 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2291.0 | 0.0042 |
| near-ai/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2256.5 | 0.0039 |
| nebius/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 557.0 | 0.0171 |
| akashml/bf16 | bf16 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2286.0 | 0.0042 |
| siliconflow/fp8 | fp8 | no | 95.0 | 141 | 0 | 1.00 | 100.0 | 100.0 | 95.7 | 95.8 | 100.0 | 2.10 | 0 | 0 | 3479.0 | 0.0245 |
| sail-research/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 861.5 | 0.0082 |
| novita/fp4 | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1044.5 | 0.0091 |
| phala | unknown | yes | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 3 | 1337.5 | 0.0244 |
| google-vertex/global | unknown | yes | 91.0 | 144 | 0 | 1.00 | 93.8 | 100.0 | 75.0 | 100.0 | 91.7 | 0.00 | 0 | 1 | 1302.0 | 0.0108 |
| digitalocean | unknown | no | 90.3 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1632.5 | 0.0087 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| streamlake/fp8 | fp8 | no | 79.5 | 132 | 4 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2459.0 | 0.0336 |
| alibaba/fp8 | fp8 | yes | 78.0 | 132 | 4 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2410.0 | 0.1301 |
| alibaba/fp8/us-east-1 | fp8 | yes | 77.3 | 132 | 3.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2285.5 | 0.1326 |
| baidu/fp8 | fp8 | no | 75.0 | 132 | 3 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1529.0 | 0.0807 |
| venice | unknown | no | 75.0 | 132 | 3 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1376.5 | 0.0691 |
| relace/fp4 | fp4 | no | 74.0 | 131 | 1.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.70 | 0 | 0 | 1387.0 | 0.0797 |
| atlas-cloud/fp4 | fp4 | yes | 72.7 | 132 | 4.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2606.5 | 0.1442 |
| deepinfra/fp8 | fp8 | yes | 72.7 | 132 | 3.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1259.5 | 0.1182 |
| siliconflow/fp8 | fp8 | no | 69.7 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2639.0 | 0.0931 |
| digitalocean | unknown | no | 58.3 | 132 | 0 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1524.5 | 0.0954 |
| azure/us | unknown | no | 57.6 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1614.0 | 0.1734 |
| crusoe/fp8 | fp8 | yes | 50.0 | 132 | 0.50 | 1.00 | 100.0 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1157.5 | 0.1562 |
| cloudflare | unknown | yes | 49.5 | 111 | 0.00 | 1.00 | 92.7 | 100.0 | 23.8 | 100.0 | 100.0 | 14.6 | 0 | 0 | 2351.0 | 0.0695 |
| novita/fp8 | fp8 | yes | 49.2 | 132 | 1 | 1.00 | 95.8 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1775.5 | 0.1303 |
| gmicloud/fp8 | fp8 | yes | 48.5 | 132 | 1.00 | 1.00 | 100.0 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2387.5 | 0.0862 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 12.

## Footer

- Rows: 5760; errors 31; misrouted 0; truncated (finish_reason length) 12; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.3373; billed: $1.9219; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
