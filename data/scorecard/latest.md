# Bitdepth scorecard 2026-11-18

Run `2026-11-18-live`, source `live`, started 2026-11-18T16:30:58Z, finished 2026-11-18T17:53:42Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 100.0 | 140 | n/a | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 265.5 | 0.0375 |
| crusoe/bf16 | bf16 | yes | 99.3 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 857.0 | 0.0064 |
| deepinfra/bf16 | bf16 | yes | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 9719.5 | 0.0046 |
| near-ai/fp4 | fp4 | yes | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1663.5 | 0.0037 |
| sambanova | unknown | no | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 388.5 | 0.0202 |
| siliconflow/fp8 | fp8 | no | 98.6 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2516.5 | 0.0241 |
| amazon-bedrock | unknown | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 802.0 | 0.0181 |
| baseten/fp4 | fp4 | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 619.0 | 0.0131 |
| baseten/fp4/us | fp4 | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 2 | 585.0 | 0.0129 |
| parasail/fast | fp4 | yes | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 499.0 | 0.0193 |
| together | unknown | no | 97.9 | 140 | 0 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 719.5 | 0.0182 |
| nebius/fp4 | fp4 | yes | 97.1 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 510.0 | 0.0177 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 778.0 | 0.0181 |
| groq | unknown | yes | 96.4 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 337.5 | 0.0182 |
| dekallm/bf16 | bf16 | yes | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1475.5 | 0.0041 |
| mancer/fp8 | fp8 | yes | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 781.5 | 0.0113 |
| parasail/fp4 | fp4 | yes | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 2 | 646.5 | 0.0152 |
| primeintellect/fp4 | fp4 | yes | 95.7 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 635.5 | 0.0307 |
| sail-research/fp4 | fp4 | yes | 94.3 | 140 | 0.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 640.0 | 0.0081 |
| akashml/fp4 | fp4 | yes | 93.6 | 140 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 652.5 | 0.0043 |
| coreweave/fp4 | fp4 | yes | 93.6 | 140 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 540.5 | 0.0040 |
| digitalocean | unknown | no | 93.6 | 140 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1400.0 | 0.0083 |
| google-vertex/global | unknown | yes | 92.1 | 140 | 0 | 1.00 | 93.8 | 95.8 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 508.5 | 0.0108 |
| venice/int4 | int4 | no | 77.1 | 140 | 0.00 | 1.00 | 66.7 | 100.0 | 83.3 | 100.0 | 79.2 | 0.00 | 0 | 18 | 1767.5 | 0.0052 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 4.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 84.6 | 136 | 1 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2051.0 | 0.1375 |
| alibaba/fp8/us-east-1 | fp8 | yes | 83.1 | 136 | 1 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1980.0 | 0.0727 |
| digitalocean | unknown | no | 81.6 | 136 | 4 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2562.0 | 0.0947 |
| streamlake/fp8 | fp8 | no | 80.1 | 136 | 5 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2413.0 | 0.0328 |
| venice | unknown | no | 80.1 | 136 | 8 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2041.0 | 0.0683 |
| deepinfra/fp8/priority | fp8 | yes | 78.7 | 136 | 8 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1807.5 | 0.0663 |
| atlas-cloud/fp4 | fp4 | yes | 74.3 | 136 | 4 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2772.5 | 0.1467 |
| deepinfra/fp8 | fp8 | yes | 74.3 | 136 | 4 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1886.5 | 0.0936 |
| relace/fp4 | fp4 | no | 72.1 | 136 | 8.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1232.5 | 0.0797 |
| deepinfra/fp8/flex | fp8 | yes | 71.3 | 136 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2625.0 | 0.0793 |
| siliconflow/fp8 | fp8 | no | 69.9 | 136 | 3 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2312.0 | 0.0804 |
| azure/us | unknown | no | 55.1 | 136 | 0 | 1.00 | 95.8 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1382.5 | 0.1735 |
| novita/fp8 | fp8 | yes | 45.6 | 136 | 1.00 | 1.00 | 95.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2104.0 | 0.1123 |
| baidu/fp8 | fp8 | no | 45.2 | 135 | 0.00 | 1.00 | 97.9 | 100.0 | 34.8 | 100.0 | 100.0 | 1.40 | 0 | 0 | 1701.0 | 0.0757 |
| gmicloud/fp8 | fp8 | yes | 44.9 | 136 | 1 | 1.00 | 97.9 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2450.0 | 0.0818 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, siliconflow/fp8, gmicloud/fp8, deepinfra/fp8/flex, digitalocean, novita/fp8, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, atlas-cloud/fp4, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 8.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fast | unknown | no | 89.4 | 66 | 0 | 1.00 | 65.2 | 100.0 | 60.0 | 100.0 | 100.0 | 53.5 | 0 | 0 | 401.0 | 0.0272 |
| ambient/fp4 | fp4 | yes | 88.1 | 143 | 0 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 458.5 | 0.0087 |
| fireworks | unknown | no | 88.1 | 143 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 755.0 | 0.0278 |
| wafer/us | mxfp4 | yes | 88.1 | 143 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 415.0 | 0.0047 |
| baseten | unknown | no | 87.4 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 781.5 | 0.0276 |
| inference-net/us | fp8 | yes | 87.4 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 384.0 | 0.0086 |
| morph/fast | fp8 | yes | 87.3 | 134 | 0 | 1.00 | 76.2 | 100.0 | 50.0 | 100.0 | 100.0 | 6.20 | 0 | 0 | 434.0 | 0.0535 |
| alibaba | unknown | yes | 86.7 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 886.5 | 0.0083 |
| coreweave/fp8 | fp8 | yes | 86.7 | 143 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 380.0 | 0.0280 |
| venice/fp8 | fp8 | no | 86.7 | 143 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1015.5 | 0.0279 |
| digitalocean | unknown | no | 86.0 | 143 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 797.5 | 0.0167 |
| primalabs | unknown | yes | 86.0 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 590.5 | 0.0222 |
| sail-research/fp4/us | fp4 | yes | 86.0 | 143 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1685.5 | 0.0033 |
| cohere/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 534.5 | 0.0136 |
| deepinfra/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 91.7 | 0.00 | 0 | 0 | 684.5 | 0.0085 |
| deepinfra/fp8/priority | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 726.5 | 0.0034 |
| modelrun/fp4 | fp4 | no | 85.3 | 143 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 819.0 | 0.0156 |
| particle-ai/us/flex | unknown | yes | 85.3 | 143 | 0 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 656.5 | 0.0043 |
| siliconflow/fp8 | fp8 | no | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 817.5 | 0.0138 |
| crusoe/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 631.5 | 0.0266 |
| fireworks/us | unknown | no | 84.6 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 658.5 | 0.0414 |
| inceptron/fp4 | fp4 | yes | 84.6 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 545.5 | 0.0280 |
| novita/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1222.0 | 0.0028 |
| streamlake/fp8 | fp8 | no | 84.6 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1486.5 | 0.0098 |
| makora/fp8 | fp8 | yes | 84.4 | 141 | 0.00 | 1.00 | 77.1 | 100.0 | 56.5 | 100.0 | 100.0 | 1.40 | 0 | 0 | 687.0 | 0.0105 |
| modal | unknown | no | 84.3 | 140 | 0.00 | 1.00 | 78.7 | 100.0 | 52.2 | 100.0 | 100.0 | 2.10 | 0 | 0 | 819.0 | 0.0229 |
| antdigital/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1475.0 | 0.0036 |
| morph/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 671.0 | 0.0064 |
| particle-ai/us | unknown | yes | 83.9 | 143 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 644.0 | 0.0052 |
| primeintellect | unknown | no | 83.9 | 143 | 0 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 657.5 | 0.0061 |
| cloudflare | unknown | yes | 83.8 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1512.0 | 0.0074 |
| inference-net/fp8 | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 417.5 | 0.0064 |
| relace/fp4 | fp4 | no | 83.2 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 828.5 | 0.0110 |
| sail-research/fp4 | fp4 | yes | 83.2 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1710.5 | 0.0022 |
| wafer/mxfp4 | mxfp4 | yes | 83.2 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 418.5 | 0.0038 |
| gmicloud/fp8 | fp8 | yes | 82.5 | 143 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 923.5 | 0.0168 |
| stepfun/fp8 | fp8 | no | 82.5 | 143 | 0 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 768.0 | 0.0099 |
| deepinfra/fp8/flex | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2223.5 | 0.0069 |
| mistral/fp8 | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 62.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 763.5 | 0.0225 |
| together | unknown | no | 81.8 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 83.3 | 100.0 | 0.00 | 0 | 0 | 380.0 | 0.0276 |
| atlas-cloud/fp8 | fp8 | yes | 81.1 | 143 | 0 | 1.00 | 77.1 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1212.0 | 0.0047 |
| dekallm | unknown | yes | 81.1 | 143 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1511.0 | 0.0165 |
| parasail/fp8 | fp8 | yes | 81.1 | 143 | 0 | 1.00 | 72.9 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 426.5 | 0.0276 |
| river | unknown | yes | 81.1 | 143 | 0 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 969.5 | 0.0110 |
| nebius/fp4 | fp4 | yes | 79.7 | 143 | 0 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 542.0 | 0.0169 |
| ionstream | unknown | yes | 79.0 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 580.0 | 0.0186 |
| near-ai | unknown | no | 76.2 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 66.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1492.5 | 0.0281 |
| baidu/fp8 | fp8 | no | 74.1 | 143 | 0 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1089.0 | 0.0139 |
| open-inference/fp4 | fp4 | yes | 74.1 | 143 | 0 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 779.5 | 0.0119 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| fireworks/spot | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: wafer/us, sail-research/fp4/us, sail-research/fp4, particle-ai/us/flex, primeintellect, morph/fp8, deepinfra/fp8/flex, particle-ai/us, inference-net/us, inference-net/fp8, alibaba, open-inference/fp4, ambient/fp4, deepinfra/fp8, cloudflare, stepfun/fp8, wafer/mxfp4, streamlake/fp8, makora/fp8, antdigital/fp8, river, novita/fp8, relace/fp4, deepinfra/fp8/priority, baidu/fp8, cohere/fp8, siliconflow/fp8, deepseek, modelrun/fp4, dekallm, nebius/fp4, digitalocean, gmicloud/fp8, atlas-cloud/fp8, ionstream, fireworks/spot, mistral/fp8, primalabs, modal, crusoe/fp8, inceptron/fp4, coreweave/fp8, near-ai, venice/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 1.

## Footer

- Rows: 12960; errors 382; misrouted 0; truncated (finish_reason length) 33; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $5.0434; billed: $2.4799; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
