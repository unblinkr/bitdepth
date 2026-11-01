# Bitdepth trend through 2026-10-31

Nights found: 5 (2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31). Self-check nights: 2026-10-27.
Each row is one OpenRouter endpoint across every night it was listed. Exact % per night is the nightly scorecard figure (match against that night's reference). Family columns are mean graded accuracy against the generated answers. Self-agree is the endpoint's night-to-night agreement with itself on the fixed prompts. Self-check columns are the one-hour two-pass agreement on the nights it was measured. All numbers are percentages unless the column says otherwise.

## gpt-oss-120b (`openai/gpt-oss-120b`)

### Exact match by night

| Endpoint | Declared quant | Nights | 10-27 | 10-28 | 10-29 | 10-30 | 10-31 | Mean | SD | Min | Max | Movement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crusoe/bf16 | bf16 | 5 | 97.2 | 97.9 | 98.6 | 97.9 | 98.6 | 98.0 | 0.5 | 97.2 | 98.6 | +0.5 |
| baseten/fp4/us | fp4 | 5 | 97.9 | 98.6 | 97.9 | 97.2 | 96.5 | 97.6 | 0.7 | 96.5 | 98.6 | -0.9 |
| deepinfra/bf16 | bf16 | 5 | 97.2 | 97.9 | 97.9 | 97.9 | 97.2 | 97.6 | 0.3 | 97.2 | 97.9 | +0.0 |
| baseten/fp4 | fp4 | 5 | 97.2 | 96.5 | 98.6 | 97.9 | 97.2 | 97.5 | 0.7 | 96.5 | 98.6 | +0.5 |
| together | unknown | 5 | 97.9 | 97.2 | 97.2 | 97.2 | 97.9 | 97.5 | 0.3 | 97.2 | 97.9 | +0.0 |
| deepinfra/fp8 | fp8 | 2 | - | - | - | 96.9 | 97.7 | 97.3 | 0.4 | 96.9 | 97.7 | +0.0 |
| amazon-bedrock | unknown | 5 | 95.8 | 97.9 | 97.9 | 96.5 | 97.9 | 97.2 | 0.9 | 95.8 | 97.9 | +0.2 |
| parasail/fp4 | fp4 | 5 | 95.1 | 97.9 | 97.9 | 98.6 | 95.8 | 97.1 | 1.4 | 95.1 | 98.6 | +0.5 |
| cerebras/fp16 | fp16 | 5 | 96.5 | 97.2 | 95.8 | 95.8 | 97.9 | 96.6 | 0.8 | 95.8 | 97.9 | +0.0 |
| groq | unknown | 5 | 97.2 | 96.5 | 97.2 | 95.1 | 97.2 | 96.6 | 0.8 | 95.1 | 97.2 | -0.5 |
| mara | unknown | 5 | 95.8 | 95.8 | 97.9 | 96.5 | 97.2 | 96.6 | 0.8 | 95.8 | 97.9 | +0.7 |
| mancer/fp8 | fp8 | 5 | 95.1 | 95.8 | 97.9 | 94.4 | 99.3 | 96.5 | 1.8 | 94.4 | 99.3 | +0.9 |
| sambanova | unknown | 5 | 95.8 | 95.1 | 97.2 | 96.5 | 97.2 | 96.4 | 0.8 | 95.1 | 97.2 | +0.9 |
| nebius/fp4 | fp4 | 5 | 93.8 | 97.2 | 95.8 | 96.5 | 97.9 | 96.2 | 1.4 | 93.8 | 97.9 | +1.1 |
| sail-research/fp4 | fp4 | 5 | 95.6 | 95.1 | 94.4 | 95.8 | 100.0 | 96.2 | 2.0 | 94.4 | 100.0 | +1.7 |
| amazon-bedrock/eu-west-1 | unknown | 5 | 92.4 | 95.8 | 96.5 | 97.2 | 98.6 | 96.1 | 2.1 | 92.4 | 98.6 | +2.5 |
| dekallm/bf16 | bf16 | 5 | 96.5 | 95.8 | 95.8 | 94.4 | 97.2 | 95.9 | 0.9 | 94.4 | 97.2 | -0.2 |
| akashml/bf16 | bf16 | 5 | 95.1 | 96.5 | 95.1 | 95.8 | 95.8 | 95.7 | 0.5 | 95.1 | 96.5 | +0.0 |
| coreweave/fp4 | fp4 | 5 | 93.8 | 95.8 | 95.8 | 94.4 | 97.2 | 95.4 | 1.2 | 93.8 | 97.2 | +0.7 |
| near-ai/fp4 | fp4 | 5 | 97.2 | 95.1 | 95.8 | 92.4 | 95.8 | 95.3 | 1.6 | 92.4 | 97.2 | -1.4 |
| venice/int4 | int4 | 5 | 91.0 | 95.8 | 97.2 | 94.4 | 96.5 | 95.0 | 2.2 | 91.0 | 97.2 | +1.4 |
| siliconflow/fp8 | fp8 | 5 | 93.1 | 93.1 | 95.0 | 95.8 | 95.7 | 94.5 | 1.2 | 93.1 | 95.8 | +1.8 |
| google-vertex/global | unknown | 5 | 94.4 | 95.1 | 91.0 | 93.8 | 97.2 | 94.3 | 2.0 | 91.0 | 97.2 | +0.5 |
| novita/fp4 | fp4 | 5 | 93.8 | 91.0 | 93.8 | 95.1 | 91.6 | 93.1 | 1.5 | 91.0 | 95.1 | +0.6 |
| phala | unknown | 5 | 90.8 | 91.7 | 92.4 | 93.8 | 95.8 | 92.9 | 1.8 | 90.8 | 95.8 | +2.4 |
| digitalocean | unknown | 5 | 94.4 | 91.0 | 90.3 | 92.4 | 90.2 | 91.7 | 1.6 | 90.2 | 94.4 | -0.9 |

### Graded accuracy and self-agreement (sorted by String, then Self-agree)

| Endpoint | Math | JSON | String | Needle | Echo | Self-agree | Pairs | Self-agree Math | JSON | String | Needle | Echo | Self-check 10-27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| siliconflow/fp8 | 97.9 | 100.0 | 89.9 | 99.2 | 100.0 | 95.1 | 470 | 97.5 | 89.6 | 88.3 | 97.5 | 100.0 | 91.7 (12) |
| cerebras/fp16 | 99.6 | 100.0 | 87.5 | 100.0 | 100.0 | 95.6 | 480 | 98.8 | 90.0 | 86.2 | 100.0 | 100.0 | 100.0 (12) |
| baseten/fp4 | 99.6 | 100.0 | 86.7 | 100.0 | 100.0 | 97.1 | 480 | 100.0 | 97.5 | 85.0 | 100.0 | 100.0 | 91.7 (12) |
| deepinfra/bf16 | 100.0 | 100.0 | 85.8 | 99.2 | 100.0 | 97.3 | 476 | 100.0 | 92.1 | 93.8 | 97.5 | 100.0 | 90.0 (10) |
| baseten/fp4/us | 99.6 | 100.0 | 85.0 | 100.0 | 100.0 | 96.9 | 478 | 100.0 | 98.8 | 82.5 | 100.0 | 100.0 | 91.7 (12) |
| deepinfra/fp8 | 100.0 | 100.0 | 84.1 | 100.0 | 100.0 | 96.0 | 99 | 100.0 | 93.8 | 81.2 | 100.0 | 100.0 | - |
| mancer/fp8 | 100.0 | 100.0 | 83.3 | 100.0 | 100.0 | 93.8 | 480 | 100.0 | 81.2 | 81.2 | 100.0 | 100.0 | 83.3 (12) |
| digitalocean | 99.6 | 100.0 | 83.3 | 100.0 | 100.0 | 89.4 | 480 | 100.0 | 53.8 | 82.5 | 100.0 | 100.0 | 83.3 (12) |
| dekallm/bf16 | 99.6 | 100.0 | 82.5 | 100.0 | 100.0 | 94.6 | 480 | 100.0 | 70.0 | 97.5 | 100.0 | 100.0 | 75.0 (12) |
| sambanova | 100.0 | 100.0 | 81.7 | 100.0 | 100.0 | 95.6 | 480 | 100.0 | 86.2 | 87.5 | 100.0 | 100.0 | 100.0 (12) |
| near-ai/fp4 | 100.0 | 100.0 | 81.7 | 100.0 | 100.0 | 92.7 | 480 | 100.0 | 77.5 | 78.8 | 100.0 | 100.0 | 91.7 (12) |
| mara | 100.0 | 100.0 | 81.4 | 100.0 | 100.0 | 96.2 | 472 | 100.0 | 88.8 | 88.2 | 100.0 | 100.0 | 100.0 (12) |
| groq | 100.0 | 100.0 | 80.8 | 100.0 | 100.0 | 98.8 | 480 | 100.0 | 97.5 | 95.0 | 100.0 | 100.0 | 100.0 (12) |
| crusoe/bf16 | 100.0 | 100.0 | 80.8 | 100.0 | 100.0 | 96.2 | 480 | 100.0 | 95.0 | 82.5 | 100.0 | 100.0 | 83.3 (12) |
| amazon-bedrock | 100.0 | 100.0 | 80.8 | 100.0 | 100.0 | 95.4 | 480 | 100.0 | 82.5 | 90.0 | 100.0 | 100.0 | 100.0 (12) |
| venice/int4 | 98.7 | 100.0 | 80.8 | 100.0 | 100.0 | 94.1 | 478 | 98.1 | 85.0 | 83.8 | 100.0 | 100.0 | 90.9 (11) |
| google-vertex/global | 93.7 | 99.2 | 80.8 | 100.0 | 98.3 | 93.5 | 478 | 97.5 | 86.2 | 85.0 | 100.0 | 95.0 | 100.0 (12) |
| akashml/bf16 | 100.0 | 100.0 | 80.8 | 100.0 | 100.0 | 93.3 | 480 | 100.0 | 72.5 | 87.5 | 100.0 | 100.0 | 100.0 (12) |
| novita/fp4 | 98.7 | 100.0 | 80.8 | 100.0 | 100.0 | 90.8 | 480 | 97.5 | 66.2 | 83.8 | 100.0 | 100.0 | 83.3 (12) |
| nebius/fp4 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 95.8 | 480 | 100.0 | 90.0 | 85.0 | 100.0 | 100.0 | 91.7 (12) |
| parasail/fp4 | 100.0 | 100.0 | 79.2 | 100.0 | 100.0 | 95.8 | 478 | 100.0 | 91.2 | 83.8 | 100.0 | 100.0 | 100.0 (8) |
| phala | 98.7 | 100.0 | 78.3 | 99.2 | 100.0 | 91.4 | 478 | 99.4 | 69.6 | 82.5 | 97.5 | 100.0 | 83.3 (12) |
| coreweave/fp4 | 99.6 | 100.0 | 77.5 | 100.0 | 100.0 | 93.9 | 475 | 100.0 | 77.2 | 86.2 | 100.0 | 100.0 | 66.7 (12) |
| sail-research/fp4 | 100.0 | 100.0 | 76.1 | 100.0 | 100.0 | 93.5 | 449 | 100.0 | 78.1 | 82.4 | 100.0 | 100.0 | 91.7 (12) |
| together | 100.0 | 100.0 | 75.0 | 100.0 | 100.0 | 97.9 | 480 | 100.0 | 97.5 | 90.0 | 100.0 | 100.0 | 83.3 (12) |
| amazon-bedrock/eu-west-1 | 100.0 | 100.0 | 74.2 | 100.0 | 100.0 | 95.2 | 480 | 100.0 | 87.5 | 83.8 | 100.0 | 100.0 | 91.7 (12) |

### Noise floor by family (night-to-night)

| Family | Endpoints | Median self-agree | P75 disagreement | Noise floor | Stable |
|---|---|---|---|---|---|
| math | 26 | 100.0 | 0.0 | 100.0 | yes |
| json | 26 | 86.8 | 22.4 | 77.6 | no |
| string | 26 | 85.0 | 17.5 | 82.5 | no |
| needle | 26 | 100.0 | 0.0 | 100.0 | yes |
| echo | 26 | 100.0 | 0.0 | 100.0 | yes |

Reference rule(s) seen: plurality among endpoints declaring bf16 or fp16.

## deepseek-v4-pro (`deepseek/deepseek-v4-pro`)

### Exact match by night

| Endpoint | Declared quant | Nights | 10-27 | 10-28 | 10-29 | 10-30 | 10-31 | Mean | SD | Min | Max | Movement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| streamlake/fp8 | fp8 | 5 | 86.2 | 78.0 | 79.5 | 78.8 | 78.9 | 80.3 | 3.0 | 78.0 | 86.2 | -2.2 |
| alibaba/fp8/us-east-1 | fp8 | 5 | 80.3 | 80.3 | 77.3 | 81.1 | 81.2 | 80.0 | 1.4 | 77.3 | 81.2 | +0.6 |
| alibaba/fp8 | fp8 | 5 | 82.3 | 75.0 | 78.0 | 81.8 | 80.5 | 79.5 | 2.7 | 75.0 | 82.3 | +1.7 |
| atlas-cloud/fp4 | fp4 | 5 | 78.7 | 78.0 | 72.7 | 78.8 | 76.7 | 77.0 | 2.3 | 72.7 | 78.8 | -0.4 |
| relace/fp4 | fp4 | 5 | 78.5 | 78.6 | 74.0 | 74.8 | 71.4 | 75.5 | 2.8 | 71.4 | 78.6 | -3.6 |
| venice | unknown | 5 | 80.2 | 72.7 | 75.0 | 68.9 | 80.5 | 75.5 | 4.4 | 68.9 | 80.5 | -1.2 |
| deepinfra/fp8 | fp8 | 5 | 71.5 | 76.5 | 72.7 | 77.3 | 73.7 | 74.3 | 2.2 | 71.5 | 77.3 | +1.0 |
| siliconflow/fp8 | fp8 | 5 | 73.0 | 71.2 | 69.7 | 68.9 | 70.7 | 70.7 | 1.4 | 68.9 | 73.0 | -1.5 |
| baidu/fp8 | fp8 | 5 | 75.4 | 68.9 | 75.0 | 53.8 | 51.9 | 65.0 | 10.2 | 51.9 | 75.4 | -12.9 * |
| digitalocean | unknown | 5 | 58.5 | 55.3 | 58.3 | 59.1 | 57.1 | 57.7 | 1.3 | 55.3 | 59.1 | +0.8 |
| azure/us | unknown | 5 | 53.9 | 59.5 | 57.6 | 53.0 | 58.6 | 56.5 | 2.6 | 53.0 | 59.5 | -0.6 |
| crusoe/fp8 | fp8 | 5 | 50.4 | 50.0 | 50.0 | 53.4 | 57.9 | 52.3 | 3.1 | 50.0 | 57.9 | +3.6 |
| novita/fp8 | fp8 | 5 | 47.2 | 48.5 | 49.2 | 50.8 | 53.4 | 49.8 | 2.1 | 47.2 | 53.4 | +2.8 |
| gmicloud/fp8 | fp8 | 5 | 44.6 | 47.7 | 48.5 | 53.8 | 54.1 | 49.7 | 3.7 | 44.6 | 54.1 | +5.2 |
| cloudflare | unknown | 5 | 45.4 | 44.7 | 49.5 | 48.5 | 50.4 | 47.7 | 2.3 | 44.7 | 50.4 | +2.9 |

### Graded accuracy and self-agreement (sorted by String, then Self-agree)

| Endpoint | Math | JSON | String | Needle | Echo | Self-agree | Pairs | Self-agree Math | JSON | String | Needle | Echo | Self-check 10-27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepinfra/fp8 | 100.0 | 100.0 | 64.2 | 100.0 | 95.0 | 66.0 | 480 | 30.6 | 67.5 | 75.0 | 100.0 | 92.5 | 66.7 (12) |
| relace/fp4 | 100.0 | 100.0 | 63.1 | 100.0 | 96.6 | 67.1 | 474 | 27.2 | 71.2 | 78.2 | 100.0 | 98.8 | 83.3 (12) |
| alibaba/fp8/us-east-1 | 100.0 | 100.0 | 60.8 | 100.0 | 95.0 | 70.0 | 476 | 34.2 | 76.2 | 75.0 | 100.0 | 100.0 | 83.3 (12) |
| venice | 100.0 | 100.0 | 60.0 | 100.0 | 98.3 | 63.4 | 476 | 28.5 | 59.5 | 67.5 | 100.0 | 96.2 | 66.7 (12) |
| atlas-cloud/fp4 | 100.0 | 100.0 | 59.2 | 100.0 | 100.0 | 69.4 | 477 | 34.0 | 71.8 | 76.2 | 100.0 | 100.0 | 58.3 (12) |
| streamlake/fp8 | 100.0 | 100.0 | 59.2 | 100.0 | 96.6 | 68.3 | 480 | 34.4 | 68.8 | 75.0 | 100.0 | 97.5 | 75.0 (12) |
| alibaba/fp8 | 100.0 | 100.0 | 59.2 | 100.0 | 95.0 | 67.3 | 480 | 30.0 | 72.5 | 71.2 | 100.0 | 100.0 | 75.0 (12) |
| siliconflow/fp8 | 100.0 | 100.0 | 59.2 | 100.0 | 97.5 | 66.0 | 477 | 32.1 | 66.2 | 67.5 | 100.0 | 98.7 | 66.7 (12) |
| azure/us | 99.2 | 100.0 | 53.8 | 100.0 | 94.7 | 50.7 | 452 | 0.0 | 55.3 | 52.6 | 100.0 | 94.6 | 20.0 (10) |
| digitalocean | 99.6 | 100.0 | 52.5 | 100.0 | 95.8 | 50.6 | 480 | 0.0 | 56.2 | 52.5 | 100.0 | 95.0 | 50.0 (12) |
| baidu/fp8 | 98.7 | 100.0 | 42.0 | 100.0 | 96.6 | 57.8 | 472 | 27.0 | 40.0 | 51.2 | 100.0 | 98.8 | 100.0 (12) |
| crusoe/fp8 | 99.6 | 100.0 | 30.5 | 100.0 | 100.0 | 79.4 | 472 | 56.0 | 85.9 | 79.5 | 100.0 | 100.0 | 83.3 (12) |
| gmicloud/fp8 | 98.7 | 100.0 | 29.2 | 100.0 | 100.0 | 68.1 | 480 | 34.4 | 75.0 | 65.0 | 100.0 | 100.0 | 75.0 (12) |
| novita/fp8 | 96.2 | 100.0 | 29.1 | 100.0 | 100.0 | 73.8 | 477 | 43.4 | 80.0 | 76.2 | 100.0 | 100.0 | 66.7 (12) |
| cloudflare | 93.2 | 100.0 | 21.4 | 100.0 | 100.0 | 79.6 | 480 | 52.5 | 98.8 | 73.8 | 100.0 | 100.0 | 75.0 (12) |

### Noise floor by family (night-to-night)

| Family | Endpoints | Median self-agree | P75 disagreement | Noise floor | Stable |
|---|---|---|---|---|---|
| math | 15 | 32.1 | 72.2 | 27.8 | no |
| json | 15 | 71.2 | 37.1 | 62.9 | no |
| string | 15 | 73.8 | 33.8 | 66.2 | no |
| needle | 15 | 100.0 | 0.0 | 100.0 | yes |
| echo | 15 | 98.8 | 3.1 | 96.9 | yes |

Reference rule(s) seen: plurality across all endpoints (fewer than two declare bf16 or fp16).

## Footer

- Nights found: 5. Self-check nights found: 1 (2026-10-27).
- Self-agree: for each pair of consecutive nights the endpoint was listed, each fixed prompt with an ok row on both nights counts once, and agrees when the stripped outputs are equal word for word. Fresh prompts are excluded because they change nightly. Pairs is the count of such prompt-night pairs.
- Movement: mean exact % over the last 3 nights minus the mean over the first 3; when fewer than 6 nights are present the two windows overlap. An asterisk marks an absolute movement at or above 10 points on at least 4 nights. Provisional; calibrate on 2026-11-10.
- Noise floor per family: 100 minus the 75th percentile across endpoints of night-to-night disagreement. Stable means the median endpoint self-agreement is at or above 95. Provisional; calibrate on 2026-11-10.
- Self-check: two passes of the same fixed prompts one hour apart on the nights listed; the figure is the share of prompts whose two outputs were equal, with the prompt count in brackets.
- Declared quant is the latest night's declaration; (changed) means it differed on some night in the range.
- Numbers against a stated reference. Not a claim about intent.
