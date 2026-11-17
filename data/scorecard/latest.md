# Bitdepth scorecard 2026-11-17

Run `2026-11-17-live`, source `live`, started 2026-11-17T16:55:55Z, finished 2026-11-17T18:10:53Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 99.3 | 143 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 256.0 | 0.0373 |
| baseten/fp4/us | fp4 | no | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 510.5 | 0.0128 |
| primeintellect/fp4 | fp4 | yes | 98.6 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 727.5 | 0.0120 |
| baseten/fp4 | fp4 | no | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 504.5 | 0.0130 |
| dekallm/bf16 | bf16 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 2136.5 | 0.0042 |
| groq | unknown | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 296.0 | 0.0181 |
| nebius/fp4 | fp4 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 433.5 | 0.0178 |
| parasail/fast | fp4 | yes | 97.9 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 2 | 514.5 | 0.0196 |
| amazon-bedrock | unknown | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 639.0 | 0.0184 |
| sail-research/fp4 | fp4 | yes | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 898.0 | 0.0085 |
| together | unknown | no | 97.2 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 724.0 | 0.0180 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 628.0 | 0.0183 |
| coreweave/fp4 | fp4 | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 565.0 | 0.0042 |
| crusoe/bf16 | bf16 | yes | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 575.5 | 0.0065 |
| siliconflow/fp8 | fp8 | no | 96.5 | 143 | 0 | 1.00 | 100.0 | 100.0 | 95.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2048.5 | 0.0256 |
| akashml/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 848.5 | 0.0043 |
| digitalocean | unknown | no | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1343.0 | 0.0085 |
| mancer/fp8 | fp8 | yes | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 968.0 | 0.0103 |
| near-ai/fp4 | fp4 | yes | 95.1 | 143 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1012.5 | 0.0037 |
| parasail/fp4 | fp4 | yes | 93.7 | 143 | 0 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 571.5 | 0.0147 |
| sambanova | unknown | no | 93.7 | 143 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 770.5 | 0.0199 |
| google-vertex/global | unknown | yes | 93.0 | 143 | 0.00 | 1.00 | 91.7 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 1 | 440.0 | 0.0111 |
| venice/int4 | int4 | no | 81.8 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 79.2 | 100.0 | 91.7 | 0.00 | 0 | 13 | 1694.5 | 0.0047 |
| deepinfra/bf16 | bf16 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 1.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 85.5 | 131 | 5 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2754.0 | 0.1281 |
| digitalocean | unknown | no | 81.7 | 131 | 4.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1564.0 | 0.0946 |
| relace/fp4 | fp4 | no | 81.7 | 131 | 3.50 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1185.5 | 0.0797 |
| streamlake/fp8 | fp8 | no | 80.9 | 131 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 91.7 | 0.00 | 0 | 0 | 2471.0 | 0.0325 |
| venice | unknown | no | 80.9 | 131 | 5 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1837.0 | 0.0717 |
| alibaba/fp8/us-east-1 | fp8 | yes | 80.2 | 131 | 4.00 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2649.5 | 0.1412 |
| atlas-cloud/fp4 | fp4 | yes | 80.2 | 131 | 1.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2504.5 | 0.1393 |
| deepinfra/fp8/flex | fp8 | yes | 77.9 | 131 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1938.5 | 0.0699 |
| deepinfra/fp8 | fp8 | yes | 77.1 | 131 | 4.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1503.0 | 0.0834 |
| deepinfra/fp8/priority | fp8 | yes | 75.6 | 131 | 3.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1432.0 | 0.0716 |
| siliconflow/fp8 | fp8 | no | 67.9 | 131 | 1.00 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2149.0 | 0.0867 |
| azure/us | unknown | no | 60.3 | 131 | 0.00 | 1.00 | 100.0 | 100.0 | 41.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1262.5 | 0.1747 |
| baidu/fp8 | fp8 | no | 48.5 | 130 | 0 | 1.00 | 95.8 | 100.0 | 37.5 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1792.0 | 0.0726 |
| gmicloud/fp8 | fp8 | yes | 48.1 | 131 | 0.00 | 1.00 | 100.0 | 100.0 | 37.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2438.0 | 0.0859 |
| novita/fp8 | fp8 | yes | 48.1 | 131 | 0.00 | 1.00 | 97.9 | 100.0 | 33.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2098.5 | 0.1065 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, deepinfra/fp8/flex, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 13.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ambient/fp4 | fp4 | yes | 94.0 | 100 | 0.00 | 1.00 | 70.0 | 100.0 | 45.0 | 100.0 | 100.0 | 30.6 | 0 | 0 | 726.0 | 0.0070 |
| baseten/fast | unknown | no | 89.4 | 132 | 0.00 | 1.00 | 73.8 | 100.0 | 45.5 | 100.0 | 100.0 | 7.60 | 0 | 0 | 277.0 | 0.0505 |
| alibaba | unknown | yes | 88.8 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 996.5 | 0.0082 |
| fireworks | unknown | no | 88.8 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 839.0 | 0.0218 |
| inference-net/fp8 | fp8 | yes | 88.8 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 389.0 | 0.0069 |
| modal | unknown | no | 88.8 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 675.0 | 0.0229 |
| primeintellect | unknown | no | 88.1 | 143 | 0 | 1.00 | 79.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 599.5 | 0.0060 |
| cloudflare | unknown | yes | 87.4 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1252.5 | 0.0098 |
| cohere/fp8 | fp8 | yes | 87.4 | 143 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 391.5 | 0.0135 |
| digitalocean | unknown | no | 87.4 | 143 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 425.5 | 0.0165 |
| modelrun/fp4 | fp4 | no | 87.4 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 705.0 | 0.0156 |
| particle-ai/us/flex | unknown | yes | 87.4 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 676.0 | 0.0043 |
| sail-research/fp4/us | fp4 | yes | 87.4 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1142.0 | 0.0032 |
| baseten | unknown | no | 86.7 | 143 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 711.0 | 0.0277 |
| relace/fp4 | fp4 | no | 86.7 | 143 | 0 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 619.5 | 0.0110 |
| coreweave/fp8 | fp8 | yes | 86.0 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 41.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 434.5 | 0.0278 |
| dekallm | unknown | yes | 86.0 | 143 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1060.0 | 0.0164 |
| venice/fp8 | fp8 | no | 86.0 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 829.0 | 0.0276 |
| morph/fast | fp8 | yes | 85.4 | 137 | 0.00 | 1.00 | 78.3 | 100.0 | 50.0 | 100.0 | 100.0 | 4.20 | 0 | 0 | 397.0 | 0.0530 |
| fireworks/spot | unknown | no | 85.3 | 143 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1973.0 | 0.0195 |
| inference-net/us | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 397.5 | 0.0082 |
| novita/fp8 | fp8 | yes | 85.3 | 143 | 0 | 1.00 | 81.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1245.5 | 0.0041 |
| particle-ai/us | unknown | yes | 85.3 | 143 | 0 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 674.5 | 0.0060 |
| siliconflow/fp8 | fp8 | no | 85.3 | 143 | 0 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1306.0 | 0.0250 |
| nebius/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 66.7 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 399.5 | 0.0275 |
| parasail/fp8 | fp8 | yes | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 421.5 | 0.0275 |
| sail-research/fp4 | fp4 | yes | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1180.0 | 0.0030 |
| streamlake/fp8 | fp8 | no | 84.6 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1503.0 | 0.0095 |
| wafer/mxfp4 | mxfp4 | yes | 84.6 | 143 | 0.00 | 1.00 | 79.2 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 386.5 | 0.0029 |
| crusoe/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 68.8 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 545.0 | 0.0268 |
| gmicloud/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 64.6 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 931.5 | 0.0166 |
| mistral/fp8 | fp8 | yes | 83.9 | 143 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 613.5 | 0.0221 |
| wafer/us | mxfp4 | yes | 83.9 | 143 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 380.0 | 0.0046 |
| atlas-cloud/fp8 | fp8 | yes | 83.2 | 143 | 0.00 | 1.00 | 77.1 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1239.5 | 0.0046 |
| primalabs | unknown | yes | 83.2 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 574.5 | 0.0222 |
| stepfun/fp8 | fp8 | no | 83.2 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 574.5 | 0.0098 |
| deepinfra/fp8 | fp8 | yes | 82.5 | 143 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 710.0 | 0.0050 |
| makora/fp8 | fp8 | yes | 82.5 | 143 | 0 | 1.00 | 75.0 | 91.7 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 943.5 | 0.0110 |
| fireworks/us | unknown | no | 81.8 | 143 | 0.00 | 1.00 | 75.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 467.0 | 0.0413 |
| morph/fp8 | fp8 | yes | 81.8 | 143 | 0.00 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 559.5 | 0.0059 |
| deepinfra/fp8/flex | fp8 | yes | 81.1 | 143 | 0 | 1.00 | 70.8 | 95.8 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1907.5 | 0.0052 |
| deepinfra/fp8/priority | fp8 | yes | 81.1 | 143 | 0 | 1.00 | 72.9 | 95.8 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 721.0 | 0.0036 |
| together | unknown | no | 81.1 | 143 | 0 | 1.00 | 75.0 | 100.0 | 45.8 | 87.5 | 100.0 | 0.00 | 0 | 0 | 425.5 | 0.0277 |
| river | unknown | yes | 79.7 | 143 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 738.5 | 0.0111 |
| ionstream | unknown | yes | 78.3 | 143 | 0 | 1.00 | 64.6 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 1 | 357.0 | 0.0188 |
| ionstream/flex | unknown | yes | 76.2 | 143 | 0.00 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 498.5 | 0.0070 |
| near-ai | unknown | no | 75.5 | 143 | 0 | 1.00 | 64.6 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1495.5 | 0.0276 |
| baidu/fp8 | fp8 | no | 74.6 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.70 | 0 | 0 | 1453.0 | 0.0122 |
| open-inference/fp4 | fp4 | yes | 72.7 | 143 | 0 | 1.00 | 52.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 751.0 | 0.0115 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: wafer/us, sail-research/fp4/us, sail-research/fp4, particle-ai/us/flex, primeintellect, morph/fp8, wafer/mxfp4, ionstream/flex, deepinfra/fp8/flex, particle-ai/us, inference-net/us, inference-net/fp8, alibaba, open-inference/fp4, ambient/fp4, deepinfra/fp8, cloudflare, stepfun/fp8, streamlake/fp8, makora/fp8, river, novita/fp8, relace/fp4, deepinfra/fp8/priority, baidu/fp8, cohere/fp8, deepseek, modelrun/fp4, dekallm, digitalocean, gmicloud/fp8, atlas-cloud/fp8, ionstream, fireworks/spot, mistral/fp8, primalabs, modal, crusoe/fp8, siliconflow/fp8, nebius/fp8, coreweave/fp8, near-ai, venice/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 1.

## Footer

- Rows: 12816; errors 351; misrouted 0; truncated (finish_reason length) 37; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $5.0192; billed: $2.5274; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
