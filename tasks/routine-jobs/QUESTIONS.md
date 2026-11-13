# Questions

1. The V4.1 Flash route list is empty until its first-look window ends (2026-11-19), so the cheapest lane model is not in the first run. Run the measurement again after that date? The module picks the model up on its own once its list has allowed endpoints.
2. In `data/public/v1/routes/deepseek/deepseek-v4.1-flash-1017.json` the excluded reasons read "only 9 nights; 7 needed" for endpoints held back by the first-look window. The reason text should say first look, not nights. Not changed in this task.
3. The baseline is one frontier model. A cheap closed model as a second baseline would show how much of the saving is open weights and how much is simply a smaller model. Add it?
4. Five instances a job is a small sample. If the first run shows a split between lane and outside endpoints, a larger run on that job alone would firm it up.
