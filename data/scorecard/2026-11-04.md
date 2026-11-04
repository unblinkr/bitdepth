# Bitdepth scorecard 2026-11-04

Run `2026-11-04-live`, source `live`, started 2026-11-04T15:28:38Z, finished 2026-11-04T18:02:27Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 99.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 230.5 | 0.0374 |
| deepinfra/bf16 | bf16 | yes | 99.3 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.70 | 0 | 1 | 2076.0 | 0.0046 |
| amazon-bedrock/eu-west-1 | unknown | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 641.0 | 0.0181 |
| baseten/fp4 | fp4 | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 553.0 | 0.0128 |
| crusoe/bf16 | bf16 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 438.0 | 0.0065 |
| dekallm/bf16 | bf16 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1357.5 | 0.0041 |
| baseten/fp4/us | fp4 | no | 97.2 | 142 | 0.00 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 542.0 | 0.0130 |
| sail-research/fp4 | fp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 903.0 | 0.0084 |
| sambanova | unknown | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 585.0 | 0.0205 |
| deepinfra/fp8 | fp8 | yes | 97.0 | 135 | 0.00 | 1.00 | 100.0 | 100.0 | 69.6 | 100.0 | 100.0 | 4.90 | 0 | 1 | 1841.0 | 0.0250 |
| mara | unknown | no | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1062.5 | 0.0198 |
| together | unknown | no | 96.5 | 142 | 0 | 1.00 | 97.9 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 2 | 764.5 | 0.0184 |
| groq | unknown | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 325.0 | 0.0180 |
| near-ai/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1277.0 | 0.0038 |
| primeintellect/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 889.0 | 0.0035 |
| nebius/fp4 | fp4 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 445.5 | 0.0177 |
| phala | unknown | yes | 95.0 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 1.40 | 0 | 4 | 1303.0 | 0.0239 |
| akashml/fp4 | fp4 | yes | 94.4 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 682.0 | 0.0042 |
| amazon-bedrock | unknown | no | 94.4 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 263.5 | 0.0180 |
| siliconflow/fp8 | fp8 | no | 94.4 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3598.5 | 0.0262 |
| google-vertex/global | unknown | yes | 94.2 | 139 | 0.00 | 1.00 | 97.8 | 100.0 | 66.7 | 100.0 | 100.0 | 2.10 | 0 | 0 | 987.0 | 0.0107 |
| parasail/fp4 | fp4 | yes | 93.7 | 142 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 616.0 | 0.0151 |
| digitalocean | unknown | no | 92.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1399.0 | 0.0085 |
| mancer/fp8 | fp8 | yes | 91.5 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1211.5 | 0.0065 |
| coreweave/fp4 | fp4 | yes | 90.8 | 142 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 687.5 | 0.0041 |
| venice/int4 | int4 | no | 79.6 | 142 | 0 | 1.00 | 60.4 | 100.0 | 75.0 | 100.0 | 91.7 | 0.00 | 0 | 17 | 1909.5 | 0.0051 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 2.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 87.5 | 128 | 8.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2415.0 | 0.1263 |
| alibaba/fp8/us-east-1 | fp8 | yes | 83.6 | 128 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2130.5 | 0.1382 |
| atlas-cloud/fp4 | fp4 | yes | 82.0 | 128 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2386.0 | 0.1519 |
| baidu/fp8 | fp8 | no | 81.7 | 120 | 6.50 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.2 | 6.90 | 0 | 0 | 1466.0 | 0.0781 |
| streamlake/fp8 | fp8 | no | 78.1 | 128 | 6.50 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2421.0 | 0.0328 |
| relace/fp4 | fp4 | no | 76.6 | 128 | 4.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1233.0 | 0.0798 |
| nebius/fp8 | fp8 | yes | 75.0 | 128 | 4.50 | 1.00 | 100.0 | 100.0 | 73.9 | 100.0 | 95.8 | 0.70 | 0 | 0 | 1901.0 | 0.1590 |
| venice | unknown | no | 74.2 | 128 | 1 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1599.5 | 0.0820 |
| deepinfra/fp8 | fp8 | yes | 73.4 | 128 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1327.5 | 0.1146 |
| siliconflow/fp8 | fp8 | no | 70.3 | 128 | 3.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2123.0 | 0.0972 |
| digitalocean | unknown | no | 60.9 | 128 | 0.00 | 1.00 | 97.9 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1446.0 | 0.0951 |
| azure/us | unknown | no | 60.2 | 128 | 1 | 1.00 | 100.0 | 95.8 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1300.5 | 0.1732 |
| novita/fp8 | fp8 | yes | 47.7 | 128 | 0 | 1.00 | 91.7 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1797.0 | 0.1028 |
| gmicloud/fp8 | fp8 | yes | 46.9 | 128 | 0.00 | 1.00 | 100.0 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2376.5 | 0.0860 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, nebius/fp8, azure/us. Prompts with no plurality (excluded from exact match): 16.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8/priority | fp8 | yes | 89.6 | 144 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1044.0 | 0.0042 |
| cohere | unknown | yes | 88.2 | 144 | 0 | 1.00 | 83.3 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 357.5 | 0.0176 |
| inference-net/fp8 | fp8 | yes | 87.5 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 440.0 | 0.0038 |
| particle-ai/us | unknown | yes | 87.5 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 839.5 | 0.0038 |
| venice/fp8 | fp8 | no | 87.5 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 486.0 | 0.0271 |
| wafer/us | mxfp4 | yes | 87.5 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 391.5 | 0.0048 |
| crusoe/fp8 | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 511.5 | 0.0268 |
| morph/fp8 | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1175.5 | 0.0033 |
| primeintellect | unknown | no | 86.8 | 144 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 585.0 | 0.0162 |
| baseten | unknown | no | 86.1 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 422.0 | 0.0142 |
| deepinfra/fp8 | fp8 | yes | 86.1 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 869.0 | 0.0057 |
| mistral/fp8 | fp8 | yes | 86.1 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 645.0 | 0.0277 |
| novita/fp8 | fp8 | yes | 86.1 | 144 | 0.00 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1265.5 | 0.0150 |
| relace/fp4 | fp4 | no | 86.1 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 528.0 | 0.0044 |
| deepinfra/fp8/flex | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2329.0 | 0.0052 |
| inference-net/us | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 408.5 | 0.0077 |
| cloudflare | unknown | yes | 85.0 | 140 | 0 | 1.00 | 67.4 | 100.0 | 50.0 | 100.0 | 100.0 | 2.80 | 0 | 0 | 1526.0 | 0.0097 |
| atlas-cloud/fp8 | fp8 | yes | 84.7 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1292.5 | 0.0043 |
| parasail/fp8 | fp8 | yes | 84.7 | 144 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 404.0 | 0.0276 |
| particle-ai/us/flex | unknown | yes | 84.7 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 815.5 | 0.0028 |
| stepfun/fp8 | fp8 | no | 84.7 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 436.0 | 0.0138 |
| wafer/mxfp4 | mxfp4 | yes | 84.7 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 376.5 | 0.0041 |
| makora/fp8 | fp8 | yes | 84.0 | 144 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 361.5 | 0.0162 |
| modal | unknown | no | 84.0 | 144 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 474.0 | 0.0231 |
| modelrun/fp4 | fp4 | no | 84.0 | 144 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 733.0 | 0.0156 |
| nebius/fp8 | fp8 | yes | 84.0 | 144 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 925.0 | 0.0280 |
| phala | unknown | yes | 84.0 | 144 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1472.5 | 0.0062 |
| alibaba | unknown | yes | 83.3 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 879.0 | 0.0153 |
| dekallm | unknown | yes | 82.6 | 144 | 0 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 864.0 | 0.0163 |
| together | unknown | no | 82.6 | 144 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 75.0 | 100.0 | 0.00 | 0 | 0 | 250.5 | 0.0276 |
| siliconflow/fp8 | fp8 | no | 82.5 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 768.0 | 0.0271 |
| fireworks | unknown | no | 81.9 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1285.5 | 0.0277 |
| relace/fast | fp4 | no | 81.9 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 451.5 | 0.0265 |
| fireworks/us | unknown | no | 81.2 | 144 | 0 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 481.0 | 0.0408 |
| sail-research/fp4/us | fp4 | yes | 79.7 | 123 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 14.6 | 0 | 0 | 506.0 | 0.0072 |
| sail-research/fp4 | fp4 | yes | 79.5 | 127 | 0.00 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 11.8 | 0 | 0 | 510.0 | 0.0029 |
| ionstream | unknown | yes | 77.1 | 144 | 0 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 836.0 | 0.0145 |
| decart/fp4 | fp4 | yes | 76.4 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 869.5 | 0.0114 |
| streamlake/fp8 | fp8 | no | 76.4 | 144 | 0.00 | 1.00 | 85.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1122.0 | 0.0134 |
| digitalocean | unknown | no | 75.7 | 144 | 0 | 1.00 | 64.6 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 445.0 | 0.0165 |
| gmicloud/fp8 | fp8 | yes | 75.0 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1628.0 | 0.0167 |
| near-ai | unknown | no | 74.3 | 144 | 0 | 1.00 | 60.4 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 669.0 | 0.0274 |
| reka | unknown | no | 73.6 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 664.5 | 0.0166 |
| baidu/fp8 | fp8 | no | 73.2 | 142 | 0.00 | 1.00 | 73.9 | 100.0 | 54.2 | 100.0 | 100.0 | 1.40 | 0 | 0 | 1102.0 | 0.0159 |
| open-inference/fp4 | fp4 | yes | 72.9 | 144 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1376.0 | 0.0044 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| fireworks/spot | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: morph/fp8, particle-ai/us/flex, open-inference/fp4, relace/fp4, wafer/us, particle-ai/us, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, deepinfra/fp8, cloudflare, sail-research/fp4/us, sail-research/fp4, decart/fp4, streamlake/fp8, deepinfra/fp8/priority, stepfun/fp8, deepseek, makora/fp8, primeintellect, wafer/mxfp4, reka, ionstream, alibaba, novita/fp8, modelrun/fp4, dekallm, digitalocean, gmicloud/fp8, cohere, atlas-cloud/fp8, phala, fireworks/spot, modal, baidu/fp8, crusoe/fp8, relace/fast, near-ai, venice/fp8, mistral/fp8, nebius/fp8, siliconflow/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us. Prompts with no plurality (excluded from exact match): 0.

## Footer

- Rows: 12528; errors 357; misrouted 0; truncated (finish_reason length) 35; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.8382; billed: $2.5385; cap $7.0; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
