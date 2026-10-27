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
