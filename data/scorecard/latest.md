# Bitdepth scorecard 2026-11-14

Run `2026-11-14-live`, source `live`, started 2026-11-14T14:13:25Z, finished 2026-11-14T23:54:57Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mancer/fp8 | fp8 | yes | 99.3 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 775.0 | 0.0068 |
| baseten/fp4 | fp4 | no | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 412.0 | 0.0127 |
| cerebras/fp16 | fp16 | yes | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 265.5 | 0.0369 |
| crusoe/bf16 | bf16 | yes | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 519.0 | 0.0065 |
| dekallm/bf16 | bf16 | yes | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 906.5 | 0.0041 |
| sambanova | unknown | no | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 443.5 | 0.0195 |
| together | unknown | no | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 545.0 | 0.0179 |
| amazon-bedrock | unknown | no | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 560.0 | 0.0181 |
| baseten/fp4/us | fp4 | no | 97.9 | 141 | 0 | 1.00 | 100.0 | 95.8 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 399.5 | 0.0129 |
| coreweave/fp4 | fp4 | yes | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 672.0 | 0.0040 |
| deepinfra/fp8 | fp8 | yes | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.70 | 0 | 1 | 1524.0 | 0.0245 |
| io-net/fp4 | fp4 | no | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1094.5 | 0.0235 |
| near-ai/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1107.5 | 0.0038 |
| nebius/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 460.5 | 0.0176 |
| parasail/fast | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 522.0 | 0.0193 |
| primeintellect/fp4 | fp4 | yes | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 696.0 | 0.0038 |
| siliconflow/fp8 | fp8 | no | 97.2 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1985.0 | 0.0264 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 544.5 | 0.0182 |
| deepinfra/bf16 | bf16 | yes | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1026.0 | 0.0048 |
| groq | unknown | yes | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 309.5 | 0.0181 |
| sail-research/fp4 | fp4 | yes | 95.7 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 2 | 907.5 | 0.0084 |
| akashml/fp4 | fp4 | yes | 94.3 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 990.0 | 0.0042 |
| google-vertex/global | unknown | yes | 94.3 | 141 | 0.00 | 1.00 | 93.8 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 805.0 | 0.0108 |
| parasail/fp4 | fp4 | yes | 94.3 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 537.0 | 0.0146 |
| digitalocean | unknown | no | 93.6 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1370.0 | 0.0087 |
| venice/int4 | int4 | no | 83.0 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 75.0 | 100.0 | 87.5 | 0.00 | 0 | 13 | 1560.0 | 0.0048 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 3.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8 | fp8 | yes | 86.8 | 129 | 4 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 855.0 | 0.1177 |
| alibaba/fp8/us-east-1 | fp8 | yes | 84.5 | 129 | 7.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2551.5 | 0.1412 |
| venice | unknown | no | 84.5 | 129 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1181.0 | 0.0684 |
| streamlake/fp8 | fp8 | no | 82.9 | 129 | 4.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1995.5 | 0.0078 |
| atlas-cloud/fp4 | fp4 | yes | 78.3 | 129 | 4.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2522.0 | 0.1518 |
| baidu/fp8 | fp8 | no | 78.3 | 129 | 4.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1385.5 | 0.0188 |
| alibaba/fp8 | fp8 | yes | 76.7 | 129 | 5.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2878.0 | 0.1281 |
| relace/fp4 | fp4 | no | 76.0 | 129 | 4 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 906.5 | 0.0795 |
| siliconflow/fp8 | fp8 | no | 70.5 | 129 | 3.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3961.0 | 0.0866 |
| azure/us | unknown | no | 62.8 | 129 | 1.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1068.0 | 0.1732 |
| digitalocean | unknown | no | 58.9 | 129 | 1 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1479.0 | 0.0948 |
| novita/fp8 | fp8 | yes | 49.6 | 129 | 1 | 1.00 | 100.0 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2170.0 | 0.1302 |
| gmicloud/fp8 | fp8 | yes | 48.8 | 129 | 0.50 | 1.00 | 97.9 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2443.0 | 0.0840 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, azure/us. Prompts with no plurality (excluded from exact match): 15.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cloudflare | unknown | yes | 90.6 | 128 | 0.00 | 1.00 | 68.2 | 100.0 | 50.0 | 100.0 | 100.0 | 10.4 | 0 | 0 | 2950.0 | 0.0067 |
| novita/fp8 | fp8 | yes | 90.1 | 142 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1363.0 | 0.0037 |
| particle-ai/us | unknown | yes | 90.1 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 661.5 | 0.0041 |
| dekallm | unknown | yes | 89.4 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1009.0 | 0.0164 |
| fireworks | unknown | no | 89.4 | 142 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1307.5 | 0.0082 |
| modal | unknown | no | 89.4 | 142 | 0 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 643.5 | 0.0229 |
| baseten | unknown | no | 88.0 | 142 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 716.0 | 0.0277 |
| mistral/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 664.5 | 0.0275 |
| sail-research/fp4/us | fp4 | yes | 88.0 | 142 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1393.5 | 0.0058 |
| fireworks/spot | unknown | no | 87.3 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1287.5 | 0.0187 |
| fireworks/us | unknown | no | 87.3 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 439.0 | 0.0413 |
| parasail/fp8 | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 503.0 | 0.0274 |
| siliconflow/fp8 | fp8 | no | 87.3 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 966.5 | 0.0250 |
| venice/fp8 | fp8 | no | 87.3 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 841.5 | 0.0261 |
| wafer/mxfp4 | mxfp4 | yes | 87.3 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 630.0 | 0.0027 |
| alibaba | unknown | yes | 86.6 | 142 | 0 | 1.00 | 64.6 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 903.0 | 0.0095 |
| atlas-cloud/fp8 | fp8 | yes | 86.6 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1267.0 | 0.0043 |
| cohere/fp8 | fp8 | yes | 86.6 | 142 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 435.0 | 0.0134 |
| deepinfra/fp8 | fp8 | yes | 86.6 | 142 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 599.5 | 0.0063 |
| sail-research/fp4 | fp4 | yes | 86.6 | 142 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1535.0 | 0.0046 |
| wafer/us | mxfp4 | yes | 86.6 | 142 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 534.5 | 0.0048 |
| baseten/fast | unknown | no | 86.5 | 133 | 0.00 | 1.00 | 65.9 | 100.0 | 45.5 | 100.0 | 100.0 | 6.20 | 0 | 0 | 310.0 | 0.0524 |
| coreweave/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 550.5 | 0.0280 |
| deepinfra/fp8/flex | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2475.0 | 0.0039 |
| makora/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 441.5 | 0.0164 |
| morph/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 564.0 | 0.0054 |
| morph/fast | fp8 | yes | 85.2 | 142 | 0 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 521.0 | 0.0085 |
| nebius/fp8 | fp8 | yes | 85.2 | 142 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1090.5 | 0.0279 |
| relace/fp4 | fp4 | no | 85.2 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1145.5 | 0.0109 |
| stepfun/fp8 | fp8 | no | 85.2 | 142 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 544.0 | 0.0097 |
| crusoe/fp8 | fp8 | yes | 84.5 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 633.5 | 0.0271 |
| deepinfra/fp8/priority | fp8 | yes | 84.5 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 630.0 | 0.0037 |
| together | unknown | no | 84.5 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 95.8 | 100.0 | 0.00 | 0 | 0 | 384.5 | 0.0275 |
| inference-net/fp8 | fp8 | yes | 83.8 | 142 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 455.5 | 0.0070 |
| ionstream | unknown | yes | 83.8 | 142 | 0 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 548.0 | 0.0184 |
| particle-ai/us/flex | unknown | yes | 83.8 | 142 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 652.0 | 0.0033 |
| primalabs | unknown | yes | 83.8 | 142 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 506.0 | 0.0221 |
| primeintellect | unknown | no | 83.8 | 142 | 0 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 647.0 | 0.0059 |
| inference-net/us | fp8 | yes | 81.7 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 451.0 | 0.0085 |
| streamlake/fp8 | fp8 | no | 81.7 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1502.0 | 0.0102 |
| gmicloud/fp8 | fp8 | yes | 81.0 | 142 | 0 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 889.5 | 0.0166 |
| river | unknown | yes | 79.6 | 142 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 571.5 | 0.0109 |
| baidu/fp8 | fp8 | no | 77.5 | 142 | 0.00 | 1.00 | 83.3 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 770.5 | 0.0092 |
| ionstream/flex | unknown | yes | 76.1 | 142 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 427.5 | 0.0070 |
| near-ai | unknown | no | 76.1 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1093.5 | 0.0277 |
| reka | unknown | no | 75.4 | 142 | 0 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 673.0 | 0.0169 |
| digitalocean | unknown | no | 71.8 | 142 | 0.00 | 1.00 | 64.6 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 538.5 | 0.0165 |
| open-inference/fp4 | fp4 | yes | 71.8 | 142 | 0.00 | 1.00 | 52.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2318.0 | 0.0086 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, primeintellect, particle-ai/us, wafer/mxfp4, open-inference/fp4, sail-research/fp4/us, sail-research/fp4, ionstream/flex, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, baidu/fp8, deepinfra/fp8, cloudflare, morph/fast, morph/fp8, stepfun/fp8, alibaba, streamlake/fp8, river, relace/fp4, deepinfra/fp8/priority, cohere/fp8, deepseek, makora/fp8, reka, novita/fp8, dekallm, digitalocean, gmicloud/fp8, atlas-cloud/fp8, ionstream, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, mistral/fp8, coreweave/fp8, near-ai, venice/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast. Prompts with no plurality (excluded from exact match): 2.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 126 | n/a | 1.00 | 100.0 | 50.0 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 17 | 3964.0 | 0.1022 |
| mistral/zdr | unknown | yes | 100.0 | 126 | n/a | 1.00 | 97.9 | 54.2 | 87.5 | 100.0 | 91.7 | 0.00 | 0 | 16 | 4290.5 | 0.1195 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 18.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| particle-ai/nvfp4 | nvfp4 | yes | 100.0 | 144 | n/a | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 616.0 | 0.0119 |
| relace/fp4 | fp4 | yes | 99.3 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1085.0 | 0.0036 |
| crusoe/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 914.5 | 0.0145 |
| darkbloom/fp4 | fp4 | yes | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 2.80 | 0 | 0 | 2079.5 | 0.0059 |
| parasail/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 668.0 | 0.0144 |
| river | unknown | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 968.5 | 0.0115 |
| streamlake/fp8 | fp8 | no | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1899.5 | 0.0085 |
| gmicloud/fp8 | fp8 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1674.0 | 0.0072 |
| kt | unknown | no | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 685.5 | 0.0144 |
| open-inference/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1071.0 | 0.0063 |
| deepinfra/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 700.5 | 0.0145 |
| dekallm | unknown | yes | 97.2 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 926.0 | 0.0104 |
| friendli | unknown | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 369.5 | 0.0144 |
| morph/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1433.0 | 0.0086 |
| nextbit/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 696.5 | 0.0118 |
| sail-research/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1095.5 | 0.0166 |
| sail-research/us | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1126.0 | 0.0169 |
| venice | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2328.5 | 0.0153 |
| atlas-cloud/fp8 | fp8 | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 91.3 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2379.0 | 0.0132 |
| baseten/fp8 | fp8 | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 512.0 | 0.0145 |
| cohere/nvfp4 | nvfp4 | yes | 96.5 | 144 | 0 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 532.5 | 0.0150 |
| inceptron/fp8 | fp8 | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 580.0 | 0.0162 |
| near-ai/fp8 | fp8 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1245.5 | 0.0087 |
| together | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 511.0 | 0.0145 |
| fireworks/us | unknown | no | 95.7 | 140 | 0.00 | 1.00 | 97.9 | 100.0 | 87.0 | 100.0 | 100.0 | 2.80 | 0 | 0 | 586.0 | 0.0210 |
| parasail/fast | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 504.5 | 0.0183 |
| siliconflow/fp8 | fp8 | no | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1072.0 | 0.0099 |
| coreweave/nvfp4 | nvfp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 612.5 | 0.0113 |
| mistral | unknown | yes | 94.4 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 771.5 | 0.0144 |
| nebius/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 988.5 | 0.0144 |
| novita/fp8 | fp8 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1340.5 | 0.0081 |
| fireworks | unknown | no | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2129.0 | 0.0145 |
| makora/fp4 | fp4 | yes | 93.1 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 619.0 | 0.0126 |
| modal/fp4 | fp4 | no | 92.4 | 144 | 0 | 1.00 | 95.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 482.0 | 0.0144 |
| z-ai/fp8 | fp8 | no | 92.4 | 144 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1598.0 | 0.0145 |
| inference-net/us | fp4 | yes | 91.7 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 79.2 | 100.0 | 95.8 | 0.00 | 0 | 1 | 531.0 | 0.0104 |
| tenstorrent/fp8 | fp8 | yes | 91.7 | 133 | 0 | 1.00 | 89.4 | 95.2 | 72.7 | 100.0 | 100.0 | 7.60 | 0 | 0 | 988.0 | 0.0065 |
| inference-net/fp4 | fp4 | yes | 88.2 | 144 | 0 | 1.00 | 97.9 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 539.0 | 0.0099 |
| reka | unknown | yes | 88.2 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 676.5 | 0.0110 |
| digitalocean | unknown | no | 86.1 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 637.5 | 0.0108 |
| wafer/us | nvfp4 | yes | 85.4 | 144 | 0 | 1.00 | 93.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 667.0 | 0.0043 |
| wafer/nvfp4 | nvfp4 | yes | 77.8 | 144 | 0.00 | 1.00 | 85.4 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 680.5 | 0.0066 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, wafer/us, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, tenstorrent/fp8, gmicloud/fp8, near-ai/fp8, novita/fp8, streamlake/fp8, morph/fp8, siliconflow/fp8, dekallm, inference-net/us, inference-net/fp4, digitalocean, reka, coreweave/nvfp4, river, nextbit/fp4, particle-ai/nvfp4, makora/fp4, mistral, kt, cohere/nvfp4, nebius/fp4, modal/fp4, crusoe/fp4, atlas-cloud/fp8, fireworks, friendli, together, parasail/fp4, baseten/fp8, venice, deepinfra/fp4, z-ai/fp8, inceptron/fp8, sail-research/us, sail-research/fp4, parasail/fast, fireworks/us. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 100.0 | 126 | n/a | 1.00 | 47.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 542.5 | 0.0124 |
| novita/bf16 | bf16 | yes | 100.0 | 126 | n/a | 1.00 | 43.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1040.5 | 0.0124 |
| sambanova | unknown | no | 98.4 | 122 | 0.00 | 1.00 | 47.8 | 100.0 | 54.2 | 100.0 | 100.0 | 3.50 | 0 | 0 | 1798.0 | 0.0325 |
| siliconflow/fp8 | fp8 | no | 92.9 | 126 | 0 | 1.00 | 43.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1167.0 | 0.0611 |
| parasail/fp8 | fp8 | yes | 92.1 | 126 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 667.5 | 0.0132 |
| friendli | unknown | yes | 89.7 | 126 | 0 | 1.00 | 37.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 301.5 | 0.0124 |
| deepinfra/fp8 | fp8 | yes | 88.9 | 126 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 599.0 | 0.0171 |
| deepinfra/fp8/flex | fp8 | yes | 88.9 | 126 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1508.5 | 0.0137 |
| deepinfra/fp8/priority | fp8 | yes | 88.9 | 126 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 625.5 | 0.0256 |
| modal | unknown | no | 87.3 | 126 | 0.00 | 1.00 | 37.5 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 524.5 | 0.0261 |
| deepinfra/turbo | fp4 | yes | 85.7 | 126 | 0.00 | 1.00 | 35.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 389.5 | 0.0102 |
| coreweave/fp4 | fp4 | yes | 84.9 | 126 | 0 | 1.00 | 39.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 443.0 | 0.0091 |
| venice/fp4 | fp4 | no | 84.1 | 126 | 0.00 | 1.00 | 37.5 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 738.5 | 0.0105 |
| dekallm | unknown | yes | 83.1 | 124 | 0 | 1.00 | 37.5 | 100.0 | 52.2 | 100.0 | 100.0 | 1.40 | 0 | 0 | 1143.0 | 0.0121 |
| chutes/fp4 | fp4 | yes | 81.7 | 126 | 0 | 1.00 | 35.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2013.0 | 0.0107 |
| kt | unknown | no | 81.7 | 126 | 0 | 1.00 | 33.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 793.5 | 0.0091 |
| primeintellect/fp4 | fp4 | yes | 79.4 | 126 | 0.00 | 1.00 | 29.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 451.0 | 0.0166 |
| nextbit/fp4 | fp4 | yes | 73.8 | 126 | 0 | 1.00 | 35.4 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 510.5 | 0.0131 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: crusoe/bf16, novita/bf16. Prompts with no plurality (excluded from exact match): 18.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| primalabs/fp8 | fp8 | yes | 97.8 | 135 | 0 | 1.00 | 77.1 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 564.0 | 0.3527 |
| xiaomi/fp8 | fp8 | no | 96.8 | 124 | 0.00 | 1.00 | 72.1 | 100.0 | 63.6 | 100.0 | 100.0 | 7.60 | 0 | 0 | 1806.0 | 0.0382 |
| deepinfra/fp8 | fp8 | yes | 92.6 | 135 | 0.00 | 1.00 | 68.8 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 727.5 | 0.0341 |
| streamlake | unknown | no | 92.6 | 135 | 0.00 | 1.00 | 72.9 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1715.0 | 0.0393 |
| gmicloud/bf16 | bf16 | yes | 74.6 | 134 | 0.00 | 1.00 | 59.6 | 100.0 | 70.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2847.0 | 0.0274 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: gmicloud/bf16, deepinfra/fp8, xiaomi/fp8, streamlake, primalabs/fp8. Prompts with no plurality (excluded from exact match): 9.

