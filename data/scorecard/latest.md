# Bitdepth scorecard 2026-11-11

Run `2026-11-11-live`, source `live`, started 2026-11-11T15:46:39Z, finished 2026-11-11T16:25:42Z.
Each row is one OpenRouter endpoint. Exact match is against the reference output for the same prompt; the reference rule per model is in the footer. Family columns are graded against the generated answer. All numbers are percentages unless the column says otherwise.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | yes | 89.9 | 119 | 2.50 | 1.00 | 100.0 | 100.0 | 60.9 | 100.0 | 95.7 | 8.30 | 0 | 0 | 2205.0 | 0.1178 |
| alibaba/fp8 | fp8 | yes | 85.4 | 123 | 4.00 | 1.00 | 100.0 | 100.0 | 63.6 | 100.0 | 95.7 | 6.20 | 0 | 0 | 2332.0 | 0.1145 |
| streamlake/fp8 | fp8 | no | 77.3 | 128 | 4 | 1.00 | 100.0 | 100.0 | 58.3 | 100.0 | 100.0 | 2.10 | 0 | 0 | 2370.0 | 0.0317 |
| atlas-cloud/fp4 | fp4 | yes | 74.8 | 119 | 0.00 | 1.00 | 100.0 | 100.0 | 56.5 | 100.0 | 100.0 | 9.70 | 0 | 0 | 2705.5 | 0.1301 |
| relace/fp4 | fp4 | no | 73.6 | 129 | 4.00 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 95.8 | 1.40 | 0 | 0 | 1310.5 | 0.0747 |
| deepinfra/fp8 | fp8 | yes | 73.4 | 124 | 3 | 1.00 | 100.0 | 100.0 | 65.2 | 100.0 | 100.0 | 4.90 | 0 | 0 | 1178.0 | 0.1064 |
| venice | unknown | no | 69.5 | 118 | 1.00 | 1.00 | 100.0 | 100.0 | 56.5 | 100.0 | 90.5 | 9.70 | 0 | 0 | 1683.5 | 0.0637 |
| siliconflow/fp8 | fp8 | no | 68.5 | 130 | 3 | 1.00 | 100.0 | 100.0 | 66.7 | 100.0 | 100.0 | 0.70 | 0 | 0 | 3906.0 | 0.0839 |
| digitalocean | unknown | no | 57.9 | 126 | 1 | 1.00 | 100.0 | 100.0 | 47.8 | 100.0 | 95.8 | 3.50 | 0 | 0 | 3037.0 | 0.0885 |
| azure/us | unknown | no | 55.2 | 116 | 1.00 | 1.00 | 100.0 | 100.0 | 60.9 | 100.0 | 95.2 | 11.8 | 0 | 0 | 1366.0 | 0.1426 |
| gmicloud/fp8 | fp8 | yes | 49.6 | 125 | 1 | 1.00 | 97.9 | 100.0 | 30.4 | 100.0 | 100.0 | 4.20 | 0 | 0 | 2508.0 | 0.0755 |
| novita/fp8 | fp8 | yes | 49.6 | 119 | 1.00 | 1.00 | 97.7 | 100.0 | 30.4 | 100.0 | 100.0 | 9.00 | 0 | 0 | 2213.0 | 0.1090 |
| baidu/fp8 | fp8 | no | 47.2 | 125 | 1.00 | 1.00 | 100.0 | 100.0 | 29.2 | 100.0 | 100.0 | 4.20 | 0 | 0 | 1681.0 | 0.0692 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: streamlake/fp8, baidu/fp8, relace/fp4, gmicloud/fp8, siliconflow/fp8, digitalocean, deepinfra/fp8, alibaba/fp8, alibaba/fp8/us-east-1, novita/fp8, venice, atlas-cloud/fp4, azure/us. Prompts with no plurality (excluded from exact match): 13.

