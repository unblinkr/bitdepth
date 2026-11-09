# REPORT: x402 pay test

Paid once, settled, confirmed on-chain. 2026-11-09.

## What happened
- Run from this repo (public, so no Actions minutes), not openclaw-news: that repo is private and out of free minutes for November, and GitHub needs a card on file for any budget. The script and workflow are the brief's, with dependencies pinned in tools/x402-pay.
- Mancy dispatched `x402 pay test` with confirm PAY. Pre-flight passed, one payment sent, never retried.

## Section 8 checks
1. No-key check mode: `ERROR: PADDOCK_SELFPAY_KEY is not set`, exit 1, nothing else printed. A random key exits with "derived address ... is not the test wallet", no key material printed.
2. Unpaid GET: HTTP 402. accepts[0]: network eip155:8453, asset 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 (Base USDC), amount 100000 (0.10 USDC), payTo 0x153AA87807D8f6deb65Bd53B137Cee7AD2dacCDb.
3. The key name appears only in tools/x402-pay/x402-pay-test.ts (as a constant) and .github/workflows/x402-pay-test.yml (env lines).
4. Em dashes in changed files: 0.
5. pytest 70 passed; node --test tests/site_api.test.mjs 5 passed.
6. Job summary: state settled, HTTP 200, success true.
7. https://basescan.org/tx/0xaf787e038ac46ac623285470cac88517f1a4eb940e5a0c76baa61b65d9ea20fc (block 55314022, status 1). Receipt log: USDC Transfer from 0x7fb0dc20f35435ba027dc267ef126f063353e159 to 0x153aa87807d8f6deb65bd53b137cee7ad2daccdb, 0.1 USDC. Judged by the Transfer event, not tx.from.
8. Wallet USDC 6.448 before, 6.348 after: down exactly 0.10.

## Bazaar
Not listed yet at 2026-11-09 19:50 UTC (full scan of 33,276 resources at api.cdp.coinbase.com/platform/v2/x402/discovery/resources). Indexing is not instant. Check again 2026-11-10, then agentic.market/validate and Mercator search.
