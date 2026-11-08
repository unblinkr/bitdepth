# Bitdepth scorecard 2026-11-08

Run `2026-11-08-live`, source `live`, started 2026-11-08T14:20:48Z, finished 2026-11-08T19:27:21Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cerebras/fp16 | fp16 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 238.5 | 0.0368 |
| deepinfra/bf16 | bf16 | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 2589.0 | 0.0047 |
| groq | unknown | yes | 98.6 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 274.5 | 0.0179 |
| baseten/fp4 | fp4 | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 391.0 | 0.0127 |
| coreweave/fp4 | fp4 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 596.5 | 0.0041 |
| sail-research/fp4 | fp4 | yes | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1009.0 | 0.0084 |
| together | unknown | no | 97.9 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 2 | 600.0 | 0.0182 |
| amazon-bedrock | unknown | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 538.5 | 0.0186 |
| baseten/fp4/us | fp4 | no | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 407.5 | 0.0129 |
| crusoe/bf16 | bf16 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 399.5 | 0.0066 |
| dekallm/bf16 | bf16 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 946.5 | 0.0042 |
| parasail/fp4 | fp4 | yes | 97.2 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 578.0 | 0.0153 |
| amazon-bedrock/eu-west-1 | unknown | no | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 524.5 | 0.0180 |
| near-ai/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 684.0 | 0.0038 |
| nebius/fp4 | fp4 | yes | 96.5 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 396.5 | 0.0176 |
| primeintellect/fp4 | fp4 | yes | 96.5 | 141 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 0 | 909.0 | 0.0024 |
| akashml/fp4 | fp4 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 759.5 | 0.0043 |
| mancer/fp8 | fp8 | yes | 95.8 | 142 | 0.00 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 770.0 | 0.0068 |
| google-vertex/global | unknown | yes | 95.7 | 139 | 0.00 | 1.00 | 100.0 | 100.0 | 78.3 | 100.0 | 100.0 | 2.10 | 0 | 0 | 4096.0 | 0.0107 |
| parasail/fast | fp4 | yes | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 512.5 | 0.0199 |
| sambanova | unknown | no | 95.1 | 142 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 1 | 532.5 | 0.0203 |
| deepinfra/fp8 | fp8 | yes | 95.0 | 139 | 0 | 1.00 | 100.0 | 100.0 | 87.0 | 100.0 | 100.0 | 2.10 | 0 | 1 | 1525.0 | 0.0251 |
| digitalocean | unknown | no | 92.3 | 142 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1060.0 | 0.0085 |
| phala | unknown | yes | 92.3 | 142 | 0 | 1.00 | 100.0 | 95.8 | 79.2 | 100.0 | 95.8 | 0.00 | 0 | 5 | 1335.0 | 0.0246 |
| siliconflow/fp8 | fp8 | no | 91.5 | 142 | 0.00 | 1.00 | 97.9 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2106.5 | 0.0277 |
| venice/int4 | int4 | no | 78.9 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 75.0 | 100.0 | 79.2 | 0.00 | 0 | 18 | 1876.0 | 0.0051 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: dekallm/bf16, deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 2.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 89.6 | 134 | 7.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2108.5 | 0.1262 |
| alibaba/fp8 | fp8 | yes | 88.1 | 134 | 5.50 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2440.0 | 0.1309 |
| deepinfra/fp8 | fp8 | yes | 81.1 | 132 | 3 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.7 | 1.40 | 0 | 0 | 1358.0 | 0.1154 |
| baidu/fp8 | fp8 | no | 77.6 | 134 | 6.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1615.0 | 0.0191 |
| atlas-cloud/fp4 | fp4 | yes | 76.1 | 134 | 4.00 | 1.00 | 100.0 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2689.5 | 0.1500 |
| venice | unknown | no | 76.1 | 134 | 6.50 | 1.00 | 100.0 | 100.0 | 50.0 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1643.5 | 0.0733 |
| relace/fp4 | fp4 | no | 75.4 | 134 | 5 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 727.5 | 0.0801 |
| nebius/fp8 | fp8 | yes | 74.6 | 134 | 5.50 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1177.0 | 0.1602 |
| streamlake/fp8 | fp8 | no | 73.1 | 134 | 8.00 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3091.5 | 0.0080 |
| siliconflow/fp8 | fp8 | no | 67.9 | 134 | 3 | 1.00 | 100.0 | 100.0 | 54.2 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1929.0 | 0.0872 |
| digitalocean | unknown | no | 56.0 | 134 | 0 | 1.00 | 97.9 | 100.0 | 41.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 4097.0 | 0.0951 |
| azure/us | unknown | no | 53.0 | 134 | 0 | 1.00 | 97.9 | 100.0 | 41.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1055.0 | 0.1753 |
| novita/fp8 | fp8 | yes | 44.0 | 134 | 1 | 1.00 | 100.0 | 100.0 | 25.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2126.0 | 0.0909 |
| gmicloud/fp8 | fp8 | yes | 41.0 | 134 | 1 | 1.00 | 97.9 | 100.0 | 16.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2355.5 | 0.0860 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, streamlake/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, nebius/fp8, azure/us. Prompts with no plurality (excluded from exact match): 10.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fireworks/ultrafast | unknown | no | 89.4 | 142 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 403.0 | 0.2202 |
| cohere/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 342.5 | 0.0176 |
| decart/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 68.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1010.5 | 0.0113 |
| inference-net/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 514.5 | 0.0035 |
| makora/fp8 | fp8 | yes | 88.0 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 318.0 | 0.0161 |
| primeintellect | unknown | no | 88.0 | 142 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 513.0 | 0.0111 |
| mistral/fp8 | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 41.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 980.0 | 0.0277 |
| modal | unknown | no | 87.3 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 632.0 | 0.0230 |
| nebius/fp8 | fp8 | yes | 87.3 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1196.5 | 0.0277 |
| particle-ai/us/flex | unknown | yes | 87.3 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 564.5 | 0.0028 |
| fireworks/spot | unknown | no | 86.6 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2112.5 | 0.0194 |
| particle-ai/us | unknown | yes | 86.6 | 142 | 0 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 568.0 | 0.0033 |
| relace/fast | fp4 | no | 86.6 | 142 | 0 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 348.0 | 0.0263 |
| relace/fp4 | fp4 | no | 86.6 | 142 | 0 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 644.5 | 0.0022 |
| wafer/mxfp4 | mxfp4 | yes | 86.6 | 142 | 0 | 1.00 | 64.6 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 372.0 | 0.0027 |
| atlas-cloud/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 77.1 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1276.5 | 0.0044 |
| inference-net/us | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 478.0 | 0.0083 |
| morph/fp8 | fp8 | yes | 85.9 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 775.5 | 0.0031 |
| primalabs | unknown | yes | 85.9 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 623.0 | 0.0220 |
| alibaba | unknown | yes | 85.2 | 142 | 0 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1019.5 | 0.0070 |
| dekallm | unknown | yes | 85.2 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 902.5 | 0.0166 |
| fireworks | unknown | no | 85.2 | 142 | 0 | 1.00 | 75.0 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2159.5 | 0.0081 |
| cloudflare | unknown | yes | 84.8 | 138 | 0 | 1.00 | 69.6 | 100.0 | 54.2 | 100.0 | 100.0 | 2.80 | 0 | 0 | 1220.5 | 0.0053 |
| baseten | unknown | no | 84.5 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 363.0 | 0.0275 |
| modelrun/fp4 | fp4 | no | 84.5 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 714.0 | 0.0156 |
| venice/fp8 | fp8 | no | 84.5 | 142 | 0.00 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1039.0 | 0.0282 |
| baseten/fast | unknown | no | 84.1 | 107 | 0 | 1.00 | 62.9 | 100.0 | 38.9 | 100.0 | 100.0 | 25.0 | 0 | 0 | 249.0 | 0.0391 |
| coreweave/fp8 | fp8 | yes | 83.8 | 142 | 0 | 1.00 | 70.8 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 350.5 | 0.0278 |
| deepinfra/fp8 | fp8 | yes | 83.8 | 142 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 410.5 | 0.0023 |
| parasail/fp8 | fp8 | yes | 83.8 | 142 | 0 | 1.00 | 60.4 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 379.0 | 0.0275 |
| phala | unknown | yes | 83.8 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1469.5 | 0.0064 |
| siliconflow/fp8 | fp8 | no | 83.8 | 142 | 0 | 1.00 | 70.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 792.0 | 0.0251 |
| deepinfra/fp8/priority | fp8 | yes | 83.1 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 446.0 | 0.0034 |
| fireworks/us | unknown | no | 83.1 | 142 | 0.00 | 1.00 | 68.8 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 423.0 | 0.0304 |
| gmicloud/fp8 | fp8 | yes | 83.1 | 142 | 0.00 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 880.5 | 0.0167 |
| novita/fp8 | fp8 | yes | 83.1 | 142 | 0.00 | 1.00 | 75.0 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1251.0 | 0.0153 |
| stepfun/fp8 | fp8 | no | 83.1 | 142 | 0.00 | 1.00 | 64.6 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 522.5 | 0.0124 |
| deepinfra/fp8/flex | fp8 | yes | 82.4 | 142 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1702.5 | 0.0069 |
| together | unknown | no | 82.4 | 142 | 0 | 1.00 | 72.9 | 100.0 | 54.2 | 87.5 | 100.0 | 0.00 | 0 | 0 | 238.0 | 0.0279 |
| crusoe/fp8 | fp8 | yes | 81.0 | 142 | 0 | 1.00 | 70.8 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 530.0 | 0.0268 |
| wafer/us | mxfp4 | yes | 81.0 | 142 | 0 | 1.00 | 79.2 | 100.0 | 50.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 339.5 | 0.0050 |
| ionstream | unknown | yes | 80.3 | 142 | 0.00 | 1.00 | 60.4 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 536.5 | 0.0146 |
| reka | unknown | no | 77.5 | 142 | 0.00 | 1.00 | 83.3 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 648.5 | 0.0171 |
| streamlake/fp8 | fp8 | no | 76.8 | 142 | 0 | 1.00 | 83.3 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1100.0 | 0.0064 |
| digitalocean | unknown | no | 75.4 | 142 | 0 | 1.00 | 60.4 | 100.0 | 58.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 378.5 | 0.0165 |
| open-inference/fp4 | fp4 | yes | 74.6 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 54.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1762.5 | 0.0042 |
| baidu/fp8 | fp8 | no | 73.8 | 141 | 0 | 1.00 | 81.2 | 100.0 | 45.8 | 100.0 | 100.0 | 0.70 | 0 | 0 | 784.0 | 0.0093 |
| near-ai | unknown | no | 73.2 | 142 | 0.00 | 1.00 | 72.9 | 100.0 | 45.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 771.5 | 0.0280 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, open-inference/fp4, morph/fp8, particle-ai/us/flex, wafer/us, particle-ai/us, wafer/mxfp4, alibaba, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, primeintellect, baidu/fp8, deepinfra/fp8, cloudflare, sail-research/fp4/us, streamlake/fp8, decart/fp8, stepfun/fp8, deepinfra/fp8/priority, deepseek, makora/fp8, sail-research/fp4, reka, ionstream, novita/fp8, modelrun/fp4, dekallm, digitalocean, gmicloud/fp8, cohere/fp8, atlas-cloud/fp8, phala, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, relace/fast, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast, fireworks/ultrafast. Prompts with no plurality (excluded from exact match): 2.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | 100.0 | 131 | n/a | 1.00 | 100.0 | 54.2 | 79.2 | 100.0 | 83.3 | 0.00 | 0 | 17 | 2660.0 | 0.1035 |
| mistral/zdr | unknown | yes | 100.0 | 131 | n/a | 1.00 | 100.0 | 50.0 | 70.8 | 100.0 | 87.5 | 0.00 | 0 | 18 | 2508.0 | 0.1264 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 13.

## Footer

- Rows: 13392; errors 482; misrouted 0; truncated (finish_reason length) 69; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $5.4312; billed: $2.913; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
