# REPORT: route-list

Run 2026-11-09 from the claude.ai session. Phase 1 only, at Mancy's request. No code changed. Phase 2 waits for her go.

## Phase 1 findings

### 1. The critical question: can a route list name a single endpoint? Yes.

OpenRouter's provider selection page says `order`, `only` and `ignore` take endpoint slugs, not just provider slugs, in the shape `provider[/variant][/region][/tier]`, with examples such as `deepinfra/turbo`, `google-vertex/us-east5` and `baseten/fp4/us`. A base slug like `deepinfra` matches every endpoint of that provider. Source: https://openrouter.ai/docs/guides/routing/provider-selection.md

Our own data proves it in practice. `probe/openrouter.py` already pins every probe request with `"provider": {"order": [tag], "allow_fallbacks": false}`, using the `tag` field from OpenRouter's endpoints API (for example `primeintellect/fp4`, `near-ai/fp4`, `venice/int4`). Across 13 nights, 112,752 pinned requests, `misrouted` is 0: every successful answer came from the endpoint we named.

So the tags Bitdepth already publishes are exactly the strings a developer puts in `provider.only`. The route list can be per endpoint, as designed. A provider with a good fp8 endpoint and a bad fp4 one can be split.

### 2. Fields the `provider` object accepts today

`order`, `only`, `ignore` (endpoint or provider slugs), `allow_fallbacks` (default true), `require_parameters`, `data_collection`, `zdr`, `enforce_distillable_text`, `quantizations`, `sort` (price, throughput, latency, or an object), `preferred_min_throughput`, `preferred_max_latency`, `max_price`. Quantization values: int4, int8, fp4, mxfp4, nvfp4, fp6, fp8, mxfp8, fp16, bf16, fp32, unknown. Same source.

`quantizations` filters on what the provider declares. That is the claim Bitdepth checks, so the route list does not rely on it. It names endpoints directly.

### 3. What happens when every listed endpoint is down

When a pinned endpoint is unavailable with fallbacks off, the request fails. In our runs this shows up as `http 404: No endpoints found for <model>` (720 rows across 13 nights) next to ordinary provider 429 and 503 errors. A one-endpoint list would break apps.

Design change: the list should never be a single pin. The free block should be `{"only": [every endpoint inside the floor], "sort": "price"}` with fallbacks left on. Fallbacks then move only among the allowed endpoints, never outside them. Phase 2 must confirm that behavior with one real request.

### 4. Account settings versus per-request settings

Account-wide allowed providers act as a ceiling; a request's `only` narrows inside it. If the two do not overlap, the request fails with a 404. Account-wide ignored providers are merged with the request's `ignore`. Same source.

So "three places that don't talk" (u/generic-d-engineer) is real: account allow list, account ignore list, per-request settings, plus presets. The api-access copy must warn that an account-wide allow list can block the route list.

### 5. Presets

Presets can carry provider routing rules. They are referenced as `"model": "@preset/name"`, `"preset": "@preset/name"`, or `model@preset/name`. They can be created and updated by API (`POST /api/v1/presets/{slug}/chat/completions` with the account's own key); a new version becomes active. Request fields override preset fields in a shallow merge, so a `provider` block in the request likely replaces the preset's whole `provider` block. Source: https://openrouter.ai/docs/guides/features/presets.md

This is the cleanest "set it and forget it" path for a customer: a tiny script on their side pulls the route list nightly and updates their preset with their own key. Bitdepth never holds the key. Not built; a snippet for the api-access page in Phase 2.

### 6. SillyTavern

Not confirmed. OpenRouter's SillyTavern guide mentions a fallback setting but no provider allow list (https://openrouter.ai/blog/tutorials/sillytavern-openrouter/), and the SillyTavern docs page could not be fetched from this session. Phase 2 should check the SillyTavern source or docs before writing a paste snippet for it. The preset route works for any client that lets you set the model string, which may cover SillyTavern anyway.

### 7. Exacto

Not re-fetched. From the 2026-11-04 findings row: Exacto ranks by tool-call success only, needs four or more providers, deprioritizes endpoints more than two standard deviations below the median, and keeps its data internal. The route list differs on three points the copy can say plainly: it covers non-tool-call quality, the method is published, and every endpoint is named with its reason.

### 8. Free versus paid: one recommendation

Free: today's list per model as JSON, the MCP tool, and the copy-paste block. It spreads.

Paid (the Watch headline): the list kept current inside their stack, with their own filters (minimum nights, maximum price, providers to always skip), the morning email when their list changes, and the preset-update snippet. Price it **per model, not per endpoint**: a route list is one model's list, and asking a developer to count endpoints to buy a list is friction. Suggested: $5 per model a month, 3 minimum, same numbers as today so the page barely changes. Mancy decides.

## Verdict

Items 1 to 3 confirm the design, with one change: the list is a multi-endpoint `only` with fallbacks on, never a single pin. Per the brief this clears Phase 2. Stopped here anyway at Mancy's request.

Sources:
- https://openrouter.ai/docs/guides/routing/provider-selection.md
- https://openrouter.ai/docs/guides/features/presets.md
- https://openrouter.ai/blog/tutorials/sillytavern-openrouter/
- `data/runs/*/responses.jsonl` (13 nights, `pinned_tag`, `returned_provider`, `misrouted`)
