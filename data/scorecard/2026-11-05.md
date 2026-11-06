# Bitdepth scorecard 2026-11-05

Run `2026-11-05-live`, source `live`, started 2026-11-05T21:03:36Z, finished 2026-11-06T01:19:22Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4 | fp4 | no | 100.0 | 139 | n/a | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 494.5 | 0.0127 |
| crusoe/bf16 | bf16 | yes | 100.0 | 139 | n/a | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 516.5 | 0.0065 |
| near-ai/fp4 | fp4 | yes | 100.0 | 139 | n/a | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 767.0 | 0.0037 |
| phala | unknown | yes | 99.3 | 139 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1678.5 | 0.0210 |
| cerebras/fp16 | fp16 | yes | 98.6 | 139 | 0.50 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 250.5 | 0.0367 |
| coreweave/fp4 | fp4 | yes | 98.6 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 607.0 | 0.0041 |
| baseten/fp4/us | fp4 | no | 97.8 | 139 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 504.5 | 0.0127 |
| sambanova | unknown | no | 97.8 | 139 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2054.0 | 0.0198 |
| together | unknown | no | 97.8 | 139 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 640.0 | 0.0178 |
| deepinfra/bf16 | bf16 | yes | 97.1 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1739.0 | 0.0048 |
| groq | unknown | yes | 97.1 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 277.0 | 0.0179 |
| mancer/fp8 | fp8 | yes | 97.1 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 95.8 | 0.00 | 0 | 1 | 874.0 | 0.0053 |
| parasail/fast | fp4 | yes | 97.1 | 139 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 459.0 | 0.0194 |
| primeintellect/fp4 | fp4 | yes | 97.1 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 883.5 | 0.0033 |
| sail-research/fp4 | fp4 | yes | 97.1 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 835.5 | 0.0083 |
| siliconflow/fp8 | fp8 | no | 97.1 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2031.5 | 0.0247 |
| deepinfra/fp8 | fp8 | yes | 96.8 | 124 | 0.00 | 1.00 | 100.0 | 100.0 | 73.9 | 100.0 | 100.0 | 10.4 | 0 | 0 | 1827.0 | 0.0218 |
| google-vertex/global | unknown | yes | 96.4 | 137 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 1.40 | 0 | 1 | 812.0 | 0.0108 |
| amazon-bedrock/eu-west-1 | unknown | no | 95.7 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 661.0 | 0.0182 |
| dekallm/bf16 | bf16 | yes | 95.7 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1120.5 | 0.0041 |
| nebius/fp4 | fp4 | yes | 95.7 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 95.8 | 100.0 | 0.00 | 0 | 1 | 440.5 | 0.0176 |
| amazon-bedrock | unknown | no | 95.0 | 139 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 681.0 | 0.0181 |
| parasail/fp4 | fp4 | yes | 95.0 | 139 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 548.5 | 0.0153 |
| akashml/fp4 | fp4 | yes | 94.2 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 766.5 | 0.0041 |
| digitalocean | unknown | no | 94.2 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2110.0 | 0.0086 |
| venice/int4 | int4 | no | 82.7 | 139 | 0.00 | 1.00 | 72.9 | 100.0 | 70.8 | 100.0 | 87.5 | 0.00 | 0 | 17 | 1900.5 | 0.0049 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 5.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 91.5 | 129 | 21 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2343.0 | 0.1294 |
| alibaba/fp8/us-east-1 | fp8 | yes | 88.4 | 129 | 8 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2054.0 | 0.1321 |
| deepinfra/fp8 | fp8 | yes | 80.0 | 100 | 1.00 | 1.00 | 100.0 | 100.0 | 65.0 | 100.0 | 95.0 | 23.6 | 0 | 0 | 1242.5 | 0.0959 |
| atlas-cloud/fp4 | fp4 | yes | 79.8 | 129 | 4.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2347.5 | 0.1403 |
| streamlake/fp8 | fp8 | no | 79.8 | 129 | 4.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2015.5 | 0.0330 |
| nebius/fp8 | fp8 | yes | 79.1 | 129 | 8 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1460.0 | 0.1590 |
| relace/fp4 | fp4 | no | 77.5 | 129 | 4 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 847.0 | 0.0594 |
| venice | unknown | no | 76.0 | 129 | 5 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1621.0 | 0.0821 |
| siliconflow/fp8 | fp8 | no | 69.8 | 129 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2252.0 | 0.0795 |
| baidu/fp8 | fp8 | no | 63.6 | 129 | 1 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1567.0 | 0.0981 |
| azure/us | unknown | no | 60.5 | 129 | 1 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1091.5 | 0.1738 |
| digitalocean | unknown | no | 60.5 | 129 | 1 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1518.5 | 0.0947 |
| gmicloud/fp8 | fp8 | yes | 48.1 | 129 | 0 | 1.00 | 95.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2249.0 | 0.0703 |
| novita/fp8 | fp8 | yes | 45.0 | 129 | 1 | 1.00 | 100.0 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1628.5 | 0.0974 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, nebius/fp8, azure/us. Prompts with no plurality (excluded from exact match): 15.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| primeintellect | unknown | no | 90.1 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 470.5 | 0.0083 |
| coreweave/fp8 | fp8 | yes | 89.4 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 411.0 | 0.0277 |
| mistral/fp8 | fp8 | yes | 89.4 | 142 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 670.5 | 0.0276 |
| cloudflare | unknown | yes | 88.7 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1101.0 | 0.0094 |
| cohere | unknown | yes | 88.7 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 371.0 | 0.0165 |
| makora/fp8 | fp8 | yes | 88.7 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 334.5 | 0.0161 |
| morph/fp8 | fp8 | yes | 88.7 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 543.0 | 0.0029 |
| deepinfra/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 460.0 | 0.0044 |
| novita/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1307.5 | 0.0084 |
| fireworks/us | unknown | no | 87.3 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 443.5 | 0.0212 |
| parasail/fp8 | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 391.0 | 0.0257 |
| wafer/us | mxfp4 | yes | 87.3 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 317.5 | 0.0049 |
| fireworks | unknown | no | 86.6 | 142 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1025.5 | 0.0271 |
| particle-ai/us | unknown | yes | 86.6 | 142 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 604.5 | 0.0040 |
| particle-ai/us/flex | unknown | yes | 86.6 | 142 | 0 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 732.0 | 0.0026 |
| siliconflow/fp8 | fp8 | no | 86.6 | 142 | 0 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 603.5 | 0.0217 |
| wafer/mxfp4 | mxfp4 | yes | 86.6 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 397.0 | 0.0034 |
| atlas-cloud/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1219.0 | 0.0044 |
| deepinfra/fp8/flex | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 62.5 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1512.0 | 0.0056 |
| deepinfra/fp8/priority | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 512.5 | 0.0035 |
| gmicloud/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 62.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 854.5 | 0.0165 |
| modelrun/fp4 | fp4 | no | 85.9 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 769.0 | 0.0152 |
| nebius/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 871.5 | 0.0276 |
| primalabs | unknown | yes | 85.6 | 139 | 0.00 | 1.00 | 68.1 | 100.0 | 52.2 | 100.0 | 100.0 | 2.10 | 0 | 0 | 701.0 | 0.0829 |
| baseten/fast | unknown | no | 85.3 | 109 | 0.00 | 1.00 | 64.5 | 100.0 | 50.0 | 100.0 | 100.0 | 24.3 | 0 | 0 | 303.0 | 0.0435 |
| decart/fp8 | fp8 | yes | 85.2 | 142 | 0 | 1.00 | 68.8 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 684.0 | 0.0113 |
| relace/fast | fp4 | no | 85.2 | 142 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 504.0 | 0.0266 |
| venice/fp8 | fp8 | no | 85.2 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1091.5 | 0.0278 |
| alibaba | unknown | yes | 84.5 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 869.5 | 0.0183 |
| baseten | unknown | no | 84.5 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 457.0 | 0.0294 |
| dekallm | unknown | yes | 84.5 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 896.5 | 0.0164 |
| inference-net/us | fp8 | yes | 84.5 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 364.5 | 0.0062 |
| stepfun/fp8 | fp8 | no | 84.5 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 518.5 | 0.0124 |
| together | unknown | no | 84.5 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 58.3 | 87.5 | 100.0 | 0.00 | 0 | 0 | 255.0 | 0.0275 |
| modal | unknown | no | 84.4 | 135 | 0 | 1.00 | 66.7 | 100.0 | 56.5 | 100.0 | 100.0 | 4.90 | 0 | 0 | 547.0 | 0.0206 |
| inference-net/fp8 | fp8 | yes | 83.8 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 371.5 | 0.0036 |
| phala | unknown | yes | 83.8 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1457.0 | 0.0063 |
| relace/fp4 | fp4 | no | 83.8 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 668.0 | 0.0022 |
| crusoe/fp8 | fp8 | yes | 82.4 | 142 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 572.0 | 0.0231 |
| ionstream | unknown | yes | 78.9 | 142 | 0.00 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 637.5 | 0.0146 |
| digitalocean | unknown | no | 78.2 | 142 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 553.0 | 0.0165 |
| streamlake/fp8 | fp8 | no | 78.2 | 142 | 0 | 1.00 | 85.4 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1180.5 | 0.0057 |
| baidu/fp8 | fp8 | no | 75.9 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 909.0 | 0.0135 |
| open-inference/fp4 | fp4 | yes | 73.2 | 142 | 0.00 | 1.00 | 58.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2832.0 | 0.0023 |
| reka | unknown | no | 72.3 | 130 | 0.00 | 1.00 | 73.3 | 100.0 | 54.5 | 100.0 | 100.0 | 8.30 | 0 | 1 | 652.5 | 0.0158 |
| near-ai | unknown | no | 70.4 | 142 | 0.00 | 1.00 | 64.6 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 677.0 | 0.0237 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| fireworks/spot | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: open-inference/fp4, relace/fp4, morph/fp8, particle-ai/us/flex, wafer/us, particle-ai/us, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, deepinfra/fp8, cloudflare, sail-research/fp4/us, sail-research/fp4, primeintellect, streamlake/fp8, decart/fp8, wafer/mxfp4, stepfun/fp8, deepinfra/fp8/priority, baidu/fp8, deepseek, makora/fp8, reka, ionstream, alibaba, novita/fp8, modelrun/fp4, dekallm, digitalocean, gmicloud/fp8, cohere, atlas-cloud/fp8, phala, fireworks/spot, modal, crusoe/fp8, siliconflow/fp8, relace/fast, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast, primalabs. Prompts with no plurality (excluded from exact match): 2.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 127 | n/a | 1.00 | 100.0 | 62.5 | 87.5 | 100.0 | 91.7 | 0.00 | 0 | 12 | 2914.0 | 0.1003 |
| mistral/zdr | unknown | yes | 100.0 | 127 | n/a | 1.00 | 100.0 | 50.0 | 83.3 | 100.0 | 79.2 | 0.00 | 0 | 17 | 2919.5 | 0.1222 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 17.

## Footer

- Rows: 13248; errors 685; misrouted 0; truncated (finish_reason length) 58; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $5.3099; billed: $2.7652; cap $7.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
