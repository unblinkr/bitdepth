# Bitdepth scorecard 2026-11-16

Run `2026-11-16-live`, source `live`, started 2026-11-16T17:06:52Z, finished 2026-11-16T22:55:13Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4 | fp4 | no | 99.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 504.0 | 0.0129 |
| cerebras/fp16 | fp16 | yes | 99.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 238.5 | 0.0371 |
| mancer/fp8 | fp8 | yes | 99.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 793.5 | 0.0080 |
| sambanova | unknown | no | 99.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 430.5 | 0.0199 |
| nebius/fp4 | fp4 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 405.0 | 0.0176 |
| baseten/fp4/us | fp4 | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 526.5 | 0.0128 |
| coreweave/fp4 | fp4 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 578.5 | 0.0041 |
| groq | unknown | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 336.0 | 0.0180 |
| together | unknown | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 639.5 | 0.0180 |
| deepinfra/bf16 | bf16 | yes | 97.5 | 121 | 0 | 1.00 | 100.0 | 100.0 | 81.0 | 94.7 | 100.0 | 14.6 | 0 | 1 | 5886.0 | 0.0031 |
| amazon-bedrock | unknown | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 896.5 | 0.0181 |
| sail-research/fp4 | fp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 970.0 | 0.0084 |
| siliconflow/fp8 | fp8 | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2887.0 | 0.0240 |
| akashml/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1584.0 | 0.0042 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 853.0 | 0.0179 |
| crusoe/bf16 | bf16 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 572.0 | 0.0067 |
| dekallm/bf16 | bf16 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1486.0 | 0.0041 |
| parasail/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 516.0 | 0.0144 |
| primeintellect/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 897.5 | 0.0051 |
| parasail/fast | fp4 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 476.5 | 0.0192 |
| google-vertex/global | unknown | yes | 94.4 | 142 | 0.00 | 1.00 | 93.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 432.0 | 0.0111 |
| near-ai/fp4 | fp4 | yes | 93.7 | 142 | 0 | 1.00 | 97.9 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1622.5 | 0.0038 |
| digitalocean | unknown | no | 92.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1132.5 | 0.0084 |
| venice/int4 | int4 | no | 74.6 | 142 | 0.00 | 1.00 | 60.4 | 100.0 | 87.5 | 100.0 | 83.3 | 0.00 | 0 | 21 | 1663.5 | 0.0053 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 2.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 81.9 | 138 | 8 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2554.5 | 0.0979 |
| streamlake/fp8 | fp8 | no | 81.9 | 138 | 5 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2367.0 | 0.0329 |
| deepinfra/fp8 | fp8 | yes | 79.7 | 138 | 8.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1251.0 | 0.1081 |
| baidu/fp8 | fp8 | no | 77.5 | 138 | 1 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1383.5 | 0.0787 |
| deepinfra/fp8/priority | fp8 | yes | 76.8 | 138 | 5.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1117.5 | 0.0666 |
| venice | unknown | no | 76.8 | 138 | 3.50 | 1.00 | 95.8 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1418.5 | 0.0683 |
| alibaba/fp8 | fp8 | yes | 76.1 | 138 | 7 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2723.5 | 0.1241 |
| atlas-cloud/fp4 | fp4 | yes | 76.1 | 138 | 4 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2504.5 | 0.1493 |
| deepinfra/fp8/flex | fp8 | yes | 76.1 | 138 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1894.0 | 0.0702 |
| relace/fp4 | fp4 | no | 75.4 | 138 | 4.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1152.0 | 0.0799 |
| siliconflow/fp8 | fp8 | no | 63.0 | 138 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2211.5 | 0.0868 |
| azure/us | unknown | no | 58.0 | 138 | 1.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1157.0 | 0.1748 |
| digitalocean | unknown | no | 55.1 | 138 | 0.50 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2053.5 | 0.0952 |
| novita/fp8 | fp8 | yes | 43.5 | 138 | 1.00 | 1.00 | 97.9 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2297.5 | 0.1029 |
| gmicloud/fp8 | fp8 | yes | 42.0 | 138 | 1.00 | 1.00 | 97.9 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2572.5 | 0.0862 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, deepinfra/fp8/flex, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 6.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fast | unknown | no | 89.8 | 118 | 0.00 | 1.00 | 67.6 | 100.0 | 42.1 | 100.0 | 100.0 | 18.1 | 0 | 0 | 311.0 | 0.0474 |
| cohere/fp8 | fp8 | yes | 88.1 | 143 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 370.0 | 0.0136 |
| siliconflow/fp8 | fp8 | no | 87.4 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1714.0 | 0.0251 |
| morph/fast | fp8 | yes | 87.1 | 124 | 0.00 | 1.00 | 69.2 | 100.0 | 47.8 | 100.0 | 100.0 | 13.2 | 0 | 0 | 604.0 | 0.0496 |
| dekallm | unknown | yes | 86.7 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1416.5 | 0.0165 |
| cloudflare | unknown | yes | 86.0 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1569.0 | 0.0087 |
| coreweave/fp8 | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 535.0 | 0.0275 |
| deepinfra/fp8 | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 659.5 | 0.0086 |
| fireworks/us | unknown | no | 86.0 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 447.0 | 0.0410 |
| particle-ai/us/flex | unknown | yes | 86.0 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 900.5 | 0.0033 |
| together | unknown | no | 86.0 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 95.8 | 100.0 | 0.00 | 0 | 0 | 412.5 | 0.0276 |
| primalabs | unknown | yes | 85.7 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 2.10 | 0 | 0 | 626.0 | 0.0212 |
| baseten | unknown | no | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 710.5 | 0.0280 |
| inference-net/us | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 482.0 | 0.0083 |
| relace/fp4 | fp4 | no | 85.3 | 143 | 0 | 1.00 | 66.7 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 973.0 | 0.0109 |
| stepfun/fp8 | fp8 | no | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 740.0 | 0.0097 |
| streamlake/fp8 | fp8 | no | 85.3 | 143 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1451.0 | 0.0103 |
| wafer/mxfp4 | mxfp4 | yes | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 437.5 | 0.0035 |
| fireworks | unknown | no | 84.6 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 764.5 | 0.0202 |
| gmicloud/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 891.0 | 0.0167 |
| makora/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 72.9 | 95.8 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 519.5 | 0.0150 |
| mistral/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 721.5 | 0.0281 |
| modal | unknown | no | 84.6 | 143 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 594.0 | 0.0231 |
| nebius/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 647.0 | 0.0282 |
| parasail/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 430.5 | 0.0278 |
| particle-ai/us | unknown | yes | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 917.5 | 0.0059 |
| sail-research/fp4/us | fp4 | yes | 84.6 | 13 | 0.00 | 1.00 | 60.0 | 100.0 | 50.0 | 100.0 | 100.0 | 91.0 | 0 | 0 | 755.0 | 0.0001 |
| wafer/us | mxfp4 | yes | 84.6 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 372.0 | 0.0047 |
| alibaba | unknown | yes | 83.9 | 143 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 794.5 | 0.0082 |
| crusoe/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 628.5 | 0.0268 |
| fireworks/spot | unknown | no | 83.9 | 124 | 0.00 | 1.00 | 75.0 | 100.0 | 55.0 | 100.0 | 100.0 | 13.9 | 0 | 0 | 993.0 | 0.0161 |
| novita/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1161.5 | 0.0045 |
| atlas-cloud/fp8 | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1176.5 | 0.0047 |
| morph/fp8 | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 570.5 | 0.0068 |
| primeintellect | unknown | no | 83.2 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 588.0 | 0.0060 |
| venice/fp8 | fp8 | no | 82.5 | 143 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 866.5 | 0.0271 |
| deepinfra/fp8/priority | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 712.0 | 0.0034 |
| inference-net/fp8 | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 485.0 | 0.0069 |
| river | unknown | yes | 81.8 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 768.5 | 0.0080 |
| digitalocean | unknown | no | 80.4 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 648.5 | 0.0165 |
| ionstream | unknown | yes | 78.3 | 143 | 0 | 1.00 | 66.7 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 653.0 | 0.0186 |
| sail-research/fp4 | fp4 | yes | 76.9 | 13 | 0 | 1.00 | 60.0 | 100.0 | 50.0 | 100.0 | 100.0 | 91.0 | 0 | 0 | 811.0 | 0.0004 |
| ionstream/flex | unknown | yes | 75.4 | 142 | 0 | 1.00 | 79.2 | 100.0 | 47.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 715.0 | 0.0070 |
| baidu/fp8 | fp8 | no | 74.1 | 143 | 0 | 1.00 | 77.1 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 832.5 | 0.0069 |
| near-ai | unknown | no | 74.1 | 143 | 0 | 1.00 | 54.2 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1154.0 | 0.0272 |
| open-inference/fp4 | fp4 | yes | 70.6 | 143 | 0.00 | 1.00 | 52.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 898.5 | 0.0107 |
| deepinfra/fp8/flex | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, primeintellect, sail-research/fp4, particle-ai/us, sail-research/fp4/us, open-inference/fp4, baidu/fp8, morph/fp8, ionstream/flex, deepinfra/fp8/flex, wafer/mxfp4, inference-net/us, inference-net/fp8, river, alibaba, deepinfra/fp8, cloudflare, stepfun/fp8, streamlake/fp8, novita/fp8, relace/fp4, deepinfra/fp8/priority, cohere/fp8, deepseek, makora/fp8, dekallm, digitalocean, gmicloud/fp8, atlas-cloud/fp8, ionstream, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, nebius/fp8, mistral/fp8, coreweave/fp8, near-ai, venice/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 1.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 136 | n/a | 1.00 | 100.0 | 62.5 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 14 | 3889.0 | 0.1079 |
| mistral/zdr | unknown | yes | 100.0 | 136 | n/a | 1.00 | 100.0 | 50.0 | 79.2 | 100.0 | 87.5 | 0.00 | 0 | 17 | 4248.0 | 0.1191 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 8.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dekallm | unknown | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 844.0 | 0.0106 |
| kt | unknown | no | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 676.0 | 0.0144 |
| parasail/fast | fp4 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 462.5 | 0.0182 |
| deepinfra/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 633.5 | 0.0144 |
| gmicloud/fp8 | fp8 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2400.5 | 0.0072 |
| particle-ai/nvfp4/flex | nvfp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 579.0 | 0.0063 |
| river | unknown | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 900.5 | 0.0092 |
| cohere/nvfp4 | nvfp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 437.0 | 0.0151 |
| darkbloom/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2053.5 | 0.0061 |
| digitalocean | unknown | no | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 710.5 | 0.0108 |
| coreweave/nvfp4 | nvfp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 598.0 | 0.0114 |
| morph/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 9478.0 | 0.0048 |
| nebius/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1163.0 | 0.0145 |
| nextbit/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 87.0 | 100.0 | 100.0 | 2.10 | 0 | 0 | 778.0 | 0.0113 |
| open-inference/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1777.0 | 0.0065 |
| particle-ai/nvfp4 | nvfp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 566.5 | 0.0062 |
| streamlake/fp8 | fp8 | no | 97.2 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1790.5 | 0.0085 |
| venice | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1139.5 | 0.0152 |
| near-ai/fp8 | fp8 | yes | 97.1 | 137 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 4.90 | 0 | 0 | 2515.0 | 0.0083 |
| inceptron/fp8 | fp8 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 582.5 | 0.0164 |
| mistral | unknown | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 731.0 | 0.0144 |
| parasail/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 604.5 | 0.0144 |
| relace/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 931.5 | 0.0036 |
| sail-research/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1110.5 | 0.0164 |
| sail-research/us | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1096.0 | 0.0171 |
| together | unknown | no | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 471.5 | 0.0146 |
| atlas-cloud/fp8 | fp8 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1935.0 | 0.0150 |
| tenstorrent/fp8 | fp8 | yes | 95.4 | 65 | 0 | 1.00 | 100.0 | 100.0 | 80.0 | 100.0 | 100.0 | 54.9 | 0 | 0 | 1051.0 | 0.0034 |
| baseten/fp8 | fp8 | no | 95.1 | 144 | 0 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 530.0 | 0.0145 |
| friendli | unknown | yes | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 353.0 | 0.0145 |
| fireworks | unknown | no | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 869.0 | 0.0146 |
| fireworks/us | unknown | no | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 506.5 | 0.0218 |
| novita/fp8 | fp8 | yes | 93.8 | 144 | 0 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1260.5 | 0.0081 |
| crusoe/fp4 | fp4 | yes | 93.1 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 847.5 | 0.0144 |
| siliconflow/fp8 | fp8 | no | 93.1 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1257.0 | 0.0099 |
| makora/fp4 | fp4 | yes | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 549.5 | 0.0125 |
| z-ai/fp8 | fp8 | no | 91.7 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1411.0 | 0.0143 |
| inference-net/fp4 | fp4 | yes | 91.0 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 390.5 | 0.0083 |
| inference-net/us | fp4 | yes | 89.6 | 144 | 0 | 1.00 | 97.9 | 95.8 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 389.5 | 0.0104 |
| modal/fp4 | fp4 | no | 88.9 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 411.5 | 0.0147 |
| reka | unknown | yes | 86.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 551.0 | 0.0110 |
| wafer/nvfp4 | nvfp4 | yes | 81.9 | 144 | 0.00 | 1.00 | 89.6 | 100.0 | 79.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 488.5 | 0.0065 |
| wafer/us | nvfp4 | yes | 80.6 | 144 | 0.00 | 1.00 | 87.5 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 501.5 | 0.0043 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, wafer/us, morph/fp8, particle-ai/nvfp4/flex, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, tenstorrent/fp8, gmicloud/fp8, near-ai/fp8, novita/fp8, streamlake/fp8, river, siliconflow/fp8, dekallm, inference-net/us, inference-net/fp4, digitalocean, reka, coreweave/nvfp4, nextbit/fp4, particle-ai/nvfp4, makora/fp4, mistral, kt, cohere/nvfp4, nebius/fp4, modal/fp4, crusoe/fp4, atlas-cloud/fp8, fireworks, friendli, together, parasail/fp4, baseten/fp8, venice, deepinfra/fp4, z-ai/fp8, inceptron/fp8, sail-research/us, sail-research/fp4, parasail/fast, fireworks/us. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 100.0 | 34 | n/a | 1.00 | 50.0 | 100.0 | 37.5 | 100.0 | 85.7 | 76.4 | 0 | 0 | 759.0 | 0.0018 |
| novita/bf16 | bf16 | yes | 100.0 | 19 | n/a | 1.00 | 50.0 | 100.0 | 66.7 | 100.0 | 100.0 | 86.8 | 0 | 0 | 1318.0 | 0.0008 |
| sambanova | unknown | no | 83.7 | 49 | 0.00 | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1448.0 | 0.0339 |
| friendli | unknown | yes | 81.6 | 49 | 0 | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 366.5 | 0.0125 |
| siliconflow/fp8 | fp8 | no | 79.6 | 49 | 0.00 | 1.00 | 41.7 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1310.5 | 0.0613 |
| parasail/fp8 | fp8 | yes | 77.6 | 49 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 793.5 | 0.0132 |
| deepinfra/fp8/priority | fp8 | yes | 75.5 | 49 | 0.00 | 1.00 | 37.5 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 590.0 | 0.0256 |
| venice/fp4 | fp4 | no | 75.5 | 49 | 0.00 | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 95.7 | 0.70 | 0 | 0 | 1004.0 | 0.0106 |
| coreweave/fp4 | fp4 | yes | 73.5 | 49 | 0 | 1.00 | 43.8 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 578.0 | 0.0092 |
| deepinfra/fp8/flex | fp8 | yes | 73.5 | 49 | 0 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1726.0 | 0.0137 |
| primeintellect/fp8 | fp8 | yes | 73.5 | 49 | 0 | 1.00 | 41.7 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1285.5 | 0.0079 |
| chutes/fp4 | fp4 | yes | 69.4 | 49 | 0 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2633.5 | 0.0107 |
| deepinfra/fp8 | fp8 | yes | 69.4 | 49 | 0 | 1.00 | 35.4 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 597.0 | 0.0171 |
| deepinfra/turbo | fp4 | yes | 69.4 | 49 | 0 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 490.0 | 0.0103 |
| modal | unknown | no | 65.3 | 49 | 0 | 1.00 | 38.3 | 100.0 | 58.3 | 100.0 | 95.8 | 0.70 | 0 | 0 | 305.0 | 0.0264 |
| kt | unknown | no | 59.2 | 49 | 0.00 | 1.00 | 33.3 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 606.0 | 0.0092 |
| nextbit/fp4 | fp4 | yes | 59.2 | 49 | 0.00 | 1.00 | 33.3 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 859.5 | 0.0131 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: crusoe/bf16, novita/bf16. Prompts with no plurality (excluded from exact match): 0.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| streamlake | unknown | no | 97.1 | 138 | 0.00 | 1.00 | 72.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1470.5 | 0.0421 |
| xiaomi/fp8 | fp8 | no | 94.9 | 138 | 0 | 1.00 | 75.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2074.0 | 0.0341 |
| gmicloud/bf16 | bf16 | yes | 94.2 | 138 | 0.00 | 1.00 | 79.2 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2099.0 | 0.0283 |
| primalabs/fp8 | fp8 | yes | 92.8 | 138 | 0.00 | 1.00 | 72.9 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 656.5 | 0.3522 |
| deepinfra/fp8 | fp8 | yes | 89.9 | 138 | 0.00 | 1.00 | 77.1 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1417.0 | 0.0343 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: gmicloud/bf16, deepinfra/fp8, xiaomi/fp8, streamlake, primalabs/fp8. Prompts with no plurality (excluded from exact match): 6.

## Footer

- Rows: 22176; errors 966; misrouted 0; truncated (finish_reason length) 63; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $7.4555; billed: $3.9494; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
