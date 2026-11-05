# REPORT: leaderboard-preview

Run 2026-11-05 from the claude.ai session at Mancy's request ("build it now" for Nov 10). Merged to main locally.

## What shipped

- `probe/site.py`: generator for the leaderboard (becomes the home page), one page per model at `/m/<slug>`, `/charts`, share cards per model (1200x630 PNG with the headline and top three rows, used as og:image so X and Reddit previews carry the finding), and Graded by Bitdepth badges per ranked provider.
- Ported from Paddock's /leaderboard and /charts: pine hero with as-of chip, three stat tiles, card grid ("cheapest real endpoint per model"), tabbed board, method cards, get-the-data card, claim-your-endpoint card, charts with Copy link / Copy image / PNG / Share on X, cite line under every figure, finding-of-the-night card, glossary.
- Missing nights break the line and carry a mark on the axis instead of a silent gap.
- Preview at `/lab/` with placeholder data (letters for providers, seeded synthetic numbers), banner on every page, noindex meta and X-Robots-Tag header, linked from nowhere.
- `scripts/go-live.sh`: one command for Nov 10. Moves the current home page to `/compare`, writes the real pages, removes `/lab`, adds sitemap rows, creates `site/.live` which switches on the nightly rebuild step.
- Models: GLM 5.3 Flash (`z-ai/glm-5.3-flash`, 42 endpoints, about $0.90 a night) and Gemma 4 31B (`google/gemma-4-31b-it`, 18 endpoints, about $0.70) added with `from: 2026-11-10`, so the Nov 9 self-check night runs on the same set as the read. Chosen from r/SillyTavernAI and r/openrouter provider-quality complaints.

## Decisions taken

1. Rank: within-state endpoints with 7 or more nights, by blended price ((3 x in + out) / 4) divided by agreement on the model's primary column (exact for gpt-oss-120b, string for DeepSeek). Outside endpoints below a divider; first look unranked.
2. Headline composed in code from the rows, never by a model.
3. The site reads `data/public/v1` (emit.py), not a separate draft JSON.

## Verification

- `pytest`: 60 passed (4 new in test_site.py, 1 new in test_run.py).
- Preview rendered in Chromium at 1280 and 390 wide: no horizontal scroll, no console errors.
- Live build dry-run into a scratch copy with real data: 46 files, idempotent on a second run. Not committed.
- No em dashes in new files.

## Open

- MiMo V2.6 Pro has the most complaint threads (12) but does not fit under $7 with the two above. Adding it needs about $7.75.
- Badges are per provider: a provider with one matching and one outside endpoint on the same model still gets a badge for the matching one.
