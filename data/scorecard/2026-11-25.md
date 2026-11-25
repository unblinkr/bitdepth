# Bitdepth scorecard 2026-11-25

Run `2026-11-25-live`, source `live`, started 2026-11-25T18:01:13Z, finished 2026-11-25T20:42:07Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/bf16 | bf16 | yes | 100.0 | 143 | n/a | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 3653.0 | 0.0042 |
| cerebras/fp16 | fp16 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 313.5 | 0.0372 |
| digitalocean | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1253.0 | 0.0086 |
| groq | unknown | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 354.5 | 0.0183 |
| baseten/fp4 | fp4 | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 574.0 | 0.0129 |
| near-ai/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 1570.5 | 0.0038 |
| nebius/fp4 | fp4 | yes | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 490.0 | 0.0177 |
| amazon-bedrock | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 734.5 | 0.0184 |
| baseten/fp4/us | fp4 | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 555.5 | 0.0130 |
| crusoe/bf16 | bf16 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 2 | 712.0 | 0.0067 |
| parasail/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 3 | 588.5 | 0.0155 |
| primeintellect/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 599.0 | 0.0363 |
| sambanova | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 406.5 | 0.0206 |
| akashml/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 954.5 | 0.0043 |
| mancer/fp8 | fp8 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 794.5 | 0.0106 |
| coreweave/fp4 | fp4 | yes | 94.4 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 790.0 | 0.0042 |
| google-vertex/global | unknown | yes | 94.4 | 144 | 0.00 | 1.00 | 93.8 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 420.0 | 0.0110 |
| amazon-bedrock/eu-west-1 | unknown | no | 93.8 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 726.0 | 0.0185 |
| parasail/fast | fp4 | yes | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 2 | 501.0 | 0.0201 |
| venice/int4 | int4 | no | 84.7 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 6 | 3918.5 | 0.0043 |
| siliconflow/fp8 | fp8 | no | 70.8 | 144 | 0.00 | 1.00 | 77.1 | 37.5 | 66.7 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1548.0 | 0.0217 |
| fireworks | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 82.8 | 128 | 12.0 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2009.5 | 0.1302 |
| alibaba/fp8 | fp8 | yes | 80.5 | 128 | 9 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1946.5 | 0.1289 |
| deepinfra/fp8 | fp8 | yes | 80.5 | 128 | 7 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1368.0 | 0.1361 |
| venice | unknown | no | 78.9 | 128 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1793.0 | 0.0690 |
| deepinfra/fp8/priority | fp8 | yes | 78.1 | 128 | 2.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1296.5 | 0.0663 |
| relace/fp4 | fp4 | no | 76.6 | 128 | 4.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 91.7 | 0.00 | 0 | 0 | 811.5 | 0.0672 |
| deepinfra/fp8/flex | fp8 | yes | 75.2 | 109 | 4 | 1.00 | 100.0 | 100.0 | 65.0 | 100.0 | 90.0 | 15.3 | 0 | 0 | 1858.5 | 0.0521 |
| baidu/fp8 | fp8 | no | 73.4 | 128 | 4.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1361.0 | 0.0673 |
| streamlake/fp8 | fp8 | no | 68.8 | 128 | 4.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2538.0 | 0.0280 |
| siliconflow/fp8 | fp8 | no | 64.8 | 128 | 3 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2127.5 | 0.0807 |
| azure/us | unknown | no | 54.7 | 128 | 0.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1173.0 | 0.1697 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, streamlake/fp8, baidu/fp8, siliconflow/fp8, deepinfra/fp8/flex, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 16.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fast | unknown | no | 91.6 | 131 | 0 | 1.00 | 76.7 | 100.0 | 39.1 | 100.0 | 100.0 | 6.90 | 0 | 0 | 332.0 | 0.0508 |
| featherless/fp8 | fp8 | yes | 90.1 | 141 | 0.00 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 896.0 | 0.0208 |
| deepinfra/fp8 | fp8 | yes | 89.4 | 141 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 750.0 | 0.0087 |
| google-vertex/global | unknown | yes | 89.4 | 141 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 547.0 | 0.0276 |
| modal | unknown | no | 89.4 | 141 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 743.5 | 0.0230 |
| morph/fast | fp8 | yes | 89.2 | 139 | 0 | 1.00 | 76.6 | 100.0 | 43.5 | 100.0 | 100.0 | 1.40 | 0 | 0 | 507.0 | 0.0549 |
| pearl-research/fp8 | fp8 | yes | 89.0 | 136 | 0 | 1.00 | 78.7 | 100.0 | 41.7 | 100.0 | 100.0 | 3.50 | 0 | 0 | 1766.0 | 0.0047 |
| venice/fp8 | fp8 | no | 88.7 | 141 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1009.0 | 0.0274 |
| fireworks/spot | unknown | no | 88.6 | 79 | 0 | 1.00 | 64.0 | 100.0 | 53.8 | 100.0 | 100.0 | 45.1 | 0 | 0 | 707.0 | 0.0074 |
| ambient/fp4 | fp4 | yes | 87.9 | 141 | 0 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 859.5 | 0.0045 |
| cloudflare | unknown | yes | 87.9 | 141 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1171.0 | 0.0042 |
| morph/fp8 | fp8 | yes | 87.9 | 141 | 0 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 576.0 | 0.0057 |
| fireworks/us | unknown | no | 87.4 | 135 | 0 | 1.00 | 75.6 | 100.0 | 45.8 | 100.0 | 100.0 | 4.20 | 0 | 0 | 520.0 | 0.0336 |
| coreweave/fp8 | fp8 | yes | 87.2 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 362.5 | 0.0276 |
| particle-ai/us | unknown | yes | 87.2 | 141 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 543.0 | 0.0044 |
| particle-ai/us/flex | unknown | yes | 87.2 | 141 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 642.5 | 0.0043 |
| primalabs | unknown | yes | 87.2 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 639.5 | 0.0222 |
| reka | unknown | no | 87.2 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 434.5 | 0.0278 |
| baseten | unknown | no | 86.5 | 141 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 684.0 | 0.0274 |
| parasail/fp8 | fp8 | yes | 86.5 | 141 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 350.0 | 0.0274 |
| primeintellect | unknown | no | 86.5 | 141 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 484.5 | 0.0159 |
| siliconflow/fp8 | fp8 | no | 86.5 | 141 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 723.0 | 0.0136 |
| mistral/fp8 | fp8 | yes | 85.8 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 873.5 | 0.0276 |
| pareto-inference/fp8 | fp8 | yes | 85.8 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1149.5 | 0.0069 |
| fireworks | unknown | no | 85.7 | 140 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 594.0 | 0.0208 |
| cohere/fp8 | fp8 | yes | 85.1 | 141 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 444.0 | 0.0105 |
| modelrun/fp4 | fp4 | no | 85.1 | 141 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 860.5 | 0.0096 |
| relace/fp4 | fp4 | no | 85.1 | 141 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 598.5 | 0.0113 |
| tenstorrent/fp8 | fp8 | yes | 85.1 | 141 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 646.0 | 0.0087 |
| wafer/mxfp4 | mxfp4 | yes | 85.1 | 141 | 0 | 1.00 | 79.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 402.5 | 0.0029 |
| alibaba | unknown | yes | 84.4 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 756.0 | 0.0083 |
| digitalocean | unknown | no | 84.4 | 141 | 0.00 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 718.0 | 0.0182 |
| wafer/us | mxfp4 | yes | 84.4 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 379.5 | 0.0046 |
| antdigital/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1201.5 | 0.0083 |
| crusoe/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 83.3 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 703.0 | 0.0176 |
| inceptron/fp4 | fp4 | yes | 83.7 | 141 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 937.0 | 0.0099 |
| inference-net/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 83.3 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 404.5 | 0.0066 |
| inference-net/us | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 372.0 | 0.0088 |
| makora/fp8 | fp8 | yes | 83.7 | 141 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 586.5 | 0.0146 |
| deepinfra/fp8/priority | fp8 | yes | 82.6 | 138 | 0.00 | 1.00 | 78.3 | 100.0 | 47.8 | 100.0 | 91.7 | 2.10 | 0 | 0 | 805.0 | 0.0033 |
| deepinfra/fp8/flex | fp8 | yes | 82.3 | 141 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 6618.0 | 0.0070 |
| ionstream | unknown | yes | 80.9 | 141 | 0 | 1.00 | 68.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 659.0 | 0.0184 |
| river | unknown | yes | 80.1 | 141 | 0.00 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 806.0 | 0.0110 |
| nebius/fp4 | fp4 | yes | 76.6 | 141 | 0 | 1.00 | 87.5 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 496.0 | 0.0172 |
| baidu/fp8 | fp8 | no | 75.9 | 141 | 0.00 | 1.00 | 83.3 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 811.5 | 0.0092 |
| open-inference/fp4 | fp4 | yes | 75.9 | 141 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 921.0 | 0.0067 |
| near-ai | unknown | no | 73.8 | 141 | 0 | 1.00 | 81.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1463.0 | 0.0281 |
| streamlake/fp8 | fp8 | no | 70.9 | 141 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1290.0 | 0.0084 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, sail-research/fp4/us, sail-research/fp4, ambient/fp4, open-inference/fp4, pearl-research/fp8, particle-ai/us, morph/fp8, wafer/mxfp4, pareto-inference/fp8, cloudflare, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, antdigital/fp8, streamlake/fp8, alibaba, tenstorrent/fp8, baidu/fp8, deepinfra/fp8, modelrun/fp4, inceptron/fp4, cohere/fp8, river, relace/fp4, deepinfra/fp8/priority, fireworks/spot, siliconflow/fp8, deepseek, makora/fp8, primeintellect, nebius/fp4, crusoe/fp8, digitalocean, ionstream, featherless/fp8, primalabs, modal, google-vertex/global, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, reka, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 3.

## Footer

- Rows: 12096; errors 692; misrouted 0; truncated (finish_reason length) 29; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.188; billed: $2.0518; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
