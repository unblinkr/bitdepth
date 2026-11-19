# Bitdepth scorecard 2026-11-19

Run `2026-11-19-live`, source `live`, started 2026-11-19T16:37:41Z, finished 2026-11-19T19:08:31Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4/us | fp4 | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 572.0 | 0.0126 |
| cerebras/fp16 | fp16 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 304.0 | 0.0372 |
| coreweave/fp4 | fp4 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 711.5 | 0.0041 |
| dekallm/bf16 | bf16 | yes | 98.6 | 141 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1264.0 | 0.0040 |
| digitalocean | unknown | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1504.0 | 0.0082 |
| primeintellect/fp4 | fp4 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 647.0 | 0.0359 |
| sail-research/fp4 | fp4 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 816.5 | 0.0083 |
| together | unknown | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 801.5 | 0.0179 |
| amazon-bedrock | unknown | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 654.5 | 0.0180 |
| parasail/fast | fp4 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 539.5 | 0.0196 |
| parasail/fp4 | fp4 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 718.0 | 0.0143 |
| siliconflow/fp8 | fp8 | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1990.5 | 0.0239 |
| baseten/fp4 | fp4 | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 547.5 | 0.0131 |
| deepinfra/bf16 | bf16 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 95.8 | 83.3 | 95.8 | 100.0 | 0.00 | 0 | 1 | 22637.0 | 0.0044 |
| groq | unknown | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 338.0 | 0.0180 |
| mancer/fp8 | fp8 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 836.0 | 0.0113 |
| sambanova | unknown | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 538.0 | 0.0198 |
| near-ai/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1267.5 | 0.0037 |
| amazon-bedrock/eu-west-1 | unknown | no | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 649.5 | 0.0180 |
| crusoe/bf16 | bf16 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 630.0 | 0.0064 |
| nebius/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 488.0 | 0.0175 |
| akashml/fp4 | fp4 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 691.0 | 0.0042 |
| google-vertex/global | unknown | yes | 95.1 | 142 | 0 | 1.00 | 95.8 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 507.0 | 0.0109 |
| venice/int4 | int4 | no | 83.1 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 87.5 | 100.0 | 66.7 | 0.00 | 0 | 13 | 1698.5 | 0.0048 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 2.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 86.3 | 131 | 18.5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1639.5 | 0.1324 |
| alibaba/fp8 | fp8 | yes | 85.5 | 131 | 8 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1840.0 | 0.1270 |
| streamlake/fp8 | fp8 | no | 81.7 | 131 | 4.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2474.0 | 0.0324 |
| deepinfra/fp8 | fp8 | yes | 80.9 | 131 | 6 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1539.0 | 0.1139 |
| siliconflow/fp8 | fp8 | no | 80.2 | 131 | 8.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2559.0 | 0.0468 |
| venice | unknown | no | 80.2 | 131 | 6.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1939.0 | 0.0686 |
| digitalocean | unknown | no | 79.4 | 131 | 5 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1354.0 | 0.0948 |
| baidu/fp8 | fp8 | no | 77.1 | 131 | 1.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1482.0 | 0.0777 |
| relace/fp4 | fp4 | no | 76.3 | 131 | 4 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 978.5 | 0.0798 |
| deepinfra/fp8/priority | fp8 | yes | 75.6 | 131 | 4.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1541.0 | 0.0710 |
| deepinfra/fp8/flex | fp8 | yes | 75.4 | 114 | 4.00 | 1.00 | 100.0 | 100.0 | 65.0 | 100.0 | 95.2 | 11.8 | 0 | 0 | 2435.0 | 0.0530 |
| atlas-cloud/fp4 | fp4 | yes | 72.5 | 131 | 3.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2356.5 | 0.1521 |
| azure/us | unknown | no | 59.5 | 131 | 1 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1157.5 | 0.1745 |
| gmicloud/fp8 | fp8 | yes | 45.8 | 131 | 1 | 1.00 | 100.0 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2437.5 | 0.0861 |
| novita/fp8 | fp8 | yes | 45.0 | 131 | 0.50 | 1.00 | 97.9 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2077.5 | 0.1038 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, siliconflow/fp8, gmicloud/fp8, deepinfra/fp8/flex, digitalocean, novita/fp8, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, atlas-cloud/fp4, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 13.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fast | unknown | no | 89.8 | 127 | 0 | 1.00 | 65.9 | 100.0 | 45.5 | 100.0 | 100.0 | 11.1 | 0 | 0 | 363.5 | 0.0497 |
| digitalocean | unknown | no | 89.5 | 143 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 652.5 | 0.0168 |
| pearl-research/fp8 | fp8 | yes | 88.1 | 143 | 0 | 1.00 | 72.9 | 95.8 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 751.0 | 0.0050 |
| cloudflare | unknown | yes | 87.4 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1465.5 | 0.0059 |
| parasail/fp8 | fp8 | yes | 87.4 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 319.0 | 0.0276 |
| ambient/fp4 | fp4 | yes | 86.7 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 602.0 | 0.0082 |
| antdigital/fp8 | fp8 | yes | 86.7 | 143 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1239.0 | 0.0095 |
| particle-ai/us/flex | unknown | yes | 86.7 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 727.5 | 0.0032 |
| relace/fp4 | fp4 | no | 86.7 | 143 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1060.5 | 0.0111 |
| wafer/us | mxfp4 | yes | 86.7 | 143 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 369.5 | 0.0047 |
| deepinfra/fp8/priority | fp8 | yes | 86.5 | 141 | 0 | 1.00 | 72.3 | 100.0 | 52.2 | 100.0 | 100.0 | 1.40 | 0 | 0 | 718.0 | 0.0037 |
| cohere/fp8 | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 62.5 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 417.5 | 0.0133 |
| inference-net/us | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 376.5 | 0.0086 |
| coreweave/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 296.0 | 0.0278 |
| inference-net/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 369.0 | 0.0074 |
| modal | unknown | no | 85.3 | 143 | 0 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 607.0 | 0.0230 |
| morph/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 564.0 | 0.0061 |
| primalabs | unknown | yes | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 586.5 | 0.0221 |
| primeintellect | unknown | no | 85.3 | 143 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 634.0 | 0.0060 |
| siliconflow/fp8 | fp8 | no | 85.3 | 143 | 0 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 760.5 | 0.0135 |
| venice/fp8 | fp8 | no | 85.3 | 143 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 861.0 | 0.0275 |
| deepinfra/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 644.0 | 0.0090 |
| inceptron/fp4 | fp4 | yes | 84.6 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 615.0 | 0.0099 |
| modelrun/fp4 | fp4 | no | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 803.5 | 0.0158 |
| particle-ai/us | unknown | yes | 84.6 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 578.0 | 0.0037 |
| atlas-cloud/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1154.0 | 0.0042 |
| baseten | unknown | no | 83.9 | 143 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 684.0 | 0.0274 |
| fireworks | unknown | no | 83.9 | 143 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 875.0 | 0.0065 |
| mistral/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 605.5 | 0.0221 |
| morph/fast | fp8 | yes | 83.8 | 142 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 512.0 | 0.0543 |
| alibaba | unknown | yes | 83.2 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 875.5 | 0.0083 |
| deepinfra/fp8/flex | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 68.8 | 95.8 | 50.0 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2039.5 | 0.0069 |
| fireworks/spot | unknown | no | 83.2 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 851.0 | 0.0194 |
| fireworks/us | unknown | no | 83.2 | 143 | 0.00 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 419.0 | 0.0414 |
| makora/fp8 | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 494.5 | 0.0148 |
| together | unknown | no | 83.2 | 143 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 79.2 | 100.0 | 0.00 | 0 | 0 | 273.0 | 0.0276 |
| wafer/mxfp4 | mxfp4 | yes | 83.2 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 403.5 | 0.0030 |
| crusoe/fp8 | fp8 | yes | 82.5 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 569.5 | 0.0272 |
| gmicloud/fp8 | fp8 | yes | 82.5 | 143 | 0 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 851.5 | 0.0167 |
| novita/fp8 | fp8 | yes | 82.5 | 143 | 0 | 1.00 | 79.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1140.0 | 0.0050 |
| stepfun/fp8 | fp8 | no | 81.8 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 719.0 | 0.0098 |
| ionstream | unknown | yes | 81.1 | 143 | 0 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 478.5 | 0.0186 |
| streamlake/fp8 | fp8 | no | 81.1 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1452.0 | 0.0098 |
| dekallm | unknown | yes | 80.4 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1078.0 | 0.0101 |
| river | unknown | yes | 79.7 | 143 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1000.0 | 0.0110 |
| nebius/fp4 | fp4 | yes | 76.9 | 143 | 0 | 1.00 | 81.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 466.0 | 0.0170 |
| baidu/fp8 | fp8 | no | 75.5 | 143 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 709.0 | 0.0141 |
| near-ai | unknown | no | 74.1 | 143 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1087.5 | 0.0276 |
| open-inference/fp4 | fp4 | yes | 72.7 | 143 | 0 | 1.00 | 62.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 942.0 | 0.0081 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, primeintellect, pearl-research/fp8, morph/fp8, particle-ai/us, open-inference/fp4, wafer/mxfp4, deepinfra/fp8/flex, ambient/fp4, inference-net/us, inference-net/fp8, alibaba, deepinfra/fp8, inceptron/fp4, dekallm, cloudflare, stepfun/fp8, streamlake/fp8, antdigital/fp8, river, relace/fp4, deepinfra/fp8/priority, baidu/fp8, cohere/fp8, siliconflow/fp8, deepseek, makora/fp8, novita/fp8, modelrun/fp4, nebius/fp4, digitalocean, gmicloud/fp8, atlas-cloud/fp8, ionstream, fireworks/spot, mistral/fp8, primalabs, modal, crusoe/fp8, coreweave/fp8, near-ai, venice/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 1.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 129 | n/a | 1.00 | 97.9 | 58.3 | 79.2 | 100.0 | 87.5 | 0.00 | 0 | 16 | 4480.5 | 0.1030 |
| mistral/zdr | unknown | yes | 100.0 | 129 | n/a | 1.00 | 97.9 | 45.8 | 66.7 | 100.0 | 91.7 | 0.00 | 0 | 22 | 4802.5 | 0.1258 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 15.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| darkbloom/fp4 | fp4 | yes | 99.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 95.7 | 100.0 | 100.0 | 1.40 | 0 | 0 | 2323.5 | 0.0059 |
| friendli | unknown | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 472.0 | 0.0146 |
| morph/fp8 | fp8 | yes | 99.3 | 144 | 0 | 1.00 | 97.9 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3370.0 | 0.0113 |
| particle-ai/nvfp4/flex | nvfp4 | yes | 99.3 | 144 | 0 | 1.00 | 97.9 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 620.5 | 0.0064 |
| streamlake/fp8 | fp8 | no | 99.3 | 144 | 0 | 1.00 | 97.9 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1959.0 | 0.0086 |
| deepinfra/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 801.0 | 0.0145 |
| digitalocean | unknown | no | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1006.5 | 0.0108 |
| gmicloud/fp8 | fp8 | yes | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2067.5 | 0.0072 |
| inceptron/fp8 | fp8 | yes | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 962.5 | 0.0144 |
| kt | unknown | no | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 726.5 | 0.0144 |
| parasail/fp8 | fp8 | yes | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 908.0 | 0.0144 |
| particle-ai/nvfp4 | nvfp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 620.0 | 0.0061 |
| relace/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1051.0 | 0.0036 |
| sail-research/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1304.0 | 0.0145 |
| venice | unknown | no | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 967.0 | 0.0151 |
| near-ai/fp8 | fp8 | yes | 98.5 | 132 | 0.00 | 1.00 | 97.7 | 100.0 | 100.0 | 100.0 | 100.0 | 8.30 | 0 | 0 | 2248.0 | 0.0081 |
| baidu/fp8 | fp8 | no | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2505.0 | 0.0143 |
| reka | unknown | yes | 97.9 | 141 | 0 | 1.00 | 97.9 | 100.0 | 95.7 | 100.0 | 100.0 | 2.10 | 0 | 0 | 2710.0 | 0.0110 |
| river | unknown | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1114.5 | 0.0115 |
| sail-research/us | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1437.0 | 0.0170 |
| together | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 838.0 | 0.0145 |
| dekallm | unknown | yes | 97.8 | 136 | 0 | 1.00 | 95.3 | 100.0 | 95.8 | 100.0 | 100.0 | 5.60 | 0 | 0 | 3048.5 | 0.0102 |
| tenstorrent/fp8 | fp8 | yes | 97.6 | 82 | 0.00 | 1.00 | 96.9 | 100.0 | 94.1 | 100.0 | 100.0 | 43.1 | 0 | 0 | 992.5 | 0.0034 |
| cohere/nvfp4 | nvfp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 622.0 | 0.0150 |
| crusoe/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 937.5 | 0.0145 |
| nebius/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1018.5 | 0.0145 |
| parasail/fast | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 498.5 | 0.0180 |
| baseten/fp8 | fp8 | no | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 795.0 | 0.0146 |
| open-inference/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1296.0 | 0.0065 |
| coreweave/nvfp4 | nvfp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 722.5 | 0.0114 |
| fireworks | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1787.5 | 0.0181 |
| novita/fp8 | fp8 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1593.5 | 0.0082 |
| modal/fp4 | fp4 | no | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 451.0 | 0.0146 |
| makora/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 709.0 | 0.0125 |
| mistral | unknown | yes | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 764.5 | 0.0145 |
| fireworks/us | unknown | no | 93.1 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 521.0 | 0.0179 |
| siliconflow/fp8 | fp8 | no | 93.1 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1608.0 | 0.0100 |
| inference-net/fp4 | fp4 | yes | 91.7 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 572.5 | 0.0084 |
| z-ai/fp8 | fp8 | no | 91.7 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1548.0 | 0.0144 |
| inference-net/us | fp4 | yes | 91.0 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 577.5 | 0.0103 |
| wafer/nvfp4 | nvfp4 | yes | 85.4 | 144 | 0 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 741.0 | 0.0065 |
| wafer/us | nvfp4 | yes | 85.4 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 793.0 | 0.0044 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, wafer/us, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, particle-ai/nvfp4/flex, tenstorrent/fp8, gmicloud/fp8, near-ai/fp8, novita/fp8, streamlake/fp8, siliconflow/fp8, dekallm, inference-net/us, inference-net/fp4, digitalocean, reka, coreweave/nvfp4, river, morph/fp8, particle-ai/nvfp4, makora/fp4, baidu/fp8, mistral, kt, cohere/nvfp4, nebius/fp4, modal/fp4, inceptron/fp8, crusoe/fp4, fireworks, friendli, together, parasail/fp8, baseten/fp8, venice, deepinfra/fp4, z-ai/fp8, sail-research/us, sail-research/fp4, parasail/fast, fireworks/us. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 100.0 | 122 | n/a | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 100.0 | 3.50 | 0 | 0 | 645.0 | 0.0119 |
| novita/bf16 | bf16 | yes | 100.0 | 100 | n/a | 1.00 | 35.7 | 100.0 | 68.4 | 100.0 | 100.0 | 18.8 | 0 | 0 | 559.0 | 0.0095 |
| sambanova | unknown | no | 100.0 | 126 | n/a | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1331.0 | 0.0340 |
| friendli | unknown | yes | 95.2 | 126 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 276.5 | 0.0125 |
| parasail/fp8 | fp8 | yes | 94.4 | 124 | 0 | 1.00 | 43.8 | 100.0 | 58.3 | 100.0 | 100.0 | 1.40 | 0 | 0 | 687.0 | 0.0132 |
| deepinfra/fp8 | fp8 | yes | 92.1 | 126 | 0.00 | 1.00 | 39.6 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 831.5 | 0.0172 |
| siliconflow/fp8 | fp8 | no | 92.0 | 125 | 0.00 | 1.00 | 39.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2727.0 | 0.0616 |
| deepinfra/fp8/flex | fp8 | yes | 88.9 | 126 | 0.00 | 1.00 | 37.5 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1413.0 | 0.0137 |
| deepinfra/fp8/priority | fp8 | yes | 88.9 | 126 | 0.00 | 1.00 | 39.6 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 677.5 | 0.0256 |
| primeintellect/fp8 | fp8 | yes | 86.6 | 112 | 0 | 1.00 | 42.2 | 100.0 | 66.7 | 100.0 | 100.0 | 11.1 | 0 | 0 | 903.0 | 0.0141 |
| chutes/fp4 | fp4 | yes | 86.5 | 126 | 0 | 1.00 | 39.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2880.5 | 0.0107 |
| modal | unknown | no | 85.7 | 126 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 743.5 | 0.0261 |
| coreweave/fp4 | fp4 | yes | 84.9 | 126 | 0 | 1.00 | 37.5 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 447.5 | 0.0091 |
| kt | unknown | no | 83.3 | 126 | 0 | 1.00 | 35.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 532.0 | 0.0091 |
| modelrun/fp4 | fp4 | no | 82.5 | 126 | 0.00 | 1.00 | 37.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 397.0 | 0.0619 |
| venice/fp4 | fp4 | no | 81.7 | 126 | 0 | 1.00 | 31.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 695.5 | 0.0106 |
| deepinfra/turbo | fp4 | yes | 78.6 | 126 | 0 | 1.00 | 29.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 405.5 | 0.0084 |
| nextbit/fp4 | fp4 | yes | 77.0 | 126 | 0 | 1.00 | 35.4 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 538.0 | 0.0110 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: crusoe/bf16, novita/bf16. Prompts with no plurality (excluded from exact match): 17.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| xiaomi/fp8 | fp8 | no | 95.8 | 142 | 2.00 | 1.00 | 77.1 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2017.5 | 0.0354 |
| primalabs/fp8 | fp8 | yes | 93.7 | 142 | 0 | 1.00 | 79.2 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 614.5 | 0.2335 |
| streamlake | unknown | no | 92.6 | 135 | 0.00 | 1.00 | 80.4 | 100.0 | 69.6 | 100.0 | 100.0 | 4.90 | 0 | 0 | 1637.0 | 0.0362 |
| deepinfra/fp8 | fp8 | yes | 92.3 | 142 | 0 | 1.00 | 83.3 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1011.5 | 0.0344 |
| gmicloud/bf16 | bf16 | yes | 81.0 | 142 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3303.5 | 0.0277 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: gmicloud/bf16, deepinfra/fp8, streamlake, xiaomi/fp8, primalabs/fp8. Prompts with no plurality (excluded from exact match): 2.

## Footer

- Rows: 22464; errors 326; misrouted 0; truncated (finish_reason length) 65; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $7.3785; billed: $3.9423; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
