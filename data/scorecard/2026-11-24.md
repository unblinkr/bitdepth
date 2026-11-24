# Bitdepth scorecard 2026-11-24

Run `2026-11-24-live`, source `live`, started 2026-11-24T18:56:45Z, finished 2026-11-24T19:49:48Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4/us | fp4 | no | 99.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 510.5 | 0.0128 |
| cerebras/fp16 | fp16 | yes | 99.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 264.5 | 0.0366 |
| amazon-bedrock/eu-west-1 | unknown | no | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 511.0 | 0.0181 |
| deepinfra/bf16 | bf16 | yes | 98.6 | 142 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.70 | 0 | 0 | 6319.0 | 0.0041 |
| parasail/fp4 | fp4 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 566.0 | 0.0148 |
| amazon-bedrock | unknown | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 567.5 | 0.0179 |
| baseten/fp4 | fp4 | no | 97.2 | 143 | 0.00 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 508.0 | 0.0130 |
| nebius/fp4 | fp4 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 446.0 | 0.0174 |
| crusoe/bf16 | bf16 | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 640.0 | 0.0066 |
| groq | unknown | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 331.0 | 0.0182 |
| mancer/fp8 | fp8 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 857.5 | 0.0103 |
| parasail/fast | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 493.0 | 0.0196 |
| google-vertex/global | unknown | yes | 95.1 | 143 | 0 | 1.00 | 91.7 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 377.5 | 0.0108 |
| near-ai/fp4 | fp4 | yes | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1327.5 | 0.0037 |
| digitalocean | unknown | no | 94.4 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1144.0 | 0.0083 |
| primeintellect/fp4 | fp4 | yes | 94.4 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 581.5 | 0.0362 |
| sambanova | unknown | no | 94.4 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 553.5 | 0.0207 |
| akashml/fp4 | fp4 | yes | 93.7 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1320.0 | 0.0041 |
| coreweave/fp4 | fp4 | yes | 93.7 | 143 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 657.5 | 0.0041 |
| venice/int4 | int4 | no | 83.2 | 143 | 0.00 | 1.00 | 81.2 | 100.0 | 70.8 | 95.8 | 91.7 | 0.00 | 0 | 10 | 2172.5 | 0.0045 |
| siliconflow/fp8 | fp8 | no | 65.7 | 143 | 1 | 1.00 | 81.2 | 4.20 | 70.8 | 100.0 | 75.0 | 0.00 | 0 | 0 | 2174.5 | 0.0214 |
| fireworks | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 1.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 82.4 | 136 | 6.50 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1917.5 | 0.1289 |
| alibaba/fp8/us-east-1 | fp8 | yes | 80.9 | 136 | 4.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1945.5 | 0.1270 |
| deepinfra/fp8/priority | fp8 | yes | 80.1 | 136 | 8 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1283.5 | 0.0712 |
| streamlake/fp8 | fp8 | no | 79.4 | 136 | 6.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2208.0 | 0.0275 |
| venice | unknown | no | 77.9 | 136 | 6.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1884.0 | 0.0694 |
| relace/fp4 | fp4 | no | 77.2 | 136 | 4 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 740.5 | 0.0654 |
| baidu/fp8 | fp8 | no | 75.0 | 136 | 4.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1475.5 | 0.0653 |
| deepinfra/fp8 | fp8 | yes | 74.3 | 136 | 4 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1442.0 | 0.1481 |
| deepinfra/fp8/flex | fp8 | yes | 69.2 | 107 | 3 | 1.00 | 100.0 | 100.0 | 37.5 | 100.0 | 94.4 | 20.8 | 0 | 0 | 1788.5 | 0.0457 |
| siliconflow/fp8 | fp8 | no | 64.0 | 136 | 3 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1933.0 | 0.0808 |
| azure/us | unknown | no | 58.1 | 136 | 1 | 1.00 | 95.8 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1094.5 | 0.1748 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, siliconflow/fp8, deepinfra/fp8/flex, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 8.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fast | unknown | no | 92.7 | 110 | 0.00 | 1.00 | 60.5 | 100.0 | 52.9 | 100.0 | 100.0 | 22.9 | 0 | 0 | 330.0 | 0.0429 |
| primeintellect | unknown | no | 91.6 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 457.5 | 0.0160 |
| venice/fp8 | fp8 | no | 89.5 | 143 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1038.0 | 0.0278 |
| inference-net/fp8 | fp8 | yes | 88.8 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 459.0 | 0.0077 |
| cloudflare | unknown | yes | 88.1 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1110.5 | 0.0069 |
| google-vertex/global | unknown | yes | 88.1 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 556.5 | 0.0276 |
| inference-net/us | fp8 | yes | 88.1 | 143 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 480.0 | 0.0081 |
| modal | unknown | no | 88.1 | 143 | 0 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 728.5 | 0.0233 |
| parasail/fp8 | fp8 | yes | 88.1 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 343.5 | 0.0273 |
| relace/fp4 | fp4 | no | 88.1 | 143 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1066.5 | 0.0111 |
| coreweave/fp8 | fp8 | yes | 87.4 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 301.5 | 0.0276 |
| ambient/fp4 | fp4 | yes | 86.7 | 143 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 887.0 | 0.0045 |
| baseten | unknown | no | 86.7 | 143 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 600.0 | 0.0277 |
| digitalocean | unknown | no | 86.7 | 143 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 681.0 | 0.0179 |
| fireworks/spot | unknown | no | 86.7 | 143 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 887.0 | 0.0140 |
| sail-research/fp4 | fp4 | yes | 86.7 | 143 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2013.5 | 0.0033 |
| deepinfra/fp8/priority | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 980.5 | 0.0034 |
| inceptron/fp4 | fp4 | yes | 86.0 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1122.0 | 0.0101 |
| makora/fp8 | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 506.5 | 0.0145 |
| wafer/mxfp4 | mxfp4 | yes | 86.0 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 454.0 | 0.0031 |
| morph/fast | fp8 | yes | 85.7 | 140 | 0.00 | 1.00 | 68.1 | 100.0 | 50.0 | 100.0 | 100.0 | 2.10 | 0 | 0 | 477.0 | 0.0514 |
| cohere/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 416.0 | 0.0104 |
| fireworks | unknown | no | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 866.5 | 0.0043 |
| pearl-research/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1308.5 | 0.0051 |
| siliconflow/fp8 | fp8 | no | 85.3 | 143 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 707.0 | 0.0137 |
| fireworks/us | unknown | no | 84.6 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 506.5 | 0.0415 |
| modelrun/fp4 | fp4 | no | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 863.5 | 0.0098 |
| tenstorrent/fp8 | fp8 | yes | 84.5 | 142 | 0.00 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 773.0 | 0.0030 |
| crusoe/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 60.4 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 677.0 | 0.0173 |
| deepinfra/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 894.5 | 0.0087 |
| deepinfra/fp8/flex | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1252.0 | 0.0069 |
| pareto-inference/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1360.5 | 0.0070 |
| sail-research/fp4/us | fp4 | yes | 83.9 | 143 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1894.5 | 0.0035 |
| alibaba | unknown | yes | 82.5 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 755.0 | 0.0084 |
| morph/fp8 | fp8 | yes | 82.5 | 143 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 649.5 | 0.0056 |
| wafer/us | mxfp4 | yes | 82.5 | 143 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 417.5 | 0.0049 |
| mistral/fp8 | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 885.0 | 0.0278 |
| particle-ai/us/flex | unknown | yes | 81.8 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 592.0 | 0.0037 |
| reka | unknown | no | 81.8 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 452.0 | 0.0275 |
| particle-ai/us | unknown | yes | 81.1 | 143 | 0 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 484.0 | 0.0043 |
| primalabs | unknown | yes | 81.1 | 132 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 7.60 | 0 | 0 | 937.0 | 0.0198 |
| antdigital/fp8 | fp8 | yes | 79.7 | 143 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1138.0 | 0.0082 |
| river | unknown | yes | 79.0 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 885.5 | 0.0110 |
| baidu/fp8 | fp8 | no | 76.2 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 767.0 | 0.0091 |
| ionstream | unknown | yes | 75.5 | 143 | 0 | 1.00 | 62.5 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 830.5 | 0.0186 |
| near-ai | unknown | no | 74.1 | 143 | 0 | 1.00 | 77.1 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1253.0 | 0.0278 |
| nebius/fp4 | fp4 | yes | 72.7 | 143 | 0 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 507.0 | 0.0173 |
| streamlake/fp8 | fp8 | no | 72.0 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1345.0 | 0.0083 |
| open-inference/fp4 | fp4 | yes | 70.6 | 143 | 0.00 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 902.0 | 0.0069 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, tenstorrent/fp8, wafer/us, sail-research/fp4/us, sail-research/fp4, ambient/fp4, open-inference/fp4, pearl-research/fp8, particle-ai/us, morph/fp8, pareto-inference/fp8, cloudflare, deepinfra/fp8/flex, wafer/mxfp4, inference-net/us, inference-net/fp8, antdigital/fp8, streamlake/fp8, alibaba, baidu/fp8, deepinfra/fp8, modelrun/fp4, inceptron/fp4, cohere/fp8, river, relace/fp4, deepinfra/fp8/priority, fireworks/spot, siliconflow/fp8, deepseek, makora/fp8, primeintellect, nebius/fp4, crusoe/fp8, digitalocean, ionstream, primalabs, modal, google-vertex/global, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, reka, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 1.

## Footer

- Rows: 11952; errors 367; misrouted 0; truncated (finish_reason length) 20; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.1216; billed: $2.0239; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