## deepseek-v4.1-flash-1017 (`deepseek/deepseek-v4.1-flash-1017`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| stepfun/fp8 | fp8 | no | 98.4 | 63 | 0 | 1.00 | 76.9 | 100.0 | 46.2 | 100.0 | 100.0 | 54.9 | 0 | 0 | 650.0 | 0.0065 |
| baseten/fast | unknown | no | 95.8 | 24 | 0 | 1.00 | 66.7 | 100.0 | 50.0 | 100.0 | 100.0 | 81.9 | 0 | 0 | 383.5 | 0.0081 |
| cohere/fp8 | fp8 | yes | 95.2 | 63 | 0 | 1.00 | 69.2 | 100.0 | 61.5 | 100.0 | 100.0 | 54.9 | 0 | 0 | 448.0 | 0.0070 |
| modal | unknown | no | 95.0 | 60 | 0 | 1.00 | 76.9 | 100.0 | 53.8 | 100.0 | 100.0 | 56.9 | 0 | 0 | 767.5 | 0.0105 |
| cloudflare | unknown | yes | 93.7 | 63 | 0.00 | 1.00 | 84.6 | 100.0 | 46.2 | 100.0 | 100.0 | 54.9 | 0 | 0 | 1634.0 | 0.0025 |
| baseten | unknown | no | 93.2 | 59 | 0.00 | 1.00 | 61.5 | 100.0 | 46.2 | 100.0 | 100.0 | 57.6 | 0 | 0 | 650.0 | 0.0120 |
| venice/fp8 | fp8 | no | 93.2 | 59 | 0.00 | 1.00 | 76.9 | 100.0 | 46.2 | 100.0 | 100.0 | 57.6 | 0 | 0 | 957.0 | 0.0119 |
| wafer/mxfp4 | mxfp4 | yes | 92.2 | 64 | 0 | 1.00 | 71.4 | 100.0 | 46.2 | 100.0 | 100.0 | 54.2 | 0 | 0 | 518.5 | 0.0015 |
| wafer/us | mxfp4 | yes | 92.2 | 64 | 0 | 1.00 | 78.6 | 100.0 | 53.8 | 100.0 | 100.0 | 54.2 | 0 | 0 | 513.0 | 0.0025 |
| primeintellect | unknown | no | 92.1 | 63 | 0 | 1.00 | 84.6 | 100.0 | 46.2 | 100.0 | 100.0 | 54.9 | 0 | 0 | 643.0 | 0.0030 |
| coreweave/fp8 | fp8 | yes | 91.7 | 60 | 0 | 1.00 | 61.5 | 100.0 | 46.2 | 100.0 | 100.0 | 56.9 | 0 | 0 | 543.0 | 0.0125 |
| makora/fp8 | fp8 | yes | 91.7 | 60 | 0 | 1.00 | 76.9 | 100.0 | 61.5 | 100.0 | 100.0 | 56.9 | 0 | 0 | 579.5 | 0.0074 |
| together | unknown | no | 91.7 | 60 | 0 | 1.00 | 76.9 | 100.0 | 46.2 | 90.9 | 100.0 | 56.9 | 0 | 0 | 442.0 | 0.0126 |
| fireworks | unknown | no | 91.5 | 59 | 0 | 1.00 | 76.9 | 100.0 | 53.8 | 100.0 | 100.0 | 57.6 | 0 | 0 | 885.0 | 0.0119 |
| fireworks/us | unknown | no | 91.5 | 59 | 0 | 1.00 | 61.5 | 100.0 | 53.8 | 100.0 | 100.0 | 57.6 | 0 | 0 | 637.0 | 0.0175 |
| nebius/fp8 | fp8 | yes | 91.5 | 59 | 0 | 1.00 | 61.5 | 100.0 | 46.2 | 100.0 | 100.0 | 57.6 | 0 | 0 | 1406.0 | 0.0116 |
| parasail/fp8 | fp8 | yes | 91.5 | 59 | 0 | 1.00 | 69.2 | 100.0 | 53.8 | 100.0 | 100.0 | 57.6 | 0 | 0 | 436.0 | 0.0117 |
| deepinfra/fp8 | fp8 | yes | 90.6 | 64 | 0.00 | 1.00 | 64.3 | 100.0 | 46.2 | 100.0 | 100.0 | 54.2 | 0 | 0 | 592.0 | 0.0016 |
| morph/fp8 | fp8 | yes | 90.6 | 64 | 0.00 | 1.00 | 78.6 | 100.0 | 46.2 | 100.0 | 100.0 | 54.2 | 0 | 0 | 1271.5 | 0.0017 |
| particle-ai/us | unknown | yes | 90.6 | 64 | 0.00 | 1.00 | 64.3 | 100.0 | 38.5 | 100.0 | 100.0 | 54.2 | 0 | 0 | 997.0 | 0.0018 |
| particle-ai/us/flex | unknown | yes | 90.6 | 64 | 0.00 | 1.00 | 71.4 | 100.0 | 53.8 | 100.0 | 100.0 | 54.2 | 0 | 0 | 811.5 | 0.0017 |
| sail-research/fp4/us | fp4 | yes | 90.6 | 64 | 0.00 | 1.00 | 57.1 | 100.0 | 46.2 | 100.0 | 100.0 | 54.2 | 0 | 0 | 1275.0 | 0.0044 |
| deepinfra/fp8/priority | fp8 | yes | 90.5 | 63 | 0.00 | 1.00 | 61.5 | 100.0 | 38.5 | 100.0 | 100.0 | 54.9 | 0 | 0 | 536.0 | 0.0015 |
| primalabs | unknown | yes | 90.0 | 60 | 0.00 | 1.00 | 61.5 | 100.0 | 53.8 | 100.0 | 100.0 | 56.9 | 0 | 0 | 725.0 | 0.0100 |
| deepinfra/fp8/flex | fp8 | yes | 89.1 | 64 | 0 | 1.00 | 64.3 | 100.0 | 46.2 | 100.0 | 100.0 | 54.2 | 0 | 0 | 2012.5 | 0.0032 |
| relace/fp4 | fp4 | no | 89.1 | 64 | 0 | 1.00 | 64.3 | 100.0 | 53.8 | 100.0 | 100.0 | 54.2 | 0 | 0 | 982.5 | 0.0010 |
| alibaba | unknown | yes | 88.9 | 63 | 0 | 1.00 | 69.2 | 100.0 | 46.2 | 100.0 | 100.0 | 54.9 | 0 | 0 | 1423.0 | 0.0051 |
| dekallm | unknown | yes | 88.5 | 61 | 0 | 1.00 | 69.2 | 100.0 | 53.8 | 100.0 | 100.0 | 56.2 | 0 | 0 | 1023.0 | 0.0080 |
| siliconflow/fp8 | fp8 | no | 88.3 | 60 | 0 | 1.00 | 69.2 | 100.0 | 53.8 | 100.0 | 100.0 | 56.9 | 0 | 0 | 1027.5 | 0.0107 |
| inference-net/us | fp8 | yes | 87.5 | 64 | 0.00 | 1.00 | 64.3 | 100.0 | 53.8 | 100.0 | 100.0 | 54.2 | 0 | 0 | 522.5 | 0.0041 |
| sail-research/fp4 | fp4 | yes | 87.5 | 64 | 0.00 | 1.00 | 57.1 | 100.0 | 46.2 | 100.0 | 100.0 | 54.2 | 0 | 0 | 1309.5 | 0.0006 |
| atlas-cloud/fp8 | fp8 | yes | 86.7 | 60 | 0.00 | 1.00 | 69.2 | 100.0 | 38.5 | 100.0 | 100.0 | 56.9 | 0 | 0 | 1442.5 | 0.0019 |
| mistral/fp8 | fp8 | yes | 86.4 | 59 | 0.00 | 1.00 | 61.5 | 100.0 | 53.8 | 100.0 | 100.0 | 57.6 | 0 | 0 | 823.0 | 0.0116 |
| inference-net/fp8 | fp8 | yes | 85.9 | 64 | 0 | 1.00 | 64.3 | 100.0 | 53.8 | 100.0 | 100.0 | 54.2 | 0 | 0 | 524.0 | 0.0036 |
| novita/fp8 | fp8 | yes | 85.7 | 63 | 0 | 1.00 | 69.2 | 100.0 | 53.8 | 100.0 | 100.0 | 54.9 | 0 | 0 | 1367.0 | 0.0016 |
| streamlake/fp8 | fp8 | no | 85.7 | 63 | 0 | 1.00 | 69.2 | 100.0 | 61.5 | 100.0 | 100.0 | 54.9 | 0 | 0 | 1623.0 | 0.0052 |
| crusoe/fp8 | fp8 | yes | 85.0 | 60 | 0 | 1.00 | 69.2 | 100.0 | 46.2 | 100.0 | 100.0 | 56.9 | 0 | 0 | 637.5 | 0.0124 |
| digitalocean | unknown | no | 85.0 | 60 | 0 | 1.00 | 69.2 | 100.0 | 53.8 | 100.0 | 100.0 | 56.9 | 0 | 0 | 682.0 | 0.0075 |
| gmicloud/fp8 | fp8 | yes | 85.0 | 60 | 0 | 1.00 | 53.8 | 100.0 | 46.2 | 100.0 | 100.0 | 56.9 | 0 | 0 | 1147.5 | 0.0076 |
| ionstream/flex | unknown | yes | 84.4 | 64 | 0.00 | 1.00 | 71.4 | 100.0 | 46.2 | 100.0 | 100.0 | 54.2 | 0 | 0 | 10588.0 | 0.0036 |
| baidu/fp8 | fp8 | no | 84.1 | 63 | 0.00 | 1.00 | 84.6 | 100.0 | 38.5 | 100.0 | 100.0 | 54.9 | 0 | 0 | 1095.0 | 0.0072 |
| near-ai | unknown | no | 83.1 | 59 | 0.00 | 1.00 | 84.6 | 100.0 | 61.5 | 100.0 | 100.0 | 57.6 | 0 | 0 | 1576.0 | 0.0121 |
| ionstream | unknown | yes | 82.5 | 63 | 0 | 1.00 | 61.5 | 100.0 | 38.5 | 100.0 | 100.0 | 54.9 | 0 | 0 | 673.0 | 0.0076 |
| open-inference/fp4 | fp4 | yes | 79.4 | 63 | 0 | 1.00 | 53.8 | 100.0 | 53.8 | 100.0 | 100.0 | 54.9 | 0 | 0 | 1991.0 | 0.0042 |
| reka | unknown | no | 78.3 | 60 | 0 | 1.00 | 61.5 | 100.0 | 53.8 | 100.0 | 100.0 | 56.9 | 0 | 0 | 873.5 | 0.0075 |
| deepseek | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| fireworks/spot | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, morph/fp8, particle-ai/us/flex, wafer/us, primeintellect, particle-ai/us, wafer/mxfp4, open-inference/fp4, ionstream/flex, deepinfra/fp8/flex, inference-net/us, inference-net/fp8, deepinfra/fp8, cloudflare, sail-research/fp4/us, alibaba, streamlake/fp8, stepfun/fp8, deepinfra/fp8/priority, baidu/fp8, cohere/fp8, deepseek, makora/fp8, sail-research/fp4, reka, ionstream, novita/fp8, dekallm, digitalocean, gmicloud/fp8, atlas-cloud/fp8, fireworks/spot, primalabs, modal, crusoe/fp8, siliconflow/fp8, mistral/fp8, coreweave/fp8, near-ai, venice/fp8, nebius/fp8, together, fireworks, baseten, parasail/fp8, fireworks/us, baseten/fast. Prompts with no plurality (excluded from exact match): 2.

