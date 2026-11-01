# QUESTIONS for selfcheck-trend

Decisions taken in the session because the brief could not be done exactly as written. Each one is reversible. None changes a hard rule.

## 1. Pre-existing banned-term hits in `tasks/probe-harness/REPORT.md`

The whole-word grep for the four terms finds one hit each in `tasks/probe-harness/REPORT.md`, lines 248 to 251, where that report pasted its own grep commands. They were already on `main` before this task and are left as they are. This task's report writes the commands with the term masked as `<term>` so it adds none. Whether to edit the earlier report is the founder's call.

## 2. Self-check nights run about 2.5 hours, and the 07:17 UTC slot has been firing late

GitHub has run the 07:17 UTC slot several hours late (13:41 UTC on Oct 31, 14:25 UTC on Oct 29). A self-check night adds pass A, a one-hour wait and pass B, so the Nov 2 and Nov 9 runs will finish roughly 2.5 hours after they start. The 11:17 UTC backup slot queues behind a running job (same concurrency group) and skips once `run.json` exists, so no night runs twice. Nothing to decide; noted so the late timestamps on those two nights are not read as a problem.
