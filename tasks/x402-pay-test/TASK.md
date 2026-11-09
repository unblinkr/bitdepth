# TASK: Make one real x402 payment to the new endpoint from the test wallet, through a manually dispatched GitHub Action

**Save this file to:** `tasks/x402-pay-test/TASK.md`
**Branch:** `task/x402-pay-test`
**Run with:** the Agent protocol in this repo's CLAUDE.md if it has one (executor subagent; `QUESTIONS.md` and `REPORT.md` go in the same folder). If the repo has no CLAUDE.md, run it directly in this session. Start this in a fresh Claude Code session, not a continued thread.
**Executor model:** inherit
**Date issued:** 2026-11-09
**todoist_task:** none
**closes:** none
**mockup:** none
**PR mode:** `merge on green` : the founder approved this test in writing on 2026-11-09. Code merges the workflow and script to main when the gates pass, then triggers the run. The payment itself is capped and confirmed in section 6.

---

## 1. Goal

The new x402 endpoint in this repo has been paid once, for real, in USDC on Base, from the founder's test wallet. The settlement is confirmed on-chain, the paid response returned 200, and the result is committed to `tasks/x402-pay-test/results.json` with a REPORT.md.

## 2. Context (self-contained; this session has no other history)

The founder built a new paid x402 endpoint in this repo. It has never been paid. An unpaid x402 route is invisible to the CDP Bazaar and the directories that read it (Agentic.Market, Mercator, x402scan), because the Bazaar indexes a route only after the CDP facilitator processes a real x402 payment to it on Base. It also means nobody has proven the paid path works end to end.

The same thing was done for Paddock's nine paid routes on 2026-09-29 in the `unblinkr/openclaw-news` repo, and it worked: nine payments, $4.101 total, all settled on-chain, merged as PR #424. This brief copies that method. The parts that matter, learned the hard way:

- A Claude Code session cannot make a real-money payment directly. The auto-mode classifier blocked every route a session tried (direct script, subagent, API). What worked was a GitHub Actions workflow with `workflow_dispatch`, a typed `PAY` confirmation input, a pre-flight step that pays nothing, then the pay step, then `always()` steps that publish a summary and an artifact whatever happens.
- The private key lives only as a GitHub Actions repo secret, referenced by name in `env:`. It is never in a command line, a log, a file, a URL, or an error message.
- Vercel will not return the value of an env var marked `sensitive` through any API. Do not try to read the key from Vercel.
- Mark the payment `attempted` in the ledger BEFORE the paid call, so a crash can never cause a silent second payment on rerun. Never retry automatically.
- The first Sept 29 run got HTTP 400 on one route because it was paid with no required query parameter. Money was not taken, but it wasted a run. Send the query the endpoint needs to return 200.
- On Base, `tx.from` on an x402 settlement is the facilitator's relayer, not the payer. To confirm the payer, read the USDC `Transfer` event, not `tx.from`.
- Payments are EIP-3009 authorizations submitted by the facilitator. The payer wallet spends no gas.

The reference implementation is `scripts/selfpay-bazaar.ts` and `.github/workflows/selfpay-bazaar.yml` in `unblinkr/openclaw-news`. Read them if this session can reach that repo. If not, everything needed is in this brief.

You know which endpoint is new. If you are not certain, stop and write the candidate URLs to `QUESTIONS.md`. Do not pay a guessed endpoint.

## 3. Decisions already made (do not re-ask)

- Pay the new endpoint exactly once. One successful settlement is the whole test.
- Payer wallet: the existing test wallet `0x7fb0Dc20F35435bA027dc267EF126f063353E159` on Base. It held 6.448 USDC on 2026-11-09. Do not generate a new wallet.
- Secret name: `PADDOCK_SELFPAY_KEY`. Same name as the openclaw-news secret, holding the same key, added to this repo.
- Price cap: refuse to pay if the live 402 asks for more than 1.00 USDC. This is a guard against a typo in the route's price, not a budget.
- Network and asset: Base mainnet (`eip155:8453`), USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`. Refuse anything else.
- This self-payment is not filtered out of any data. The founder accepted that on 2026-09-29 for the same wallet and the same reason.
- Libraries: `@x402/fetch` (`wrapFetchWithPaymentFromConfig`), `@x402/evm` (`ExactEvmScheme`), `viem` (`privateKeyToAccount`, a public client on `https://mainnet.base.org`). Versions `^2.15.0` for the x402 packages and `^2.55.5` for viem worked on 2026-09-29. Add them as dev dependencies if this repo lacks them.
- The workflow stays in the repo after the test. It is reusable: the endpoint URL is an input, so the next new route is a form fill, not a new brief.

