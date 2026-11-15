# Bitdepth scorecard 2026-11-15

Run `2026-11-15-live`, source `live`, started 2026-11-15T14:48:28Z, finished 2026-11-15T15:28:12Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 99.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 218.5 | 0.0372 |
| baseten/fp4 | fp4 | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 344.0 | 0.0126 |
| sail-research/fp4 | fp4 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 957.0 | 0.0085 |
| together | unknown | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 703.5 | 0.0178 |
| deepinfra/bf16 | bf16 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2514.0 | 0.0047 |
| deepinfra/fp8 | fp8 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1395.0 | 0.0249 |
| near-ai/fp4 | fp4 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1067.5 | 0.0037 |
| sambanova | unknown | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 450.0 | 0.0198 |
| crusoe/bf16 | bf16 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 464.5 | 0.0064 |
| groq | unknown | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 265.5 | 0.0180 |
| parasail/fast | fp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 469.5 | 0.0193 |
| baseten/fp4/us | fp4 | no | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 362.5 | 0.0127 |
| dekallm/bf16 | bf16 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1412.5 | 0.0041 |
| mancer/fp8 | fp8 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 758.5 | 0.0080 |
| siliconflow/fp8 | fp8 | no | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2139.5 | 0.0254 |
| akashml/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 588.0 | 0.0042 |
| amazon-bedrock | unknown | no | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 508.0 | 0.0178 |
| amazon-bedrock/eu-west-1 | unknown | no | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 482.0 | 0.0178 |
| nebius/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 412.5 | 0.0174 |
| parasail/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 497.0 | 0.0147 |
| google-vertex/global | unknown | yes | 95.1 | 142 | 0 | 1.00 | 93.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 377.5 | 0.0108 |
| primeintellect/fp4 | fp4 | yes | 94.4 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 940.0 | 0.0037 |
| coreweave/fp4 | fp4 | yes | 93.7 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 551.5 | 0.0041 |
| io-net/fp4 | fp4 | no | 93.7 | 142 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1047.0 | 0.0235 |
| digitalocean | unknown | no | 92.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1214.5 | 0.0084 |
| venice/int4 | int4 | no | 81.0 | 142 | 0 | 1.00 | 77.1 | 100.0 | 75.0 | 100.0 | 87.5 | 0.00 | 0 | 12 | 1535.5 | 0.0046 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 2.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8/flex | fp8 | yes | 85.8 | 134 | 5 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1891.0 | 0.0646 |
| streamlake/fp8 | fp8 | no | 82.8 | 134 | 1 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2318.0 | 0.0079 |
| alibaba/fp8 | fp8 | yes | 79.1 | 134 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 3101.5 | 0.1274 |
| baidu/fp8 | fp8 | no | 79.1 | 134 | 2.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1665.0 | 0.0188 |
| deepinfra/fp8 | fp8 | yes | 79.1 | 134 | 4.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1319.5 | 0.0869 |
| deepinfra/fp8/priority | fp8 | yes | 78.4 | 134 | 3 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1376.5 | 0.0656 |
| venice | unknown | no | 76.9 | 134 | 1 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1750.0 | 0.0681 |
| relace/fp4 | fp4 | no | 74.6 | 134 | 4.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1035.0 | 0.0795 |
| atlas-cloud/fp4 | fp4 | yes | 73.9 | 134 | 1 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2678.5 | 0.1484 |
| alibaba/fp8/us-east-1 | fp8 | yes | 73.1 | 134 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2702.5 | 0.1409 |
| siliconflow/fp8 | fp8 | no | 63.4 | 134 | 3 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2158.0 | 0.0865 |
| digitalocean | unknown | no | 58.2 | 134 | 0.00 | 1.00 | 95.8 | 100.0 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1454.0 | 0.0947 |
| azure/us | unknown | no | 56.7 | 134 | 0.50 | 1.00 | 100.0 | 100.0 | 41.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1109.5 | 0.1740 |
| novita/fp8 | fp8 | yes | 46.3 | 134 | 1.00 | 1.00 | 95.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2268.5 | 0.1272 |
| gmicloud/fp8 | fp8 | yes | 44.0 | 134 | 1 | 1.00 | 100.0 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2573.0 | 0.0838 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, deepinfra/fp8/flex, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 10.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| modal | unknown | no | 90.1 | 141 | 0.00 | 1.00 | 85.4 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 533.0 | 0.0229 |
| baseten/fast | unknown | no | 89.3 | 131 | 0.00 | 1.00 | 70.5 | 100.0 | 47.6 | 100.0 | 100.0 | 6.90 | 0 | 0 | 296.0 | 0.0507 |
| cloudflare | unknown | yes | 88.7 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1366.5 | 0.0097 |
| cohere/fp8 | fp8 | yes | 88.7 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 375.5 | 0.0134 |
| fireworks/spot | unknown | no | 88.7 | 141 | 0.00 | 1.00 | 85.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1938.5 | 0.0194 |
| inference-net/fp8 | fp8 | yes | 88.7 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 409.0 | 0.0066 |
| sail-research/fp4 | fp4 | yes | 88.7 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1441.5 | 0.0020 |
| sail-research/fp4/us | fp4 | yes | 88.7 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1352.5 | 0.0032 |
| streamlake/fp8 | fp8 | no | 88.7 | 141 | 0.00 | 1.00 | 83.3 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1449.5 | 0.0101 |
| atlas-cloud/fp8 | fp8 | yes | 87.9 | 141 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1216.5 | 0.0043 |
| mistral/fp8 | fp8 | yes | 87.9 | 141 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 643.0 | 0.0278 |
| novita/fp8 | fp8 | yes | 87.9 | 141 | 0 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1176.0 | 0.0039 |
| venice/fp8 | fp8 | no | 87.9 | 141 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 958.5 | 0.0276 |
| baseten | unknown | no | 87.2 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 630.5 | 0.0288 |
| deepinfra/fp8/priority | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 550.5 | 0.0034 |
| fireworks | unknown | no | 87.2 | 141 | 0.00 | 1.00 | 85.4 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2094.0 | 0.0077 |
| morph/fp8 | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 457.5 | 0.0070 |
| nebius/fp8 | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1375.0 | 0.0278 |
| stepfun/fp8 | fp8 | no | 87.2 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 572.0 | 0.0098 |
| wafer/us | mxfp4 | yes | 87.2 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 371.0 | 0.0048 |
| particle-ai/us/flex | unknown | yes | 86.5 | 141 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 666.0 | 0.0032 |
| crusoe/fp8 | fp8 | yes | 85.8 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 586.0 | 0.0269 |
| inference-net/us | fp8 | yes | 85.8 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 416.0 | 0.0081 |
| particle-ai/us | unknown | yes | 85.8 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 686.5 | 0.0041 |
| primeintellect | unknown | no | 85.8 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 653.0 | 0.0060 |
| together | unknown | no | 85.8 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 324.5 | 0.0275 |
| makora/fp8 | fp8 | yes | 85.1 | 141 | 0 | 1.00 | 85.4 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 421.0 | 0.0166 |
| siliconflow/fp8 | fp8 | no | 85.1 | 141 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 944.5 | 0.0250 |
| primalabs | unknown | yes | 85.0 | 140 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 495.0 | 0.0121 |
| deepinfra/fp8/flex | fp8 | yes | 84.4 | 141 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1823.0 | 0.0028 |
| gmicloud/fp8 | fp8 | yes | 84.4 | 141 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 763.5 | 0.0167 |
| relace/fp4 | fp4 | no | 84.4 | 141 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 690.0 | 0.0109 |
| wafer/mxfp4 | mxfp4 | yes | 84.4 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 360.5 | 0.0033 |
| alibaba | unknown | yes | 83.7 | 141 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 792.5 | 0.0096 |
| coreweave/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 491.5 | 0.0278 |
| deepinfra/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 524.0 | 0.0074 |
| fireworks/us | unknown | no | 83.0 | 141 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 405.5 | 0.0387 |
| dekallm | unknown | yes | 82.3 | 141 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 806.0 | 0.0164 |
| parasail/fp8 | fp8 | yes | 81.6 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 300.5 | 0.0275 |
| ionstream | unknown | yes | 79.4 | 141 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 489.0 | 0.0184 |
| river | unknown | yes | 78.7 | 141 | 0.00 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 670.5 | 0.0099 |
| digitalocean | unknown | no | 77.3 | 141 | 0.00 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 595.5 | 0.0164 |
| reka | unknown | no | 77.3 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 615.5 | 0.0165 |
| baidu/fp8 | fp8 | no | 76.6 | 141 | 0 | 1.00 | 79.2 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 731.0 | 0.0083 |
| ionstream/flex | unknown | yes | 74.5 | 141 | 0.00 | 1.00 | 87.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 531.5 | 0.0070 |
| near-ai | unknown | no | 74.5 | 141 | 0.00 | 1.00 | 66.7 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 854.5 | 0.0275 |
| open-inference/fp4 | fp4 | yes | 70.2 | 141 | 0.00 | 1.00 | 54.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1506.0 | 0.0087 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: sail-research/fp4, particle-ai/us/flex, wafer/us, primeintellect, particle-ai/us, wafer/mxfp4, open-inference/fp4, morph/fp8, sail-research/fp4/us, ionstream/flex, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, baidu/fp8, deepinfra/fp8, cloudflare, stepfun/fp8, alibaba, river, streamlake/fp8, relace/fp4, deepinfra/fp8/priority, cohere/fp8, deepseek, makora/fp8, reka, novita/fp8, dekallm, digitalocean, gmicloud/fp8, atlas-cloud/fp8, ionstream, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, mistral/fp8, coreweave/fp8, near-ai, venice/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast. Prompts with no plurality (excluded from exact match): 3.

## Footer

- Rows: 12816; errors 155; misrouted 0; truncated (finish_reason length) 28; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.8026; billed: $2.4186; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
