# Bitdepth scorecard 2026-11-21

Run `2026-11-21-live`, source `live`, started 2026-11-21T15:25:48Z, finished 2026-11-21T16:25:51Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 100.0 | 138 | n/a | 1.00 | 100.0 | 100.0 | 78.3 | 100.0 | 100.0 | 2.10 | 0 | 2 | 499.0 | 0.0064 |
| baseten/fp4/us | fp4 | no | 99.3 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 606.5 | 0.0129 |
| cerebras/fp16 | fp16 | yes | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 309.0 | 0.0368 |
| mancer/fp8 | fp8 | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 771.5 | 0.0104 |
| nebius/fp4 | fp4 | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 478.0 | 0.0173 |
| sambanova | unknown | no | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 471.0 | 0.0205 |
| akashml/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 880.5 | 0.0044 |
| baseten/fp4 | fp4 | no | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 602.0 | 0.0127 |
| groq | unknown | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 310.0 | 0.0182 |
| parasail/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 582.5 | 0.0151 |
| primeintellect/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 672.5 | 0.0365 |
| dekallm/bf16 | bf16 | yes | 97.1 | 102 | 0 | 1.00 | 100.0 | 100.0 | 76.5 | 100.0 | 100.0 | 27.8 | 0 | 1 | 1212.0 | 0.0031 |
| amazon-bedrock | unknown | no | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 562.5 | 0.0181 |
| near-ai/fp4 | fp4 | yes | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1313.0 | 0.0038 |
| parasail/fast | fp4 | yes | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 538.0 | 0.0199 |
| together | unknown | no | 96.5 | 141 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 602.5 | 0.0184 |
| coreweave/fp4 | fp4 | yes | 95.7 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 571.0 | 0.0041 |
| amazon-bedrock/eu-west-1 | unknown | no | 95.0 | 141 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 545.0 | 0.0183 |
| digitalocean | unknown | no | 95.0 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1221.5 | 0.0083 |
| google-vertex/global | unknown | yes | 95.0 | 141 | 0 | 1.00 | 93.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 446.5 | 0.0109 |
| venice/int4 | int4 | no | 80.1 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 66.7 | 100.0 | 87.5 | 0.00 | 0 | 11 | 1762.0 | 0.0048 |
| deepinfra/bf16 | bf16 | yes | 78.0 | 141 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 70.8 | 0.00 | 0 | 25 | 5627.0 | 0.0072 |
| siliconflow/fp8 | fp8 | no | 66.7 | 141 | 0 | 1.00 | 77.1 | 12.5 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2692.5 | 0.0216 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 3.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| digitalocean | unknown | no | 83.3 | 114 | 4 | 1.00 | 100.0 | 100.0 | 57.1 | 100.0 | 95.2 | 16.0 | 0 | 0 | 1163.0 | 0.0821 |
| alibaba/fp8 | fp8 | yes | 81.6 | 136 | 8 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1965.0 | 0.1282 |
| alibaba/fp8/us-east-1 | fp8 | yes | 80.9 | 136 | 7.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1903.0 | 0.1310 |
| deepinfra/fp8 | fp8 | yes | 80.9 | 136 | 5.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1289.0 | 0.0725 |
| deepinfra/fp8/flex | fp8 | yes | 79.4 | 136 | 6.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1862.0 | 0.0823 |
| deepinfra/fp8/priority | fp8 | yes | 77.2 | 136 | 4 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1184.0 | 0.0664 |
| siliconflow/fp8 | fp8 | no | 76.5 | 136 | 5.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2373.0 | 0.0400 |
| streamlake/fp8 | fp8 | no | 75.7 | 136 | 5 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2334.0 | 0.0252 |
| venice | unknown | no | 75.0 | 136 | 5.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1667.5 | 0.0698 |
| baidu/fp8 | fp8 | no | 74.3 | 136 | 4 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1494.0 | 0.0600 |
| relace/fp4 | fp4 | no | 69.1 | 136 | 5.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1049.5 | 0.0799 |
| azure/us | unknown | no | 59.6 | 136 | 1 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1035.0 | 0.1736 |
| novita/fp8 | fp8 | yes | 44.1 | 136 | 1.00 | 1.00 | 97.9 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2347.0 | 0.1148 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, siliconflow/fp8, deepinfra/fp8/flex, digitalocean, novita/fp8, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 8.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ambient/fp4 | fp4 | yes | 90.8 | 142 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1322.0 | 0.0044 |
| baseten/fast | unknown | no | 90.8 | 131 | 0.00 | 1.00 | 68.9 | 100.0 | 50.0 | 100.0 | 100.0 | 7.60 | 0 | 0 | 292.0 | 0.0452 |
| particle-ai/us/flex | unknown | yes | 90.8 | 142 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 807.5 | 0.0031 |
| digitalocean | unknown | no | 90.1 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 674.0 | 0.0138 |
| deepinfra/fp8/priority | fp8 | yes | 89.4 | 142 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 546.0 | 0.0033 |
| relace/fp4 | fp4 | no | 89.4 | 142 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1021.5 | 0.0110 |
| deepinfra/fp8/flex | fp8 | yes | 88.7 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1811.0 | 0.0069 |
| antdigital/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1319.0 | 0.0089 |
| cloudflare | unknown | yes | 88.0 | 142 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1350.5 | 0.0046 |
| inference-net/us | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 385.0 | 0.0084 |
| mistral/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 653.0 | 0.0274 |
| modal | unknown | no | 88.0 | 142 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 561.0 | 0.0230 |
| sail-research/fp4 | fp4 | yes | 88.0 | 142 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 914.5 | 0.0034 |
| wafer/mxfp4 | mxfp4 | yes | 88.0 | 142 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 389.5 | 0.0028 |
| inference-net/fp8 | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 372.0 | 0.0066 |
| novita/fp8 | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1066.0 | 0.0067 |
| stepfun/fp8 | fp8 | no | 87.3 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 680.0 | 0.0097 |
| cohere/fp8 | fp8 | yes | 86.6 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 404.5 | 0.0103 |
| crusoe/fp8 | fp8 | yes | 86.6 | 142 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 545.0 | 0.0267 |
| dekallm | unknown | yes | 86.6 | 142 | 0 | 1.00 | 79.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 842.5 | 0.0100 |
| parasail/fp8 | fp8 | yes | 86.6 | 142 | 0 | 1.00 | 81.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 323.5 | 0.0275 |
| particle-ai/us | unknown | yes | 86.6 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 603.5 | 0.0052 |
| primeintellect | unknown | no | 86.6 | 142 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 524.5 | 0.0070 |
| coreweave/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 286.5 | 0.0276 |
| modelrun/fp4 | fp4 | no | 85.9 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 825.5 | 0.0156 |
| morph/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 583.5 | 0.0050 |
| reka | unknown | no | 85.9 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 422.0 | 0.0276 |
| baseten | unknown | no | 85.2 | 142 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 451.5 | 0.0277 |
| fireworks/us | unknown | no | 85.2 | 142 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 419.0 | 0.0411 |
| inceptron/fp4 | fp4 | yes | 85.2 | 142 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 557.0 | 0.0090 |
| morph/fast | fp8 | yes | 85.2 | 135 | 0.00 | 1.00 | 75.6 | 100.0 | 60.9 | 100.0 | 100.0 | 4.90 | 0 | 0 | 386.0 | 0.0551 |
| pearl-research/fp8 | fp8 | yes | 85.2 | 142 | 0 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 746.0 | 0.0050 |
| siliconflow/fp8 | fp8 | no | 85.2 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 664.5 | 0.0137 |
| venice/fp8 | fp8 | no | 85.2 | 142 | 0 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1110.5 | 0.0280 |
| alibaba | unknown | yes | 84.5 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 748.0 | 0.0083 |
| deepinfra/fp8 | fp8 | yes | 84.5 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 516.5 | 0.0086 |
| sail-research/fp4/us | fp4 | yes | 84.5 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 922.5 | 0.0035 |
| wafer/us | mxfp4 | yes | 84.5 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 347.0 | 0.0047 |
| ionstream | unknown | yes | 83.1 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 477.0 | 0.0184 |
| primalabs | unknown | yes | 83.1 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 504.5 | 0.0219 |
| fireworks/spot | unknown | no | 82.4 | 142 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 784.5 | 0.0142 |
| makora/fp8 | fp8 | yes | 82.4 | 142 | 0 | 1.00 | 75.0 | 95.8 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 554.5 | 0.0146 |
| fireworks | unknown | no | 81.7 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 799.5 | 0.0043 |
| river | unknown | yes | 81.0 | 142 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 848.5 | 0.0110 |
| together | unknown | no | 80.3 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 397.0 | 0.0276 |
| nebius/fp4 | fp4 | yes | 79.6 | 142 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 460.0 | 0.0167 |
| streamlake/fp8 | fp8 | no | 78.7 | 141 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1221.0 | 0.0066 |
| baidu/fp8 | fp8 | no | 78.2 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 734.0 | 0.0091 |
| open-inference/fp4 | fp4 | yes | 73.9 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 700.0 | 0.0067 |
| near-ai | unknown | no | 72.5 | 142 | 0 | 1.00 | 58.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1066.0 | 0.0273 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, sail-research/fp4/us, sail-research/fp4, ambient/fp4, pearl-research/fp8, open-inference/fp4, primeintellect, morph/fp8, particle-ai/us, wafer/mxfp4, streamlake/fp8, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, alibaba, baidu/fp8, deepinfra/fp8, inceptron/fp4, dekallm, cloudflare, stepfun/fp8, cohere/fp8, antdigital/fp8, river, relace/fp4, deepinfra/fp8/priority, fireworks/spot, digitalocean, siliconflow/fp8, deepseek, makora/fp8, novita/fp8, modelrun/fp4, nebius/fp4, ionstream, primalabs, modal, crusoe/fp8, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, reka, together, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 2.

## Footer

- Rows: 12528; errors 229; misrouted 0; truncated (finish_reason length) 51; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.5235; billed: $2.1904; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
