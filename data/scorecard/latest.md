# Bitdepth scorecard 2026-11-26

Run `2026-11-26-live`, source `live`, started 2026-11-26T17:46:40Z, finished 2026-11-26T20:45:27Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 99.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 455.0 | 0.0066 |
| deepinfra/bf16 | bf16 | yes | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2271.5 | 0.0046 |
| amazon-bedrock | unknown | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 544.5 | 0.0184 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 556.5 | 0.0183 |
| baseten/fp4 | fp4 | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 2 | 403.5 | 0.0129 |
| cerebras/fp16 | fp16 | yes | 97.2 | 143 | 6.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 1 | 266.5 | 0.0366 |
| groq | unknown | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 287.0 | 0.0182 |
| baseten/fp4/us | fp4 | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 411.5 | 0.0128 |
| parasail/fast | fp4 | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 491.0 | 0.0192 |
| parasail/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 78.3 | 100.0 | 100.0 | 0.70 | 0 | 1 | 894.0 | 0.0148 |
| sambanova | unknown | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 467.5 | 0.0209 |
| akashml/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1385.0 | 0.0043 |
| nebius/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 438.5 | 0.0179 |
| coreweave/fp4 | fp4 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 677.0 | 0.0040 |
| digitalocean | unknown | no | 94.4 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1178.5 | 0.0083 |
| primeintellect/fp4 | fp4 | yes | 94.4 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 591.5 | 0.0361 |
| google-vertex/global | unknown | yes | 93.0 | 143 | 0.00 | 1.00 | 93.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 399.0 | 0.0109 |
| near-ai/fp4 | fp4 | yes | 93.0 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1695.5 | 0.0039 |
| mancer/fp8 | fp8 | yes | 90.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 799.5 | 0.0106 |
| venice/int4 | int4 | no | 79.7 | 143 | 0 | 1.00 | 70.8 | 100.0 | 70.8 | 100.0 | 83.3 | 0.00 | 0 | 15 | 1609.5 | 0.0050 |
| siliconflow/fp8 | fp8 | no | 72.7 | 143 | 0 | 1.00 | 79.2 | 54.2 | 70.8 | 100.0 | 83.3 | 0.00 | 0 | 0 | 1435.5 | 0.0217 |
| fireworks | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 1.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 80.1 | 136 | 8 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2036.5 | 0.1279 |
| baidu/fp8 | fp8 | no | 80.1 | 136 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1482.5 | 0.0707 |
| relace/fp4 | fp4 | no | 80.1 | 136 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 734.0 | 0.0706 |
| alibaba/fp8/us-east-1 | fp8 | yes | 78.7 | 136 | 4 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2080.0 | 0.1371 |
| streamlake/fp8 | fp8 | no | 78.7 | 136 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2639.0 | 0.0303 |
| deepinfra/fp8 | fp8 | yes | 77.2 | 136 | 3 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1064.0 | 0.1058 |
| deepinfra/fp8/flex | fp8 | yes | 77.2 | 136 | 6 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1699.0 | 0.0477 |
| deepinfra/fp8/priority | fp8 | yes | 75.7 | 136 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 988.5 | 0.0665 |
| venice | unknown | no | 71.3 | 136 | 5 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1413.0 | 0.0724 |
| siliconflow/fp8 | fp8 | no | 68.4 | 136 | 3 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2122.0 | 0.0805 |
| azure/us | unknown | no | 55.9 | 136 | 1.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1133.5 | 0.1729 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, relace/fp4, streamlake/fp8, siliconflow/fp8, deepinfra/fp8/flex, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 8.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ambient/fp4 | fp4 | yes | 91.7 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 808.0 | 0.0044 |
| baseten/fast | unknown | no | 90.5 | 137 | 0 | 1.00 | 70.2 | 100.0 | 45.8 | 100.0 | 100.0 | 4.90 | 0 | 0 | 268.0 | 0.0533 |
| cloudflare | unknown | yes | 89.6 | 144 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1125.0 | 0.0068 |
| fireworks/flex | unknown | no | 88.7 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 1.40 | 0 | 0 | 593.5 | 0.0133 |
| alibaba | unknown | yes | 88.2 | 144 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 826.0 | 0.0082 |
| wafer/mxfp4 | mxfp4 | yes | 88.2 | 144 | 0 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 398.5 | 0.0027 |
| parasail/fp8 | fp8 | yes | 87.5 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 410.5 | 0.0273 |
| particle-ai/us | unknown | yes | 87.5 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 372.0 | 0.0042 |
| digitalocean | unknown | no | 86.8 | 144 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 410.5 | 0.0179 |
| inference-net/fp8 | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 308.5 | 0.0073 |
| mistral/fp8 | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 805.0 | 0.0274 |
| pareto-inference/fp8 | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1085.5 | 0.0070 |
| baseten | unknown | no | 86.1 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 617.5 | 0.0275 |
| deepinfra/fp8/flex | fp8 | yes | 86.1 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1312.0 | 0.0069 |
| modelrun/fp4 | fp4 | no | 86.1 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 710.0 | 0.0095 |
| particle-ai/us/flex | unknown | yes | 86.1 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 392.5 | 0.0057 |
| siliconflow/fp8 | fp8 | no | 86.1 | 144 | 0.00 | 1.00 | 62.5 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 578.5 | 0.0135 |
| antdigital/fp8 | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1204.0 | 0.0082 |
| crusoe/fp8 | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1066.0 | 0.0174 |
| featherless/fp8 | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1376.5 | 0.0198 |
| inceptron/fp4 | fp4 | yes | 85.4 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 878.5 | 0.0099 |
| inference-net/us | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 317.0 | 0.0086 |
| modal | unknown | no | 85.4 | 144 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 864.0 | 0.0231 |
| primalabs | unknown | yes | 85.4 | 144 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 492.0 | 0.0221 |
| primeintellect | unknown | no | 85.4 | 144 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 485.0 | 0.0085 |
| relace/fp4 | fp4 | no | 85.4 | 144 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 753.0 | 0.0111 |
| cohere/fp8 | fp8 | yes | 84.7 | 144 | 0.00 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 381.5 | 0.0103 |
| coreweave/fp8 | fp8 | yes | 84.7 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 466.5 | 0.0275 |
| fireworks/us | unknown | no | 84.7 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 565.0 | 0.0338 |
| morph/fast | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 253.0 | 0.0556 |
| wafer/us | mxfp4 | yes | 84.0 | 144 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 415.5 | 0.0047 |
| tenstorrent/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 63.8 | 100.0 | 52.2 | 100.0 | 100.0 | 2.10 | 0 | 0 | 695.0 | 0.0051 |
| makora/fp8 | fp8 | yes | 83.3 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 380.5 | 0.0145 |
| morph/fp8 | fp8 | yes | 83.3 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 496.0 | 0.0060 |
| venice/fp8 | fp8 | no | 83.3 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 965.5 | 0.0274 |
| deepinfra/fp8 | fp8 | yes | 82.6 | 144 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 772.5 | 0.0089 |
| fireworks | unknown | no | 82.6 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 802.5 | 0.0215 |
| google-vertex/global | unknown | yes | 82.6 | 144 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 484.5 | 0.0278 |
| deepinfra/fp8/priority | fp8 | yes | 81.9 | 144 | 0.00 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 789.0 | 0.0035 |
| reka | unknown | no | 81.9 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 302.0 | 0.0276 |
| ionstream | unknown | yes | 81.2 | 144 | 0 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 472.0 | 0.0183 |
| pearl-research/fp8 | fp8 | yes | 81.2 | 144 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 930.0 | 0.0049 |
| nebius/fp4 | fp4 | yes | 78.5 | 144 | 0 | 1.00 | 83.3 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 360.0 | 0.0169 |
| river | unknown | yes | 78.5 | 144 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 774.5 | 0.0110 |
| near-ai | unknown | no | 77.1 | 144 | 0 | 1.00 | 62.5 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1079.5 | 0.0272 |
| baidu/fp8 | fp8 | no | 76.4 | 144 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 813.5 | 0.0120 |
| fireworks/spot | unknown | no | 75.8 | 95 | 0 | 1.00 | 71.1 | 100.0 | 57.1 | 100.0 | 100.0 | 34.0 | 0 | 0 | 486.0 | 0.0082 |
| open-inference/fp4 | fp4 | yes | 75.0 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1082.5 | 0.0065 |
| streamlake/fp8 | fp8 | no | 72.2 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1380.0 | 0.0083 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: wafer/us, sail-research/fp4/us, sail-research/fp4, particle-ai/us/flex, primeintellect, ambient/fp4, open-inference/fp4, tenstorrent/fp8, pearl-research/fp8, particle-ai/us, morph/fp8, wafer/mxfp4, pareto-inference/fp8, cloudflare, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, antdigital/fp8, streamlake/fp8, alibaba, deepinfra/fp8, modelrun/fp4, inceptron/fp4, cohere/fp8, river, relace/fp4, deepinfra/fp8/priority, baidu/fp8, fireworks/flex, fireworks/spot, siliconflow/fp8, deepseek, makora/fp8, nebius/fp4, crusoe/fp8, digitalocean, ionstream, featherless/fp8, primalabs, modal, google-vertex/global, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, reka, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 0.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 131 | n/a | 1.00 | 95.8 | 50.0 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 18 | 2435.5 | 0.1144 |
| mistral/zdr | unknown | yes | 100.0 | 131 | n/a | 1.00 | 95.8 | 41.7 | 79.2 | 100.0 | 95.8 | 0.00 | 0 | 21 | 2898.0 | 0.1162 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 13.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| near-ai/fp8 | fp8 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1747.0 | 0.0087 |
| sail-research/fp4 | fp4 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1538.5 | 0.0162 |
| deepinfra/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 712.0 | 0.0086 |
| friendli | unknown | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 409.5 | 0.0145 |
| pareto-inference/nvfp4 | nvfp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1074.0 | 0.0036 |
| relace/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1022.5 | 0.0032 |
| darkbloom/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1952.5 | 0.0061 |
| fireworks/us | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 411.0 | 0.0214 |
| parasail/fast | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 412.5 | 0.0183 |
| sail-research/us | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1423.0 | 0.0170 |
| streamlake/fp8 | fp8 | no | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1631.5 | 0.0082 |
| baseten/fp8 | fp8 | no | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 580.5 | 0.0145 |
| morph/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 817.5 | 0.0128 |
| open-inference/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 712.0 | 0.0066 |
| parasail/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 477.5 | 0.0146 |
| tenstorrent/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 980.0 | 0.0072 |
| venice | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 686.0 | 0.0151 |
| baidu/fp8 | fp8 | no | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2462.5 | 0.0143 |
| fireworks | unknown | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 675.5 | 0.0146 |
| particle-ai/nvfp4 | nvfp4 | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 704.0 | 0.0135 |
| reka | unknown | yes | 96.5 | 144 | 0 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 539.5 | 0.0112 |
| river | unknown | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 848.5 | 0.0115 |
| cohere/nvfp4 | nvfp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 474.5 | 0.0106 |
| coreweave/nvfp4 | nvfp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 726.0 | 0.0113 |
| inceptron/fp8 | fp8 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 772.5 | 0.0144 |
| nebius/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 940.0 | 0.0146 |
| crusoe/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 852.5 | 0.0115 |
| fireworks/flex | unknown | no | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 576.0 | 0.0072 |
| mistral | unknown | yes | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 802.5 | 0.0144 |
| modal/fp4 | fp4 | no | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 429.0 | 0.0145 |
| siliconflow/fp8 | fp8 | no | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1493.5 | 0.0099 |
| z-ai/fp8 | fp8 | no | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1350.5 | 0.0143 |
| digitalocean | unknown | no | 91.0 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 737.0 | 0.0109 |
| kt | unknown | no | 90.3 | 144 | 0.00 | 1.00 | 87.5 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 653.0 | 0.0145 |
| inference-net/fp4 | fp4 | yes | 89.6 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 607.0 | 0.0087 |
| makora/fp4 | fp4 | yes | 89.6 | 144 | 0 | 1.00 | 97.9 | 50.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 587.0 | 0.0132 |
| inference-net/us | fp4 | yes | 86.8 | 144 | 0 | 1.00 | 95.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 578.0 | 0.0102 |
| wafer/us | nvfp4 | yes | 83.3 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 435.5 | 0.0044 |
| wafer/nvfp4 | nvfp4 | yes | 79.9 | 144 | 0 | 1.00 | 93.8 | 100.0 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 0 | 404.5 | 0.0064 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, pareto-inference/nvfp4, wafer/us, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, fireworks/flex, tenstorrent/fp8, near-ai/fp8, streamlake/fp8, deepinfra/fp4, siliconflow/fp8, cohere/nvfp4, inference-net/us, inference-net/fp4, digitalocean, reka, coreweave/nvfp4, river, crusoe/fp4, particle-ai/nvfp4, morph/fp8, makora/fp4, baidu/fp8, mistral, kt, nebius/fp4, modal/fp4, inceptron/fp8, fireworks, friendli, parasail/fp8, baseten/fp8, venice, z-ai/fp8, sail-research/us, sail-research/fp4, parasail/fast, fireworks/us. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 94.0 | 134 | 0.00 | 1.00 | 46.7 | 100.0 | 54.2 | 100.0 | 100.0 | 3.50 | 0 | 0 | 706.0 | 0.0123 |
| sambanova | unknown | no | 91.4 | 139 | 0.00 | 1.00 | 45.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1379.0 | 0.0339 |
| deepinfra/fp8/priority | fp8 | yes | 90.6 | 139 | 0 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 635.0 | 0.0256 |
| siliconflow/fp8 | fp8 | no | 90.6 | 139 | 0 | 1.00 | 43.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 874.0 | 0.0610 |
| deepinfra/fp8 | fp8 | yes | 89.9 | 139 | 0.00 | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 750.0 | 0.0170 |
| deepinfra/fp8/flex | fp8 | yes | 89.9 | 139 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1326.0 | 0.0136 |
| friendli | unknown | yes | 89.2 | 139 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 265.0 | 0.0124 |
| parasail/fp8 | fp8 | yes | 89.2 | 139 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 752.0 | 0.0132 |
| primeintellect/fp8 | fp8 | yes | 88.5 | 139 | 0.00 | 1.00 | 45.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 546.0 | 0.0163 |
| coreweave/fp4 | fp4 | yes | 83.5 | 139 | 0 | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 964.0 | 0.0091 |
| deepinfra/turbo | fp4 | yes | 83.5 | 139 | 0 | 1.00 | 41.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 588.5 | 0.0089 |
| modal | unknown | no | 83.5 | 139 | 0 | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 395.0 | 0.0262 |
| chutes/fp4 | fp4 | yes | 82.0 | 139 | 0 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2131.0 | 0.0107 |
| modelrun/fp4 | fp4 | no | 81.3 | 139 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 201.0 | 0.0617 |
| venice/fp4 | fp4 | no | 79.1 | 139 | 0 | 1.00 | 41.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 736.0 | 0.0106 |
| kt | unknown | no | 72.7 | 139 | 0.00 | 1.00 | 39.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 488.5 | 0.0092 |
| nextbit/fp4 | fp4 | yes | 71.9 | 139 | 0 | 1.00 | 31.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 482.5 | 0.0111 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: kt, coreweave/fp4, venice/fp4, chutes/fp4, nextbit/fp4, deepinfra/turbo, crusoe/bf16, friendli, primeintellect/fp8, parasail/fp8, deepinfra/fp8/flex, deepinfra/fp8, deepinfra/fp8/priority, modal, sambanova, modelrun/fp4, siliconflow/fp8. Prompts with no plurality (excluded from exact match): 5.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| primalabs/fp8 | fp8 | yes | 97.1 | 138 | 8.50 | 1.00 | 77.1 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 506.0 | 0.2327 |
| deepinfra/fp8 | fp8 | yes | 95.7 | 138 | 0.00 | 1.00 | 72.9 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 941.5 | 0.0342 |
| xiaomi/fp8 | fp8 | no | 92.0 | 138 | 0 | 1.00 | 77.1 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1889.5 | 0.0389 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: deepinfra/fp8, xiaomi/fp8, primalabs/fp8. Prompts with no plurality (excluded from exact match): 6.

## Footer

- Rows: 21024; errors 645; misrouted 0; truncated (finish_reason length) 69; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $6.3704; billed: $3.3894; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
