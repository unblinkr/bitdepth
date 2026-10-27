# Bitdepth

This repository probes every OpenRouter endpoint serving two open-weight models with a fixed set of generated prompts at temperature zero, every night. A scorecard is one Markdown table per model with one row per endpoint, scoring each endpoint's outputs against a reference built from the endpoints that declare full precision. The one secret is `OPENROUTER_API_KEY`, set as a GitHub Actions secret and read from the environment. The repository is public so the nightly job runs on free Actions minutes; the scorecards in it are working data from an experiment in progress, scored against a stated reference, and are not findings about any provider.

## Run

```
pip install -r requirements.txt
python -m probe.generators --write-fixed
python -m probe.run --date 2026-10-27 --dry-run
python -m probe.run --date 2026-10-27 --source local
python -m probe.score --date 2026-10-27
pytest
```
