# Bitdepth scorecard 2026-11-27

Run `2026-11-27-live`, source `live`, started 2026-11-27T17:31:15Z, finished 2026-11-27T20:44:35Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| parasail/fast | fp4 | yes | 100.0 | 144 | n/a | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 526.0 | 0.0194 |
| cerebras/fp16 | fp16 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 0.00 | 0 | 0 | 301.5 | 0.0363 |
| crusoe/bf16 | bf16 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 1 | 598.5 | 0.0064 |
| deepinfra/bf16 | bf16 | yes | 99.3 | 144 | 0 | 1.00 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 0.00 | 0 | 0 | 3572.5 | 0.0045 |
| baseten/fp4 | fp4 | no | 98.6 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 87.5 | 100.0 | 100.0 | 0.00 | 0 | 0 | 482.5 | 0.0125 |
| akashml/fp4 | fp4 | yes | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1492.5 | 0.0042 |
| amazon-bedrock | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 537.5 | 0.0180 |
| amazon-bedrock/eu-west-1 | unknown | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 543.5 | 0.0177 |
| baseten/fp4/us | fp4 | no | 97.9 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 467.0 | 0.0127 |
| digitalocean | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 0 | 1312.5 | 0.0080 |
| groq | unknown | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 306.0 | 0.0180 |
| nebius/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 445.5 | 0.0175 |
| parasail/fp4 | fp4 | yes | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 0 | 591.5 | 0.0148 |
| sambanova | unknown | no | 97.2 | 144 | 0.00 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 494.5 | 0.0205 |
| coreweave/fp4 | fp4 | yes | 95.8 | 143 | 0.00 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.70 | 0 | 1 | 1368.0 | 0.0040 |
| near-ai/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 0.00 | 0 | 1 | 1462.5 | 0.0039 |
| primeintellect/fp4 | fp4 | yes | 95.1 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 683.0 | 0.0350 |
| google-vertex/global | unknown | yes | 94.4 | 144 | 0.00 | 1.00 | 93.8 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 450.5 | 0.0106 |
| mancer/fp8 | fp8 | yes | 92.4 | 144 | 0 | 1.00 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 0.00 | 0 | 1 | 857.0 | 0.0106 |
| venice/int4 | int4 | no | 79.2 | 144 | 0.00 | 1.00 | 75.0 | 100.0 | 75.0 | 100.0 | 83.3 | 0.00 | 0 | 18 | 1713.0 | 0.0052 |
| siliconflow/fp8 | fp8 | no | 65.3 | 144 | 0.50 | 1.00 | 85.4 | 8.30 | 54.2 | 100.0 | 66.7 | 0.00 | 0 | 0 | 1411.5 | 0.0215 |
| fireworks | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: deepinfra/bf16, crusoe/bf16, cerebras/fp16. Prompts with no plurality (excluded from exact match): 0.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8 | fp8 | yes | 84.6 | 136 | 4 | 1.00 | 100.0 | 100.0 | 62.5 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2058.0 | 0.1281 |
| alibaba/fp8/us-east-1 | fp8 | yes | 82.4 | 136 | 6.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1982.0 | 0.1211 |
| relace/fp4 | fp4 | no | 82.4 | 136 | 7.50 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 647.0 | 0.0646 |
| streamlake/fp8 | fp8 | no | 81.6 | 136 | 4 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 2629.5 | 0.0268 |
| baidu/fp8 | fp8 | no | 78.7 | 136 | 5 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1526.5 | 0.0643 |
| venice | unknown | no | 76.9 | 134 | 5 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.7 | 1.40 | 0 | 0 | 6959.0 | 0.0673 |
| deepinfra/fp8 | fp8 | yes | 75.7 | 136 | 4 | 1.00 | 97.9 | 100.0 | 70.8 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1931.5 | 0.1623 |
| deepinfra/fp8/priority | fp8 | yes | 75.7 | 136 | 4 | 1.00 | 97.9 | 100.0 | 66.7 | 100.0 | 91.7 | 0.00 | 0 | 0 | 1888.5 | 0.0660 |
| siliconflow/fp8 | fp8 | no | 67.6 | 136 | 3.00 | 1.00 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | 0.00 | 0 | 0 | 2099.5 | 0.0803 |
| deepinfra/fp8/flex | fp8 | yes | 67.3 | 49 | 5.00 | 1.00 | 96.6 | 100.0 | 100.0 | 100.0 | 100.0 | 64.6 | 0 | 0 | 2326.0 | 0.0168 |
| azure/us | unknown | no | 61.0 | 136 | 1 | 1.00 | 97.9 | 100.0 | 66.7 | 100.0 | 95.8 | 0.00 | 0 | 0 | 1068.5 | 0.1735 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: baidu/fp8, relace/fp4, streamlake/fp8, siliconflow/fp8, deepinfra/fp8/flex, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, venice, azure/us, deepinfra/fp8/priority. Prompts with no plurality (excluded from exact match): 8.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| morph/fast | fp8 | yes | 93.8 | 65 | 0.00 | 1.00 | 69.2 | 100.0 | 50.0 | 100.0 | 100.0 | 54.9 | 0 | 0 | 529.0 | 0.0274 |
| primeintellect | unknown | no | 92.9 | 70 | 0 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 51.4 | 0 | 0 | 656.0 | 0.0099 |
| modal | unknown | no | 92.6 | 68 | 0 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 52.8 | 0 | 0 | 683.5 | 0.0121 |
| baseten/fast | unknown | no | 92.3 | 65 | 0 | 1.00 | 69.2 | 100.0 | 50.0 | 100.0 | 100.0 | 54.9 | 0 | 0 | 372.0 | 0.0270 |
| ambient/fp4 | fp4 | yes | 92.0 | 75 | 0.00 | 1.00 | 81.2 | 100.0 | 46.7 | 100.0 | 100.0 | 47.2 | 0 | 0 | 658.0 | 0.0026 |
| pearl-research/fp8 | fp8 | yes | 91.7 | 72 | 0.00 | 1.00 | 73.3 | 100.0 | 42.9 | 100.0 | 100.0 | 50.0 | 0 | 0 | 980.5 | 0.0028 |
| fireworks/flex | unknown | no | 91.4 | 70 | 0.00 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 51.4 | 0 | 0 | 461.0 | 0.0079 |
| crusoe/fp8 | fp8 | yes | 91.3 | 69 | 0.00 | 1.00 | 71.4 | 100.0 | 50.0 | 100.0 | 100.0 | 52.1 | 0 | 0 | 917.0 | 0.0097 |
| makora/fp8 | fp8 | yes | 91.3 | 69 | 0.00 | 1.00 | 64.3 | 100.0 | 50.0 | 100.0 | 100.0 | 52.1 | 0 | 0 | 501.0 | 0.0080 |
| parasail/fp8 | fp8 | yes | 91.2 | 68 | 0.00 | 1.00 | 64.3 | 100.0 | 57.1 | 100.0 | 100.0 | 52.8 | 0 | 0 | 373.5 | 0.0136 |
| venice/fp8 | fp8 | no | 91.2 | 68 | 0.00 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 52.8 | 0 | 0 | 1178.0 | 0.0148 |
| cloudflare | unknown | yes | 90.3 | 72 | 0 | 1.00 | 73.3 | 100.0 | 57.1 | 100.0 | 100.0 | 50.0 | 0 | 0 | 1150.5 | 0.0021 |
| deepinfra/fp8 | fp8 | yes | 90.3 | 72 | 0 | 1.00 | 66.7 | 100.0 | 57.1 | 100.0 | 100.0 | 50.0 | 0 | 0 | 860.0 | 0.0049 |
| tenstorrent/fp8 | fp8 | yes | 90.3 | 72 | 0 | 1.00 | 60.0 | 100.0 | 50.0 | 100.0 | 100.0 | 50.0 | 0 | 0 | 781.0 | 0.0030 |
| fireworks | unknown | no | 89.9 | 69 | 0 | 1.00 | 71.4 | 100.0 | 57.1 | 100.0 | 100.0 | 52.1 | 0 | 0 | 833.0 | 0.0154 |
| baseten | unknown | no | 89.7 | 68 | 0 | 1.00 | 64.3 | 100.0 | 50.0 | 100.0 | 100.0 | 52.8 | 0 | 0 | 528.0 | 0.0146 |
| digitalocean | unknown | no | 89.7 | 68 | 0 | 1.00 | 78.6 | 100.0 | 57.1 | 100.0 | 100.0 | 52.8 | 0 | 0 | 703.0 | 0.0095 |
| featherless/fp8 | fp8 | yes | 89.7 | 68 | 0 | 1.00 | 71.4 | 100.0 | 57.1 | 100.0 | 100.0 | 52.8 | 0 | 0 | 1262.5 | 0.0109 |
| mistral/fp8 | fp8 | yes | 89.7 | 68 | 0 | 1.00 | 64.3 | 100.0 | 50.0 | 100.0 | 100.0 | 52.8 | 0 | 0 | 1008.5 | 0.0145 |
| modelrun/fp4 | fp4 | no | 88.7 | 71 | 0.00 | 1.00 | 73.3 | 100.0 | 57.1 | 100.0 | 100.0 | 50.7 | 0 | 0 | 870.0 | 0.0055 |
| wafer/mxfp4 | mxfp4 | yes | 88.7 | 71 | 0.00 | 1.00 | 60.0 | 100.0 | 50.0 | 100.0 | 100.0 | 50.7 | 0 | 0 | 413.0 | 0.0015 |
| inference-net/us | fp8 | yes | 88.6 | 70 | 0.00 | 1.00 | 71.4 | 100.0 | 50.0 | 100.0 | 100.0 | 51.4 | 0 | 0 | 495.5 | 0.0047 |
| particle-ai/us | unknown | yes | 88.6 | 70 | 0.00 | 1.00 | 64.3 | 100.0 | 57.1 | 100.0 | 100.0 | 51.4 | 0 | 0 | 446.0 | 0.0021 |
| particle-ai/us/flex | unknown | yes | 88.6 | 70 | 0.00 | 1.00 | 64.3 | 100.0 | 57.1 | 100.0 | 100.0 | 51.4 | 0 | 0 | 465.0 | 0.0031 |
| wafer/us | mxfp4 | yes | 87.5 | 72 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 50.0 | 0 | 0 | 410.0 | 0.0027 |
| deepinfra/fp8/priority | fp8 | yes | 87.3 | 71 | 0 | 1.00 | 66.7 | 100.0 | 57.1 | 100.0 | 100.0 | 50.7 | 0 | 0 | 975.0 | 0.0017 |
| morph/fp8 | fp8 | yes | 87.3 | 71 | 0 | 1.00 | 60.0 | 100.0 | 50.0 | 100.0 | 100.0 | 50.7 | 0 | 0 | 699.0 | 0.0032 |
| relace/fp4 | fp4 | no | 87.3 | 71 | 0 | 1.00 | 73.3 | 100.0 | 50.0 | 100.0 | 100.0 | 50.7 | 0 | 0 | 891.0 | 0.0064 |
| inference-net/fp8 | fp8 | yes | 87.1 | 70 | 0 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 51.4 | 0 | 0 | 518.5 | 0.0028 |
| reka | unknown | no | 86.8 | 68 | 0 | 1.00 | 71.4 | 100.0 | 57.1 | 100.0 | 100.0 | 52.8 | 0 | 0 | 465.0 | 0.0144 |
| primalabs | unknown | yes | 86.6 | 67 | 0 | 1.00 | 71.4 | 100.0 | 50.0 | 100.0 | 100.0 | 53.5 | 0 | 0 | 555.0 | 0.0117 |
| cohere/fp8 | fp8 | yes | 85.9 | 71 | 0.00 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 50.7 | 0 | 0 | 448.0 | 0.0059 |
| coreweave/fp8 | fp8 | yes | 85.3 | 68 | 0.00 | 1.00 | 64.3 | 100.0 | 50.0 | 100.0 | 100.0 | 52.8 | 0 | 0 | 373.0 | 0.0144 |
| deepinfra/fp8/flex | fp8 | yes | 85.3 | 75 | 0 | 1.00 | 68.8 | 100.0 | 46.7 | 100.0 | 100.0 | 47.2 | 0 | 0 | 928.0 | 0.0040 |
| fireworks/us | unknown | no | 85.3 | 68 | 0.00 | 1.00 | 64.3 | 100.0 | 57.1 | 100.0 | 100.0 | 52.8 | 0 | 0 | 482.0 | 0.0218 |
| alibaba | unknown | yes | 84.7 | 72 | 0 | 1.00 | 86.7 | 100.0 | 57.1 | 100.0 | 100.0 | 50.0 | 0 | 0 | 792.0 | 0.0048 |
| river | unknown | yes | 84.5 | 71 | 0 | 1.00 | 60.0 | 100.0 | 50.0 | 100.0 | 100.0 | 50.7 | 0 | 0 | 845.0 | 0.0062 |
| inceptron/fp4 | fp4 | yes | 84.3 | 70 | 0 | 1.00 | 85.7 | 100.0 | 50.0 | 100.0 | 100.0 | 51.4 | 0 | 0 | 1183.0 | 0.0057 |
| siliconflow/fp8 | fp8 | no | 84.3 | 70 | 0 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 51.4 | 0 | 0 | 2355.5 | 0.0077 |
| google-vertex/global | unknown | yes | 84.1 | 69 | 0 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 52.1 | 0 | 0 | 599.0 | 0.0157 |
| pareto-inference/fp8 | fp8 | yes | 83.3 | 72 | 0.00 | 1.00 | 60.0 | 100.0 | 50.0 | 100.0 | 100.0 | 50.0 | 0 | 0 | 1259.5 | 0.0039 |
| baidu/fp8 | fp8 | no | 82.9 | 70 | 0.00 | 1.00 | 85.7 | 100.0 | 42.9 | 100.0 | 100.0 | 51.4 | 0 | 0 | 858.0 | 0.0079 |
| nebius/fp4 | fp4 | yes | 82.9 | 70 | 0.00 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 51.4 | 0 | 0 | 527.5 | 0.0095 |
| ionstream | unknown | yes | 81.2 | 69 | 0 | 1.00 | 71.4 | 100.0 | 42.9 | 100.0 | 100.0 | 52.1 | 0 | 0 | 559.0 | 0.0098 |
| near-ai | unknown | no | 80.9 | 68 | 0 | 1.00 | 78.6 | 100.0 | 50.0 | 100.0 | 100.0 | 52.8 | 0 | 0 | 2172.0 | 0.0147 |
| open-inference/fp4 | fp4 | yes | 78.6 | 70 | 0 | 1.00 | 57.1 | 100.0 | 57.1 | 100.0 | 100.0 | 51.4 | 0 | 0 | 940.5 | 0.0032 |
| streamlake/fp8 | fp8 | no | 75.0 | 72 | 0.00 | 1.00 | 46.7 | 100.0 | 42.9 | 100.0 | 100.0 | 50.0 | 0 | 0 | 1414.5 | 0.0046 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| fireworks/spot | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: wafer/us, sail-research/fp4/us, sail-research/fp4, particle-ai/us/flex, ambient/fp4, open-inference/fp4, pearl-research/fp8, particle-ai/us, tenstorrent/fp8, morph/fp8, wafer/mxfp4, pareto-inference/fp8, cloudflare, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, streamlake/fp8, alibaba, deepinfra/fp8, modelrun/fp4, inceptron/fp4, cohere/fp8, river, relace/fp4, deepinfra/fp8/priority, baidu/fp8, fireworks/flex, fireworks/spot, siliconflow/fp8, deepseek, makora/fp8, nebius/fp4, crusoe/fp8, primeintellect, digitalocean, ionstream, featherless/fp8, primalabs, modal, google-vertex/global, coreweave/fp8, near-ai, venice/fp8, mistral/fp8, reka, fireworks, baseten, parasail/fp8, fireworks/us, morph/fast, baseten/fast. Prompts with no plurality (excluded from exact match): 1.

## Footer

- Rows: 12096; errors 4299; misrouted 0; truncated (finish_reason length) 25; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $4.1999; billed: $1.6829; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
