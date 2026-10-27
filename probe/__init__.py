"""Bitdepth nightly probe of OpenRouter inference endpoints."""

BUDGET_USD = 5.00
CONCURRENCY = 4
MAX_TOKENS = 512
SEED = 42
FIXED_SEED = 20261026

# Models probed every night. The label is used in file names and scorecard headings.
MODELS = [
    {"label": "gpt-oss-120b", "slug": "openai/gpt-oss-120b"},
    {"label": "deepseek-v4-pro", "slug": "deepseek/deepseek-v4-pro"},
]

# Declared quantizations that count as full precision for the reference rule.
FULL_PRECISION = {"bf16", "fp16"}
