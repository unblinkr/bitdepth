# TASK: Turn the nightly grade into a route list developers plug into OpenRouter, and make it the reason to subscribe

**Repository:** `unblinkr/bitdepth`
**Save this file to:** `tasks/route-list/TASK.md`
**Branch:** `task/route-list`
**Run with:** this brief alone. Read `CLAUDE.md` first; its Rules section is binding. Branch per change, tests green, merge locally, push `main`. Write `QUESTIONS.md` and `REPORT.md` next to this file.
**Start this task in a fresh Claude Code session.** Do not continue an existing thread; stale context burns tokens and this brief is self-contained.
**Before anything else:** confirm `data/public/v1/index.json` exists and lists at least three models, and that `site/api/mcp.js` contains a `check_before_route` tool. If either is missing, write that one line to `QUESTIONS.md` and stop.
**Executor model:** your choice
**Date issued:** 2026-11-09
**todoist_task:** Bitdepth board, API and pricing
**closes:** none
**mockup:** none
**PR mode:** two phases. Phase 1 (investigate) ends with `REPORT.md` section "Phase 1 findings" and stops for Mancy's yes unless every item in section 6 checks out as assumed, in which case go straight to Phase 2. Phase 2 (build) is `merge on green`, except site copy, which goes to a branch preview and waits for Mancy (section 7, Change E). The nightly workflow commits to `main`; do not merge while a run is in progress (check the Actions tab).

---

## 1. Goal

Today Bitdepth tells a developer which endpoints are good. Developers say they want the router to stop sending them to the bad ones. After this task, Bitdepth publishes, every night, a **route list** per model: the endpoints to allow, in a shape that drops straight into an OpenRouter request or settings page. The free version is today's list. The paid version is the same list kept current inside the developer's own stack: a keyed URL their code fetches, an email when the list changes, and their own filters. That paid version becomes the headline of the Watch plan.

## 2. Why (the evidence)