## Noise floor (self-check, two passes one hour apart)

| Model | Endpoint | Prompts | Agreement % |
|---|---|---|---|
| deepseek-v4-pro | relace/fp4 | 36 | 83.3 |
| deepseek-v4-pro | deepinfra/fp8 | 36 | 77.8 |
| deepseek-v4-pro | baidu/fp8 | 36 | 77.8 |
| deepseek-v4-pro | venice | 36 | 75.0 |
| deepseek-v4-pro | siliconflow/fp8 | 36 | 75.0 |
| deepseek-v4-pro | alibaba/fp8/us-east-1 | 36 | 72.2 |
| deepseek-v4-pro | atlas-cloud/fp4 | 36 | 72.2 |
| deepseek-v4-pro | streamlake/fp8 | 36 | 69.4 |
| deepseek-v4-pro | alibaba/fp8 | 36 | 69.4 |
| deepseek-v4-pro | novita/fp8 | 36 | 69.4 |
| deepseek-v4-pro | gmicloud/fp8 | 36 | 61.1 |
| deepseek-v4-pro | azure/us | 36 | 55.6 |
| deepseek-v4-pro | digitalocean | 36 | 50.0 |
| deepseek-v4.1-flash-1017 | relace/fp4 | 36 | 100.0 |
| deepseek-v4.1-flash-1017 | river | 36 | 100.0 |
| deepseek-v4.1-flash-1017 | baseten/fast | 34 | 100.0 |
| deepseek-v4.1-flash-1017 | primeintellect | 36 | 97.2 |
| deepseek-v4.1-flash-1017 | stepfun/fp8 | 36 | 97.2 |
| deepseek-v4.1-flash-1017 | primalabs | 36 | 97.2 |
| deepseek-v4.1-flash-1017 | modal | 36 | 97.2 |
| deepseek-v4.1-flash-1017 | venice/fp8 | 36 | 97.2 |
| deepseek-v4.1-flash-1017 | baseten | 36 | 97.2 |
| deepseek-v4.1-flash-1017 | sail-research/fp4 | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | baidu/fp8 | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | open-inference/fp4 | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | cohere/fp8 | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | ionstream | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | coreweave/fp8 | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | siliconflow/fp8 | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | fireworks/us | 36 | 94.4 |
| deepseek-v4.1-flash-1017 | inference-net/fp8 | 36 | 91.7 |
| deepseek-v4.1-flash-1017 | inference-net/us | 36 | 91.7 |
| deepseek-v4.1-flash-1017 | morph/fast | 36 | 91.7 |
| deepseek-v4.1-flash-1017 | streamlake/fp8 | 36 | 91.7 |
| deepseek-v4.1-flash-1017 | mistral/fp8 | 36 | 91.7 |
| deepseek-v4.1-flash-1017 | fireworks | 36 | 91.7 |
| deepseek-v4.1-flash-1017 | parasail/fp8 | 36 | 91.7 |
| deepseek-v4.1-flash-1017 | particle-ai/us/flex | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | sail-research/fp4/us | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | particle-ai/us | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | ionstream/flex | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | morph/fp8 | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | alibaba | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | gmicloud/fp8 | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | fireworks/spot | 36 | 88.9 |
| deepseek-v4.1-flash-1017 | makora/fp8 | 36 | 86.1 |
| deepseek-v4.1-flash-1017 | dekallm | 36 | 86.1 |
| deepseek-v4.1-flash-1017 | atlas-cloud/fp8 | 36 | 86.1 |
| deepseek-v4.1-flash-1017 | crusoe/fp8 | 36 | 86.1 |
| deepseek-v4.1-flash-1017 | together | 36 | 86.1 |
| deepseek-v4.1-flash-1017 | nebius/fp8 | 36 | 86.1 |
| deepseek-v4.1-flash-1017 | cloudflare | 33 | 84.8 |
| deepseek-v4.1-flash-1017 | wafer/mxfp4 | 36 | 83.3 |
| deepseek-v4.1-flash-1017 | wafer/us | 36 | 83.3 |
| deepseek-v4.1-flash-1017 | deepinfra/fp8/flex | 36 | 83.3 |
| deepseek-v4.1-flash-1017 | deepinfra/fp8 | 36 | 80.6 |
| deepseek-v4.1-flash-1017 | reka | 36 | 80.6 |
| deepseek-v4.1-flash-1017 | novita/fp8 | 36 | 80.6 |
| deepseek-v4.1-flash-1017 | deepinfra/fp8/priority | 36 | 77.8 |
| deepseek-v4.1-flash-1017 | digitalocean | 36 | 69.4 |
| deepseek-v4.1-flash-1017 | near-ai | 36 | 69.4 |
| gemma-4-31b-it | deepinfra/fp8 | 36 | 100.0 |
| gemma-4-31b-it | sambanova | 36 | 100.0 |
| gemma-4-31b-it | coreweave/fp4 | 36 | 97.2 |
| gemma-4-31b-it | deepinfra/fp8/flex | 36 | 97.2 |
| gemma-4-31b-it | crusoe/bf16 | 36 | 97.2 |
| gemma-4-31b-it | deepinfra/fp8/priority | 36 | 94.4 |
| gemma-4-31b-it | nextbit/fp4 | 36 | 91.7 |
| gemma-4-31b-it | novita/bf16 | 36 | 91.7 |
| gemma-4-31b-it | siliconflow/fp8 | 36 | 91.7 |
| gemma-4-31b-it | kt | 36 | 88.9 |
| gemma-4-31b-it | friendli | 36 | 86.1 |
| gemma-4-31b-it | modal | 36 | 86.1 |
| gemma-4-31b-it | deepinfra/turbo | 36 | 83.3 |
| gemma-4-31b-it | parasail/fp8 | 36 | 83.3 |
| gemma-4-31b-it | venice/fp4 | 36 | 80.6 |
| gemma-4-31b-it | chutes/fp4 | 36 | 77.8 |
| gemma-4-31b-it | dekallm | 35 | 77.1 |
| gemma-4-31b-it | primeintellect/fp4 | 36 | 75.0 |
| glm-5.3-flash | tenstorrent/fp8 | 27 | 100.0 |
| glm-5.3-flash | open-inference/fp4 | 36 | 100.0 |
| glm-5.3-flash | gmicloud/fp8 | 36 | 100.0 |
| glm-5.3-flash | river | 36 | 100.0 |
| glm-5.3-flash | particle-ai/nvfp4 | 36 | 100.0 |
| glm-5.3-flash | mistral | 36 | 100.0 |
| glm-5.3-flash | fireworks/us | 36 | 100.0 |
| glm-5.3-flash | darkbloom/fp4 | 36 | 97.2 |
| glm-5.3-flash | relace/fp4 | 36 | 97.2 |
| glm-5.3-flash | near-ai/fp8 | 36 | 97.2 |
| glm-5.3-flash | dekallm | 36 | 97.2 |
| glm-5.3-flash | streamlake/fp8 | 36 | 97.2 |
| glm-5.3-flash | kt | 36 | 97.2 |
| glm-5.3-flash | nebius/fp4 | 36 | 97.2 |
| glm-5.3-flash | together | 36 | 97.2 |
| glm-5.3-flash | parasail/fp4 | 36 | 97.2 |
| glm-5.3-flash | inceptron/fp8 | 36 | 97.2 |
| glm-5.3-flash | deepinfra/fp4 | 36 | 97.2 |
| glm-5.3-flash | parasail/fast | 36 | 97.2 |
| glm-5.3-flash | sail-research/us | 36 | 97.2 |
| glm-5.3-flash | sail-research/fp4 | 36 | 97.2 |
| glm-5.3-flash | morph/fp8 | 36 | 94.4 |
| glm-5.3-flash | siliconflow/fp8 | 36 | 94.4 |
| glm-5.3-flash | novita/fp8 | 36 | 94.4 |
| glm-5.3-flash | coreweave/nvfp4 | 36 | 94.4 |
| glm-5.3-flash | nextbit/fp4 | 36 | 94.4 |
| glm-5.3-flash | makora/fp4 | 36 | 94.4 |
| glm-5.3-flash | friendli | 36 | 94.4 |
| glm-5.3-flash | baseten/fp8 | 36 | 94.4 |
| glm-5.3-flash | reka | 36 | 91.7 |
| glm-5.3-flash | digitalocean | 36 | 91.7 |
| glm-5.3-flash | modal/fp4 | 36 | 91.7 |
| glm-5.3-flash | venice | 36 | 91.7 |
| glm-5.3-flash | atlas-cloud/fp8 | 36 | 91.7 |
| glm-5.3-flash | inference-net/us | 36 | 88.9 |
| glm-5.3-flash | cohere/nvfp4 | 36 | 88.9 |
| glm-5.3-flash | crusoe/fp4 | 36 | 88.9 |
| glm-5.3-flash | fireworks | 36 | 86.1 |
| glm-5.3-flash | wafer/us | 36 | 83.3 |
| glm-5.3-flash | wafer/nvfp4 | 36 | 83.3 |
| glm-5.3-flash | inference-net/fp4 | 36 | 80.6 |
| glm-5.3-flash | z-ai/fp8 | 36 | 77.8 |
| gpt-oss-120b | near-ai/fp4 | 26 | 100.0 |
| gpt-oss-120b | baseten/fp4/us | 36 | 100.0 |
| gpt-oss-120b | sambanova | 36 | 100.0 |
| gpt-oss-120b | amazon-bedrock | 36 | 100.0 |
| gpt-oss-120b | groq | 36 | 100.0 |
| gpt-oss-120b | cerebras/fp16 | 36 | 100.0 |
| gpt-oss-120b | parasail/fast | 36 | 100.0 |
| gpt-oss-120b | deepinfra/fp8 | 36 | 100.0 |
| gpt-oss-120b | akashml/fp4 | 36 | 97.2 |
| gpt-oss-120b | sail-research/fp4 | 36 | 97.2 |
| gpt-oss-120b | io-net/fp4 | 36 | 97.2 |
| gpt-oss-120b | siliconflow/fp8 | 36 | 97.2 |
| gpt-oss-120b | google-vertex/global | 36 | 97.2 |
| gpt-oss-120b | mancer/fp8 | 36 | 94.4 |
| gpt-oss-120b | baseten/fp4 | 36 | 94.4 |
| gpt-oss-120b | amazon-bedrock/eu-west-1 | 36 | 94.4 |
| gpt-oss-120b | nebius/fp4 | 36 | 94.4 |
| gpt-oss-120b | together | 36 | 94.4 |
| gpt-oss-120b | digitalocean | 36 | 94.4 |
| gpt-oss-120b | crusoe/bf16 | 36 | 91.7 |
| gpt-oss-120b | deepinfra/bf16 | 36 | 91.7 |
| gpt-oss-120b | primeintellect/fp4 | 36 | 91.7 |
| gpt-oss-120b | venice/int4 | 36 | 91.7 |
| gpt-oss-120b | dekallm/bf16 | 36 | 91.7 |
| gpt-oss-120b | coreweave/fp4 | 36 | 88.9 |
| gpt-oss-120b | parasail/fp4 | 36 | 83.3 |
| mimo-v2.6-pro | primalabs/fp8 | 36 | 97.2 |
| mimo-v2.6-pro | deepinfra/fp8 | 36 | 94.4 |
| mimo-v2.6-pro | streamlake | 36 | 94.4 |
| mimo-v2.6-pro | xiaomi/fp8 | 36 | 86.1 |
| mimo-v2.6-pro | gmicloud/bf16 | 36 | 72.2 |
| mistral-large-4-0 | mistral/eu | 4 | 100.0 |
| mistral-large-4-0 | mistral/zdr | 4 | 100.0 |

## Footer

- Rows: 22320; errors 208; misrouted 0; truncated (finish_reason length) 64; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $6.9146; billed: $5.3329; cap $7.75; runtime budget stop: True.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
