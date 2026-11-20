# Bitdepth scorecard 2026-11-20

Run `2026-11-20-live`, source `live`, started 2026-11-20T16:13:20Z, finished 2026-11-20T17:40:39Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 100.0 | 141 | n/a | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 263.5 | 0.0371 |
| baseten/fp4 | fp4 | no | 99.3 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 527.0 | 0.0127 |
| baseten/fp4/us | fp4 | no | 99.3 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 511.0 | 0.0126 |
| sambanova | unknown | no | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 472.5 | 0.0201 |
| together | unknown | no | 98.6 | 141 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 661.5 | 0.0181 |
| deepinfra/bf16 | bf16 | yes | 97.9 | 141 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 3978.5 | 0.0046 |
| groq | unknown | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 338.5 | 0.0180 |
| parasail/fast | fp4 | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 498.0 | 0.0196 |
| akashml/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 990.0 | 0.0042 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 583.5 | 0.0180 |
| coreweave/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 634.0 | 0.0041 |
| parasail/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 608.5 | 0.0147 |
| amazon-bedrock | unknown | no | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 558.0 | 0.0180 |
| crusoe/bf16 | bf16 | yes | 95.7 | 141 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 511.5 | 0.0065 |
| nebius/fp4 | fp4 | yes | 95.7 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 442.5 | 0.0178 |
| dekallm/bf16 | bf16 | yes | 95.6 | 137 | 0.00 | 1.00 | 100.0 | 100.0 | 82.6 | 100.0 | 100.0 | 3.50 | 0 | 0 | 3218.0 | 0.0039 |
| digitalocean | unknown | no | 95.0 | 141 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1525.5 | 0.0082 |
| near-ai/fp4 | fp4 | yes | 95.0 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1201.5 | 0.0038 |
| primeintellect/fp4 | fp4 | yes | 95.0 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 618.5 | 0.0352 |
| mancer/fp8 | fp8 | yes | 93.6 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 800.5 | 0.0105 |
| sail-research/fp4 | fp4 | yes | 93.3 | 120 | 0.00 | 1.00 | 100.0 | 100.0 | 71.4 | 100.0 | 100.0 | 14.6 | 0 | 0 | 920.0 | 0.0072 |
| google-vertex/global | unknown | yes | 92.9 | 141 | 0.00 | 1.00 | 91.7 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 422.5 | 0.0108 |
| venice/int4 | int4 | no | 84.2 | 139 | 0.00 | 1.00 | 83.3 | 100.0 | 75.0 | 100.0 | 83.3 | 1.40 | 0 | 12 | 1838.0 | 0.0047 |
| siliconflow/fp8 | fp8 | no | 62.4 | 141 | 0 | 1.00 | 77.1 | 0.00 | 45.8 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1902.0 | 0.0215 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 3.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 87.3 | 134 | 7 | 1.00 | 97.9 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1916.0 | 0.1260 |
| alibaba/fp8/us-east-1 | fp8 | yes | 86.6 | 134 | 10.0 | 1.00 | 97.9 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1819.5 | 0.1300 |
| siliconflow/fp8 | fp8 | no | 85.8 | 134 | 16 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2431.5 | 0.0498 |
| baidu/fp8 | fp8 | no | 82.1 | 134 | 5.50 | 1.00 | 97.9 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1428.0 | 0.0745 |
| deepinfra/fp8 | fp8 | yes | 80.6 | 134 | 1.50 | 1.00 | 97.9 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2315.5 | 0.1046 |
| digitalocean | unknown | no | 78.4 | 134 | 5 | 1.00 | 97.9 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1621.5 | 0.0951 |
| streamlake/fp8 | fp8 | no | 78.4 | 134 | 7 | 1.00 | 97.9 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2430.0 | 0.0307 |
| deepinfra/fp8/priority | fp8 | yes | 77.6 | 134 | 4.00 | 1.00 | 97.9 | 100.0 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2002.5 | 0.0673 |
| deepinfra/fp8/flex | fp8 | yes | 74.3 | 105 | 1 | 1.00 | 100.0 | 100.0 | 61.9 | 100.0 | 95.2 | 21.5 | 0 | 0 | 2214.0 | 0.0574 |
| venice | unknown | no | 71.9 | 128 | 4.50 | 1.00 | 95.7 | 100.0 | 47.8 | 100.0 | 100.0 | 4.20 | 0 | 0 | 2201.5 | 0.0660 |
| atlas-cloud/fp4 | fp4 | yes | 68.7 | 134 | 4.50 | 1.00 | 97.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2259.0 | 0.1529 |
| relace/fp4 | fp4 | no | 68.7 | 134 | 8.00 | 1.00 | 97.9 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 929.0 | 0.0798 |
| azure/us | unknown | no | 56.7 | 134 | 1.00 | 1.00 | 97.9 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1050.5 | 0.1757 |
| novita/fp8 | fp8 | yes | 43.3 | 134 | 0.00 | 1.00 | 93.8 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2226.5 | 0.1060 |
| gmicloud/fp8 | fp8 | yes | 41.8 | 134 | 0.00 | 1.00 | 93.8 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2571.0 | 0.0802 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, siliconflow/fp8, gmicloud/fp8, deepinfra/fp8/flex, digitalocean, novita/fp8, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, atlas-cloud/fp4, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 10.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| atlas-cloud/fp8 | fp8 | yes | 89.6 | 144 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1217.5 | 0.0044 |
| baseten/fast | unknown | no | 89.2 | 130 | 0.00 | 1.00 | 64.3 | 100.0 | 42.9 | 100.0 | 100.0 | 9.70 | 0 | 0 | 320.5 | 0.0528 |
| novita/fp8 | fp8 | yes | 88.2 | 144 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1072.5 | 0.0058 |
| antdigital/fp8 | fp8 | yes | 87.5 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1325.0 | 0.0103 |
| modelrun/fp4 | fp4 | no | 86.1 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 790.5 | 0.0157 |
| morph/fast | fp8 | yes | 85.8 | 141 | 0.00 | 1.00 | 70.2 | 100.0 | 39.1 | 100.0 | 100.0 | 2.10 | 0 | 0 | 390.0 | 0.0535 |
| baseten | unknown | no | 85.4 | 144 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 842.0 | 0.0276 |
| digitalocean | unknown | no | 84.7 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 635.0 | 0.0167 |
| inference-net/fp8 | fp8 | yes | 84.7 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 400.0 | 0.0076 |
| makora/fp8 | fp8 | yes | 84.7 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 474.0 | 0.0149 |
| morph/fp8 | fp8 | yes | 84.7 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 513.0 | 0.0050 |
| primalabs | unknown | yes | 84.7 | 144 | 0.00 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 579.5 | 0.0220 |
| cohere/fp8 | fp8 | yes | 84.0 | 144 | 0 | 1.00 | 66.7 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 428.5 | 0.0103 |
| coreweave/fp8 | fp8 | yes | 84.0 | 144 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 304.0 | 0.0278 |
| pearl-research/fp8 | fp8 | yes | 84.0 | 144 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 834.5 | 0.0052 |
| primeintellect | unknown | no | 84.0 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 644.5 | 0.0061 |
| siliconflow/fp8 | fp8 | no | 84.0 | 144 | 0 | 1.00 | 62.5 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 727.5 | 0.0136 |
| venice/fp8 | fp8 | no | 84.0 | 144 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 977.0 | 0.0279 |
| wafer/us | mxfp4 | yes | 84.0 | 144 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 410.0 | 0.0048 |
| deepinfra/fp8/flex | fp8 | yes | 83.3 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1962.0 | 0.0069 |
| dekallm | unknown | yes | 83.3 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1240.0 | 0.0102 |
| inference-net/us | fp8 | yes | 83.3 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 391.5 | 0.0084 |
| parasail/fp8 | fp8 | yes | 83.3 | 144 | 0.00 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 341.0 | 0.0279 |
| particle-ai/us | unknown | yes | 83.3 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 603.5 | 0.0053 |
| reka | unknown | no | 83.3 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 394.0 | 0.0274 |
| alibaba | unknown | yes | 82.6 | 144 | 0 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 866.0 | 0.0082 |
| cloudflare | unknown | yes | 82.6 | 144 | 0 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1776.5 | 0.0056 |
| crusoe/fp8 | fp8 | yes | 82.6 | 144 | 0 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 646.5 | 0.0271 |
| fireworks/us | unknown | no | 82.6 | 144 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 559.5 | 0.0418 |
| modal | unknown | no | 82.6 | 144 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 562.0 | 0.0230 |
| relace/fp4 | fp4 | no | 82.6 | 144 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1086.5 | 0.0112 |
| ambient/fp4 | fp4 | yes | 81.9 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2071.5 | 0.0044 |
| fireworks | unknown | no | 81.9 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 469.0 | 0.0044 |
| fireworks/spot | unknown | no | 81.9 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 446.0 | 0.0139 |
| inceptron/fp4 | fp4 | yes | 81.9 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 855.5 | 0.0091 |
| wafer/mxfp4 | mxfp4 | yes | 81.9 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 430.5 | 0.0027 |
| gmicloud/fp8 | fp8 | yes | 81.2 | 144 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 812.5 | 0.0169 |
| deepinfra/fp8/priority | fp8 | yes | 80.6 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 678.5 | 0.0035 |
| mistral/fp8 | fp8 | yes | 80.6 | 144 | 0.00 | 1.00 | 62.5 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 656.5 | 0.0278 |
| particle-ai/us/flex | unknown | yes | 80.6 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 790.0 | 0.0032 |
| stepfun/fp8 | fp8 | no | 80.6 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 766.5 | 0.0099 |
| deepinfra/fp8 | fp8 | yes | 79.9 | 144 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 635.0 | 0.0087 |
| ionstream | unknown | yes | 79.9 | 144 | 0 | 1.00 | 64.6 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 524.0 | 0.0185 |
| together | unknown | no | 78.5 | 144 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 452.5 | 0.0279 |
| streamlake/fp8 | fp8 | no | 75.7 | 144 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1116.0 | 0.0103 |
| nebius/fp4 | fp4 | yes | 75.0 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 485.0 | 0.0169 |
| river | unknown | yes | 75.0 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1113.0 | 0.0111 |
| open-inference/fp4 | fp4 | yes | 72.9 | 144 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 713.5 | 0.0077 |
| baidu/fp8 | fp8 | no | 71.5 | 144 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 704.0 | 0.0140 |
| near-ai | unknown | no | 70.8 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1059.5 | 0.0283 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, primeintellect, ambient/fp4, pearl-research/fp8, morph/fp8, particle-ai/us, open-inference/fp4, wafer/mxfp4, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, alibaba, deepinfra/fp8, inceptron/fp4, dekallm, cloudflare, stepfun/fp8, streamlake/fp8, cohere/fp8, antdigital/fp8, river, relace/fp4, deepinfra/fp8/priority, baidu/fp8, fireworks/spot, siliconflow/fp8, deepseek, makora/fp8, novita/fp8, modelrun/fp4, nebius/fp4, digitalocean, gmicloud/fp8, atlas-cloud/fp8, ionstream, primalabs, modal, crusoe/fp8, mistral/fp8, coreweave/fp8, near-ai, venice/fp8, reka, together, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 0.

## Footer

- Rows: 12960; errors 226; misrouted 0; truncated (finish_reason length) 22; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $5.0367; billed: $2.5021; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
