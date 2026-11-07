# Bitdepth scorecard 2026-11-07

Run `2026-11-07-live`, source `live`, started 2026-11-07T14:06:21Z, finished 2026-11-07T19:00:15Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 100.0 | 140 | n/a | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 556.0 | 0.0066 |
| cerebras/fp16 | fp16 | yes | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 293.0 | 0.0372 |
| parasail/fast | fp4 | yes | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 489.5 | 0.0199 |
| baseten/fp4 | fp4 | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 2 | 408.5 | 0.0131 |
| baseten/fp4/us | fp4 | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 405.5 | 0.0131 |
| deepinfra/bf16 | bf16 | yes | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1896.0 | 0.0048 |
| mancer/fp8 | fp8 | yes | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 771.0 | 0.0069 |
| parasail/fp4 | fp4 | yes | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 570.0 | 0.0152 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 865.0 | 0.0183 |
| deepinfra/fp8 | fp8 | yes | 97.1 | 138 | 0.00 | 1.00 | 100.0 | 100.0 | 82.6 | 100.0 | 100.0 | 1.40 | 0 | 0 | 1514.5 | 0.0256 |
| dekallm/bf16 | bf16 | yes | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1083.0 | 0.0042 |
| groq | unknown | yes | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 319.5 | 0.0181 |
| sambanova | unknown | no | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 517.5 | 0.0206 |
| akashml/fp4 | fp4 | yes | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 794.0 | 0.0042 |
| google-vertex/global | unknown | yes | 96.4 | 137 | 0 | 1.00 | 100.0 | 100.0 | 82.6 | 100.0 | 100.0 | 2.10 | 0 | 0 | 835.0 | 0.0106 |
| primeintellect/fp4 | fp4 | yes | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 921.5 | 0.0021 |
| together | unknown | no | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 572.5 | 0.0183 |
| amazon-bedrock | unknown | no | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 866.0 | 0.0181 |
| nebius/fp4 | fp4 | yes | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 497.0 | 0.0177 |
| siliconflow/fp8 | fp8 | no | 95.7 | 139 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2144.0 | 0.0259 |
| near-ai/fp4 | fp4 | yes | 95.0 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 854.5 | 0.0039 |
| sail-research/fp4 | fp4 | yes | 95.0 | 140 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 921.0 | 0.0086 |
| coreweave/fp4 | fp4 | yes | 93.6 | 140 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 566.0 | 0.0041 |
| digitalocean | unknown | no | 93.6 | 140 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1331.5 | 0.0088 |
| phala | unknown | yes | 92.9 | 140 | 0.00 | 1.00 | 97.9 | 95.8 | 87.5 | 100.0 | 95.8 | 0.00 | 0 | 2 | 1409.5 | 0.0249 |
| venice/int4 | int4 | no | 85.7 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 12 | 1811.0 | 0.0049 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 4.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 84.3 | 140 | 8.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2162.0 | 0.1268 |
| alibaba/fp8 | fp8 | yes | 82.1 | 140 | 8 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2387.5 | 0.1316 |
| venice | unknown | no | 77.9 | 140 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1260.5 | 0.0691 |
| baidu/fp8 | fp8 | no | 77.1 | 140 | 4.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1476.0 | 0.0587 |
| nebius/fp8 | fp8 | yes | 75.7 | 140 | 7.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1450.5 | 0.1596 |
| relace/fp4 | fp4 | no | 75.7 | 140 | 7.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 864.5 | 0.0798 |
| streamlake/fp8 | fp8 | no | 75.7 | 140 | 8.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2359.0 | 0.0245 |
| atlas-cloud/fp4 | fp4 | yes | 74.3 | 140 | 5.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2679.5 | 0.1524 |
| deepinfra/fp8 | fp8 | yes | 73.6 | 140 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1074.0 | 0.1184 |
| siliconflow/fp8 | fp8 | no | 65.7 | 140 | 3.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2059.0 | 0.0869 |
| digitalocean | unknown | no | 56.4 | 140 | 1 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1549.5 | 0.0951 |
| azure/us | unknown | no | 55.0 | 140 | 1 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1263.5 | 0.1743 |
| gmicloud/fp8 | fp8 | yes | 41.4 | 140 | 1.00 | 1.00 | 100.0 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2451.0 | 0.0860 |
| novita/fp8 | fp8 | yes | 41.4 | 140 | 1.00 | 1.00 | 97.9 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2086.0 | 0.0922 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, nebius/fp8, azure/us. Prompts with no plurality (excluded from exact match): 4.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cloudflare | unknown | yes | 92.9 | 141 | 0.00 | 1.00 | 68.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1233.0 | 0.0064 |
| particle-ai/us | unknown | yes | 89.4 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 547.5 | 0.0038 |
| dekallm | unknown | yes | 88.7 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 859.5 | 0.0162 |
| makora/fp8 | fp8 | yes | 88.7 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 369.0 | 0.0160 |
| cohere/fp8 | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 336.0 | 0.0175 |
| deepinfra/fp8/flex | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1400.5 | 0.0067 |
| deepinfra/fp8/priority | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 64.6 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 423.5 | 0.0034 |
| primeintellect | unknown | no | 87.3 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 513.0 | 0.0131 |
| relace/fast | fp4 | no | 87.3 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 385.0 | 0.0264 |
| alibaba | unknown | yes | 86.6 | 142 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 940.0 | 0.0069 |
| inference-net/fp8 | fp8 | yes | 86.6 | 142 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 417.0 | 0.0036 |
| venice/fp8 | fp8 | no | 86.6 | 142 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 924.5 | 0.0276 |
| deepinfra/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 465.5 | 0.0025 |
| morph/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 689.0 | 0.0029 |
| primalabs | unknown | yes | 85.8 | 106 | 0 | 1.00 | 61.5 | 100.0 | 47.4 | 100.0 | 100.0 | 25.7 | 0 | 0 | 580.0 | 0.0173 |
| atlas-cloud/fp8 | fp8 | yes | 85.2 | 142 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1273.5 | 0.0045 |
| coreweave/fp8 | fp8 | yes | 85.2 | 142 | 0 | 1.00 | 70.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 365.0 | 0.0277 |
| fireworks | unknown | no | 85.2 | 142 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 796.5 | 0.0060 |
| crusoe/fp8 | fp8 | yes | 84.5 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 561.0 | 0.0265 |
| relace/fp4 | fp4 | no | 84.5 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1035.5 | 0.0023 |
| wafer/us | mxfp4 | yes | 84.5 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 377.5 | 0.0048 |
| novita/fp8 | fp8 | yes | 83.8 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1290.0 | 0.0152 |
| siliconflow/fp8 | fp8 | no | 83.8 | 142 | 0 | 1.00 | 68.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 856.0 | 0.0250 |
| stepfun/fp8 | fp8 | no | 83.8 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 668.0 | 0.0126 |
| wafer/mxfp4 | mxfp4 | yes | 83.8 | 142 | 0 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 397.0 | 0.0030 |
| baseten/fast | unknown | no | 83.2 | 125 | 0 | 1.00 | 65.9 | 100.0 | 30.0 | 100.0 | 100.0 | 12.5 | 0 | 0 | 262.0 | 0.0486 |
| decart/fp8 | fp8 | yes | 83.1 | 142 | 0.00 | 1.00 | 60.4 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 929.5 | 0.0111 |
| fireworks/us | unknown | no | 83.1 | 142 | 0.00 | 1.00 | 60.4 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 425.0 | 0.0414 |
| gmicloud/fp8 | fp8 | yes | 83.1 | 142 | 0.00 | 1.00 | 62.5 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 953.5 | 0.0166 |
| modelrun/fp4 | fp4 | no | 83.1 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 730.0 | 0.0156 |
| nebius/fp8 | fp8 | yes | 83.1 | 142 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1050.5 | 0.0278 |
| particle-ai/us/flex | unknown | yes | 83.1 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 501.5 | 0.0028 |
| phala | unknown | yes | 83.1 | 142 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1498.5 | 0.0062 |
| fireworks/spot | unknown | no | 83.0 | 141 | 0.00 | 1.00 | 70.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 850.0 | 0.0195 |
| baseten | unknown | no | 82.4 | 142 | 0 | 1.00 | 62.5 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 386.0 | 0.0273 |
| inference-net/us | fp8 | yes | 82.4 | 142 | 0 | 1.00 | 62.5 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 393.0 | 0.0081 |
| mistral/fp8 | fp8 | yes | 82.4 | 142 | 0 | 1.00 | 66.7 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 881.0 | 0.0277 |
| modal | unknown | no | 82.4 | 142 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 590.5 | 0.0230 |
| parasail/fp8 | fp8 | yes | 82.4 | 142 | 0 | 1.00 | 62.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 393.5 | 0.0273 |
| together | unknown | no | 81.0 | 142 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 70.8 | 100.0 | 0.00 | 0 | 0 | 289.0 | 0.0277 |
| digitalocean | unknown | no | 75.4 | 142 | 0 | 1.00 | 56.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 542.5 | 0.0164 |
| ionstream | unknown | yes | 75.4 | 142 | 0 | 1.00 | 66.7 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 585.5 | 0.0148 |
| streamlake/fp8 | fp8 | no | 75.4 | 142 | 0 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1128.5 | 0.0053 |
| baidu/fp8 | fp8 | no | 73.9 | 142 | 0 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 752.5 | 0.0093 |
| near-ai | unknown | no | 71.1 | 142 | 0 | 1.00 | 64.6 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 908.5 | 0.0275 |
| open-inference/fp4 | fp4 | yes | 71.1 | 142 | 0 | 1.00 | 60.4 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1383.0 | 0.0036 |
| reka | unknown | no | 71.1 | 142 | 0 | 1.00 | 77.1 | 95.8 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 722.0 | 0.0168 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, open-inference/fp4, morph/fp8, particle-ai/us/flex, wafer/us, particle-ai/us, wafer/mxfp4, alibaba, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, baidu/fp8, deepinfra/fp8, cloudflare, sail-research/fp4/us, primeintellect, streamlake/fp8, decart/fp8, stepfun/fp8, deepinfra/fp8/priority, deepseek, makora/fp8, sail-research/fp4, reka, ionstream, novita/fp8, modelrun/fp4, dekallm, digitalocean, gmicloud/fp8, cohere/fp8, atlas-cloud/fp8, phala, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, relace/fast, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast. Prompts with no plurality (excluded from exact match): 2.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 135 | n/a | 1.00 | 100.0 | 37.5 | 79.2 | 100.0 | 87.5 | 0.00 | 0 | 19 | 2460.0 | 0.0982 |
| mistral/zdr | unknown | yes | 100.0 | 135 | n/a | 1.00 | 100.0 | 50.0 | 75.0 | 100.0 | 91.7 | 0.00 | 0 | 17 | 2646.5 | 0.1257 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 9.

## Footer

- Rows: 13248; errors 495; misrouted 0; truncated (finish_reason length) 68; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $5.1179; billed: $2.7574; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
