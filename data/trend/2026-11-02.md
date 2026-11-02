# Bitdepth trend through 2026-11-02

Nights found: 7 (2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02). Self-check nights: 2026-10-27, 2026-11-02.
Each row is one OpenRouter endpoint across every night it was listed. Exact % per night is the nightly scorecard figure (match against that night's reference). Family columns are mean graded accuracy against the generated answers. Self-agree is the endpoint's night-to-night agreement with itself on the fixed prompts. Self-check columns are the one-hour two-pass agreement on the nights it was measured. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

### Exact match by night

| Endpoint | Declared quant | Nights | 10-27 | 10-28 | 10-29 | 10-30 | 10-31 | 11-01 | 11-02 | Mean | SD | Min | Max | Movement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8 | fp8 | 4 | - | - | - | 96.9 | 97.7 | 97.0 | 100.0 | 97.9 | 1.3 | 96.9 | 100.0 | +1.0 |
| baseten/fp4 | fp4 | 7 | 97.2 | 96.5 | 98.6 | 97.9 | 97.2 | 98.6 | 97.9 | 97.7 | 0.7 | 96.5 | 98.6 | +0.5 |
| baseten/fp4/us | fp4 | 7 | 97.9 | 98.6 | 97.9 | 97.2 | 96.5 | 98.6 | 97.2 | 97.7 | 0.7 | 96.5 | 98.6 | -0.7 |
| crusoe/bf16 | bf16 | 7 | 97.2 | 97.9 | 98.6 | 97.9 | 98.6 | 95.8 | 97.2 | 97.6 | 0.9 | 95.8 | 98.6 | -0.7 |
| parasail/fp4 | fp4 | 7 | 95.1 | 97.9 | 97.9 | 98.6 | 95.8 | 97.9 | 97.2 | 97.2 | 1.2 | 95.1 | 98.6 | +0.0 |
| deepinfra/bf16 | bf16 | 7 | 97.2 | 97.9 | 97.9 | 97.9 | 97.2 | 97.2 | 94.4 | 97.1 | 1.1 | 94.4 | 97.9 | -1.4 |
| mara | unknown | 7 | 95.8 | 95.8 | 97.9 | 96.5 | 97.2 | 97.2 | 99.3 | 97.1 | 1.1 | 95.8 | 99.3 | +1.4 |
| amazon-bedrock | unknown | 7 | 95.8 | 97.9 | 97.9 | 96.5 | 97.9 | 94.4 | 98.6 | 97.0 | 1.4 | 94.4 | 98.6 | -0.2 |
| cerebras/fp16 | fp16 | 7 | 96.5 | 97.2 | 95.8 | 95.8 | 97.9 | 96.5 | 99.3 | 97.0 | 1.2 | 95.8 | 99.3 | +1.4 |
| together | unknown | 7 | 97.9 | 97.2 | 97.2 | 97.2 | 97.9 | 95.8 | 95.8 | 97.0 | 0.8 | 95.8 | 97.9 | -0.9 |
| sambanova | unknown | 7 | 95.8 | 95.1 | 97.2 | 96.5 | 97.2 | 97.2 | 99.3 | 96.9 | 1.2 | 95.1 | 99.3 | +1.9 |
| groq | unknown | 7 | 97.2 | 96.5 | 97.2 | 95.1 | 97.2 | 96.5 | 97.9 | 96.8 | 0.8 | 95.1 | 97.9 | +0.2 |
| dekallm/bf16 | bf16 | 7 | 96.5 | 95.8 | 95.8 | 94.4 | 97.2 | 97.9 | 97.2 | 96.4 | 1.1 | 94.4 | 97.9 | +1.4 |
| amazon-bedrock/eu-west-1 | unknown | 7 | 92.4 | 95.8 | 96.5 | 97.2 | 98.6 | 95.8 | 96.5 | 96.1 | 1.8 | 92.4 | 98.6 | +2.1 |
| mancer/fp8 | fp8 | 7 | 95.1 | 95.8 | 97.9 | 94.4 | 99.3 | 94.4 | 95.8 | 96.1 | 1.7 | 94.4 | 99.3 | +0.2 |
| nebius/fp4 | fp4 | 7 | 93.8 | 97.2 | 95.8 | 96.5 | 97.9 | 93.1 | 97.9 | 96.0 | 1.8 | 93.1 | 97.9 | +0.7 |
| akashml/bf16 | bf16 | 7 | 95.1 | 96.5 | 95.1 | 95.8 | 95.8 | 93.8 | 98.6 | 95.8 | 1.4 | 93.8 | 98.6 | +0.5 |
| sail-research/fp4 | fp4 | 7 | 95.6 | 95.1 | 94.4 | 95.8 | 100.0 | 93.1 | 95.1 | 95.6 | 2.0 | 93.1 | 100.0 | +1.0 |
| near-ai/fp4 | fp4 | 7 | 97.2 | 95.1 | 95.8 | 92.4 | 95.8 | 97.2 | 95.1 | 95.5 | 1.5 | 92.4 | 97.2 | +0.0 |
| siliconflow/fp8 | fp8 | 7 | 93.1 | 93.1 | 95.0 | 95.8 | 95.7 | 97.2 | 95.8 | 95.1 | 1.4 | 93.1 | 97.2 | +2.5 |
| primeintellect/fp4 | fp4 | 2 | - | - | - | - | - | 93.1 | 96.4 | 94.8 | 1.7 | 93.1 | 96.4 | +0.0 |
| coreweave/fp4 | fp4 | 7 | 93.8 | 95.8 | 95.8 | 94.4 | 97.2 | 91.7 | 94.4 | 94.7 | 1.6 | 91.7 | 97.2 | -0.7 |
| google-vertex/global | unknown | 7 | 94.4 | 95.1 | 91.0 | 93.8 | 97.2 | 90.9 | 90.4 | 93.3 | 2.4 | 90.4 | 97.2 | -0.7 |
| phala | unknown | 7 | 90.8 | 91.7 | 92.4 | 93.8 | 95.8 | 92.4 | 93.1 | 92.9 | 1.5 | 90.8 | 95.8 | +2.1 |
| novita/fp4 | fp4 | 7 | 93.8 | 91.0 | 93.8 | 95.1 | 91.6 | 92.4 | 90.3 | 92.6 | 1.6 | 90.3 | 95.1 | -1.4 |
| digitalocean | unknown | 7 | 94.4 | 91.0 | 90.3 | 92.4 | 90.2 | 88.9 | 91.7 | 91.3 | 1.6 | 88.9 | 94.4 | -1.6 |
| venice/int4 | int4 | 7 | 91.0 | 95.8 | 97.2 | 94.4 | 96.5 | 81.9 | 75.0 | 90.3 | 7.9 | 75.0 | 97.2 | -10.2 * |

### Graded accuracy and self-agreement (sorted by String, then Self-agree)

| Endpoint | Math | JSON | String | Needle | Echo | Self-agree | Pairs | Self-agree Math | JSON | String | Needle | Echo | Self-check 10-27 | Self-check 11-02 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| siliconflow/fp8 | 98.5 | 100.0 | 88.5 | 99.4 | 99.4 | 94.6 | 702 | 97.9 | 86.8 | 87.7 | 98.3 | 98.3 | 91.7 (12) | 91.7 (36) |
| cerebras/fp16 | 99.7 | 100.0 | 87.5 | 100.0 | 100.0 | 97.1 | 720 | 99.2 | 93.3 | 90.8 | 100.0 | 100.0 | 100.0 (12) | 100.0 (36) |
| digitalocean | 99.7 | 100.0 | 85.1 | 100.0 | 100.0 | 88.9 | 720 | 100.0 | 52.5 | 80.8 | 100.0 | 100.0 | 83.3 (12) | 88.9 (36) |
| deepinfra/fp8 | 100.0 | 100.0 | 84.6 | 100.0 | 100.0 | 97.4 | 307 | 100.0 | 97.9 | 86.8 | 100.0 | 100.0 | - | 100.0 (34) |
| baseten/fp4 | 99.7 | 100.0 | 84.5 | 100.0 | 100.0 | 97.5 | 720 | 100.0 | 98.3 | 86.7 | 100.0 | 100.0 | 91.7 (12) | 97.2 (36) |
| deepinfra/bf16 | 100.0 | 100.0 | 83.9 | 99.4 | 100.0 | 97.8 | 716 | 100.0 | 94.0 | 94.2 | 98.3 | 100.0 | 90.0 (10) | 100.0 (36) |
| baseten/fp4/us | 99.7 | 100.0 | 83.3 | 100.0 | 100.0 | 97.2 | 718 | 100.0 | 98.3 | 85.0 | 100.0 | 100.0 | 91.7 (12) | 91.4 (35) |
| mancer/fp8 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 94.2 | 720 | 100.0 | 81.7 | 83.3 | 100.0 | 100.0 | 83.3 (12) | 94.4 (36) |
| sambanova | 100.0 | 100.0 | 82.1 | 100.0 | 100.0 | 96.4 | 720 | 100.0 | 90.8 | 87.5 | 100.0 | 100.0 | 100.0 (12) | 100.0 (36) |
| mara | 100.0 | 100.0 | 81.9 | 100.0 | 100.0 | 96.8 | 712 | 100.0 | 92.5 | 87.9 | 100.0 | 100.0 | 100.0 (12) | 100.0 (36) |
| groq | 100.0 | 100.0 | 81.6 | 100.0 | 100.0 | 98.3 | 720 | 100.0 | 98.3 | 91.7 | 100.0 | 100.0 | 100.0 (12) | 100.0 (36) |
| near-ai/fp4 | 99.7 | 100.0 | 81.6 | 100.0 | 100.0 | 93.5 | 720 | 100.0 | 79.2 | 81.7 | 100.0 | 100.0 | 91.7 (12) | 97.2 (36) |
| dekallm/bf16 | 99.7 | 100.0 | 81.5 | 100.0 | 100.0 | 95.0 | 720 | 100.0 | 74.2 | 95.8 | 100.0 | 100.0 | 75.0 (12) | 94.4 (36) |
| amazon-bedrock | 100.0 | 100.0 | 80.9 | 100.0 | 100.0 | 95.1 | 720 | 100.0 | 82.5 | 88.3 | 100.0 | 100.0 | 100.0 (12) | 97.2 (36) |
| parasail/fp4 | 100.0 | 100.0 | 80.4 | 100.0 | 100.0 | 95.7 | 718 | 100.0 | 92.5 | 81.7 | 100.0 | 100.0 | 100.0 (8) | 94.4 (36) |
| akashml/bf16 | 100.0 | 100.0 | 80.4 | 100.0 | 100.0 | 93.8 | 720 | 100.0 | 73.3 | 89.2 | 100.0 | 100.0 | 100.0 (12) | 94.4 (36) |
| crusoe/bf16 | 100.0 | 100.0 | 79.8 | 100.0 | 100.0 | 96.2 | 720 | 100.0 | 95.0 | 82.5 | 100.0 | 100.0 | 83.3 (12) | 88.9 (36) |
| nebius/fp4 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 94.6 | 720 | 100.0 | 82.5 | 85.0 | 100.0 | 100.0 | 91.7 (12) | 94.4 (36) |
| novita/fp4 | 98.5 | 100.0 | 78.6 | 99.4 | 99.4 | 90.6 | 720 | 97.1 | 67.5 | 83.3 | 100.0 | 98.3 | 83.3 (12) | 91.7 (36) |
| venice/int4 | 91.1 | 100.0 | 78.6 | 100.0 | 93.5 | 88.7 | 718 | 87.4 | 81.7 | 83.3 | 100.0 | 92.5 | 90.9 (11) | 83.3 (36) |
| coreweave/fp4 | 99.7 | 100.0 | 78.0 | 100.0 | 100.0 | 92.9 | 714 | 100.0 | 72.9 | 84.2 | 100.0 | 100.0 | 66.7 (12) | 94.4 (36) |
| google-vertex/global | 93.0 | 99.4 | 78.0 | 100.0 | 98.2 | 92.7 | 710 | 97.4 | 80.0 | 85.6 | 100.0 | 95.8 | 100.0 (12) | 71.9 (32) |
| phala | 99.1 | 100.0 | 78.0 | 99.4 | 98.8 | 91.6 | 718 | 99.2 | 75.6 | 80.8 | 98.3 | 96.7 | 83.3 (12) | 83.3 (36) |
| together | 100.0 | 100.0 | 76.8 | 100.0 | 100.0 | 97.5 | 720 | 100.0 | 98.3 | 86.7 | 100.0 | 100.0 | 83.3 (12) | 100.0 (36) |
| primeintellect/fp4 | 100.0 | 100.0 | 76.7 | 100.0 | 100.0 | 92.2 | 116 | 100.0 | 75.0 | 78.9 | 100.0 | 100.0 | - | 100.0 (36) |
| sail-research/fp4 | 100.0 | 100.0 | 75.2 | 100.0 | 100.0 | 93.2 | 689 | 100.0 | 77.9 | 80.7 | 100.0 | 100.0 | 91.7 (12) | 97.2 (36) |
| amazon-bedrock/eu-west-1 | 100.0 | 100.0 | 74.4 | 100.0 | 100.0 | 95.1 | 720 | 100.0 | 85.8 | 85.0 | 100.0 | 100.0 | 91.7 (12) | 97.2 (36) |

### Noise floor by family (night-to-night)

| Family | Endpoints | Median self-agree | P75 disagreement | Noise floor | Stable |
|---|---|---|---|---|---|
| math | 27 | 100.0 | 0.0 | 100.0 | yes |
| json | 27 | 82.5 | 23.2 | 76.8 | no |
| string | 27 | 85.0 | 17.1 | 82.9 | no |
| needle | 27 | 100.0 | 0.0 | 100.0 | yes |
| echo | 27 | 100.0 | 0.0 | 100.0 | yes |

Reference rule(s) seen: plurality among endpoints declaring bf16 or fp16.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

### Exact match by night

| Endpoint | Declared quant | Nights | 10-27 | 10-28 | 10-29 | 10-30 | 10-31 | 11-01 | 11-02 | Mean | SD | Min | Max | Movement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | 7 | 80.3 | 80.3 | 77.3 | 81.1 | 81.2 | 87.6 | 88.8 | 82.4 | 3.9 | 77.3 | 88.8 | +6.6 |
| alibaba/fp8 | fp8 | 7 | 82.3 | 75.0 | 78.0 | 81.8 | 80.5 | 86.1 | 86.6 | 81.5 | 3.8 | 75.0 | 86.6 | +6.0 |
| streamlake/fp8 | fp8 | 7 | 86.2 | 78.0 | 79.5 | 78.8 | 78.9 | 74.5 | 72.4 | 78.3 | 4.0 | 72.4 | 86.2 | -6.0 |
| atlas-cloud/fp4 | fp4 | 7 | 78.7 | 78.0 | 72.7 | 78.8 | 76.7 | 72.3 | 77.6 | 76.4 | 2.6 | 72.3 | 78.8 | -0.9 |
| deepinfra/fp8 | fp8 | 7 | 71.5 | 76.5 | 72.7 | 77.3 | 73.7 | 78.8 | 75.8 | 75.2 | 2.4 | 71.5 | 78.8 | +2.5 |
| venice | unknown | 7 | 80.2 | 72.7 | 75.0 | 68.9 | 80.5 | 76.6 | 72.4 | 75.2 | 3.9 | 68.9 | 80.5 | +0.5 |
| relace/fp4 | fp4 | 7 | 78.5 | 78.6 | 74.0 | 74.8 | 71.4 | 70.1 | 74.4 | 74.5 | 3.0 | 70.1 | 78.6 | -5.1 |
| siliconflow/fp8 | fp8 | 7 | 73.0 | 71.2 | 69.7 | 68.9 | 70.7 | 68.6 | 71.6 | 70.5 | 1.5 | 68.6 | 73.0 | -1.0 |
| baidu/fp8 | fp8 | 7 | 75.4 | 68.9 | 75.0 | 53.8 | 51.9 | 81.0 | 77.9 | 69.1 | 10.8 | 51.9 | 81.0 | -2.8 |
| digitalocean | unknown | 7 | 58.5 | 55.3 | 58.3 | 59.1 | 57.1 | 51.8 | 58.7 | 57.0 | 2.4 | 51.8 | 59.1 | -1.5 |
| azure/us | unknown | 7 | 53.9 | 59.5 | 57.6 | 53.0 | 58.6 | 59.9 | 54.9 | 56.8 | 2.6 | 53.0 | 59.9 | +0.8 |
| crusoe/fp8 | fp8 | 7 | 50.4 | 50.0 | 50.0 | 53.4 | 57.9 | 49.6 | 50.7 | 51.7 | 2.8 | 49.6 | 57.9 | +2.6 |
| gmicloud/fp8 | fp8 | 7 | 44.6 | 47.7 | 48.5 | 53.8 | 54.1 | 48.2 | 46.3 | 49.0 | 3.3 | 44.6 | 54.1 | +2.6 |
| novita/fp8 | fp8 | 7 | 47.2 | 48.5 | 49.2 | 50.8 | 53.4 | 46.7 | 44.8 | 48.7 | 2.6 | 44.8 | 53.4 | +0.0 |
| cloudflare | unknown | 7 | 45.4 | 44.7 | 49.5 | 48.5 | 50.4 | 43.1 | 45.1 | 46.7 | 2.6 | 43.1 | 50.4 | -0.3 |

### Graded accuracy and self-agreement (sorted by String, then Self-agree)

| Endpoint | Math | JSON | String | Needle | Echo | Self-agree | Pairs | Self-agree Math | JSON | String | Needle | Echo | Self-check 10-27 | Self-check 11-02 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| relace/fp4 | 100.0 | 100.0 | 65.0 | 100.0 | 96.4 | 66.7 | 709 | 27.4 | 68.9 | 77.6 | 100.0 | 99.2 | 83.3 (12) | 91.7 (36) |
| deepinfra/fp8 | 100.0 | 100.0 | 64.3 | 99.4 | 95.2 | 65.7 | 718 | 32.9 | 64.2 | 72.5 | 98.3 | 94.1 | 66.7 (12) | 75.0 (36) |
| streamlake/fp8 | 100.0 | 100.0 | 63.1 | 100.0 | 96.4 | 68.5 | 720 | 34.6 | 69.2 | 74.2 | 100.0 | 98.3 | 75.0 (12) | 63.9 (36) |
| venice | 100.0 | 100.0 | 62.5 | 99.4 | 97.6 | 65.1 | 716 | 32.8 | 61.3 | 68.3 | 98.3 | 96.7 | 66.7 (12) | 69.4 (36) |
| alibaba/fp8/us-east-1 | 100.0 | 100.0 | 61.3 | 100.0 | 95.2 | 75.1 | 716 | 47.1 | 76.7 | 80.0 | 100.0 | 100.0 | 83.3 (12) | 83.3 (36) |
| alibaba/fp8 | 100.0 | 100.0 | 60.1 | 100.0 | 95.2 | 72.4 | 720 | 42.1 | 72.5 | 77.5 | 100.0 | 100.0 | 75.0 (12) | 86.1 (36) |
| siliconflow/fp8 | 100.0 | 100.0 | 60.1 | 100.0 | 97.6 | 65.3 | 717 | 29.7 | 65.0 | 70.0 | 100.0 | 97.5 | 66.7 (12) | 69.4 (36) |
| atlas-cloud/fp4 | 100.0 | 100.0 | 59.5 | 100.0 | 100.0 | 69.5 | 717 | 35.6 | 70.3 | 75.0 | 100.0 | 100.0 | 58.3 (12) | 72.2 (36) |
| azure/us | 99.1 | 100.0 | 55.7 | 100.0 | 95.0 | 51.2 | 692 | 0.0 | 57.8 | 53.4 | 100.0 | 94.7 | 20.0 (10) | 52.8 (36) |
| digitalocean | 99.4 | 100.0 | 53.3 | 100.0 | 95.8 | 50.2 | 711 | 0.0 | 55.9 | 50.4 | 100.0 | 95.0 | 50.0 (12) | 55.6 (36) |
| baidu/fp8 | 99.1 | 100.0 | 48.0 | 100.0 | 96.3 | 58.0 | 703 | 25.3 | 43.7 | 53.4 | 100.0 | 98.3 | 100.0 (12) | 96.7 (30) |
| crusoe/fp8 | 96.7 | 100.0 | 33.1 | 100.0 | 100.0 | 73.0 | 712 | 44.8 | 79.7 | 69.5 | 100.0 | 100.0 | 83.3 (12) | 88.9 (36) |
| novita/fp8 | 94.6 | 100.0 | 30.9 | 100.0 | 100.0 | 72.1 | 717 | 41.8 | 78.3 | 70.8 | 100.0 | 100.0 | 66.7 (12) | 77.8 (36) |
| gmicloud/fp8 | 97.9 | 100.0 | 29.8 | 100.0 | 100.0 | 67.9 | 720 | 36.2 | 71.7 | 63.3 | 100.0 | 100.0 | 75.0 (12) | 75.0 (36) |
| cloudflare | 93.3 | 100.0 | 21.2 | 100.0 | 100.0 | 77.5 | 719 | 48.8 | 96.7 | 70.8 | 100.0 | 100.0 | 75.0 (12) | 75.0 (36) |

### Noise floor by family (night-to-night)

| Family | Endpoints | Median self-agree | P75 disagreement | Noise floor | Stable |
|---|---|---|---|---|---|
| math | 15 | 34.6 | 71.4 | 28.6 | no |
| json | 15 | 69.2 | 37.2 | 62.8 | no |
| string | 15 | 70.8 | 34.2 | 65.8 | no |
| needle | 15 | 100.0 | 0.0 | 100.0 | yes |
| echo | 15 | 99.2 | 2.9 | 97.1 | yes |

Reference rule(s) seen: plurality across all endpoints (fewer than two declare bf16 or fp16).

## Footer

- Nights found: 7. Self-check nights found: 2 (2026-10-27, 2026-11-02).
- Self-agree: for each pair of consecutive nights the endpoint was listed, each fixed prompt with an ok row on both nights counts once, and agrees when the stripped outputs are equal word for word. Fresh prompts are excluded because they change nightly. Pairs is the count of such prompt-night pairs.
- Movement: mean exact % over the last 3 nights minus the mean over the first 3; when fewer than 6 nights are present the two windows overlap. An asterisk marks an absolute movement at or above 10 points on at least 4 nights. Provisional; calibrate on 2026-11-10.
- Noise floor per family: 100 minus the 75th percentile across endpoints of night-to-night disagreement. Stable means the median endpoint self-agreement is at or above 95. Provisional; calibrate on 2026-11-10.
- Self-check: two passes of the same fixed prompts one hour apart on the nights listed; the figure is the share of prompts whose two outputs were equal, with the prompt count in brackets.
- Declared quant is the latest night's declaration; (changed) means it differed on some night in the range.
- Numbers against a stated reference. Not a claim about intent.
