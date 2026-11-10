# Bitdepth scorecard 2026-11-10

Run `2026-11-10-dispatch`, source `dispatch`, started 2026-11-10T15:34:56Z, finished 2026-11-10T20:21:21Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 738.0 | 0.0064 |
| deepinfra/bf16 | bf16 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1953.0 | 0.0049 |
| deepinfra/fp8 | fp8 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1508.5 | 0.0262 |
| primeintellect/fp4 | fp4 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 969.0 | 0.0039 |
| sambanova | unknown | no | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 590.5 | 0.0211 |
| baseten/fp4 | fp4 | no | 97.9 | 142 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 536.0 | 0.0128 |
| cerebras/fp16 | fp16 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 271.0 | 0.0370 |
| groq | unknown | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 344.0 | 0.0179 |
| siliconflow/fp8 | fp8 | no | 97.9 | 141 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.70 | 0 | 0 | 2044.0 | 0.0259 |
| together | unknown | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 647.0 | 0.0183 |
| near-ai/fp4 | fp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1300.5 | 0.0039 |
| parasail/fast | fp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 528.5 | 0.0197 |
| baseten/fp4/us | fp4 | no | 96.5 | 142 | 0 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 497.0 | 0.0130 |
| nebius/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 509.0 | 0.0178 |
| coreweave/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 977.5 | 0.0041 |
| dekallm/bf16 | bf16 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1876.0 | 0.0042 |
| sail-research/fp4 | fp4 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 983.0 | 0.0085 |
| google-vertex/global | unknown | yes | 95.0 | 139 | 0 | 1.00 | 100.0 | 100.0 | 65.2 | 100.0 | 100.0 | 2.10 | 0 | 1 | 620.0 | 0.0110 |
| akashml/fp4 | fp4 | yes | 94.4 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2353.5 | 0.0043 |
| mancer/fp8 | fp8 | yes | 94.4 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 813.0 | 0.0069 |
| parasail/fp4 | fp4 | yes | 94.4 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 689.5 | 0.0145 |
| amazon-bedrock | unknown | no | 93.7 | 142 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 761.5 | 0.0181 |
| amazon-bedrock/eu-west-1 | unknown | no | 93.0 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 787.0 | 0.0183 |
| digitalocean | unknown | no | 92.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1480.0 | 0.0088 |
| venice/int4 | int4 | no | 85.2 | 142 | 0 | 1.00 | 79.2 | 100.0 | 75.0 | 100.0 | 87.5 | 0.00 | 0 | 11 | 2049.5 | 0.0046 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 2.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baidu/fp8 | fp8 | no | 86.5 | 96 | 4 | 1.00 | 100.0 | 100.0 | 55.0 | 100.0 | 94.7 | 22.9 | 0 | 0 | 1532.0 | 0.1163 |
| alibaba/fp8/us-east-1 | fp8 | yes | 85.0 | 127 | 5 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2088.0 | 0.1377 |
| alibaba/fp8 | fp8 | yes | 82.7 | 127 | 3.50 | 1.00 | 100.0 | 100.0 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2362.5 | 0.1287 |
| atlas-cloud/fp4 | fp4 | yes | 81.1 | 127 | 3.50 | 1.00 | 100.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2784.0 | 0.1544 |
| streamlake/fp8 | fp8 | no | 80.3 | 127 | 7 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2809.0 | 0.0363 |
| deepinfra/fp8 | fp8 | yes | 78.0 | 127 | 2.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1334.5 | 0.1181 |
| venice | unknown | no | 75.6 | 127 | 1 | 1.00 | 100.0 | 100.0 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1455.5 | 0.0727 |
| siliconflow/fp8 | fp8 | no | 73.2 | 127 | 3.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 3238.0 | 0.0873 |
| relace/fp4 | fp4 | no | 71.0 | 124 | 4.00 | 1.00 | 100.0 | 100.0 | 60.9 | 100.0 | 95.7 | 2.80 | 0 | 0 | 1955.0 | 0.0794 |
| azure/us | unknown | no | 62.2 | 127 | 1.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1154.0 | 0.1745 |
| digitalocean | unknown | no | 55.9 | 127 | 1.00 | 1.00 | 100.0 | 95.8 | 45.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1692.0 | 0.0956 |
| gmicloud/fp8 | fp8 | yes | 50.4 | 127 | 1 | 1.00 | 100.0 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2578.0 | 0.0861 |
| novita/fp8 | fp8 | yes | 48.8 | 127 | 1 | 1.00 | 100.0 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2271.0 | 0.0938 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, streamlake/fp8, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, baidu/fp8, azure/us. Prompts with no plurality (excluded from exact match): 17.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| novita/fp8 | fp8 | yes | 90.3 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1306.0 | 0.0039 |
| atlas-cloud/fp8 | fp8 | yes | 89.6 | 144 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1299.5 | 0.0045 |
| cohere/fp8 | fp8 | yes | 89.6 | 144 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 387.0 | 0.0134 |
| morph/fp8 | fp8 | yes | 88.9 | 144 | 0.00 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 6524.5 | 0.0032 |
| cloudflare | unknown | yes | 88.8 | 143 | 0.00 | 1.00 | 74.5 | 100.0 | 41.7 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1685.0 | 0.0049 |
| fireworks | unknown | no | 88.2 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1110.5 | 0.0261 |
| siliconflow/fp8 | fp8 | no | 88.2 | 144 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 919.0 | 0.0251 |
| deepinfra/fp8/priority | fp8 | yes | 87.5 | 144 | 0.00 | 1.00 | 66.7 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 440.0 | 0.0033 |
| fireworks/spot | unknown | no | 87.5 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1094.0 | 0.0192 |
| inference-net/us | fp8 | yes | 87.5 | 144 | 0.00 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 483.5 | 0.0083 |
| venice/fp8 | fp8 | no | 87.5 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1103.5 | 0.0278 |
| deepinfra/fp8/flex | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 70.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1800.0 | 0.0063 |
| gmicloud/fp8 | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 64.6 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 997.5 | 0.0167 |
| nebius/fp8 | fp8 | yes | 86.8 | 144 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1126.0 | 0.0277 |
| particle-ai/us/flex | unknown | yes | 86.8 | 144 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 845.5 | 0.0029 |
| phala | unknown | yes | 86.8 | 144 | 0 | 1.00 | 83.3 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1513.5 | 0.0074 |
| streamlake/fp8 | fp8 | no | 86.8 | 144 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1530.0 | 0.0102 |
| wafer/mxfp4 | mxfp4 | yes | 86.8 | 144 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 455.5 | 0.0036 |
| primalabs | unknown | yes | 86.7 | 143 | 0 | 1.00 | 72.3 | 100.0 | 45.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 805.0 | 0.0222 |
| makora/fp8 | fp8 | yes | 86.1 | 144 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 610.0 | 0.0161 |
| primeintellect | unknown | no | 86.1 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 702.0 | 0.0060 |
| alibaba | unknown | yes | 85.4 | 144 | 0 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1317.0 | 0.0097 |
| coreweave/fp8 | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 382.0 | 0.0279 |
| crusoe/fp8 | fp8 | yes | 85.4 | 144 | 0 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 625.5 | 0.0268 |
| wafer/us | mxfp4 | yes | 85.4 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 444.5 | 0.0049 |
| modelrun/fp4 | fp4 | no | 84.7 | 144 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 816.5 | 0.0157 |
| deepinfra/fp8 | fp8 | yes | 84.0 | 144 | 0 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 428.0 | 0.0031 |
| dekallm | unknown | yes | 84.0 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1448.0 | 0.0166 |
| fireworks/us | unknown | no | 84.0 | 144 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 602.0 | 0.0421 |
| modal | unknown | no | 84.0 | 144 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 790.0 | 0.0229 |
| parasail/fp8 | fp8 | yes | 84.0 | 144 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 360.5 | 0.0278 |
| relace/fp4 | fp4 | no | 84.0 | 81 | 0 | 1.00 | 81.8 | 100.0 | 33.3 | 100.0 | 100.0 | 43.8 | 0 | 0 | 3757.0 | 0.0014 |
| stepfun/fp8 | fp8 | no | 84.0 | 144 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 734.0 | 0.0125 |
| together | unknown | no | 84.0 | 144 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 87.5 | 100.0 | 0.00 | 0 | 0 | 314.5 | 0.0279 |
| particle-ai/us | unknown | yes | 83.3 | 144 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 877.5 | 0.0039 |
| inference-net/fp8 | fp8 | yes | 82.6 | 144 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 452.0 | 0.0067 |
| decart/fp8 | fp8 | yes | 82.5 | 126 | 0.00 | 1.00 | 71.4 | 100.0 | 33.3 | 100.0 | 100.0 | 12.5 | 0 | 0 | 612.5 | 0.0103 |
| baseten/fast | unknown | no | 81.9 | 83 | 0 | 1.00 | 64.0 | 100.0 | 36.4 | 100.0 | 100.0 | 42.4 | 0 | 0 | 390.0 | 0.0363 |
| mistral/fp8 | fp8 | yes | 81.9 | 144 | 0.00 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1002.5 | 0.0283 |
| baseten | unknown | no | 81.2 | 144 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 592.0 | 0.0279 |
| ionstream | unknown | yes | 77.8 | 144 | 0.00 | 1.00 | 68.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 691.0 | 0.0146 |
| near-ai | unknown | no | 77.1 | 144 | 0 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1055.5 | 0.0276 |
| reka | unknown | no | 77.1 | 144 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 801.5 | 0.0167 |
| open-inference/fp4 | fp4 | yes | 75.0 | 144 | 0.00 | 1.00 | 62.5 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2892.0 | 0.0068 |
| baidu/fp8 | fp8 | no | 74.3 | 144 | 0 | 1.00 | 79.2 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 964.0 | 0.0135 |
| digitalocean | unknown | no | 74.3 | 144 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 638.0 | 0.0166 |
| ionstream/flex | unknown | yes | 73.6 | 144 | 0.00 | 1.00 | 85.4 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 427.0 | 0.0075 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, morph/fp8, particle-ai/us/flex, wafer/us, primeintellect, particle-ai/us, open-inference/fp4, wafer/mxfp4, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, ionstream/flex, deepinfra/fp8, cloudflare, sail-research/fp4/us, alibaba, streamlake/fp8, decart/fp8, stepfun/fp8, deepinfra/fp8/priority, baidu/fp8, cohere/fp8, deepseek, makora/fp8, sail-research/fp4, reka, ionstream, novita/fp8, modelrun/fp4, dekallm, digitalocean, gmicloud/fp8, atlas-cloud/fp8, phala, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast. Prompts with no plurality (excluded from exact match): 0.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 129 | n/a | 1.00 | 97.9 | 45.8 | 75.0 | 100.0 | 95.8 | 0.00 | 0 | 19 | 2702.5 | 0.1124 |
| mistral/zdr | unknown | yes | 100.0 | 129 | n/a | 1.00 | 100.0 | 58.3 | 79.2 | 100.0 | 87.5 | 0.00 | 0 | 14 | 2711.0 | 0.1173 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 15.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| darkbloom/fp4 | fp4 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2571.0 | 0.0061 |
| deepinfra/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 790.5 | 0.0145 |
| inceptron/fp8 | fp8 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 860.5 | 0.0162 |
| near-ai/fp8 | fp8 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1150.0 | 0.0088 |
| nextbit/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1121.5 | 0.0118 |
| venice | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 846.5 | 0.0151 |
| relace/fp4 | fp4 | yes | 97.6 | 127 | 0 | 1.00 | 97.8 | 100.0 | 85.0 | 100.0 | 100.0 | 11.8 | 0 | 0 | 3263.0 | 0.0033 |
| cohere/nvfp4 | nvfp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 557.5 | 0.0153 |
| coreweave/nvfp4 | nvfp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 1.40 | 0 | 0 | 711.0 | 0.0111 |
| crusoe/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 975.0 | 0.0144 |
| gmicloud/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2797.0 | 0.0073 |
| nebius/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1000.0 | 0.0145 |
| river | unknown | yes | 97.2 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 985.0 | 0.0116 |
| streamlake/fp8 | fp8 | no | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1852.0 | 0.0085 |
| parasail/fast | fp4 | yes | 97.1 | 137 | 0.00 | 1.00 | 100.0 | 100.0 | 90.9 | 100.0 | 100.0 | 4.90 | 0 | 0 | 707.0 | 0.0168 |
| friendli | unknown | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 505.5 | 0.0146 |
| open-inference/fp4 | fp4 | yes | 96.5 | 143 | 0 | 1.00 | 95.8 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 3259.0 | 0.0062 |
| primeintellect | unknown | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1266.0 | 0.0054 |
| mistral | unknown | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 820.5 | 0.0145 |
| morph/fp8 | fp8 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 95.7 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1953.0 | 0.0072 |
| novita/fp8 | fp8 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1330.5 | 0.0081 |
| particle-ai/nvfp4 | nvfp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1013.5 | 0.0120 |
| sail-research/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1593.5 | 0.0088 |
| inference-net/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 95.8 | 0.00 | 0 | 1 | 602.0 | 0.0084 |
| sail-research/us | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1543.0 | 0.0165 |
| together | unknown | no | 95.1 | 144 | 0 | 1.00 | 93.8 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1076.0 | 0.0146 |
| z-ai/fp8 | fp8 | no | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2068.5 | 0.0144 |
| baseten/fp8 | fp8 | no | 94.4 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 943.0 | 0.0145 |
| fireworks | unknown | no | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 892.0 | 0.0148 |
| makora/fp4 | fp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 821.0 | 0.0125 |
| wafer/us | nvfp4 | yes | 94.4 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 997.5 | 0.0044 |
| modal/fp4 | fp4 | no | 93.8 | 144 | 0 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 671.0 | 0.0147 |
| phala/nvfp4 | nvfp4 | yes | 93.8 | 144 | 0 | 1.00 | 95.8 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1555.0 | 0.0053 |
| siliconflow/fp8 | fp8 | no | 93.8 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1765.0 | 0.0145 |
| tenstorrent/fp8 | fp8 | yes | 92.7 | 137 | 0.00 | 1.00 | 91.5 | 100.0 | 68.2 | 100.0 | 100.0 | 4.90 | 0 | 1 | 1112.0 | 0.0068 |
| atlas-cloud/fp8 | fp8 | yes | 92.4 | 144 | 0 | 1.00 | 97.9 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2417.5 | 0.0120 |
| digitalocean | unknown | no | 90.3 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1080.0 | 0.0109 |
| inference-net/us | fp4 | yes | 90.3 | 144 | 0.00 | 1.00 | 95.8 | 95.8 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 568.5 | 0.0105 |
| wafer/nvfp4 | nvfp4 | yes | 88.9 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 95.8 | 0.00 | 0 | 1 | 1012.0 | 0.0065 |
| reka | unknown | yes | 87.5 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 825.5 | 0.0111 |
| baseten/fp8/us | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| parasail/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, wafer/us, primeintellect, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, morph/fp8, tenstorrent/fp8, gmicloud/fp8, near-ai/fp8, novita/fp8, streamlake/fp8, inference-net/us, inference-net/fp4, phala/nvfp4, digitalocean, reka, coreweave/nvfp4, river, nextbit/fp4, particle-ai/nvfp4, makora/fp4, mistral, cohere/nvfp4, nebius/fp4, modal/fp4, baseten/fp8/us, crusoe/fp4, atlas-cloud/fp8, fireworks, friendli, siliconflow/fp8, together, parasail/fp4, baseten/fp8, venice, deepinfra/fp4, z-ai/fp8, inceptron/fp8, sail-research/us, sail-research/fp4, parasail/fast. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | yes | 100.0 | 120 | n/a | 1.00 | 44.4 | 100.0 | 54.2 | 100.0 | 100.0 | 3.50 | 0 | 0 | 865.0 | 0.0123 |
| novita/bf16 | bf16 | yes | 100.0 | 117 | n/a | 1.00 | 37.2 | 100.0 | 58.3 | 100.0 | 100.0 | 5.60 | 0 | 0 | 1486.5 | 0.0123 |
| sambanova | unknown | no | 99.0 | 98 | 0 | 1.00 | 43.3 | 100.0 | 54.5 | 100.0 | 100.0 | 23.6 | 0 | 0 | 1416.0 | 0.0277 |
| siliconflow/fp8 | fp8 | no | 95.8 | 120 | 0 | 1.00 | 42.2 | 100.0 | 56.5 | 100.0 | 100.0 | 3.50 | 0 | 0 | 991.0 | 0.0607 |
| deepinfra/fp8 | fp8 | yes | 93.5 | 124 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1115.5 | 0.0171 |
| parasail/fp8 | fp8 | yes | 93.5 | 124 | 0.00 | 1.00 | 43.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1099.0 | 0.0131 |
| deepinfra/fp8/flex | fp8 | yes | 92.7 | 124 | 0 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2868.5 | 0.0137 |
| deepinfra/fp8/priority | fp8 | yes | 92.7 | 124 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1146.0 | 0.0256 |
| friendli | unknown | yes | 92.7 | 124 | 0 | 1.00 | 39.6 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 342.5 | 0.0125 |
| coreweave/fp4 | fp4 | yes | 88.7 | 124 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 481.5 | 0.0091 |
| io-net | unknown | no | 87.9 | 124 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 854.0 | 0.0320 |
| modal | unknown | no | 87.1 | 124 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 532.0 | 0.0262 |
| deepinfra/turbo | fp4 | yes | 86.3 | 124 | 0 | 1.00 | 35.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 579.0 | 0.0089 |
| dekallm | unknown | yes | 86.2 | 116 | 0.00 | 1.00 | 39.1 | 100.0 | 59.1 | 100.0 | 100.0 | 5.60 | 0 | 0 | 1135.0 | 0.0112 |
| chutes/fp4 | fp4 | yes | 85.5 | 124 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1976.0 | 0.0107 |
| modelrun/fp4 | fp4 | no | 85.5 | 124 | 0.00 | 1.00 | 37.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 213.5 | 0.0618 |
| nextbit/fp4 | fp4 | yes | 83.9 | 124 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1034.5 | 0.0132 |
| venice/fp4 | fp4 | no | 83.1 | 124 | 0 | 1.00 | 35.4 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 724.5 | 0.0106 |
| primeintellect/fp4 | fp4 | yes | 80.6 | 124 | 0.00 | 1.00 | 27.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 586.0 | 0.0165 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: crusoe/bf16, novita/bf16. Prompts with no plurality (excluded from exact match): 19.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| streamlake | unknown | no | 94.9 | 138 | 0 | 1.00 | 70.8 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1468.5 | 0.0424 |
| deepinfra/fp8 | fp8 | yes | 94.2 | 138 | 0.00 | 1.00 | 70.8 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 981.5 | 0.0343 |
| gmicloud/bf16 | bf16 | yes | 93.5 | 138 | 0 | 1.00 | 72.9 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2083.5 | 0.0264 |
| primalabs/fp8 | fp8 | yes | 91.3 | 138 | 0.00 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 599.5 | 0.3542 |
| xiaomi/fp8 | fp8 | no | 91.3 | 138 | 0.00 | 1.00 | 66.7 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1635.0 | 0.0376 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: gmicloud/bf16, deepinfra/fp8, xiaomi/fp8, streamlake, primalabs/fp8. Prompts with no plurality (excluded from exact match): 6.

## Footer

- Rows: 22464; errors 1000; misrouted 0; truncated (finish_reason length) 65; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $7.3649; billed: $3.9919; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