## 4. Hard rules (violating any fails the task)

- The private key never becomes output. Not in chat, a commit, a PR body, a log line, an artifact, or an error. Errors about the key report its length only.
- No payment is sent from this session's own shell. Payment happens only inside the GitHub Action.
- No automatic retry. If the pay step fails, stop and report. A second attempt needs a human to confirm on-chain that the first did not settle.
- Pre-flight must pass before the pay step runs: live 402 parsed, amount at or under the cap, network and asset match section 3, wallet USDC balance at or above the amount, derived address equals the wallet address. Any mismatch exits non-zero with nothing sent.
- No em dashes in anything committed.
- Never commit to main except by the merge in section 9. Never touch any route, price, or production config in this task.

## 5. Banned terms

none

## 6. Build scope

### Change A: `scripts/x402-pay-test.ts`

A generalized copy of `scripts/selfpay-bazaar.ts` that pays ONE URL once.

Usage:
- `npx tsx scripts/x402-pay-test.ts check <url> <max_usdc>` : pre-flight only, pays nothing.
- `npx tsx scripts/x402-pay-test.ts pay <url> <max_usdc>` : pre-flight, then one payment.

Behaviour, in order:
1. Read `PADDOCK_SELFPAY_KEY` from `process.env` only. Strip `0x`, require 64 hex characters, else exit with the length only.
2. Derive the account with `privateKeyToAccount`. Exit if its address is not `0x7fb0Dc20F35435bA027dc267EF126f063353E159`.
3. Unpaid GET to the URL. Require HTTP 402 with a JSON body containing `accepts[]`. Pick the first accept whose `network` is `eip155:8453` and `asset` is Base USDC. Exit if none.
4. Exit if that accept's `amount` (atomic, 6 decimals) is above `max_usdc * 1e6`.
5. Read the wallet's USDC balance. Exit if below the amount.
6. Write the ledger `tasks/x402-pay-test/results.json` with: url, unpaid_status, amount_atomic, network, asset, payTo, wallet balance before, timestamp, state `checked`. In `check` mode, stop here.
7. If the ledger already shows state `attempted`, `failed`, or `settled` for this URL, exit without paying.
8. Set state `attempted`, save the ledger, THEN make the paid call with `wrapFetchWithPaymentFromConfig(fetch, { schemes: [{ network: "eip155:8453", client: new ExactEvmScheme(account) }] })`.
9. Decode the `PAYMENT-RESPONSE` header (fall back to `X-PAYMENT-RESPONSE`), base64 JSON. Record paid_status, success, transaction, payer.
10. Settled only if HTTP 200, `success === true`, and the transaction matches `^0x[0-9a-fA-F]{64}$`. Otherwise record state `failed` with the status and any error fields from the body (truncated to 400 chars) and exit non-zero.
11. Read the USDC balance again and record it.

### Change B: `.github/workflows/x402-pay-test.yml`

```yaml
name: x402 pay test

# Manually dispatched. Makes ONE real x402 payment (USDC on Base) to the
# given URL from the test wallet. The key is a repo secret referenced by
# name in env only; the script never prints it.

on:
  workflow_dispatch:
    inputs:
      url:
        description: "Full URL of the paid endpoint, with any query it needs"
        required: true
      max_usdc:
        description: "Refuse to pay above this many USDC"
        required: true
        default: "1.00"
      confirm:
        description: "Type PAY to send a real payment"
        required: true
        default: "no"

permissions:
  contents: read

concurrency:
  group: x402-pay-test
  cancel-in-progress: false

jobs:
  pay:
    runs-on: ubuntu-latest
    if: ${{ inputs.confirm == 'PAY' }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 24
      - run: npm ci
      - name: Pre-flight (pays nothing)
        env:
          PADDOCK_SELFPAY_KEY: ${{ secrets.PADDOCK_SELFPAY_KEY }}
          URL: ${{ inputs.url }}
          MAX: ${{ inputs.max_usdc }}
        run: npx tsx scripts/x402-pay-test.ts check "$URL" "$MAX"
      - name: Pay once
        env:
          PADDOCK_SELFPAY_KEY: ${{ secrets.PADDOCK_SELFPAY_KEY }}
          URL: ${{ inputs.url }}
          MAX: ${{ inputs.max_usdc }}
        run: npx tsx scripts/x402-pay-test.ts pay "$URL" "$MAX"
      - name: Ledger to job summary
        if: ${{ always() }}
        run: |
          echo '### results.json' >> "$GITHUB_STEP_SUMMARY"
          echo '```json' >> "$GITHUB_STEP_SUMMARY"
          cat tasks/x402-pay-test/results.json >> "$GITHUB_STEP_SUMMARY" || true
          echo '```' >> "$GITHUB_STEP_SUMMARY"
      - uses: actions/upload-artifact@v4
        if: ${{ always() }}
        with:
          name: x402-pay-test-results
          path: tasks/x402-pay-test/results.json