## mistral-large-4-0 (`mistralai/mistral-large-4-0`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mistral/eu | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| mistral/zdr | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: mistral/zdr, mistral/eu. Prompts with no plurality (excluded from exact match): 0.

## glm-5.3-flash (`z-ai/glm-5.3-flash`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| atlas-cloud/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| baseten/fp8 | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| baseten/fp8/us | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| cohere/nvfp4 | nvfp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| coreweave/nvfp4 | nvfp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| crusoe/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| darkbloom/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| deepinfra/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| dekallm | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| digitalocean | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| fireworks | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| friendli | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| gmicloud/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| inceptron/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| inference-net/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| inference-net/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| kt | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| makora/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| mistral | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| modal/fp4 | fp4 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| morph/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| near-ai/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| nebius/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| nextbit/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| novita/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| open-inference/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| parasail/fast | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| parasail/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| particle-ai/nvfp4 | nvfp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| primeintellect | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| reka | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| relace/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sail-research/us | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| siliconflow/fp8 | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| streamlake/fp8 | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| tenstorrent/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| together | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| venice | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| wafer/nvfp4 | nvfp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| wafer/us | nvfp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| z-ai/fp8 | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: relace/fp4, wafer/us, primeintellect, open-inference/fp4, darkbloom/fp4, wafer/nvfp4, tenstorrent/fp8, gmicloud/fp8, near-ai/fp8, novita/fp8, streamlake/fp8, morph/fp8, dekallm, inference-net/us, inference-net/fp4, digitalocean, reka, coreweave/nvfp4, nextbit/fp4, particle-ai/nvfp4, makora/fp4, mistral, kt, cohere/nvfp4, nebius/fp4, modal/fp4, baseten/fp8/us, crusoe/fp4, atlas-cloud/fp8, fireworks, friendli, siliconflow/fp8, together, parasail/fp4, baseten/fp8, venice, deepinfra/fp4, z-ai/fp8, inceptron/fp8, sail-research/us, sail-research/fp4, parasail/fast. Prompts with no plurality (excluded from exact match): 0.

