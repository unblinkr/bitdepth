# REPORT: apify-probe

Run 2026-11-03 from the claude.ai session. Branch `apify-probe`, merged to `main`.

## What shipped

An Apify actor, Bitdepth Endpoint Probe (`.actor/`, `actor/`). Input: a graded model and a target (an OpenRouter endpoint tag, or an https OpenAI-compatible base URL with model name and key). It loads the latest night from this repo on raw GitHub, builds the reference with `probe.score.build_reference`, sends the fixed prompts with `probe.run.send_all` (concurrency 4), grades with `probe.score.endpoint_metrics`, and places the result against last night's endpoints on the same prompts. Output schema `bitdepth.probe.v1`.

- Charged once, event `endpoint-probe`, on the dataset push, only when at least half the prompts were answered and the spend cap did not stop the run.
- Spend cap $1.00 per probe on Bitdepth's OpenRouter key. Last night's per-endpoint cost: gpt-oss-120b median $0.013, DeepSeek V4 Pro max $0.175.
- Custom URLs: https only; private, loopback, link-local and reserved addresses refused. The key lives in a closure for the run and is never logged or returned.
- Fixed prompts only (120); fresh prompts have a reference only on their night. Self-agreement is not computed from one probe and is listed under `not_checked`.

## Verification

1. `python -m pytest -q`: 55 passed (12 new in `tests/test_actor_probe.py`).
2. Entry point under the Apify SDK local mode: bad model, unknown tag and private URL each exit 1 with a clear status message and no charge.
3. Happy path end to end, completions stubbed with last night's reference answers: real reference from GitHub (night 2026-11-03), real OpenRouter listing, 120 of 120 answered, exact 100%, rank 1 of 26, charge attempted (ignored off-platform, as expected).
4. Not tested: a live run with real completions. Needs the actor env var below.

## Needs Mancy (Apify Console)

1. Develop new, source Git repository: `https://github.com/unblinkr/bitdepth`, branch `main`. Build.
2. Settings, environment variables: `OPENROUTER_API_KEY`, marked secret.
3. Publication, Monetization: pay per event, event name `endpoint-probe`, price $5.00.
4. Keep it private until 2026-11-10. Store listing goes live with the scorecard.