The idea came from an r/openrouter thread on 2026-11-08, "What's your biggest pain point with OpenRouter?" (https://www.reddit.com/r/openrouter/comments/1xr85fr/whats_your_biggest_pain_point_with_openrouter/, 27 comments). The largest cluster of replies (six of thirteen top-level threads) was provider quality, and nobody asked to be told which provider is bad. They asked not to be routed to it:

- u/CaffeinatedTech: providers run bad configs, managing allow and block lists is tedious, precision should be mandatory, "I want to be able to set a minimum precision and context size and let the router do the rest." Would pay more on OpenRouter than on OpenCode Go.
- u/deltapilot97 (top quality comment): wants to force certain quantizations so they are not routed to badly quantized providers; the cheapest provider usually has awful latency.
- u/Late-Replacement-481: wants something between "free for all" and Exacto.
- u/Bino5150: one provider served a completely broken model; found it only by testing, then filtering and pinning providers in his own harness.
- u/generic-d-engineer: three different places to allow or deny providers and none of them talk to each other; support did nothing about a provider spitting nonsense.
- u/Nan__Fu: asks whether quality problems persist when you pin one provider and rerun the same small test set (the nightly probe is exactly that).

The same workflow shows up elsewhere in the project: Konstantin on the OpenRouter Discord (Oct 10) looks up the generation ID, finds the provider, blocks it with `provider.ignore`; @beayushb on X pinned DeepInfra FP8 and turned off fallbacks; opencode removed two bad routes carrying about 12% of its DeepSeek traffic only after complaints (Nov 1). The route list is the automated version of what they do by hand. It also gives developers a reason to come back daily, which the free table alone does not.

## 3. What already exists (read these, do not rebuild them)

- `data/public/v1/or/<author>/<slug>.json` (schema `bitdepth.or.v1`), rewritten nightly by `probe/emit.py`. Per endpoint: `tag` (for example `deepinfra/fp8`, `mistral/eu`), `provider_slug`, `declared_quant`, `declared_changed`, `nights`, `exact`, `string`, `self_agree`, `families`, `movement`, `movement_flag`, `price_in_per_m`, `price_out_per_m`, `state` (`within`, `outside`, `no_data`, `stale`). Models today: `openai/gpt-oss-120b` (29 endpoints), `deepseek/deepseek-v4-pro` (16), `deepseek/deepseek-v4.1-flash-1017` (53), `mistralai/mistral-large-4-0` (2). MiMo V2.6 Pro joins on 2026-11-10.
- `data/public/v1/changes.json` and `probe/watch.py`: the nightly change feed and the Watch emails (Stripe subscriptions read for active watchers, Resend for email; endpoints named in the Checkout custom field as `<author/slug>:<tag>` or `<tag>`; quantity caps the count; nothing sent on quiet nights).
- `site/api/mcp.js`: free MCP server with 9 tools. `check_before_route` already returns route true (state `within` and at least `MIN_ROUTE_NIGHTS` nights), false (`outside`) or inconclusive, plus the best value alternative. `get_best_value_endpoint` already ranks endpoints inside the floor by blended price. The route list is the per-model, all-endpoints version of `check_before_route`. Reuse its rule; do not invent a second one.
- `site/api/public.js` (free JSON at `/v1/*`, allowlisted paths only), `site/api/row.js` (0.10 USDC per full row via x402 on Base), `site/api/_lib/data.js` (loader, reads raw GitHub `main`, 10-minute cache).
- `site/pricing/index.html`: Free / Watch ($5 per endpoint a month, 3 minimum, $15) / Pay per call / Enterprise (Custom, "Talk to us"). Headline: "Read the grades free. Pay when you act on them."
- Project docs for background (read via the claude.ai Project if available, otherwise skip): `claude/api-tool-set-2026-11-03.md`, `claude/product-set-2026-11-02.md`, `claude/findings-log.md` (row dated 2026-11-09).

## 4. Decisions already made (do not re-ask)

- Pricing page pattern: plans whose feature lists build on each other; enterprise is one "Custom" box with "Talk to us". No new named company tiers with prices.
- Watch stays $5 per endpoint a month, 3 minimum, unless Phase 1 recommends a different unit for route lists (per model instead of per endpoint is a reasonable question). Recommend; Mancy decides the price.
- Enterprise numbers are for sales calls only and never appear on the site.
- Bitdepth never holds a customer's OpenRouter key and never sends traffic on their behalf in this task. No proxy, no gateway.
- The inclusion rule is the existing `check_before_route` rule. Thresholds stay where they are.

## 5. How the product works (the design to verify and build)

A route list for one model, for one night:

```json
{
  "schema": "bitdepth.routelist.v1",
  "model": "deepseek/deepseek-v4-pro",
  "as_of": "2026-11-10",
  "rule": "state within, 7+ nights",
  "allow": ["provider-a/fp8", "provider-b/bf16"],
  "excluded": [{"tag": "provider-c/fp4", "why": "outside"}, {"tag": "provider-d/fp8", "why": "only 3 nights"}],
  "openrouter": {"provider": {"only": ["..."], "allow_fallbacks": false}},
  "method_url": "https://bitdepth.dev/method",
  "footer": "Numbers against a stated reference. Not a claim about intent."
}
```

Ways a developer uses it (each one must be verified in Phase 1):

1. **In code, per request.** Their app fetches the list once a night or at startup and puts the `openrouter.provider` block into every request body. Works with any OpenRouter client that passes extra body fields (OpenAI SDK `extra_body`, LiteLLM, opencode config).
2. **Paste into settings.** A one-click copy of the provider names for OpenRouter's account-level allowed or ignored providers, and for SillyTavern's OpenRouter provider picker. Manual, free, good for sharing.
3. **Agents.** A free MCP tool `get_route_list(model)` beside `check_before_route`.
4. **Paid, kept current.** A keyed URL (`/api/v1/route-list?model=&key=` or similar) that returns their filtered list, plus a Watch email the morning their list changes ("provider-c dropped out of your DeepSeek V4 Pro list"). Their filters: minimum declared precision, maximum price, providers to always exclude, minimum nights.

## 6. Phase 1: investigate (write answers in REPORT.md, sources linked)

Check each against OpenRouter's current docs (openrouter.ai/docs, provider routing page) and say what is confirmed, what is not, and what that changes:

1. Which fields `provider` accepts today: `order`, `only`, `ignore`, `allow_fallbacks`, `quantizations`, `sort`, and any others. Exact field names and value formats.
2. **The critical one:** can `only` / `order` / `ignore` target a single endpoint (a tag like `deepinfra/fp8`), or only a provider slug? If only provider slugs, how does a developer allow one provider's fp8 endpoint and not its fp4 one? (Combine `only` with `quantizations`? Note that `quantizations` filters on the declared value, which is exactly what Bitdepth says is unverified; say how the list handles that.) This decides whether the list is per endpoint or per provider.
3. Does `only` with `allow_fallbacks: false` fail the request when no listed provider is up, and what does the developer see? What should the list recommend instead (for example a second-tier fallback list)?
4. Account-level provider settings: where they live, whether there is an API to set them, and whether they combine with per-request settings. (u/generic-d-engineer's "three places that don't talk" is evidence they are confusing; say which places exist.)
5. OpenRouter presets: can a preset carry provider settings, and can it be updated by API? Report only; do not build anything that needs the customer's key.
6. SillyTavern: does its OpenRouter connection have a provider allow list, and what format does it take?
7. Exacto and Auto Exacto: what they already do (tool-call accuracy only, 4+ providers, deprioritize more than 2 standard deviations below median, per the 2026-11-04 findings row), so the copy can say where the route list differs (non-tool-call quality, published method, every endpoint named).
8. Free versus paid: the free JSON already lets anyone compute the list. Recommend what the paid tier must add so it is worth paying for (current inside their stack, change email, their filters, more models), and whether the unit is per endpoint or per model. One recommendation, not a menu.

If items 1 to 3 confirm the design in section 5, continue to Phase 2 without waiting. If item 2 says provider slugs only, write the per-provider version of the design in `REPORT.md`, put the decision in `QUESTIONS.md`, and stop.

## 7. Phase 2: build scope

### Change A: `probe/emit.py`
Write `data/public/v1/routes/<author>/<slug>.json` per model nightly, schema `bitdepth.routelist.v1`, from the model file already in memory. Same inclusion rule as `check_before_route` (import or mirror the constant; one source of truth, with a test that the two agree). The `openrouter` block uses whatever format Phase 1 confirmed. Add the routes paths to `index.json`.

### Change B: free API
`site/api/public.js` serves `/v1/routes/<author>/<slug>.json` (add to the allowlist; traversal still 404s). MCP gains `get_route_list` (free, `readOnlyHint`), envelope with `as_of`, `method_url`, footer.

### Change C: paid route list
A keyed endpoint for Watch subscribers that returns the list filtered by their settings (minimum declared precision, maximum blended price, always-exclude providers, minimum nights). Keys: reuse whatever the Watch Stripe flow can carry with the least new machinery; say what you chose and why. If a key system is more than a day's work, ship the filters as query parameters on the free route instead, and put the key question in `QUESTIONS.md`.

### Change D: Watch email
`probe/watch.py` adds a section to the existing email when a model the watcher follows gains or loses an endpoint in its route list. Nothing sent on quiet nights, as today.

### Change E: site copy (branch preview only, Mancy approves before merge)
- Pricing: make the route list the first line of the Watch card ("Your route list, current every morning, in your OpenRouter calls"), and add the free route list to the Free card. Keep the Paddock pattern.
- A short "Use the route list" section on `/api-access` with the three copy-paste snippets (OpenAI SDK `extra_body`, curl body, SillyTavern or settings paste), written from the verified Phase 1 formats.
- Draft a new homepage subline and pricing headline that say the action, not just the grade (the thread's words: stop getting routed to bad providers). Two options at most in `REPORT.md`, one recommended.
- Do not undersell: say what it does plainly. No hedging about readiness.

## 8. Hard rules (violating any fails the task)

- Every rule in `CLAUDE.md`, Rules section, including no em dashes anywhere. Grep U+2014 and the banned terms across tracked files except `tasks/*/TASK.md` before merging; each count is 0.
- No change to the probe capture: prompts, request parameters, models, concurrency, cap, graders, reference rule.
- No file characterises a provider's intent or conduct. A list exclusion says `outside`, `only N nights` or `stale`, nothing else.
- No customer OpenRouter key is ever requested, stored or used.
- Route lists are published under the same rule as the public table: every endpoint named, included or excluded with its reason.

## 9. Verification

1. `pytest` and `node --test tests/site_api.test.mjs` green, with new tests for: route list matches `check_before_route` for every endpoint of every model; excluded endpoints carry a reason; traversal on `/v1/routes/` 404s; MCP `get_route_list` returns the envelope; the paid filters narrow the list correctly.
2. One real OpenRouter request (small prompt, under $0.01, key from the environment only) using the generated `openrouter.provider` block for one model, showing in the response which provider served it and that it was on the list. Record cost in `REPORT.md`.
3. Screenshot or text dump of the pricing and api-access preview for Mancy.

## 10. Report

`REPORT.md`: Phase 1 findings with links; what was built; what was not and why; the copy options with one recommended; the price-unit recommendation; anything Mancy must do, as numbered steps.

```
BOARD SYNC
todoist_task: Bitdepth, API and pricing: route list
closes: none
new issues opened: none
needs_mancy: approve site copy on the preview; decide Watch unit (per endpoint or per model)
live: <what is on main>
```