## gemma-4-31b-it (`google/gemma-4-31b-it`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| chutes/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| coreweave/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| crusoe/bf16 | bf16 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| deepinfra/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| deepinfra/fp8/flex | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| deepinfra/fp8/priority | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| deepinfra/turbo | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| dekallm | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| friendli | unknown | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| kt | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| modal | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| nextbit/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| novita/bf16 | bf16 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| parasail/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| primeintellect/fp4 | fp4 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| sambanova | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| siliconflow/fp8 | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| venice/fp4 | fp4 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: crusoe/bf16, novita/bf16. Prompts with no plurality (excluded from exact match): 0.

## mimo-v2.6-pro (`xiaomi/mimo-v2.6-pro`)

| Endpoint | Declared quant | Seed | Exact % | Compared | Div. word | Len ratio | Math | JSON | String | Needle | Echo | Err % | Misrouted | Truncated | Latency ms | Cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| gmicloud/bf16 | bf16 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| primalabs/fp8 | fp8 | yes | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| streamlake | unknown | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |
| xiaomi/fp8 | fp8 | no | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100.0 | 0 | 0 | n/a | 0.0000 |

Reference rule: plurality across all endpoints (fewer than two declare bf16 or fp16). Reference endpoints: gmicloud/bf16, deepinfra/fp8, xiaomi/fp8, streamlake, primalabs/fp8. Prompts with no plurality (excluded from exact match): 0.

## Footer

- Rows: 18288; errors 13693; misrouted 0; truncated (finish_reason length) 0; skipped by runtime budget stop 0.
- Prompts kept 144 of 144; dropped for budget: 0 ().
- Estimate before sending: $6.5078; billed: $1.5075; cap $7.75; runtime budget stop: False.
- Div. word is the median index of the first differing word, on whitespace-split words, over non-matching outputs only. Len ratio is the median of output words divided by reference words.
- Misrouted means the provider named in the response differs from the pinned provider; those rows are excluded from every metric. Detection is at provider level, not endpoint-variant level.
- A row counts as truncated when the endpoint stopped at max_tokens; its output is still scored as returned.
- Numbers describe outputs against a stated reference and nothing else.
