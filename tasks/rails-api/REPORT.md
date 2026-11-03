# REPORT: rails-api

Run 2026-11-03 from the claude.ai session, on branch `rails`. Implements the API half of `rails-site` (Changes B, C, D, E). The scorecard pages (Change A, `/grades`) are not in this branch; the Nov 2 decision moved the leaderboard to the home page, so that is its own task.

## Deviation from the rails-site brief

The brief assumed a separate `unblinkr/bitdepth-site` repo with a build step. The site lives in `site/` of this repo, deployed by Vercel with Root Directory `site`, no build step. So:

- Functions sit in `site/api/`, plain Node ESM, zero dependencies (`site/package.json` only sets `"type": "module"`).
- The functions read `data/public/v1/` and `data/trend/latest.json` from raw GitHub on `main`, cached 10 minutes per warm instance. No copy step, nothing to rebuild nightly: the morning after a probe run the API serves it.
- `/v1/*` is a rewrite to `api/public.js`, which serves only `index.json`, `drift.json` and `or/<author>/<slug>.json` listed in the index. Path traversal returns 404 (tested).

## Files

- `site/api/_lib/data.js` loader and the paid-row join.
- `site/api/_lib/x402.js` x402 v2 ported from paddock.finance `src/lib/paddock/x402.ts`. CDP facilitator verify then settle, JWT signed with `node:crypto` (Ed25519 or EC). Settles before serving, so a replayed signature fails at settle and no nonce store is needed. The row is built before payment is taken.
- `site/api/public.js` free JSON, CORS `*`, `max-age=21600`.
- `site/api/row.js` `GET /api/v1/row?model=&endpoint=`, 0.10 USDC on Base. Returns the free row plus trend detail: min and max, per-family self-agreement with pair counts, self-check nights.
- `site/api/mcp.js` free MCP, streamable HTTP, stateless JSON-RPC. Tools `list_models`, `get_scorecard`, `get_endpoint`, `get_drift`. Every result carries `as_of`, `method_url`, footer.
- `site/api-access/index.html`, `site/skill.md`, `site/.well-known/mcp.json`, `site/vercel.json` (rewrites, CORS, noindex).
- `tests/site_api.test.mjs` (run `node --test tests/site_api.test.mjs`).

## Verification

1. `node --test tests/site_api.test.mjs`: 4 of 4 pass against live `main` data. Covers the 404 allowlist, every MCP tool and error path, 503 without `X402_PAYTO`, the 402 challenge, amount and payTo mismatch rejected before the facilitator is called, a stubbed verify and settle serving the full row with `PAYMENT-RESPONSE`, and a failed settle serving no data. The CDP JWT signature is checked against the generated key.
2. Official `@modelcontextprotocol/sdk` client over streamable HTTP against a local server: connects, lists 4 tools, `get_scorecard(openai/gpt-oss-120b)` returns 27 endpoints, as_of 2026-11-03.
3. Not tested: a real USDC payment. Needs the env vars below on the preview, then one paid call from an x402 client.

## Needs Mancy (Vercel project, Preview and Production)

- `X402_PAYTO`: the Base wallet for Bitdepth payouts. If the wallet you set on Nov 2 is under another name, rename it or add this one. Until set, the row route answers 503.
- `CDP_API_KEY_ID`, `CDP_API_KEY_SECRET`: copy from the Paddock Vercel project.
- Confirm Vercel Authentication is on for Preview deployments (Project, Settings, Deployment Protection).

## Go live on 2026-11-10 (after the read)

1. Merge `rails` into `main`.
2. In `site/vercel.json`, delete the header block whose only key is `X-Robots-Tag: noindex`.
3. In `site/api-access/index.html`, change `<meta name="robots" content="noindex">` back to `index,follow`.
4. Add `/api-access` to `site/sitemap.xml`, and the API, MCP and skill lines to `site/llms.txt`.
5. Submit `https://bitdepth.dev/api/mcp/mcp` to the Anthropic connector directory, as Paddock was.

```
BOARD SYNC
todoist_task: Bitdepth, Rails: site, API, MCP, x402 (hidden branch)
closes: none
new issues opened: none
needs_mancy: set X402_PAYTO and CDP keys in Vercel; confirm preview protection
live: branch rails (preview); production unchanged
```
