# site/

The bitdepth.dev pages: static HTML, no build step, no analytics. `api/` holds the Vercel functions: free public JSON at `/v1/*`, the free MCP server at `/api/mcp/mcp`, and the x402 row at `/api/v1/row`. They read the probe repo's `data/public/v1/` and `data/trend/latest.json` from raw GitHub on `main`; no numbers live in `site/`. Env: `X402_PAYTO`, `CDP_API_KEY_ID`, `CDP_API_KEY_SECRET`. Deployed by Vercel with the Root Directory set to `site`. No page here names a provider or carries a number from the scorecards in `data/`.

Last deploy trigger: 2026-10-29 16:16 ET.
