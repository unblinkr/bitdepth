# QUESTIONS for probe-harness

Decisions taken in the session because the brief could not be built exactly as written. Each one is reversible. None changes a hard rule.

## 1. GLM-5.2 replaced by DeepSeek V4 Pro (brief section 3, models)

GLM-5.2 (`z-ai/glm-5.2`) has 34 endpoints on OpenRouter on Oct 27, 2026, and several charge $7 to $8 per million output tokens. With the brief's estimate (every prompt to every endpoint) GLM-5.2 alone comes to about $13 a night, and still about $9 after dropping needle and fresh prompts, so every night would abort under the $5 cap. The brief's own fallback model, DeepSeek V4 Pro (`deepseek/deepseek-v4-pro`), has 15 endpoints and fits: the full 144-prompt set across both models estimates at $3.38 a night. DeepSeek V4 Pro is also in Artificial Analysis's Endpoint Accuracy Index v1.0, so the positive-control argument holds. GLM-5.2 can be added later on a higher cap if the founder wants it.

## 2. Estimate formula uses expected output tokens per family, not a flat 512

The brief's formula (512 output tokens for every prompt) over-estimates by about eight times for short-answer families and would have forced the model swap above even for cheaper models. The estimate now uses expected output tokens per family (math 96, string 64, needle 64, echo 256, json 320), with input still estimated as characters divided by four. The $5 cap is also enforced at run time from billed cost (`usage.cost` from OpenRouter per response), so the hard rule holds whatever the estimate says: once billed spend reaches $5.00 the remaining rows are written as `skipped_budget` and nothing more is sent.

## 3. Reasoning is turned off where the endpoint allows it

Both models are reasoning models. Reasoning tokens are billed as output and count toward `max_tokens` on most providers, so with `max_tokens: 512` a thinking budget could consume the whole answer. Each request is sent with `reasoning: {"enabled": false}`; if an endpoint rejects the parameter the request is retried with `{"effort": "low"}`, then without it. The mode used is recorded per row. Rows that stop at `max_tokens` are counted as truncated on the scorecard. This is the first thing to look at on the night-one scorecard.

## 4. Night one runs in GitHub Actions, not in the session

The session cannot read the repository secret (the proxy blocks that path), so night one is started by `workflow_dispatch` with `selfcheck=true` and runs with the secret in Actions. The run record carries `source: dispatch`. The one-hour self-check wait happens inside the job.

## 5. Misroute detection is at provider level

The chat completion response names the serving provider, not the endpoint variant. A row is `misrouted` when the returned provider differs from the pinned endpoint's provider. Two variants of the same provider (for example `baseten/fp4` and `baseten/fp4/us`) cannot be told apart from the response alone.

## 6. Fewer than six endpoints

If a configured model ever lists fewer than six endpoints, the run records `short: true` for it and probes it anyway rather than substituting a third model.
