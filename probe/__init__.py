"""Bitdepth nightly probe of OpenRouter inference endpoints."""

BUDGET_USD = 7.00
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
]

# Declared quantizations that count as full precision for the reference rule.
FULL_PRECISION = {"bf16", "fp16"}
