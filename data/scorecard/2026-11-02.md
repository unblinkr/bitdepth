# Bitdepth scorecard 2026-11-02

Run `2026-11-02-live`, source `live`, started 2026-11-02T17:08:49Z, finished 2026-11-02T20:17:54Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8 | fp8 | yes | 100.0 | 136 | n/a | 1.00 | 100.0 | 100.0 | 87.0 | 100.0 | 100.0 | 5.60 | 0 | 1 | 1629.0 | 0.0239 |
| cerebras/fp16 | fp16 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 289.5 | 0.0373 |
| mara | unknown | no | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 950.5 | 0.0191 |
| sambanova | unknown | no | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 722.0 | 0.0203 |
| akashml/bf16 | bf16 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 828.0 | 0.0042 |
| amazon-bedrock | unknown | no | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 349.5 | 0.0180 |
| baseten/fp4 | fp4 | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 599.0 | 0.0127 |
| groq | unknown | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 343.5 | 0.0180 |
| nebius/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 572.0 | 0.0175 |
| baseten/fp4/us | fp4 | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 592.0 | 0.0129 |
| crusoe/bf16 | bf16 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 656.5 | 0.0064 |
| dekallm/bf16 | bf16 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1503.5 | 0.0042 |
| parasail/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 533.0 | 0.0145 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 712.0 | 0.0181 |
| primeintellect/fp4 | fp4 | yes | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 82.6 | 100.0 | 100.0 | 2.80 | 0 | 1 | 950.5 | 0.0054 |
| mancer/fp8 | fp8 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1214.0 | 0.0064 |
| siliconflow/fp8 | fp8 | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3137.5 | 0.0248 |
| together | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 618.5 | 0.0179 |
| near-ai/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1320.0 | 0.0037 |
| sail-research/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 681.0 | 0.0084 |
| coreweave/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 744.0 | 0.0041 |
| deepinfra/bf16 | bf16 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2467.5 | 0.0048 |
| phala | unknown | yes | 93.1 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 3 | 1633.5 | 0.0239 |
| digitalocean | unknown | no | 91.7 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1435.5 | 0.0085 |
| google-vertex/global | unknown | yes | 90.4 | 136 | 0 | 1.00 | 88.4 | 100.0 | 68.2 | 100.0 | 95.8 | 5.60 | 0 | 1 | 5558.0 | 0.0107 |
| novita/fp4 | fp4 | yes | 90.3 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 5 | 1381.5 | 0.0092 |
| venice/int4 | int4 | no | 75.0 | 144 | 0.00 | 1.00 | 62.5 | 100.0 | 70.8 | 100.0 | 75.0 | 0.00 | 0 | 25 | 2078.5 | 0.0056 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, akashml/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 88.8 | 134 | 8 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2184.0 | 0.0767 |
| alibaba/fp8 | fp8 | yes | 86.6 | 134 | 13.0 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2221.5 | 0.1354 |
| baidu/fp8 | fp8 | no | 77.9 | 122 | 8 | 1.00 | 100.0 | 100.0 | 63.6 | 100.0 | 95.2 | 8.30 | 0 | 0 | 1483.0 | 0.0720 |
| atlas-cloud/fp4 | fp4 | yes | 77.6 | 134 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2352.5 | 0.1476 |
| deepinfra/fp8 | fp8 | yes | 75.8 | 132 | 4.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.7 | 1.40 | 0 | 0 | 1180.5 | 0.1140 |
| relace/fp4 | fp4 | no | 74.4 | 129 | 4 | 1.00 | 100.0 | 100.0 | 72.7 | 100.0 | 95.7 | 3.50 | 0 | 0 | 1213.0 | 0.0790 |
| streamlake/fp8 | fp8 | no | 72.4 | 134 | 5 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2462.0 | 0.0325 |
| venice | unknown | no | 72.4 | 134 | 3 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1408.5 | 0.0722 |
| siliconflow/fp8 | fp8 | no | 71.6 | 134 | 3.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2213.0 | 0.0932 |
| digitalocean | unknown | no | 58.7 | 126 | 1.00 | 1.00 | 97.8 | 100.0 | 65.0 | 100.0 | 95.8 | 6.90 | 0 | 0 | 1678.0 | 0.0881 |
| azure/us | unknown | no | 54.9 | 133 | 1.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.70 | 0 | 0 | 1439.0 | 0.1732 |
| crusoe/fp8 | fp8 | yes | 50.7 | 134 | 0.00 | 1.00 | 79.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 780.5 | 0.1477 |
| gmicloud/fp8 | fp8 | yes | 46.3 | 134 | 1.00 | 1.00 | 97.9 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2537.5 | 0.0860 |
| cloudflare | unknown | yes | 45.1 | 133 | 0 | 1.00 | 93.8 | 100.0 | 20.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2054.0 | 0.0911 |
| novita/fp8 | fp8 | yes | 44.8 | 134 | 1.00 | 1.00 | 89.6 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1705.5 | 0.1148 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, cloudflare, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, crusoe/fp8, azure/us. Prompts with no plurality (excluded from exact match): 10.