```

If this repo does not use npm (pnpm, yarn, bun), swap `npm ci` for its install command and say so in REPORT.md. Nothing else in the file changes.

### Change C: the secret

Check whether `PADDOCK_SELFPAY_KEY` exists in this repo's Actions secrets (names only, never values). If it does, move on.

If it does not, this session cannot create it: the founder holds the key in Phantom, and the Actions secrets API is blocked through the session proxy. Put this at the top of REPORT.md under NEEDS MANCY, exactly:

```
Add the test wallet key as a GitHub secret (2 minutes):
1. Open Phantom. Select the wallet ending E159. Settings, Manage Accounts, the account, Show Private Key. Copy it.
2. On GitHub, open this repo. Settings, Secrets and variables, Actions, New repository secret.
3. Name: PADDOCK_SELFPAY_KEY
4. Secret: paste the key. Click Add secret.
5. Tell Claude "secret added" and it will run the test.
```

Then finish everything else and stop.

## 7. Out of scope (do not do)

- The endpoint itself: its code, price, 402 shape, Bazaar extension. If the unpaid 402 looks wrong, record what it returned in REPORT.md and stop. Do not fix it here.
- Registering the endpoint anywhere (MPPScan, x402scan, Agentic.Market, the MCP registry).
- Funding the wallet, or moving USDC anywhere.
- Deleting `selfpay-bazaar.yml` or anything in `unblinkr/openclaw-news`.

## 8. Verification checks (run them; paste results into REPORT.md)

1. Before merging: run the script in `check` mode locally WITHOUT the key set and confirm it exits with the "not set" error and no other output about a key. Paste the output.
2. The unpaid GET to the endpoint returns 402. Paste status, `accepts[]` network, asset, amount, payTo (payTo is public).
3. `grep -rn "PADDOCK_SELFPAY_KEY" .` shows the name only in the script and the workflow, never a value. Paste the output.
4. Em dash count in every changed file is 0. Paste the command and output.
5. The repo's own gates pass (type check, tests, build, lint unchanged from main). Paste each.
6. After the run: the job summary shows state `settled`, HTTP 200, and a transaction hash.
7. On Basescan, the transaction contains a USDC `Transfer` from `0x7fb0Dc20F35435bA027dc267EF126f063353E159` to the payTo for the 402 amount. Paste the tx link and the Transfer line. Do not judge by `tx.from`.
8. Wallet USDC after equals before minus the amount. Paste both.

## 9. Handback

1. Commit Changes A and B on `task/x402-pay-test`, open a PR, run the gates, merge to main by this repo's normal convention. `workflow_dispatch` only works once the file is on the default branch.
2. Trigger the run: `gh workflow run x402-pay-test.yml -f url="<the endpoint URL>" -f max_usdc="1.00" -f confirm="PAY"`, then watch it with `gh run watch`.
3. If this session cannot dispatch the workflow (proxy 403 or a classifier block), do not try another route. Put this under NEEDS MANCY, exactly, with the real URL filled in:

```
Run the payment (1 minute):
1. On GitHub, open this repo. Actions tab. Click "x402 pay test" on the left.
2. Click Run workflow.
3. url: <the endpoint URL>
4. max_usdc: leave 1.00
5. confirm: type PAY
6. Click the green Run workflow button. Tell Claude when it finishes.
```

4. After a settled run, download the artifact, commit `results.json` to the task branch, write REPORT.md with every check from section 8, and merge that commit.
5. Bazaar indexing is not instant. Note in REPORT.md that the route should appear on `agentic.market/validate` and in Mercator search after the next indexing pass, and that this is checked tomorrow, not today.

End the session with this block, exactly this shape:

```
BOARD SYNC
todoist_task: none
closes: none
new issues opened: <#n title> | none
needs_mancy: <one line> | none
live: <tx link> | not paid (<reason>)
```