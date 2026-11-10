# Split the nightly run and recalibrate the state rule

**Date:** 2026-11-10. From the fourteen-night read, sections 1 and 9.

## Why

- Nov 9 was cancelled three times by the 330-minute job limit. Nov 8 already took 5 h 7 min on four models; from Nov 10 the run has seven models and about 65 more endpoints.
- The provisional state rule called venice/int4 on gpt-oss-120b `within` and ranked it in the route list, while the read puts it 10.4 points under the pack.

## What changed

- `probe/run.py`: `--model LABEL` runs one model into `data/runs/<date>/parts/<label>/` with its share of the night's cap (its estimate over the night's estimate, so the parts together stay under $7.75). `--merge` joins the parts into the usual night files and records `parts` and `missing_parts` in run.json. `--list-models` prints the active labels for a date.
- `.github/workflows/nightly.yml`: a `plan` job, one `probe` job per model run one after another (`max-parallel: 1`, so concurrency stays at 4; each job has its own 330-minute limit and the 290-minute deadline), and a `finish` job that downloads the parts, merges, scores, trends, emits, runs Watch and commits. A missing part does not stop the night; the merge records it.
- `.gitignore`: part folders are not committed; only the merged night is.
- `probe/emit.py`: `GAP_MAX` 10 to 15; new floor test (more than 8 points under the median of 7+-night endpoints on the model's first primary column is `outside`); V4.1 Flash pinned to `exact`.

## Effect on the current data (trend through Nov 8)

- DeepSeek V4 Pro outside: crusoe/fp8, gmicloud/fp8, novita/fp8, cloudflare (unchanged).
- gpt-oss-120b outside: venice/int4 (new; it leaves the route list).
- V4.1 Flash and Mistral Large 4: none yet (under seven nights / two endpoints).

## Not done

- A self-check night on the parts layout runs the one-hour wait once per model. No self-check date is scheduled; pick one before adding it to `SELFCHECK_DATES`.
