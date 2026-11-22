# Bitdepth scorecard 2026-11-22

Run `2026-11-22-live`, source `live`, started 2026-11-22T15:25:01Z, finished 2026-11-22T16:15:43Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| parasail/fast | fp4 | yes | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 537.5 | 0.0193 |
| parasail/fp4 | fp4 | yes | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 642.5 | 0.0148 |
| together | unknown | no | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 585.0 | 0.0179 |
| deepinfra/bf16 | bf16 | yes | 98.5 | 134 | 0.00 | 1.00 | 100.0 | 100.0 | 86.4 | 100.0 | 100.0 | 6.20 | 0 | 1 | 5210.0 | 0.0037 |
| baseten/fp4 | fp4 | no | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 548.0 | 0.0128 |
| cerebras/fp16 | fp16 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 302.0 | 0.0366 |
| groq | unknown | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 301.5 | 0.0180 |
| near-ai/fp4 | fp4 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1302.0 | 0.0038 |
| baseten/fp4/us | fp4 | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 499.0 | 0.0129 |
| crusoe/bf16 | bf16 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 513.0 | 0.0065 |
| akashml/fp4 | fp4 | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 896.0 | 0.0042 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 471.5 | 0.0179 |
| digitalocean | unknown | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1355.0 | 0.0084 |
| amazon-bedrock | unknown | no | 95.8 | 143 | 0.00 | 1.00 | 97.9 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 482.0 | 0.0180 |
| coreweave/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 648.5 | 0.0041 |
| dekallm/bf16 | bf16 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 5702.5 | 0.0041 |
| primeintellect/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 606.5 | 0.0342 |
| mancer/fp8 | fp8 | yes | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 809.5 | 0.0105 |
| sambanova | unknown | no | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 453.5 | 0.0206 |
| nebius/fp4 | fp4 | yes | 92.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 473.5 | 0.0176 |
| google-vertex/global | unknown | yes | 88.8 | 143 | 0.00 | 1.00 | 93.8 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 445.0 | 0.0109 |
| venice/int4 | int4 | no | 81.1 | 143 | 0 | 1.00 | 68.8 | 100.0 | 79.2 | 100.0 | 83.3 | 0.00 | 0 | 16 | 2106.0 | 0.0051 |
| siliconflow/fp8 | fp8 | no | 65.7 | 143 | 0 | 1.00 | 83.3 | 8.30 | 50.0 | 95.8 | 91.7 | 0.00 | 0 | 0 | 1890.5 | 0.0216 |
| fireworks | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 1.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 85.4 | 130 | 8 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2066.5 | 0.1276 |
| digitalocean | unknown | no | 85.4 | 130 | 1 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 10848.5 | 0.0963 |
| deepinfra/fp8/flex | fp8 | yes | 83.1 | 130 | 7.50 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1912.5 | 0.0829 |
| alibaba/fp8/us-east-1 | fp8 | yes | 81.5 | 130 | 7.50 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1876.0 | 0.1385 |
| deepinfra/fp8/priority | fp8 | yes | 80.0 | 130 | 5.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1145.0 | 0.0686 |
| streamlake/fp8 | fp8 | no | 78.5 | 130 | 1.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2399.5 | 0.0258 |
| siliconflow/fp8 | fp8 | no | 77.7 | 130 | 3 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2615.0 | 0.0504 |
| venice | unknown | no | 76.9 | 130 | 6.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1420.0 | 0.0701 |
| baidu/fp8 | fp8 | no | 75.4 | 130 | 3.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2084.5 | 0.0604 |
| relace/fp4 | fp4 | no | 74.6 | 130 | 5 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 811.5 | 0.0803 |
| deepinfra/fp8 | fp8 | yes | 73.8 | 130 | 0.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1238.5 | 0.0640 |
| azure/us | unknown | no | 60.8 | 130 | 1 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1446.0 | 0.1753 |
| novita/fp8 | fp8 | yes | 46.2 | 130 | 0.50 | 1.00 | 97.9 | 100.0 | 29.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2192.5 | 0.1153 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, siliconflow/fp8, deepinfra/fp8/flex, digitalocean, novita/fp8, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 14.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cloudflare | unknown | yes | 89.5 | 143 | 0 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 938.5 | 0.0059 |
| baseten/fast | unknown | no | 88.6 | 132 | 0 | 1.00 | 78.3 | 100.0 | 33.3 | 100.0 | 100.0 | 7.60 | 0 | 0 | 313.0 | 0.0507 |
| relace/fp4 | fp4 | no | 88.1 | 143 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1301.0 | 0.0110 |
| fireworks | unknown | no | 87.4 | 143 | 0.00 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 677.5 | 0.0043 |
| parasail/fp8 | fp8 | yes | 87.4 | 143 | 0.00 | 1.00 | 79.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 278.0 | 0.0276 |
| ambient/fp4 | fp4 | yes | 86.7 | 143 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1052.5 | 0.0045 |
| modal | unknown | no | 86.7 | 143 | 0 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 569.0 | 0.0231 |
| coreweave/fp8 | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 260.0 | 0.0277 |
| inceptron/fp4 | fp4 | yes | 86.0 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 928.5 | 0.0100 |
| primeintellect | unknown | no | 86.0 | 143 | 0.00 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 664.5 | 0.0071 |
| deepinfra/fp8/flex | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 79.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1573.0 | 0.0069 |
| dekallm | unknown | yes | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1042.5 | 0.0098 |
| fireworks/us | unknown | no | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 381.5 | 0.0413 |
| inference-net/us | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 79.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 390.5 | 0.0084 |
| morph/fast | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 472.0 | 0.0547 |
| morph/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 412.0 | 0.0043 |
| novita/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 943.0 | 0.0094 |
| particle-ai/us | unknown | yes | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 537.0 | 0.0050 |
| sail-research/fp4 | fp4 | yes | 85.3 | 143 | 0 | 1.00 | 81.2 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 952.5 | 0.0034 |
| sail-research/fp4/us | fp4 | yes | 85.3 | 143 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 952.5 | 0.0035 |
| cohere/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 375.5 | 0.0104 |
| fireworks/spot | unknown | no | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 674.5 | 0.0138 |
| particle-ai/us/flex | unknown | yes | 84.6 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 734.5 | 0.0031 |
| pearl-research/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 832.5 | 0.0050 |
| primalabs | unknown | yes | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 496.5 | 0.0221 |
| venice/fp8 | fp8 | no | 84.6 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 993.5 | 0.0280 |
| deepinfra/fp8/priority | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 70.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 566.0 | 0.0034 |
| siliconflow/fp8 | fp8 | no | 83.9 | 143 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 685.0 | 0.0137 |
| wafer/us | mxfp4 | yes | 83.9 | 143 | 0 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 307.0 | 0.0048 |
| crusoe/fp8 | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 553.5 | 0.0268 |
| digitalocean | unknown | no | 83.2 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 658.0 | 0.0141 |
| inference-net/fp8 | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 384.0 | 0.0071 |
| modelrun/fp4 | fp4 | no | 83.2 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 783.0 | 0.0157 |
| baseten | unknown | no | 82.5 | 143 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1216.5 | 0.0292 |
| reka | unknown | no | 82.5 | 143 | 0 | 1.00 | 72.9 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 407.5 | 0.0279 |
| alibaba | unknown | yes | 81.8 | 143 | 0.00 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 757.5 | 0.0083 |
| antdigital/fp8 | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 83.3 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1177.5 | 0.0094 |
| makora/fp8 | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 81.2 | 95.8 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 490.5 | 0.0148 |
| wafer/mxfp4 | mxfp4 | yes | 81.1 | 143 | 0 | 1.00 | 85.4 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 330.0 | 0.0033 |
| mistral/fp8 | fp8 | yes | 80.4 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 641.5 | 0.0278 |
| deepinfra/fp8 | fp8 | yes | 79.7 | 143 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 530.5 | 0.0087 |
| river | unknown | yes | 79.7 | 143 | 0 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 758.5 | 0.0110 |
| together | unknown | no | 79.7 | 143 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 403.0 | 0.0282 |
| ionstream | unknown | yes | 78.3 | 143 | 0 | 1.00 | 68.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 542.5 | 0.0181 |
| nebius/fp4 | fp4 | yes | 76.9 | 143 | 0 | 1.00 | 85.4 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 448.0 | 0.0173 |
| baidu/fp8 | fp8 | no | 74.8 | 143 | 0.00 | 1.00 | 83.3 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 645.5 | 0.0092 |
| streamlake/fp8 | fp8 | no | 74.1 | 143 | 0 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 981.5 | 0.0070 |
| near-ai | unknown | no | 72.0 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1050.0 | 0.0277 |
| open-inference/fp4 | fp4 | yes | 70.6 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 881.0 | 0.0070 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: particle-ai/us/flex, wafer/us, sail-research/fp4/us, sail-research/fp4, ambient/fp4, pearl-research/fp8, open-inference/fp4, primeintellect, morph/fp8, particle-ai/us, wafer/mxfp4, streamlake/fp8, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, alibaba, baidu/fp8, deepinfra/fp8, inceptron/fp4, dekallm, cloudflare, cohere/fp8, antdigital/fp8, river, relace/fp4, deepinfra/fp8/priority, fireworks/spot, digitalocean, siliconflow/fp8, deepseek, makora/fp8, novita/fp8, modelrun/fp4, nebius/fp4, ionstream, primalabs, modal, crusoe/fp8, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, reka, together, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 1.

## Footer

- Rows: 12528; errors 308; misrouted 0; truncated (finish_reason length) 23; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.5327; billed: $2.221; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
