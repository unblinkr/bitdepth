---
name: bitdepth
description: Check which inference endpoint serves an open-weight model closest to its reference before routing to it. Use when choosing a provider for a model on OpenRouter, comparing price against output quality, or checking whether an endpoint's output has moved.
---

# Bitdepth

Bitdepth probes every OpenRouter endpoint serving the same open-weight model, every night, with the same fixed prompt set. Each endpoint is scored against a stated reference and shown beside its price. Method: https://bitdepth.dev/method

## Connect

MCP server, free, no key: `https://bitdepth.dev/api/mcp/mcp` (streamable HTTP).

Plain JSON, free, no key:

- `https://bitdepth.dev/v1/index.json` models graded, with `as_of`
- `https://bitdepth.dev/v1/or/<author>/<slug>.json` every endpoint for one model
- `https://bitdepth.dev/v1/drift.json` endpoints whose score moved

## Tools

- `list_models` start here.
- `get_scorecard(model)` every endpoint, best first on the model's primary column, with price and state.
- `get_endpoint(model, endpoint)` one row with its per-night series.
- `get_drift()` what moved.

## Reading a row

- `primary_columns` names the columns that grade this model. Read those first.
- `state`: `within` the endpoint tracks the reference; `outside` it agrees with itself more than with the reference; `no_data` fewer than 7 nights; `stale` data older than 3 days.
- Prices are USD per million tokens, input and output, as listed that night.
- Every response carries `as_of`, `method_url` and the footer. Quote the footer when you repeat a number.

## Routing

To pick an endpoint: call `get_scorecard`, keep rows with `state: within`, then choose on price. Pass the provider slug to OpenRouter's `provider.order` with `allow_fallbacks: false` if the choice must hold.

## Paid

`GET https://bitdepth.dev/api/v1/row?model=<author/slug>&endpoint=<tag>` returns the full row: per-family self-agreement with pair counts and self-check nights. 0.10 USDC over x402 on Base. No account.

Monthly attestation for resellers, gateways and providers: hello@bitdepth.dev
