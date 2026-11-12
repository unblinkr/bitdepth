# Bitdepth scorecard 2026-11-12

Run `2026-11-12-live`, source `live`, started 2026-11-12T16:00:55Z, finished 2026-11-12T19:21:28Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4/us | fp4 | no | 99.3 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 508.5 | 0.0126 |
| dekallm/bf16 | bf16 | yes | 99.3 | 141 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 95.8 | 100.0 | 0.00 | 0 | 0 | 1432.0 | 0.0042 |
| io-net/fp4 | fp4 | no | 99.2 | 133 | 0 | 1.00 | 100.0 | 100.0 | 81.8 | 100.0 | 100.0 | 5.60 | 0 | 1 | 2676.5 | 0.0036 |
| deepinfra/bf16 | bf16 | yes | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 95.8 | 100.0 | 0.00 | 0 | 1 | 1623.5 | 0.0047 |
| groq | unknown | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 352.0 | 0.0182 |
| near-ai/fp4 | fp4 | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1768.5 | 0.0038 |
| sail-research/fp4 | fp4 | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 95.8 | 100.0 | 0.00 | 0 | 1 | 1081.0 | 0.0083 |
| google-vertex/global | unknown | yes | 97.8 | 134 | 0 | 1.00 | 100.0 | 95.8 | 78.3 | 100.0 | 100.0 | 5.60 | 0 | 1 | 680.5 | 0.0104 |
| coreweave/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 639.5 | 0.0041 |
| mancer/fp8 | fp8 | yes | 97.2 | 141 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 779.5 | 0.0069 |
| parasail/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 694.5 | 0.0149 |
| sambanova | unknown | no | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 95.8 | 100.0 | 0.00 | 0 | 1 | 521.5 | 0.0201 |
| together | unknown | no | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 553.5 | 0.0184 |
| nebius/fp4 | fp4 | yes | 97.1 | 140 | 0.00 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.70 | 0 | 1 | 470.0 | 0.0172 |
| deepinfra/fp8 | fp8 | yes | 96.9 | 127 | 0.00 | 1.00 | 100.0 | 100.0 | 78.3 | 100.0 | 100.0 | 10.4 | 0 | 1 | 1557.0 | 0.0230 |
| akashml/fp4 | fp4 | yes | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 95.8 | 100.0 | 0.00 | 0 | 0 | 1042.5 | 0.0042 |
| cerebras/fp16 | fp16 | yes | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 259.0 | 0.0366 |
| crusoe/bf16 | bf16 | yes | 96.5 | 141 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 664.5 | 0.0066 |
| baseten/fp4 | fp4 | no | 95.7 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 478.5 | 0.0129 |
| siliconflow/fp8 | fp8 | no | 95.7 | 141 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2116.0 | 0.0256 |
| amazon-bedrock | unknown | no | 95.0 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 648.0 | 0.0180 |
| parasail/fast | fp4 | yes | 95.0 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 95.8 | 100.0 | 0.00 | 0 | 0 | 508.0 | 0.0197 |
| amazon-bedrock/eu-west-1 | unknown | no | 94.3 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 695.0 | 0.0180 |
| primeintellect/fp4 | fp4 | yes | 94.3 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 95.8 | 100.0 | 0.00 | 0 | 1 | 934.0 | 0.0065 |
| digitalocean | unknown | no | 90.8 | 141 | 0 | 1.00 | 100.0 | 100.0 | 95.8 | 95.8 | 100.0 | 0.00 | 0 | 0 | 1332.5 | 0.0084 |
| venice/int4 | int4 | no | 86.5 | 141 | 0 | 1.00 | 83.3 | 100.0 | 75.0 | 100.0 | 79.2 | 0.00 | 0 | 10 | 1628.5 | 0.0047 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 3.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 87.6 | 129 | 3.00 | 1.00 | 97.9 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2016.0 | 0.1401 |
| alibaba/fp8 | fp8 | yes | 86.0 | 129 | 8.00 | 1.00 | 97.9 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2349.0 | 0.1273 |
| streamlake/fp8 | fp8 | no | 79.8 | 129 | 7.50 | 1.00 | 97.9 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2387.0 | 0.0338 |
| relace/fp4 | fp4 | no | 77.5 | 129 | 1 | 1.00 | 97.9 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1066.0 | 0.0799 |
| venice | unknown | no | 75.2 | 129 | 1.00 | 1.00 | 97.9 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1529.0 | 0.0728 |
| deepinfra/fp8 | fp8 | yes | 74.4 | 129 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1369.5 | 0.1182 |
| atlas-cloud/fp4 | fp4 | yes | 72.1 | 129 | 1.00 | 1.00 | 97.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2659.0 | 0.1502 |
| siliconflow/fp8 | fp8 | no | 72.1 | 129 | 3.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2339.5 | 0.0870 |
| azure/us | unknown | no | 58.9 | 129 | 0 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1117.5 | 0.1741 |
| digitalocean | unknown | no | 54.3 | 129 | 1 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1300.5 | 0.0954 |
| novita/fp8 | fp8 | yes | 48.1 | 129 | 1 | 1.00 | 100.0 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2258.5 | 0.1283 |
| baidu/fp8 | fp8 | no | 46.5 | 129 | 0 | 1.00 | 97.9 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1720.0 | 0.0749 |
| gmicloud/fp8 | fp8 | yes | 45.7 | 129 | 0.50 | 1.00 | 100.0 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2564.0 | 0.0844 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, azure/us. Prompts with no plurality (excluded from exact match): 15.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| siliconflow/fp8 | fp8 | no | 88.6 | 140 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 809.5 | 0.0251 |
| modal | unknown | no | 87.9 | 140 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 643.5 | 0.0230 |
| wafer/us | mxfp4 | yes | 87.9 | 140 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 479.0 | 0.0049 |
| inference-net/fp8 | fp8 | yes | 87.1 | 140 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 430.5 | 0.0073 |
| inference-net/us | fp8 | yes | 87.1 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 472.5 | 0.0082 |
| morph/fp8 | fp8 | yes | 87.1 | 139 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 6751.0 | 0.0030 |
| particle-ai/us | unknown | yes | 87.1 | 140 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 794.0 | 0.0045 |
| relace/fp4 | fp4 | no | 87.1 | 140 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 550.5 | 0.0110 |
| streamlake/fp8 | fp8 | no | 87.1 | 140 | 0.00 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1493.0 | 0.0099 |
| venice/fp8 | fp8 | no | 87.1 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 824.0 | 0.0276 |
| baseten/fast | unknown | no | 87.0 | 131 | 0 | 1.00 | 63.0 | 100.0 | 47.8 | 100.0 | 100.0 | 6.20 | 0 | 0 | 266.0 | 0.0510 |
| alibaba | unknown | yes | 86.4 | 140 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 911.0 | 0.0096 |
| crusoe/fp8 | fp8 | yes | 86.4 | 140 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 580.0 | 0.0266 |
| novita/fp8 | fp8 | yes | 86.4 | 140 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1206.5 | 0.0039 |
| particle-ai/us/flex | unknown | yes | 86.4 | 140 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 731.0 | 0.0035 |
| baseten | unknown | no | 85.7 | 140 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 721.5 | 0.0275 |
| fireworks/us | unknown | no | 85.7 | 140 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 507.5 | 0.0412 |
| makora/fp8 | fp8 | yes | 85.7 | 140 | 0.00 | 1.00 | 70.8 | 95.8 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 386.0 | 0.0165 |
| parasail/fp8 | fp8 | yes | 85.7 | 140 | 0.00 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 422.0 | 0.0275 |
| atlas-cloud/fp8 | fp8 | yes | 85.0 | 140 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1233.0 | 0.0046 |
| deepinfra/fp8 | fp8 | yes | 85.0 | 140 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 544.0 | 0.0061 |
| fireworks | unknown | no | 85.0 | 140 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 723.0 | 0.0238 |
| mistral/fp8 | fp8 | yes | 85.0 | 140 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 697.0 | 0.0279 |
| sail-research/fp4 | fp4 | yes | 85.0 | 140 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 925.0 | 0.0123 |
| sail-research/fp4/us | fp4 | yes | 85.0 | 140 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 957.0 | 0.0150 |
| stepfun/fp8 | fp8 | no | 85.0 | 140 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 468.5 | 0.0098 |
| cloudflare | unknown | yes | 84.7 | 118 | 0.00 | 1.00 | 64.9 | 100.0 | 61.9 | 100.0 | 100.0 | 15.3 | 0 | 0 | 2129.0 | 0.0052 |
| cohere/fp8 | fp8 | yes | 84.3 | 140 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 399.5 | 0.0134 |
| dekallm | unknown | yes | 84.3 | 140 | 0.00 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1026.0 | 0.0165 |
| deepinfra/fp8/flex | fp8 | yes | 83.6 | 140 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1882.5 | 0.0047 |
| deepinfra/fp8/priority | fp8 | yes | 83.6 | 140 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 553.5 | 0.0035 |
| gmicloud/fp8 | fp8 | yes | 83.6 | 140 | 0 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 841.0 | 0.0166 |
| nebius/fp8 | fp8 | yes | 83.6 | 140 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1337.0 | 0.0282 |
| primalabs | unknown | yes | 83.1 | 136 | 0 | 1.00 | 73.9 | 100.0 | 50.0 | 100.0 | 100.0 | 2.80 | 0 | 0 | 627.0 | 0.0215 |
| coreweave/fp8 | fp8 | yes | 82.9 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 451.5 | 0.0279 |
| fireworks/spot | unknown | no | 82.9 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1251.5 | 0.0194 |
| wafer/mxfp4 | mxfp4 | yes | 82.9 | 140 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 525.5 | 0.0036 |
| river | unknown | yes | 82.1 | 140 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 780.0 | 0.0111 |
| together | unknown | no | 82.1 | 140 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 91.7 | 100.0 | 0.00 | 0 | 0 | 461.0 | 0.0276 |
| reka | unknown | no | 81.4 | 140 | 0.00 | 1.00 | 89.6 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 599.0 | 0.0175 |
| primeintellect | unknown | no | 80.7 | 140 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 730.5 | 0.0062 |
| ionstream | unknown | yes | 80.0 | 140 | 0.00 | 1.00 | 60.4 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 660.5 | 0.0145 |
| digitalocean | unknown | no | 79.3 | 140 | 0 | 1.00 | 54.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 432.0 | 0.0166 |
| baidu/fp8 | fp8 | no | 76.4 | 140 | 0 | 1.00 | 64.6 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1035.5 | 0.0138 |
| ionstream/flex | unknown | yes | 76.4 | 140 | 0 | 1.00 | 83.3 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1707.5 | 0.0070 |
| near-ai | unknown | no | 75.7 | 140 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1618.5 | 0.0277 |
| open-inference/fp4 | fp4 | yes | 75.0 | 140 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2082.5 | 0.0085 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: morph/fp8, particle-ai/us/flex, wafer/us, primeintellect, particle-ai/us, open-inference/fp4, ionstream/flex, deepinfra/fp8/flex, wafer/mxfp4, inference-net/us, inference-net/fp8, deepinfra/fp8, cloudflare, stepfun/fp8, alibaba, streamlake/fp8, river, relace/fp4, deepinfra/fp8/priority, baidu/fp8, cohere/fp8, deepseek, makora/fp8, reka, ionstream, novita/fp8, dekallm, digitalocean, gmicloud/fp8, sail-research/fp4/us, sail-research/fp4, atlas-cloud/fp8, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, mistral/fp8, coreweave/fp8, near-ai, venice/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast. Prompts with no plurality (excluded from exact match): 4.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 128 | n/a | 1.00 | 100.0 | 41.7 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 18 | 2876.5 | 0.1167 |
| mistral/zdr | unknown | yes | 100.0 | 128 | n/a | 1.00 | 97.9 | 62.5 | 83.3 | 100.0 | 87.5 | 0.00 | 0 | 14 | 3221.0 | 0.1145 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 16.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| particle-ai/nvfp4 | nvfp4 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1178.5 | 0.0128 |
| relace/fp4 | fp4 | yes | 99.2 | 120 | 0 | 1.00 | 100.0 | 100.0 | 95.2 | 100.0 | 100.0 | 16.7 | 0 | 0 | 3928.0 | 0.0030 |
| cohere/nvfp4 | nvfp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 595.0 | 0.0153 |
| deepinfra/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 888.0 | 0.0145 |
| open-inference/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 9623.0 | 0.0064 |
| primeintellect | unknown | yes | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1235.0 | 0.0054 |
| darkbloom/fp4 | fp4 | yes | 98.5 | 135 | 0.00 | 1.00 | 97.9 | 100.0 | 95.7 | 100.0 | 100.0 | 6.20 | 0 | 0 | 2700.0 | 0.0051 |
| inceptron/fp8 | fp8 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 882.0 | 0.0163 |
| nebius/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1008.5 | 0.0145 |
| parasail/fast | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 540.0 | 0.0183 |
| venice | unknown | no | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1027.0 | 0.0150 |
| dekallm | unknown | yes | 97.8 | 139 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 3.50 | 0 | 0 | 2080.0 | 0.0100 |
| sail-research/us | fp4 | yes | 97.8 | 138 | 0 | 1.00 | 100.0 | 100.0 | 91.3 | 100.0 | 100.0 | 4.20 | 0 | 0 | 2570.0 | 0.0147 |
| kt | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 731.5 | 0.0144 |
| morph/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 3130.0 | 0.0101 |
| makora/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 787.0 | 0.0126 |
| nextbit/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1444.0 | 0.0118 |
| parasail/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 899.5 | 0.0144 |
| streamlake/fp8 | fp8 | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2412.5 | 0.0085 |
| sail-research/fp4 | fp4 | yes | 96.3 | 134 | 0 | 1.00 | 100.0 | 100.0 | 77.3 | 100.0 | 100.0 | 6.90 | 0 | 0 | 2118.0 | 0.0126 |
| fireworks | unknown | no | 96.2 | 133 | 0 | 1.00 | 100.0 | 100.0 | 77.3 | 100.0 | 100.0 | 7.60 | 0 | 0 | 1187.0 | 0.0117 |
| baseten/fp8 | fp8 | no | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 885.5 | 0.0145 |
| crusoe/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1002.0 | 0.0145 |
| friendli | unknown | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 518.0 | 0.0145 |
| near-ai/fp8 | fp8 | yes | 95.7 | 139 | 0.00 | 1.00 | 97.8 | 100.0 | 91.7 | 100.0 | 100.0 | 3.50 | 0 | 0 | 1746.0 | 0.0084 |
| tenstorrent/fp8 | fp8 | yes | 95.5 | 89 | 0.00 | 1.00 | 100.0 | 100.0 | 73.3 | 100.0 | 100.0 | 38.2 | 0 | 0 | 990.0 | 0.0044 |
| atlas-cloud/fp8 | fp8 | yes | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2311.0 | 0.0146 |
| coreweave/nvfp4 | nvfp4 | yes | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 600.5 | 0.0114 |
| gmicloud/fp8 | fp8 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2457.5 | 0.0072 |
| siliconflow/fp8 | fp8 | no | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1528.0 | 0.0099 |
| modal/fp4 | fp4 | no | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 573.0 | 0.0147 |
| mistral | unknown | yes | 93.8 | 144 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 845.5 | 0.0145 |
| novita/fp8 | fp8 | yes | 93.8 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1375.5 | 0.0082 |
| together | unknown | no | 93.8 | 144 | 0 | 1.00 | 95.8 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1113.5 | 0.0144 |
| digitalocean | unknown | no | 93.1 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 848.5 | 0.0108 |
| z-ai/fp8 | fp8 | no | 91.7 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2012.5 | 0.0146 |
| inference-net/fp4 | fp4 | yes | 91.0 | 144 | 0 | 1.00 | 91.7 | 100.0 | 83.3 | 100.0 | 95.8 | 0.00 | 0 | 1 | 652.5 | 0.0080 |
| wafer/nvfp4 | nvfp4 | yes | 90.9 | 143 | 0 | 1.00 | 97.9 | 100.0 | 78.3 | 100.0 | 95.8 | 0.70 | 0 | 0 | 812.0 | 0.0063 |
| inference-net/us | fp4 | yes | 88.2 | 144 | 0 | 1.00 | 95.8 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 657.5 | 0.0104 |
| reka | unknown | yes | 88.2 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 775.5 | 0.0110 |
| wafer/us | nvfp4 | yes | 88.1 | 143 | 0 | 1.00 | 93.6 | 100.0 | 79.2 | 100.0 | 95.8 | 0.70 | 0 | 0 | 814.0 | 0.0043 |
| baseten/fp8/us | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, wafer/us, primeintellect, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, tenstorrent/fp8, gmicloud/fp8, near-ai/fp8, novita/fp8, streamlake/fp8, siliconflow/fp8, dekallm, inference-net/us, inference-net/fp4, digitalocean, morph/fp8, reka, coreweave/nvfp4, nextbit/fp4, particle-ai/nvfp4, makora/fp4, mistral, kt, cohere/nvfp4, nebius/fp4, modal/fp4, baseten/fp8/us, crusoe/fp4, atlas-cloud/fp8, fireworks, friendli, together, parasail/fp4, baseten/fp8, venice, deepinfra/fp4, z-ai/fp8, inceptron/fp8, sail-research/us, sail-research/fp4, parasail/fast. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 100.0 | 121 | n/a | 1.00 | 44.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1098.0 | 0.0125 |
| novita/bf16 | bf16 | yes | 100.0 | 122 | n/a | 1.00 | 43.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1157.0 | 0.0125 |
| sambanova | unknown | no | 99.2 | 122 | 0 | 1.00 | 45.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2817.5 | 0.0339 |
| siliconflow/fp8 | fp8 | no | 94.3 | 122 | 0 | 1.00 | 41.7 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1681.0 | 0.0616 |
| friendli | unknown | yes | 92.6 | 122 | 0 | 1.00 | 39.6 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 381.0 | 0.0125 |
| parasail/fp8 | fp8 | yes | 92.6 | 122 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 700.0 | 0.0133 |
| deepinfra/fp8/flex | fp8 | yes | 91.0 | 122 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2729.0 | 0.0137 |
| deepinfra/fp8 | fp8 | yes | 90.2 | 122 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1367.5 | 0.0172 |
| deepinfra/fp8/priority | fp8 | yes | 90.2 | 122 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1339.0 | 0.0256 |
| coreweave/fp4 | fp4 | yes | 86.1 | 122 | 0 | 1.00 | 39.6 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 574.5 | 0.0091 |
| venice/fp4 | fp4 | no | 86.1 | 122 | 0 | 1.00 | 33.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 842.0 | 0.0106 |
| modal | unknown | no | 83.6 | 122 | 0.00 | 1.00 | 37.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 428.5 | 0.0265 |
| kt | unknown | no | 82.2 | 118 | 0 | 1.00 | 29.8 | 100.0 | 52.2 | 100.0 | 100.0 | 2.80 | 0 | 0 | 589.5 | 0.0088 |
| deepinfra/turbo | fp4 | yes | 81.1 | 122 | 0 | 1.00 | 29.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 527.5 | 0.0088 |
| chutes/fp4 | fp4 | yes | 78.7 | 122 | 0.00 | 1.00 | 33.3 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2684.5 | 0.0108 |
| primeintellect/fp4 | fp4 | yes | 78.7 | 122 | 0.00 | 1.00 | 27.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 882.5 | 0.0166 |
| nextbit/fp4 | fp4 | yes | 76.2 | 122 | 0 | 1.00 | 33.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 794.5 | 0.0133 |
| dekallm | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: crusoe/bf16, novita/bf16. Prompts with no plurality (excluded from exact match): 22.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| xiaomi/fp8 | fp8 | no | 97.1 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1951.0 | 0.0389 |
| primalabs/fp8 | fp8 | yes | 95.7 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 521.0 | 0.3536 |
| streamlake | unknown | no | 93.6 | 140 | 0 | 1.00 | 75.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1798.5 | 0.0438 |
| deepinfra/fp8 | fp8 | yes | 90.7 | 140 | 0 | 1.00 | 70.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1070.5 | 0.0343 |
| gmicloud/bf16 | bf16 | yes | 77.1 | 140 | 0.00 | 1.00 | 58.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2722.0 | 0.0284 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: gmicloud/bf16, deepinfra/fp8, xiaomi/fp8, streamlake, primalabs/fp8. Prompts with no plurality (excluded from exact match): 4.

## Footer

- Rows: 22176; errors 634; misrouted 0; truncated (finish_reason length) 63; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $7.0671; billed: $3.9413; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
