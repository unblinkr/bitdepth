# Bitdepth scorecard 2026-11-23

Run `2026-11-23-live`, source `live`, started 2026-11-23T19:17:33Z, finished 2026-11-23T21:16:42Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/bf16 | bf16 | yes | 99.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 5230.0 | 0.0045 |
| near-ai/fp4 | fp4 | yes | 99.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1240.0 | 0.0037 |
| baseten/fp4 | fp4 | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 672.0 | 0.0131 |
| baseten/fp4/us | fp4 | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 697.5 | 0.0129 |
| cerebras/fp16 | fp16 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 264.5 | 0.0365 |
| groq | unknown | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 292.5 | 0.0181 |
| mancer/fp8 | fp8 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 790.0 | 0.0103 |
| primeintellect/fp4 | fp4 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 588.0 | 0.0325 |
| amazon-bedrock | unknown | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 502.5 | 0.0181 |
| crusoe/bf16 | bf16 | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 593.5 | 0.0065 |
| amazon-bedrock/eu-west-1 | unknown | no | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 468.5 | 0.0184 |
| nebius/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 432.5 | 0.0176 |
| parasail/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 576.5 | 0.0152 |
| sambanova | unknown | no | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 422.0 | 0.0206 |
| coreweave/fp4 | fp4 | yes | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 619.0 | 0.0041 |
| akashml/fp4 | fp4 | yes | 94.4 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1347.0 | 0.0042 |
| google-vertex/global | unknown | yes | 92.3 | 143 | 0 | 1.00 | 93.8 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 425.0 | 0.0109 |
| parasail/fast | fp4 | yes | 90.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 473.5 | 0.0190 |
| digitalocean | unknown | no | 90.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1073.0 | 0.0083 |
| venice/int4 | int4 | no | 82.5 | 143 | 0 | 1.00 | 77.1 | 100.0 | 75.0 | 100.0 | 87.5 | 0.00 | 0 | 12 | 1572.5 | 0.0048 |
| siliconflow/fp8 | fp8 | no | 64.3 | 143 | 0 | 1.00 | 77.1 | 4.20 | 50.0 | 100.0 | 87.5 | 0.00 | 0 | 1 | 1838.0 | 0.0219 |
| fireworks | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 1.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 90.0 | 130 | 0 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1968.0 | 0.1275 |
| alibaba/fp8 | fp8 | yes | 86.9 | 130 | 4 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1984.0 | 0.1289 |
| digitalocean | unknown | no | 82.1 | 28 | 8 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 100.0 | 79.9 | 0 | 0 | 5911.0 | 0.0228 |
| deepinfra/fp8 | fp8 | yes | 80.0 | 130 | 3.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1972.0 | 0.1583 |
| relace/fp4 | fp4 | no | 77.7 | 130 | 8 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 865.5 | 0.0800 |
| deepinfra/fp8/priority | fp8 | yes | 76.2 | 130 | 8 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1629.5 | 0.0676 |
| siliconflow/fp8 | fp8 | no | 75.4 | 130 | 8.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2537.5 | 0.0332 |
| streamlake/fp8 | fp8 | no | 75.4 | 130 | 4.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2236.5 | 0.0231 |
| venice | unknown | no | 73.8 | 130 | 6.00 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2161.5 | 0.0733 |
| deepinfra/fp8/flex | fp8 | yes | 69.6 | 69 | 5 | 1.00 | 100.0 | 100.0 | 53.8 | 100.0 | 83.3 | 44.4 | 0 | 0 | 2751.5 | 0.0361 |
| azure/us | unknown | no | 57.7 | 130 | 1 | 1.00 | 95.8 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 1 | 1099.0 | 0.1774 |
| baidu/fp8 | fp8 | no | 40.8 | 130 | 1 | 1.00 | 95.8 | 100.0 | 20.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1852.0 | 0.0555 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, siliconflow/fp8, deepinfra/fp8/flex, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 14.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fast | unknown | no | 90.7 | 118 | 0 | 1.00 | 75.0 | 100.0 | 55.6 | 100.0 | 100.0 | 15.3 | 0 | 0 | 303.0 | 0.0470 |
| primeintellect | unknown | no | 89.3 | 140 | 0 | 1.00 | 83.3 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 557.5 | 0.0088 |
| crusoe/fp8 | fp8 | yes | 88.6 | 140 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 628.5 | 0.0177 |
| coreweave/fp8 | fp8 | yes | 87.9 | 140 | 0 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 312.5 | 0.0282 |
| parasail/fp8 | fp8 | yes | 87.9 | 140 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 350.5 | 0.0280 |
| ambient/fp4 | fp4 | yes | 87.1 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 734.5 | 0.0045 |
| makora/fp8 | fp8 | yes | 87.1 | 140 | 0.00 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 564.0 | 0.0151 |
| morph/fp8 | fp8 | yes | 87.1 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 562.0 | 0.0062 |
| particle-ai/us | unknown | yes | 87.1 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 524.5 | 0.0040 |
| particle-ai/us/flex | unknown | yes | 87.1 | 140 | 0.00 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 660.0 | 0.0037 |
| antdigital/fp8 | fp8 | yes | 86.4 | 140 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1153.5 | 0.0083 |
| cloudflare | unknown | yes | 86.4 | 140 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1145.0 | 0.0076 |
| digitalocean | unknown | no | 86.4 | 140 | 0 | 1.00 | 79.2 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 672.0 | 0.0183 |
| reka | unknown | no | 85.7 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 413.5 | 0.0281 |
| relace/fp4 | fp4 | no | 85.7 | 140 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 649.0 | 0.0112 |
| sail-research/fp4/us | fp4 | yes | 85.7 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 998.0 | 0.0035 |
| wafer/us | mxfp4 | yes | 85.7 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 377.0 | 0.0048 |
| baseten | unknown | no | 85.0 | 140 | 0 | 1.00 | 79.2 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 739.0 | 0.0280 |
| deepinfra/fp8 | fp8 | yes | 85.0 | 140 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 639.5 | 0.0087 |
| fireworks/us | unknown | no | 85.0 | 140 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 462.5 | 0.0417 |
| google-vertex/global | unknown | yes | 85.0 | 140 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 560.0 | 0.0280 |
| pearl-research/fp8 | fp8 | yes | 85.0 | 140 | 0 | 1.00 | 75.0 | 95.8 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 897.0 | 0.0051 |
| wafer/mxfp4 | mxfp4 | yes | 85.0 | 140 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 391.0 | 0.0036 |
| deepinfra/fp8/flex | fp8 | yes | 84.3 | 140 | 0.00 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1908.0 | 0.0071 |
| fireworks | unknown | no | 84.3 | 140 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 862.5 | 0.0048 |
| venice/fp8 | fp8 | no | 84.3 | 140 | 0.00 | 1.00 | 81.2 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1071.5 | 0.0281 |
| modal | unknown | no | 83.9 | 137 | 0.00 | 1.00 | 76.6 | 100.0 | 54.2 | 100.0 | 100.0 | 2.10 | 0 | 0 | 674.0 | 0.0224 |
| cohere/fp8 | fp8 | yes | 83.6 | 140 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 383.5 | 0.0105 |
| deepinfra/fp8/priority | fp8 | yes | 83.6 | 140 | 0 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 699.0 | 0.0036 |
| mistral/fp8 | fp8 | yes | 83.6 | 140 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 732.5 | 0.0280 |
| modelrun/fp4 | fp4 | no | 83.6 | 140 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 781.5 | 0.0158 |
| primalabs | unknown | yes | 83.6 | 140 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 580.0 | 0.0224 |
| inference-net/fp8 | fp8 | yes | 82.9 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 426.5 | 0.0064 |
| siliconflow/fp8 | fp8 | no | 82.9 | 140 | 0.00 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 669.5 | 0.0137 |
| morph/fast | fp8 | yes | 82.8 | 134 | 0 | 1.00 | 76.1 | 100.0 | 59.1 | 100.0 | 100.0 | 4.20 | 0 | 0 | 367.5 | 0.0554 |
| alibaba | unknown | yes | 82.1 | 140 | 0 | 1.00 | 68.8 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 779.0 | 0.0084 |
| inceptron/fp4 | fp4 | yes | 82.1 | 140 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 975.0 | 0.0103 |
| inference-net/us | fp8 | yes | 81.4 | 140 | 0.00 | 1.00 | 70.8 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 427.0 | 0.0085 |
| river | unknown | yes | 81.4 | 140 | 0.00 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 973.5 | 0.0113 |
| sail-research/fp4 | fp4 | yes | 81.4 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 995.5 | 0.0029 |
| ionstream | unknown | yes | 80.0 | 140 | 0.00 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 584.5 | 0.0186 |
| fireworks/spot | unknown | no | 79.3 | 140 | 0 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 799.5 | 0.0144 |
| tenstorrent/fp8 | fp8 | yes | 79.2 | 125 | 0.00 | 1.00 | 70.5 | 100.0 | 45.5 | 100.0 | 100.0 | 10.4 | 0 | 0 | 879.0 | 0.0028 |
| near-ai | unknown | no | 77.9 | 140 | 0 | 1.00 | 66.7 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1106.5 | 0.0277 |
| baidu/fp8 | fp8 | no | 77.1 | 140 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 722.5 | 0.0092 |
| nebius/fp4 | fp4 | yes | 76.4 | 140 | 0 | 1.00 | 85.4 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 488.5 | 0.0173 |
| open-inference/fp4 | fp4 | yes | 72.1 | 140 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 682.0 | 0.0064 |
| streamlake/fp8 | fp8 | no | 72.1 | 140 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1096.5 | 0.0103 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, tenstorrent/fp8, wafer/us, sail-research/fp4/us, sail-research/fp4, ambient/fp4, pearl-research/fp8, particle-ai/us, open-inference/fp4, morph/fp8, wafer/mxfp4, primeintellect, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, antdigital/fp8, alibaba, baidu/fp8, deepinfra/fp8, inceptron/fp4, cloudflare, streamlake/fp8, cohere/fp8, river, relace/fp4, deepinfra/fp8/priority, fireworks/spot, siliconflow/fp8, deepseek, makora/fp8, modelrun/fp4, nebius/fp4, crusoe/fp8, digitalocean, ionstream, primalabs, modal, google-vertex/global, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, reka, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 4.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 136 | n/a | 1.00 | 100.0 | 41.7 | 70.8 | 100.0 | 91.7 | 0.00 | 0 | 21 | 3918.5 | 0.1101 |
| mistral/zdr | unknown | yes | 100.0 | 136 | n/a | 1.00 | 100.0 | 45.8 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 21 | 4283.0 | 0.1192 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 8.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| darkbloom/fp4 | fp4 | yes | 99.3 | 144 | 0 | 1.00 | 97.9 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1884.0 | 0.0061 |
| baseten/fp8 | fp8 | no | 98.6 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 380.0 | 0.0146 |
| deepinfra/fp4 | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 671.5 | 0.0097 |
| near-ai/fp8 | fp8 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1763.0 | 0.0088 |
| parasail/fast | fp4 | yes | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 438.0 | 0.0183 |
| reka | unknown | yes | 98.6 | 144 | 0.00 | 1.00 | 95.8 | 100.0 | 100.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 441.5 | 0.0111 |
| friendli | unknown | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 354.5 | 0.0146 |
| morph/fp8 | fp8 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1844.0 | 0.0120 |
| parasail/fp8 | fp8 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 654.5 | 0.0144 |
| particle-ai/nvfp4 | nvfp4 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 518.5 | 0.0068 |
| particle-ai/nvfp4/flex | nvfp4 | yes | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 609.0 | 0.0068 |
| river | unknown | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 686.5 | 0.0116 |
| sail-research/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1340.5 | 0.0161 |
| sail-research/us | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1275.0 | 0.0166 |
| streamlake/fp8 | fp8 | no | 97.9 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1652.5 | 0.0085 |
| tenstorrent/fp8 | fp8 | yes | 97.3 | 111 | 0 | 1.00 | 97.6 | 100.0 | 87.5 | 100.0 | 100.0 | 22.9 | 0 | 0 | 960.0 | 0.0053 |
| inceptron/fp8 | fp8 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 441.0 | 0.0161 |
| open-inference/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 775.5 | 0.0064 |
| relace/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2647.5 | 0.0042 |
| coreweave/nvfp4 | nvfp4 | yes | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 581.0 | 0.0114 |
| digitalocean | unknown | no | 96.5 | 144 | 0 | 1.00 | 93.8 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 439.0 | 0.0094 |
| modal/fp4 | fp4 | no | 96.5 | 144 | 0 | 1.00 | 95.8 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 472.5 | 0.0147 |
| siliconflow/fp8 | fp8 | no | 96.5 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1420.5 | 0.0099 |
| venice | unknown | no | 96.5 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 772.5 | 0.0155 |
| baidu/fp8 | fp8 | no | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2185.5 | 0.0144 |
| cohere/nvfp4 | nvfp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 97.9 | 100.0 | 91.3 | 100.0 | 100.0 | 0.70 | 0 | 1 | 865.0 | 0.0106 |
| crusoe/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 794.5 | 0.0145 |
| fireworks/us | unknown | no | 95.8 | 144 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 420.0 | 0.0218 |
| nebius/fp4 | fp4 | yes | 95.8 | 144 | 0.00 | 1.00 | 93.8 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 746.0 | 0.0145 |
| mistral | unknown | yes | 95.1 | 144 | 0 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 593.0 | 0.0145 |
| fireworks | unknown | no | 93.8 | 144 | 0 | 1.00 | 97.9 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 658.0 | 0.0151 |
| makora/fp4 | fp4 | yes | 93.8 | 144 | 0 | 1.00 | 95.8 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 457.0 | 0.0126 |
| z-ai/fp8 | fp8 | no | 92.4 | 144 | 0 | 1.00 | 97.9 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1145.5 | 0.0145 |
| kt | unknown | no | 90.3 | 144 | 0.00 | 1.00 | 87.5 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 670.0 | 0.0145 |
| inference-net/fp4 | fp4 | yes | 89.6 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 287.5 | 0.0100 |
| inference-net/us | fp4 | yes | 86.8 | 144 | 0 | 1.00 | 97.9 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 306.0 | 0.0105 |
| wafer/nvfp4 | nvfp4 | yes | 81.9 | 144 | 0.00 | 1.00 | 93.8 | 100.0 | 83.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 369.5 | 0.0066 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, particle-ai/nvfp4/flex, tenstorrent/fp8, near-ai/fp8, streamlake/fp8, digitalocean, siliconflow/fp8, deepinfra/fp4, cohere/nvfp4, inference-net/us, inference-net/fp4, reka, coreweave/nvfp4, river, morph/fp8, particle-ai/nvfp4, makora/fp4, baidu/fp8, mistral, kt, nebius/fp4, modal/fp4, crusoe/fp4, fireworks, friendli, parasail/fp8, baseten/fp8, venice, z-ai/fp8, inceptron/fp8, sail-research/us, sail-research/fp4, parasail/fast, fireworks/us. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8/flex | fp8 | yes | 92.8 | 138 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2325.0 | 0.0137 |
| deepinfra/fp8 | fp8 | yes | 91.3 | 138 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 851.5 | 0.0171 |
| deepinfra/fp8/priority | fp8 | yes | 91.3 | 138 | 0.00 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 886.0 | 0.0256 |
| crusoe/bf16 | bf16 | yes | 89.1 | 138 | 0 | 1.00 | 43.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 640.5 | 0.0125 |
| siliconflow/fp8 | fp8 | no | 89.1 | 138 | 0 | 1.00 | 41.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1153.0 | 0.0611 |
| sambanova | unknown | no | 88.4 | 138 | 0.00 | 1.00 | 43.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1384.5 | 0.0340 |
| friendli | unknown | yes | 84.1 | 138 | 0.00 | 1.00 | 37.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 273.5 | 0.0125 |
| parasail/fp8 | fp8 | yes | 84.1 | 138 | 0.00 | 1.00 | 39.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2210.5 | 0.0133 |
| venice/fp4 | fp4 | no | 82.6 | 138 | 0.00 | 1.00 | 41.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 825.0 | 0.0104 |
| primeintellect/fp8 | fp8 | yes | 81.2 | 138 | 0.00 | 1.00 | 39.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 630.5 | 0.0168 |
| coreweave/fp4 | fp4 | yes | 80.4 | 138 | 0 | 1.00 | 39.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 480.0 | 0.0092 |
| modal | unknown | no | 80.3 | 137 | 0 | 1.00 | 38.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 591.0 | 0.0261 |
| deepinfra/turbo | fp4 | yes | 79.7 | 138 | 0.00 | 1.00 | 39.6 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 555.0 | 0.0098 |
| chutes/fp4 | fp4 | yes | 79.0 | 138 | 0 | 1.00 | 33.3 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2738.5 | 0.0107 |
| modelrun/fp4 | fp4 | no | 77.5 | 138 | 0 | 1.00 | 37.5 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 199.5 | 0.0619 |
| nextbit/fp4 | fp4 | yes | 73.9 | 138 | 0.00 | 1.00 | 33.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 459.0 | 0.0110 |
| kt | unknown | no | 73.2 | 138 | 0 | 1.00 | 37.5 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 509.5 | 0.0092 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: kt, coreweave/fp4, venice/fp4, chutes/fp4, nextbit/fp4, deepinfra/turbo, crusoe/bf16, friendli, parasail/fp8, deepinfra/fp8/flex, primeintellect/fp8, deepinfra/fp8, deepinfra/fp8/priority, modal, sambanova, modelrun/fp4, siliconflow/fp8. Prompts with no plurality (excluded from exact match): 6.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| primalabs/fp8 | fp8 | yes | 95.0 | 139 | 0 | 1.00 | 70.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1004.5 | 0.2336 |
| deepinfra/fp8 | fp8 | yes | 91.4 | 139 | 0.00 | 1.00 | 75.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 764.0 | 0.0343 |
| streamlake | unknown | no | 90.6 | 139 | 0 | 1.00 | 75.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1292.5 | 0.0390 |
| xiaomi/fp8 | fp8 | no | 89.2 | 139 | 0 | 1.00 | 68.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2438.0 | 0.0365 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: deepinfra/fp8, streamlake, xiaomi/fp8, primalabs/fp8. Prompts with no plurality (excluded from exact match): 5.

## Footer

- Rows: 20592; errors 548; misrouted 0; truncated (finish_reason length) 70; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $6.4592; billed: $3.3821; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
