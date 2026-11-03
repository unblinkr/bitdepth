# Bitdepth Endpoint Probe

Probe one LLM inference endpoint and see whether it serves the model the way every other endpoint does.

The same open-weight model is served by dozens of providers at different precisions and prices. This actor sends Bitdepth's fixed prompt set to the endpoint you name, at temperature 0, and grades every answer against the reference Bitdepth publishes each night for that model. You get the endpoint's scores beside last night's field of endpoints serving the same model.

## What you can probe

- **An OpenRouter endpoint.** Give the model and the endpoint tag (for example `deepinfra/fp8`). The probe is pinned to that endpoint with fallbacks off and runs on Bitdepth's OpenRouter key. You need no OpenRouter account.
- **Your own endpoint.** Give an https OpenAI-compatible base URL, the model name your server expects and an API key if it needs one. Use it to check a quantized or self-hosted deployment against the reference before you ship it.

Models with a nightly reference today: `openai/gpt-oss-120b`, `deepseek/deepseek-v4-pro`.

## What you get

One record (dataset item and `OUTPUT`), schema `bitdepth.probe.v1`:

- `result`: exact match against the reference, per-family scores (math, JSON, string, long-context needle, echo), error rate, misroutes, truncations, median latency.
- `against_last_night`: for each column, your score, its rank among last night's endpoints, last night's median, and the lowest score among endpoints inside the noise floor. `at_or_above_lowest_within` checks the model's primary columns.
- `last_night_row`: the endpoint's own nightly row, when it is an OpenRouter endpoint Bitdepth already grades.
- `reference`: the night, the reference rule and the prompt count, so the comparison can be checked.

Method: https://bitdepth.dev/method

## Pricing

One charge per completed probe. A probe is not charged when the input is refused or fewer than half the prompts get an answer.

## Notes

- Fixed prompts only, graded with the same code as the nightly run against that night's reference.
- Self-agreement needs several nights, so a single probe does not compute it. For models whose primary columns include it, `not_checked` says so.
- Your API key is sent only to your base URL for the length of the run. It is never written to the output or the log.

Numbers against a stated reference. Not a claim about intent.

Monthly attestation for resellers, gateways and providers: hello@bitdepth.dev
