# Bitdepth trend through 2026-11-01

Nights found: 6 (2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31, 2026-11-01). Self-check nights: 2026-10-27.
Each row is one OpenRouter endpoint across every night it was listed. Exact % per night is the nightly scorecard figure (match against that night's reference). Family columns are mean graded accuracy against the generated answers. Self-agree is the endpoint's night-to-night agreement with itself on the fixed prompts. Self-check columns are the one-hour two-pass agreement on the nights it was measured. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

### Exact match by night

| Endpoint | Declared quant | Nights | 10-27 | 10-28 | 10-29 | 10-30 | 10-31 | 11-01 | Mean | SD | Min | Max | Movement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseten/fp4/us | fp4 | 6 | 97.9 | 98.6 | 97.9 | 97.2 | 96.5 | 98.6 | 97.8 | 0.7 | 96.5 | 98.6 | -0.7 |
| baseten/fp4 | fp4 | 6 | 97.2 | 96.5 | 98.6 | 97.9 | 97.2 | 98.6 | 97.7 | 0.8 | 96.5 | 98.6 | +0.5 |
| crusoe/bf16 | bf16 | 6 | 97.2 | 97.9 | 98.6 | 97.9 | 98.6 | 95.8 | 97.7 | 1.0 | 95.8 | 98.6 | -0.5 |
| deepinfra/bf16 | bf16 | 6 | 97.2 | 97.9 | 97.9 | 97.9 | 97.2 | 97.2 | 97.6 | 0.4 | 97.2 | 97.9 | -0.2 |
| deepinfra/fp8 | fp8 | 3 | - | - | - | 96.9 | 97.7 | 97.0 | 97.2 | 0.4 | 96.9 | 97.7 | +0.0 |
| parasail/fp4 | fp4 | 6 | 95.1 | 97.9 | 97.9 | 98.6 | 95.8 | 97.9 | 97.2 | 1.3 | 95.1 | 98.6 | +0.5 |
| together | unknown | 6 | 97.9 | 97.2 | 97.2 | 97.2 | 97.9 | 95.8 | 97.2 | 0.7 | 95.8 | 97.9 | -0.5 |
| amazon-bedrock | unknown | 6 | 95.8 | 97.9 | 97.9 | 96.5 | 97.9 | 94.4 | 96.7 | 1.3 | 94.4 | 97.9 | -0.9 |
| mara | unknown | 6 | 95.8 | 95.8 | 97.9 | 96.5 | 97.2 | 97.2 | 96.7 | 0.8 | 95.8 | 97.9 | +0.5 |
| cerebras/fp16 | fp16 | 6 | 96.5 | 97.2 | 95.8 | 95.8 | 97.9 | 96.5 | 96.6 | 0.7 | 95.8 | 97.9 | +0.2 |
| groq | unknown | 6 | 97.2 | 96.5 | 97.2 | 95.1 | 97.2 | 96.5 | 96.6 | 0.7 | 95.1 | 97.2 | -0.7 |
| sambanova | unknown | 6 | 95.8 | 95.1 | 97.2 | 96.5 | 97.2 | 97.2 | 96.5 | 0.8 | 95.1 | 97.2 | +0.9 |
| dekallm/bf16 | bf16 | 6 | 96.5 | 95.8 | 95.8 | 94.4 | 97.2 | 97.9 | 96.3 | 1.1 | 94.4 | 97.9 | +0.5 |
| mancer/fp8 | fp8 | 6 | 95.1 | 95.8 | 97.9 | 94.4 | 99.3 | 94.4 | 96.1 | 1.8 | 94.4 | 99.3 | -0.2 |
| amazon-bedrock/eu-west-1 | unknown | 6 | 92.4 | 95.8 | 96.5 | 97.2 | 98.6 | 95.8 | 96.0 | 1.9 | 92.4 | 98.6 | +2.3 |
| nebius/fp4 | fp4 | 6 | 93.8 | 97.2 | 95.8 | 96.5 | 97.9 | 93.1 | 95.7 | 1.7 | 93.1 | 97.9 | +0.2 |
| sail-research/fp4 | fp4 | 6 | 95.6 | 95.1 | 94.4 | 95.8 | 100.0 | 93.1 | 95.7 | 2.1 | 93.1 | 100.0 | +1.3 |
| near-ai/fp4 | fp4 | 6 | 97.2 | 95.1 | 95.8 | 92.4 | 95.8 | 97.2 | 95.6 | 1.6 | 92.4 | 97.2 | -0.9 |
| akashml/bf16 | bf16 | 6 | 95.1 | 96.5 | 95.1 | 95.8 | 95.8 | 93.8 | 95.4 | 0.8 | 93.8 | 96.5 | -0.4 |
| siliconflow/fp8 | fp8 | 6 | 93.1 | 93.1 | 95.0 | 95.8 | 95.7 | 97.2 | 95.0 | 1.5 | 93.1 | 97.2 | +2.5 |
| coreweave/fp4 | fp4 | 6 | 93.8 | 95.8 | 95.8 | 94.4 | 97.2 | 91.7 | 94.8 | 1.8 | 91.7 | 97.2 | -0.7 |
| google-vertex/global | unknown | 6 | 94.4 | 95.1 | 91.0 | 93.8 | 97.2 | 90.9 | 93.7 | 2.2 | 90.9 | 97.2 | +0.5 |
| primeintellect/fp4 | fp4 | 1 | - | - | - | - | - | 93.1 | 93.1 | 0.0 | 93.1 | 93.1 | n/a |
| novita/fp4 | fp4 | 6 | 93.8 | 91.0 | 93.8 | 95.1 | 91.6 | 92.4 | 93.0 | 1.4 | 91.0 | 95.1 | +0.2 |
| phala | unknown | 6 | 90.8 | 91.7 | 92.4 | 93.8 | 95.8 | 92.4 | 92.8 | 1.6 | 90.8 | 95.8 | +2.4 |
| venice/int4 | int4 | 6 | 91.0 | 95.8 | 97.2 | 94.4 | 96.5 | 81.9 | 92.8 | 5.3 | 81.9 | 97.2 | -3.7 |
| digitalocean | unknown | 6 | 94.4 | 91.0 | 90.3 | 92.4 | 90.2 | 88.9 | 91.2 | 1.8 | 88.9 | 94.4 | -1.4 |

### Graded accuracy and self-agreement (sorted by String, then Self-agree)

| Endpoint | Math | JSON | String | Needle | Echo | Self-agree | Pairs | Self-agree Math | JSON | String | Needle | Echo | Self-check 10-27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| siliconflow/fp8 | 98.2 | 100.0 | 88.0 | 99.3 | 99.3 | 94.7 | 584 | 97.5 | 87.4 | 88.4 | 98.0 | 99.0 | 91.7 (12) |
| cerebras/fp16 | 99.6 | 100.0 | 86.8 | 100.0 | 100.0 | 96.5 | 600 | 99.0 | 92.0 | 89.0 | 100.0 | 100.0 | 100.0 (12) |
| baseten/fp4 | 99.6 | 100.0 | 85.4 | 100.0 | 100.0 | 97.3 | 600 | 100.0 | 98.0 | 86.0 | 100.0 | 100.0 | 91.7 (12) |
| deepinfra/bf16 | 100.0 | 100.0 | 84.0 | 99.3 | 100.0 | 97.7 | 596 | 100.0 | 93.8 | 94.0 | 98.0 | 100.0 | 90.0 (10) |
| baseten/fp4/us | 99.6 | 100.0 | 84.0 | 100.0 | 100.0 | 97.0 | 598 | 100.0 | 98.0 | 84.0 | 100.0 | 100.0 | 91.7 (12) |
| digitalocean | 99.6 | 100.0 | 84.0 | 100.0 | 100.0 | 89.0 | 600 | 100.0 | 53.0 | 81.0 | 100.0 | 100.0 | 83.3 (12) |
| deepinfra/fp8 | 100.0 | 100.0 | 83.8 | 100.0 | 100.0 | 96.5 | 202 | 100.0 | 96.8 | 82.4 | 100.0 | 100.0 | - |
| mancer/fp8 | 100.0 | 100.0 | 82.0 | 100.0 | 100.0 | 94.0 | 600 | 100.0 | 81.0 | 83.0 | 100.0 | 100.0 | 83.3 (12) |
| sambanova | 100.0 | 100.0 | 81.9 | 100.0 | 100.0 | 96.0 | 600 | 100.0 | 89.0 | 87.0 | 100.0 | 100.0 | 100.0 (12) |
| mara | 100.0 | 100.0 | 81.7 | 100.0 | 100.0 | 96.5 | 592 | 100.0 | 91.0 | 87.5 | 100.0 | 100.0 | 100.0 (12) |
| near-ai/fp4 | 100.0 | 100.0 | 81.3 | 100.0 | 100.0 | 93.2 | 600 | 100.0 | 78.0 | 81.0 | 100.0 | 100.0 | 91.7 (12) |
| dekallm/bf16 | 99.6 | 100.0 | 81.2 | 100.0 | 100.0 | 95.0 | 600 | 100.0 | 73.0 | 97.0 | 100.0 | 100.0 | 75.0 (12) |
| groq | 100.0 | 100.0 | 80.6 | 100.0 | 100.0 | 98.7 | 600 | 100.0 | 98.0 | 94.0 | 100.0 | 100.0 | 100.0 (12) |
| amazon-bedrock | 100.0 | 100.0 | 80.5 | 100.0 | 100.0 | 95.0 | 600 | 100.0 | 82.0 | 88.0 | 100.0 | 100.0 | 100.0 (12) |
| crusoe/bf16 | 100.0 | 100.0 | 79.9 | 100.0 | 100.0 | 96.3 | 600 | 100.0 | 95.0 | 83.0 | 100.0 | 100.0 | 83.3 (12) |
| akashml/bf16 | 100.0 | 100.0 | 79.9 | 100.0 | 100.0 | 93.5 | 600 | 100.0 | 73.0 | 88.0 | 100.0 | 100.0 | 100.0 (12) |
| venice/int4 | 95.8 | 100.0 | 79.9 | 100.0 | 96.5 | 91.8 | 598 | 94.4 | 82.0 | 84.0 | 100.0 | 96.0 | 90.9 (11) |
| novita/fp4 | 98.6 | 100.0 | 79.9 | 99.3 | 99.3 | 90.7 | 600 | 97.5 | 67.0 | 83.0 | 100.0 | 99.0 | 83.3 (12) |
| google-vertex/global | 93.8 | 99.3 | 79.7 | 100.0 | 98.6 | 93.1 | 597 | 98.0 | 82.0 | 85.0 | 100.0 | 96.0 | 100.0 (12) |
| parasail/fp4 | 100.0 | 100.0 | 78.5 | 100.0 | 100.0 | 95.7 | 598 | 100.0 | 91.0 | 83.0 | 100.0 | 100.0 | 100.0 (8) |
| nebius/fp4 | 100.0 | 100.0 | 78.5 | 100.0 | 100.0 | 94.8 | 600 | 100.0 | 85.0 | 84.0 | 100.0 | 100.0 | 91.7 (12) |
| coreweave/fp4 | 99.6 | 100.0 | 77.1 | 100.0 | 100.0 | 93.6 | 594 | 100.0 | 75.5 | 86.0 | 100.0 | 100.0 | 66.7 (12) |
| phala | 98.9 | 100.0 | 77.1 | 99.3 | 98.6 | 91.6 | 598 | 99.0 | 74.7 | 81.0 | 98.0 | 98.0 | 83.3 (12) |
| together | 100.0 | 100.0 | 75.7 | 100.0 | 100.0 | 97.7 | 600 | 100.0 | 98.0 | 88.0 | 100.0 | 100.0 | 83.3 (12) |
| sail-research/fp4 | 100.0 | 100.0 | 74.5 | 100.0 | 100.0 | 93.5 | 569 | 100.0 | 78.5 | 81.9 | 100.0 | 100.0 | 91.7 (12) |
| amazon-bedrock/eu-west-1 | 100.0 | 100.0 | 74.3 | 100.0 | 100.0 | 95.2 | 600 | 100.0 | 87.0 | 84.0 | 100.0 | 100.0 | 91.7 (12) |
| primeintellect/fp4 | 100.0 | 100.0 | 70.8 | 100.0 | 100.0 | n/a | 0 | n/a | n/a | n/a | n/a | n/a | - |

### Noise floor by family (night-to-night)

| Family | Endpoints | Median self-agree | P75 disagreement | Noise floor | Stable |
|---|---|---|---|---|---|
| math | 26 | 100.0 | 0.0 | 100.0 | yes |
| json | 26 | 86.0 | 21.9 | 78.1 | no |
| string | 26 | 84.5 | 17.0 | 83.0 | no |
| needle | 26 | 100.0 | 0.0 | 100.0 | yes |
| echo | 26 | 100.0 | 0.0 | 100.0 | yes |

Reference rule(s) seen: plurality among endpoints declaring bf16 or fp16.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

### Exact match by night

| Endpoint | Declared quant | Nights | 10-27 | 10-28 | 10-29 | 10-30 | 10-31 | 11-01 | Mean | SD | Min | Max | Movement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba/fp8/us-east-1 | fp8 | 6 | 80.3 | 80.3 | 77.3 | 81.1 | 81.2 | 87.6 | 81.3 | 3.1 | 77.3 | 87.6 | +4.0 |
| alibaba/fp8 | fp8 | 6 | 82.3 | 75.0 | 78.0 | 81.8 | 80.5 | 86.1 | 80.6 | 3.5 | 75.0 | 86.1 | +4.4 |
| streamlake/fp8 | fp8 | 6 | 86.2 | 78.0 | 79.5 | 78.8 | 78.9 | 74.5 | 79.3 | 3.5 | 74.5 | 86.2 | -3.8 |
| atlas-cloud/fp4 | fp4 | 6 | 78.7 | 78.0 | 72.7 | 78.8 | 76.7 | 72.3 | 76.2 | 2.7 | 72.3 | 78.8 | -0.5 |
| venice | unknown | 6 | 80.2 | 72.7 | 75.0 | 68.9 | 80.5 | 76.6 | 75.6 | 4.1 | 68.9 | 80.5 | -0.6 |
| deepinfra/fp8 | fp8 | 6 | 71.5 | 76.5 | 72.7 | 77.3 | 73.7 | 78.8 | 75.1 | 2.6 | 71.5 | 78.8 | +3.0 |
| relace/fp4 | fp4 | 6 | 78.5 | 78.6 | 74.0 | 74.8 | 71.4 | 70.1 | 74.6 | 3.2 | 70.1 | 78.6 | -4.9 |
| siliconflow/fp8 | fp8 | 6 | 73.0 | 71.2 | 69.7 | 68.9 | 70.7 | 68.6 | 70.4 | 1.5 | 68.6 | 73.0 | -1.9 |
| baidu/fp8 | fp8 | 6 | 75.4 | 68.9 | 75.0 | 53.8 | 51.9 | 81.0 | 67.7 | 11.1 | 51.9 | 81.0 | -10.9 * |
| azure/us | unknown | 6 | 53.9 | 59.5 | 57.6 | 53.0 | 58.6 | 59.9 | 57.1 | 2.7 | 53.0 | 59.9 | +0.2 |
| digitalocean | unknown | 6 | 58.5 | 55.3 | 58.3 | 59.1 | 57.1 | 51.8 | 56.7 | 2.5 | 51.8 | 59.1 | -1.4 |
| crusoe/fp8 | fp8 | 6 | 50.4 | 50.0 | 50.0 | 53.4 | 57.9 | 49.6 | 51.9 | 3.0 | 49.6 | 57.9 | +3.5 |
| gmicloud/fp8 | fp8 | 6 | 44.6 | 47.7 | 48.5 | 53.8 | 54.1 | 48.2 | 49.5 | 3.4 | 44.6 | 54.1 | +5.1 |
| novita/fp8 | fp8 | 6 | 47.2 | 48.5 | 49.2 | 50.8 | 53.4 | 46.7 | 49.3 | 2.3 | 46.7 | 53.4 | +2.0 |
| cloudflare | unknown | 6 | 45.4 | 44.7 | 49.5 | 48.5 | 50.4 | 43.1 | 46.9 | 2.7 | 43.1 | 50.4 | +0.8 |

### Graded accuracy and self-agreement (sorted by String, then Self-agree)

| Endpoint | Math | JSON | String | Needle | Echo | Self-agree | Pairs | Self-agree Math | JSON | String | Needle | Echo | Self-check 10-27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8 | 100.0 | 100.0 | 63.9 | 99.3 | 95.1 | 65.8 | 600 | 32.0 | 65.0 | 74.0 | 99.0 | 93.0 | 66.7 (12) |
| relace/fp4 | 100.0 | 100.0 | 63.7 | 100.0 | 96.5 | 66.2 | 594 | 26.8 | 68.0 | 76.5 | 100.0 | 99.0 | 83.3 (12) |
| streamlake/fp8 | 100.0 | 100.0 | 62.5 | 100.0 | 96.5 | 68.0 | 600 | 34.5 | 68.0 | 73.0 | 100.0 | 98.0 | 75.0 (12) |
| venice | 100.0 | 100.0 | 61.8 | 99.3 | 97.9 | 65.1 | 596 | 31.8 | 62.6 | 69.0 | 99.0 | 96.0 | 66.7 (12) |
| alibaba/fp8/us-east-1 | 100.0 | 100.0 | 61.1 | 100.0 | 95.1 | 73.3 | 596 | 42.9 | 75.0 | 79.0 | 100.0 | 100.0 | 83.3 (12) |
| alibaba/fp8 | 100.0 | 100.0 | 59.7 | 100.0 | 95.1 | 70.2 | 600 | 37.0 | 71.0 | 76.0 | 100.0 | 100.0 | 75.0 (12) |
| atlas-cloud/fp4 | 100.0 | 100.0 | 59.7 | 100.0 | 100.0 | 69.2 | 597 | 35.2 | 68.4 | 76.0 | 100.0 | 100.0 | 58.3 (12) |
| siliconflow/fp8 | 100.0 | 100.0 | 59.7 | 100.0 | 97.2 | 65.8 | 597 | 31.2 | 66.0 | 69.0 | 100.0 | 98.0 | 66.7 (12) |
| azure/us | 99.0 | 100.0 | 54.6 | 100.0 | 94.9 | 51.2 | 572 | 0.0 | 58.3 | 53.1 | 100.0 | 94.7 | 20.0 (10) |
| digitalocean | 99.6 | 100.0 | 51.4 | 100.0 | 95.8 | 50.7 | 600 | 0.0 | 57.0 | 52.0 | 100.0 | 95.0 | 50.0 (12) |
| baidu/fp8 | 98.9 | 100.0 | 45.4 | 100.0 | 96.5 | 54.7 | 592 | 22.4 | 35.0 | 48.0 | 100.0 | 98.0 | 100.0 (12) |
| crusoe/fp8 | 99.6 | 100.0 | 31.7 | 100.0 | 100.0 | 78.9 | 592 | 53.8 | 86.7 | 79.6 | 100.0 | 100.0 | 83.3 (12) |
| gmicloud/fp8 | 97.9 | 100.0 | 30.6 | 100.0 | 100.0 | 68.5 | 600 | 36.0 | 75.0 | 64.0 | 100.0 | 100.0 | 75.0 (12) |
| novita/fp8 | 95.5 | 100.0 | 30.5 | 100.0 | 100.0 | 73.2 | 597 | 43.2 | 80.0 | 73.0 | 100.0 | 100.0 | 66.7 (12) |
| cloudflare | 93.3 | 100.0 | 21.3 | 100.0 | 100.0 | 78.3 | 600 | 50.0 | 98.0 | 72.0 | 100.0 | 100.0 | 75.0 (12) |

### Noise floor by family (night-to-night)

| Family | Endpoints | Median self-agree | P75 disagreement | Noise floor | Stable |
|---|---|---|---|---|---|
| math | 15 | 34.5 | 71.0 | 29.0 | no |
| json | 15 | 68.0 | 36.2 | 63.8 | no |
| string | 15 | 73.0 | 33.5 | 66.5 | no |
| needle | 15 | 100.0 | 0.0 | 100.0 | yes |
| echo | 15 | 99.0 | 3.0 | 97.0 | yes |

Reference rule(s) seen: plurality across all endpoints (fewer than two declare bf16 or fp16).

## Footer

- Nights found: 6. Self-check nights found: 1 (2026-10-27).
- Self-agree: for each pair of consecutive nights the endpoint was listed, each fixed prompt with an ok row on both nights counts once, and agrees when the stripped outputs are equal word for word. Fresh prompts are excluded because they change nightly. Pairs is the count of such prompt-night pairs.
- Movement: mean exact % over the last 3 nights minus the mean over the first 3; when fewer than 6 nights are present the two windows overlap. An asterisk marks an absolute movement at or above 10 points on at least 4 nights. Provisional; calibrate on 2026-11-10.
- Noise floor per family: 100 minus the 75th percentile across endpoints of night-to-night disagreement. Stable means the median endpoint self-agreement is at or above 95. Provisional; calibrate on 2026-11-10.
- Self-check: two passes of the same fixed prompts one hour apart on the nights listed; the figure is the share of prompts whose two outputs were equal, with the prompt count in brackets.
- Declared quant is the latest night's declaration; (changed) means it differed on some night in the range.
- Numbers against a stated reference. Not a claim about intent.