## Noise floor (self-check, two passes one hour apart)

| Model | Endpoint | Prompts | Agreement % |
|---|---|---|---|
| deepseek-v4-pro | baidu/fp8 | 30 | 96.7 |
| deepseek-v4-pro | relace/fp4 | 36 | 91.7 |
| deepseek-v4-pro | crusoe/fp8 | 36 | 88.9 |
| deepseek-v4-pro | alibaba/fp8 | 36 | 86.1 |
| deepseek-v4-pro | alibaba/fp8/us-east-1 | 36 | 83.3 |
| deepseek-v4-pro | novita/fp8 | 36 | 77.8 |
| deepseek-v4-pro | gmicloud/fp8 | 36 | 75.0 |
| deepseek-v4-pro | cloudflare | 36 | 75.0 |
| deepseek-v4-pro | deepinfra/fp8 | 36 | 75.0 |
| deepseek-v4-pro | atlas-cloud/fp4 | 36 | 72.2 |
| deepseek-v4-pro | siliconflow/fp8 | 36 | 69.4 |
| deepseek-v4-pro | venice | 36 | 69.4 |
| deepseek-v4-pro | streamlake/fp8 | 36 | 63.9 |
| deepseek-v4-pro | digitalocean | 36 | 55.6 |
| deepseek-v4-pro | azure/us | 36 | 52.8 |
| gpt-oss-120b | primeintellect/fp4 | 36 | 100.0 |
| gpt-oss-120b | sambanova | 36 | 100.0 |
| gpt-oss-120b | deepinfra/bf16 | 36 | 100.0 |
| gpt-oss-120b | together | 36 | 100.0 |
| gpt-oss-120b | groq | 36 | 100.0 |
| gpt-oss-120b | cerebras/fp16 | 36 | 100.0 |
| gpt-oss-120b | deepinfra/fp8 | 34 | 100.0 |
| gpt-oss-120b | mara | 36 | 100.0 |
| gpt-oss-120b | near-ai/fp4 | 36 | 97.2 |
| gpt-oss-120b | sail-research/fp4 | 36 | 97.2 |
| gpt-oss-120b | baseten/fp4 | 36 | 97.2 |
| gpt-oss-120b | amazon-bedrock/eu-west-1 | 36 | 97.2 |
| gpt-oss-120b | amazon-bedrock | 36 | 97.2 |
| gpt-oss-120b | dekallm/bf16 | 36 | 94.4 |
| gpt-oss-120b | coreweave/fp4 | 36 | 94.4 |
| gpt-oss-120b | akashml/bf16 | 36 | 94.4 |
| gpt-oss-120b | mancer/fp8 | 36 | 94.4 |
| gpt-oss-120b | parasail/fp4 | 36 | 94.4 |
| gpt-oss-120b | nebius/fp4 | 36 | 94.4 |
| gpt-oss-120b | novita/fp4 | 36 | 91.7 |
| gpt-oss-120b | siliconflow/fp8 | 36 | 91.7 |
| gpt-oss-120b | baseten/fp4/us | 35 | 91.4 |
| gpt-oss-120b | crusoe/bf16 | 36 | 88.9 |
| gpt-oss-120b | digitalocean | 36 | 88.9 |
| gpt-oss-120b | venice/int4 | 36 | 83.3 |
| gpt-oss-120b | phala | 36 | 83.3 |
| gpt-oss-120b | google-vertex/global | 32 | 71.9 |

## Footer

- Rows: 6048; errors 51; misrouted 0; truncated (finish_reason length) 46; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $3.3805; billed: $2.8292; cap $5.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
