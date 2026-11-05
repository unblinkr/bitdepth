"""Bitdepth nightly probe of OpenRouter inference endpoints."""

BUDGET_USD = 7.75
CONCURRENCY = 4
MAX_TOKENS = 512
SEED = 42
FIXED_SEED = 20261026

# Models probed every night. The label is used in file names and scorecard headings.
MODELS = [
    {"label": "gpt-oss-120b", "slug": "openai/gpt-oss-120b"},
    {"label": "deepseek-v4-pro", "slug": "deepseek/deepseek-v4-pro"},
    # Added 2026-11-04: the model every public complaint in the 2026-10-27 sweeps names.
    {"label": "deepseek-v4.1-flash-1017", "slug": "deepseek/deepseek-v4.1-flash-1017"},
    # Added 2026-11-04: open weights released 2026-10-29; Mistral serves it first-party, so the
    # pool can be graded against its own lab as third-party hosts arrive. Two to three endpoints
    # at launch, under six, so the run flags it short until hosts join.
    {"label": "mistral-large-4-0", "slug": "mistralai/mistral-large-4-0"},
    # Added 2026-11-05, first probed 2026-11-10 so the Nov 9 self-check night runs on the
    # same set as the fourteen-night read. Picked from r/SillyTavernAI and r/openrouter
    # complaints about which provider serves a weaker copy. Estimated about $0.90 and
    # $0.70 a night at 2026-11-05 prices; four models were about $5.24, so six stay under the cap.
    {"label": "glm-5.3-flash", "slug": "z-ai/glm-5.3-flash", "from": "2026-11-10"},
    {"label": "gemma-4-31b-it", "slug": "google/gemma-4-31b-it", "from": "2026-11-10"},
    # Added 2026-11-05 with the cap raised to $7.75: the model with the most provider-quality
    # complaint threads in r/SillyTavernAI (12 in 60 days). Five endpoints, about $0.81 a night,
    # most of it one endpoint at $4 / $8 per M.
    {"label": "mimo-v2.6-pro", "slug": "xiaomi/mimo-v2.6-pro", "from": "2026-11-10"},
]

# Declared quantizations that count as full precision for the reference rule.
FULL_PRECISION = {"bf16", "fp16"}
