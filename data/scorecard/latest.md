# Bitdepth scorecard 2026-11-06

Run `2026-11-06-live`, source `live`, started 2026-11-06T15:07:13Z, finished 2026-11-06T19:31:57Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 332.0 | 0.0368 |
| deepinfra/bf16 | bf16 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2485.5 | 0.0048 |
| baseten/fp4 | fp4 | no | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 548.5 | 0.0128 |
| deepinfra/fp8 | fp8 | yes | 98.5 | 137 | 0.00 | 1.00 | 100.0 | 100.0 | 87.0 | 100.0 | 100.0 | 4.90 | 0 | 1 | 1516.0 | 0.0241 |
| sambanova | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 418.5 | 0.0201 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 905.5 | 0.0179 |
| baseten/fp4/us | fp4 | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 557.5 | 0.0128 |
| siliconflow/fp8 | fp8 | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2128.5 | 0.0243 |
| together | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 771.0 | 0.0180 |
| amazon-bedrock | unknown | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 945.0 | 0.0180 |
| crusoe/bf16 | bf16 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 419.5 | 0.0065 |
| groq | unknown | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 343.5 | 0.0180 |
| near-ai/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1050.0 | 0.0037 |
| sail-research/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 856.0 | 0.0084 |
| google-vertex/global | unknown | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2019.0 | 0.0108 |
| nebius/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 546.5 | 0.0176 |
| coreweave/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 550.0 | 0.0041 |
| mancer/fp8 | fp8 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 911.0 | 0.0067 |
| parasail/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 583.5 | 0.0144 |
| primeintellect/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 862.0 | 0.0028 |
| akashml/fp4 | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 805.5 | 0.0042 |
| dekallm/bf16 | bf16 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1605.5 | 0.0041 |
| parasail/fast | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 2 | 446.0 | 0.0197 |
| phala | unknown | yes | 93.7 | 142 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 1.40 | 0 | 4 | 1218.0 | 0.0239 |
| digitalocean | unknown | no | 91.7 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2014.5 | 0.0087 |
| venice/int4 | int4 | no | 81.2 | 144 | 0 | 1.00 | 77.1 | 100.0 | 62.5 | 100.0 | 87.5 | 0.00 | 0 | 15 | 1907.0 | 0.0050 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 92.5 | 133 | 4.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2224.5 | 0.1327 |
| alibaba/fp8 | fp8 | yes | 91.7 | 133 | 7 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2440.0 | 0.1299 |
| deepinfra/fp8 | fp8 | yes | 83.7 | 86 | 8.50 | 1.00 | 100.0 | 100.0 | 56.2 | 100.0 | 100.0 | 34.7 | 0 | 0 | 1568.5 | 0.0824 |
| baidu/fp8 | fp8 | no | 80.5 | 133 | 4.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1487.5 | 0.0765 |
| relace/fp4 | fp4 | no | 77.4 | 133 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1191.5 | 0.0800 |
| venice | unknown | no | 75.2 | 133 | 7 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2079.5 | 0.0993 |
| atlas-cloud/fp4 | fp4 | yes | 74.4 | 133 | 4.00 | 1.00 | 100.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2375.0 | 0.1529 |
| nebius/fp8 | fp8 | yes | 72.9 | 133 | 6.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1756.0 | 0.1596 |
| streamlake/fp8 | fp8 | no | 72.2 | 133 | 8 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2391.5 | 0.0320 |
| siliconflow/fp8 | fp8 | no | 69.2 | 133 | 3 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2069.0 | 0.0869 |
| azure/us | unknown | no | 56.4 | 133 | 1.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1401.5 | 0.1750 |
| digitalocean | unknown | no | 56.4 | 133 | 1.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1990.0 | 0.0957 |
| novita/fp8 | fp8 | yes | 43.6 | 133 | 1 | 1.00 | 93.8 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1836.0 | 0.0860 |
| gmicloud/fp8 | fp8 | yes | 42.9 | 133 | 0.50 | 1.00 | 97.9 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2411.5 | 0.0863 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, nebius/fp8, azure/us. Prompts with no plurality (excluded from exact match): 11.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wafer/us | mxfp4 | yes | 89.9 | 139 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 326.0 | 0.0048 |
| makora/fp8 | fp8 | yes | 88.5 | 139 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 474.0 | 0.0162 |
| wafer/mxfp4 | mxfp4 | yes | 88.5 | 139 | 0.00 | 1.00 | 85.4 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 365.5 | 0.0037 |
| baseten/fast | unknown | no | 88.2 | 76 | 0 | 1.00 | 75.0 | 100.0 | 54.5 | 100.0 | 100.0 | 46.5 | 0 | 0 | 368.0 | 0.0271 |
| morph/fp8 | fp8 | yes | 87.8 | 139 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 749.0 | 0.0028 |
| decart/fp8 | fp8 | yes | 87.1 | 139 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1143.5 | 0.0113 |
| particle-ai/us/flex | unknown | yes | 87.1 | 139 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 726.5 | 0.0028 |
| primeintellect | unknown | no | 87.1 | 139 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 660.5 | 0.0133 |
| relace/fast | fp4 | no | 87.1 | 139 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 780.0 | 0.0267 |
| relace/fp4 | fp4 | no | 87.1 | 139 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 848.5 | 0.0023 |
| stepfun/fp8 | fp8 | no | 87.1 | 139 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 774.5 | 0.0126 |
| venice/fp8 | fp8 | no | 87.1 | 139 | 0.00 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1236.5 | 0.0280 |
| atlas-cloud/fp8 | fp8 | yes | 86.3 | 139 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1218.5 | 0.0045 |
| cloudflare | unknown | yes | 86.3 | 139 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1294.5 | 0.0096 |
| cohere | unknown | yes | 86.3 | 139 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 391.0 | 0.0177 |
| coreweave/fp8 | fp8 | yes | 86.3 | 139 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 472.0 | 0.0277 |
| deepinfra/fp8/flex | fp8 | yes | 86.3 | 139 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2014.0 | 0.0044 |
| fireworks | unknown | no | 86.3 | 139 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1058.0 | 0.0279 |
| modal | unknown | no | 86.3 | 139 | 0 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 626.0 | 0.0233 |
| baseten | unknown | no | 85.6 | 139 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 453.0 | 0.0274 |
| deepinfra/fp8/priority | fp8 | yes | 84.9 | 139 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 600.5 | 0.0034 |
| dekallm | unknown | yes | 84.9 | 139 | 0 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1236.5 | 0.0169 |
| modelrun/fp4 | fp4 | no | 84.9 | 139 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 833.5 | 0.0158 |
| parasail/fp8 | fp8 | yes | 84.9 | 139 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 387.0 | 0.0276 |
| together | unknown | no | 84.9 | 139 | 0 | 1.00 | 81.2 | 100.0 | 50.0 | 79.2 | 100.0 | 0.00 | 0 | 0 | 334.5 | 0.0277 |
| primalabs | unknown | yes | 84.7 | 131 | 0.00 | 1.00 | 78.3 | 100.0 | 50.0 | 100.0 | 100.0 | 5.60 | 0 | 0 | 714.0 | 0.0828 |
| deepinfra/fp8 | fp8 | yes | 84.2 | 139 | 0.00 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 625.5 | 0.0057 |
| fireworks/us | unknown | no | 84.2 | 139 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 536.0 | 0.0417 |
| mistral/fp8 | fp8 | yes | 84.2 | 139 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 930.0 | 0.0274 |
| particle-ai/us | unknown | yes | 84.2 | 139 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 668.0 | 0.0040 |
| phala | unknown | yes | 84.2 | 139 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1617.0 | 0.0065 |
| alibaba | unknown | yes | 83.5 | 139 | 0 | 1.00 | 83.3 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 856.0 | 0.0070 |
| crusoe/fp8 | fp8 | yes | 83.5 | 139 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 643.0 | 0.0274 |
| siliconflow/fp8 | fp8 | no | 83.5 | 139 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 907.0 | 0.0253 |
| inference-net/fp8 | fp8 | yes | 82.7 | 139 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 483.0 | 0.0034 |
| gmicloud/fp8 | fp8 | yes | 82.0 | 139 | 0 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 926.0 | 0.0168 |
| nebius/fp8 | fp8 | yes | 82.0 | 139 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1090.0 | 0.0278 |
| novita/fp8 | fp8 | yes | 82.0 | 139 | 0 | 1.00 | 81.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1487.0 | 0.0153 |
| inference-net/us | fp8 | yes | 79.1 | 139 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 448.0 | 0.0082 |
| baidu/fp8 | fp8 | no | 77.7 | 139 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 739.0 | 0.0140 |
| ionstream | unknown | yes | 77.7 | 139 | 0 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 539.5 | 0.0148 |
| streamlake/fp8 | fp8 | no | 76.3 | 139 | 0 | 1.00 | 79.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1047.5 | 0.0103 |
| near-ai | unknown | no | 74.1 | 139 | 0.00 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 958.5 | 0.0276 |
| reka | unknown | no | 74.1 | 139 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 758.0 | 0.0169 |
| digitalocean | unknown | no | 73.4 | 139 | 0 | 1.00 | 56.2 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 762.5 | 0.0166 |
| open-inference/fp4 | fp4 | yes | 71.2 | 139 | 0.00 | 1.00 | 62.5 | 100.0 | 50.0 | 95.8 | 100.0 | 0.00 | 0 | 0 | 2120.5 | 0.0029 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| fireworks/spot | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, open-inference/fp4, morph/fp8, particle-ai/us/flex, wafer/us, particle-ai/us, alibaba, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, deepinfra/fp8, cloudflare, sail-research/fp4/us, primeintellect, streamlake/fp8, decart/fp8, stepfun/fp8, deepinfra/fp8/priority, baidu/fp8, deepseek, makora/fp8, sail-research/fp4, wafer/mxfp4, reka, ionstream, novita/fp8, modelrun/fp4, dekallm, digitalocean, gmicloud/fp8, cohere, atlas-cloud/fp8, phala, fireworks/spot, modal, crusoe/fp8, siliconflow/fp8, relace/fast, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast, primalabs. Prompts with no plurality (excluded from exact match): 5.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 125 | n/a | 1.00 | 97.9 | 50.0 | 75.0 | 100.0 | 91.7 | 0.00 | 0 | 18 | 3873.0 | 0.1072 |
| mistral/zdr | unknown | yes | 100.0 | 125 | n/a | 1.00 | 100.0 | 50.0 | 66.7 | 100.0 | 87.5 | 0.00 | 0 | 18 | 3906.0 | 0.1264 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 19.

## Footer

- Rows: 13248; errors 711; misrouted 0; truncated (finish_reason length) 67; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $5.3103; billed: $2.8449; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
