# Bitdepth scorecard 2026-11-13

Run `2026-11-13-live`, source `live`, started 2026-11-13T15:27:11Z, finished 2026-11-13T16:18:19Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/bf16 | bf16 | yes | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2176.0 | 0.0048 |
| baseten/fp4 | fp4 | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 493.0 | 0.0127 |
| crusoe/bf16 | bf16 | yes | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 734.5 | 0.0066 |
| deepinfra/fp8 | fp8 | yes | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1495.5 | 0.0251 |
| io-net/fp4 | fp4 | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1954.5 | 0.0038 |
| sambanova | unknown | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 438.5 | 0.0200 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 776.5 | 0.0183 |
| baseten/fp4/us | fp4 | no | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 486.0 | 0.0128 |
| cerebras/fp16 | fp16 | yes | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 277.0 | 0.0376 |
| coreweave/fp4 | fp4 | yes | 97.1 | 138 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 1.40 | 0 | 0 | 691.5 | 0.0040 |
| primeintellect/fp4 | fp4 | yes | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 973.5 | 0.0075 |
| together | unknown | no | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 711.0 | 0.0181 |
| akashml/fp4 | fp4 | yes | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1273.0 | 0.0042 |
| dekallm/bf16 | bf16 | yes | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1616.5 | 0.0042 |
| sail-research/fp4 | fp4 | yes | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1244.5 | 0.0084 |
| amazon-bedrock | unknown | no | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 786.5 | 0.0182 |
| digitalocean | unknown | no | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1440.0 | 0.0083 |
| mancer/fp8 | fp8 | yes | 95.7 | 140 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 910.5 | 0.0067 |
| nebius/fp4 | fp4 | yes | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 539.0 | 0.0177 |
| groq | unknown | yes | 95.0 | 140 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 403.5 | 0.0178 |
| near-ai/fp4 | fp4 | yes | 95.0 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1636.0 | 0.0038 |
| parasail/fp4 | fp4 | yes | 95.0 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 724.0 | 0.0146 |
| siliconflow/fp8 | fp8 | no | 95.0 | 140 | 0 | 1.00 | 91.7 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2275.5 | 0.0254 |
| parasail/fast | fp4 | yes | 93.6 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 482.0 | 0.0203 |
| google-vertex/global | unknown | yes | 92.9 | 140 | 0.00 | 1.00 | 95.8 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 542.0 | 0.0106 |
| venice/int4 | int4 | no | 83.6 | 140 | 0 | 1.00 | 81.2 | 100.0 | 66.7 | 100.0 | 91.7 | 0.00 | 0 | 14 | 1552.0 | 0.0048 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 4.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| venice | unknown | no | 80.9 | 131 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1583.0 | 0.0720 |
| deepinfra/fp8 | fp8 | yes | 80.2 | 131 | 6.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1325.0 | 0.1151 |
| alibaba/fp8 | fp8 | yes | 79.4 | 131 | 1 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 91.7 | 0.00 | 0 | 0 | 3124.0 | 0.1282 |
| alibaba/fp8/us-east-1 | fp8 | yes | 78.6 | 131 | 3.50 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2732.0 | 0.1414 |
| baidu/fp8 | fp8 | no | 78.6 | 131 | 1.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1435.0 | 0.0761 |
| atlas-cloud/fp4 | fp4 | yes | 77.1 | 131 | 2.50 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2763.5 | 0.1472 |
| streamlake/fp8 | fp8 | no | 76.3 | 131 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2367.0 | 0.0312 |
| siliconflow/fp8 | fp8 | no | 74.8 | 131 | 3 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2318.5 | 0.0868 |
| relace/fp4 | fp4 | no | 70.2 | 131 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1100.0 | 0.0796 |
| digitalocean | unknown | no | 58.0 | 131 | 1 | 1.00 | 97.9 | 100.0 | 50.0 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1601.5 | 0.0954 |
| azure/us | unknown | no | 56.5 | 131 | 0 | 1.00 | 100.0 | 100.0 | 45.8 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1135.5 | 0.1746 |
| novita/fp8 | fp8 | yes | 48.1 | 131 | 1.00 | 1.00 | 93.8 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2142.5 | 0.1364 |
| gmicloud/fp8 | fp8 | yes | 46.6 | 131 | 0.00 | 1.00 | 95.8 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2579.5 | 0.0814 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, azure/us. Prompts with no plurality (excluded from exact match): 13.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fireworks/us | unknown | no | 90.8 | 141 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 457.0 | 0.0415 |
| alibaba | unknown | yes | 88.7 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 912.5 | 0.0098 |
| deepinfra/fp8/priority | fp8 | yes | 88.7 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 665.0 | 0.0034 |
| morph/fp8 | fp8 | yes | 88.7 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 953.5 | 0.0090 |
| parasail/fp8 | fp8 | yes | 88.7 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 448.0 | 0.0275 |
| streamlake/fp8 | fp8 | no | 88.7 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1463.0 | 0.0102 |
| venice/fp8 | fp8 | no | 88.7 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 908.0 | 0.0279 |
| inference-net/fp8 | fp8 | yes | 87.9 | 141 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 521.5 | 0.0058 |
| modal | unknown | no | 87.9 | 141 | 0 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 793.0 | 0.0234 |
| siliconflow/fp8 | fp8 | no | 87.9 | 141 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 976.5 | 0.0251 |
| baseten | unknown | no | 87.2 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 639.0 | 0.0287 |
| cloudflare | unknown | yes | 87.2 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1646.0 | 0.0052 |
| coreweave/fp8 | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 465.5 | 0.0280 |
| dekallm | unknown | yes | 87.2 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1087.0 | 0.0165 |
| fireworks | unknown | no | 87.2 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 780.5 | 0.0280 |
| fireworks/spot | unknown | no | 87.2 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 915.5 | 0.0196 |
| gmicloud/fp8 | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 66.7 | 95.8 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 990.0 | 0.0164 |
| inference-net/us | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 471.5 | 0.0085 |
| novita/fp8 | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1237.0 | 0.0038 |
| relace/fp4 | fp4 | no | 87.2 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1174.0 | 0.0110 |
| cohere/fp8 | fp8 | yes | 86.5 | 141 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 471.5 | 0.0135 |
| makora/fp8 | fp8 | yes | 86.5 | 141 | 0 | 1.00 | 83.3 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 657.5 | 0.0165 |
| stepfun/fp8 | fp8 | no | 86.5 | 141 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 576.5 | 0.0098 |
| wafer/us | mxfp4 | yes | 86.5 | 141 | 0 | 1.00 | 83.3 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 513.0 | 0.0051 |
| deepinfra/fp8/flex | fp8 | yes | 85.8 | 141 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1918.5 | 0.0053 |
| particle-ai/us | unknown | yes | 85.8 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2758.0 | 0.0063 |
| particle-ai/us/flex | unknown | yes | 85.8 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2880.0 | 0.0032 |
| primeintellect | unknown | no | 85.8 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2264.0 | 0.0060 |
| sail-research/fp4/us | fp4 | yes | 85.8 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1153.5 | 0.0058 |
| deepinfra/fp8 | fp8 | yes | 85.1 | 141 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 679.5 | 0.0052 |
| sail-research/fp4 | fp4 | yes | 85.1 | 141 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1173.5 | 0.0044 |
| baseten/fast | unknown | no | 84.9 | 139 | 0 | 1.00 | 68.8 | 100.0 | 39.1 | 100.0 | 100.0 | 1.40 | 0 | 0 | 349.5 | 0.0535 |
| nebius/fp8 | fp8 | yes | 84.4 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1650.0 | 0.0281 |
| atlas-cloud/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1279.0 | 0.0043 |
| primalabs | unknown | yes | 83.7 | 141 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 547.5 | 0.0224 |
| crusoe/fp8 | fp8 | yes | 83.0 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 665.0 | 0.0273 |
| mistral/fp8 | fp8 | yes | 83.0 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 792.5 | 0.0280 |
| river | unknown | yes | 83.0 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 716.5 | 0.0110 |
| together | unknown | no | 83.0 | 141 | 0.00 | 1.00 | 83.3 | 100.0 | 50.0 | 87.5 | 100.0 | 0.00 | 0 | 0 | 462.0 | 0.0280 |
| wafer/mxfp4 | mxfp4 | yes | 83.0 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 540.0 | 0.0039 |
| ionstream | unknown | yes | 80.1 | 141 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 660.5 | 0.0146 |
| baidu/fp8 | fp8 | no | 78.7 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 875.5 | 0.0141 |
| reka | unknown | no | 78.7 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 663.5 | 0.0167 |
| digitalocean | unknown | no | 76.3 | 139 | 0 | 1.00 | 70.2 | 100.0 | 62.5 | 100.0 | 100.0 | 1.40 | 0 | 0 | 614.5 | 0.0166 |
| ionstream/flex | unknown | yes | 75.2 | 141 | 0 | 1.00 | 87.5 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 483.0 | 0.0071 |
| near-ai | unknown | no | 73.8 | 141 | 0 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1219.0 | 0.0275 |
| open-inference/fp4 | fp4 | yes | 73.0 | 141 | 0.00 | 1.00 | 60.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1994.5 | 0.0084 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, primeintellect, particle-ai/us, open-inference/fp4, sail-research/fp4/us, sail-research/fp4, ionstream/flex, deepinfra/fp8/flex, wafer/mxfp4, inference-net/us, inference-net/fp8, morph/fp8, deepinfra/fp8, cloudflare, stepfun/fp8, alibaba, streamlake/fp8, river, relace/fp4, deepinfra/fp8/priority, baidu/fp8, cohere/fp8, deepseek, makora/fp8, reka, ionstream, novita/fp8, dekallm, digitalocean, gmicloud/fp8, atlas-cloud/fp8, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, mistral/fp8, coreweave/fp8, near-ai, venice/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast. Prompts with no plurality (excluded from exact match): 3.

## Footer

- Rows: 12528; errors 150; misrouted 0; truncated (finish_reason length) 31; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.5422; billed: $2.4438; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
