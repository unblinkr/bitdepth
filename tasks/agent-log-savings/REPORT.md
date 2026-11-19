# REPORT: agent-log-savings

**Run by:** the claude.ai chat session, 2026-11-19 (Mancy asked for it to run without her).
**Status:** stages 1 and 2 done on four public datasets. Stage 3 (replay) built, tested and estimated; not yet sent, because the OpenRouter key is only available inside GitHub Actions. One click runs it (see "Next").

## What was built

- `probe/agentlogs.py`: parse, jobs, replay. Reads the DataClaw export format. A customer can make the same file from their own OpenClaw, Hermes, Claude Code or Codex history with `dataclaw export --no-push`, which also redacts secrets, so the script never needs to read a raw agent folder. This replaces the "raw .openclaw format" parser in the brief.
- `tests/test_agentlogs.py`: 8 tests on hand-written fixtures. All pass.
- `.github/workflows/agent-logs.yml`: manual dispatch, typed RUN, estimate first, refuses while the nightly runs, commits counts and costs only, report as artifact.
- Replay design: the export has no agent system prompt, so a full re-run is impossible. The replay sends the recorded job instructions plus the recorded tool results and asks for the final message. Grade: same decision as the original model (stay quiet with NO_REPLY, or write a report). String comparison only.

## Datasets (stages 1 and 2, no spend)

| Dataset | Agent | Sessions | Unattended share of spend weight |
| --- | --- | --- | --- |
| akenove/my-personal-codex-data | OpenClaw (199) + Codex (4) | 203 | 16% |
| peteromallet/my-dataclaw-data, `hermes/` folder | Hermes Agent | 278 | 86% |
| wop/my-personal-codex-data | OpenCode, Codex, Claude Code | 57 | 0% |
| xuechengjiang/my-personal-codex-data | Claude Code | 19 | 0% |

Spend weight is input tokens plus 4 times output tokens. Across all four: 17%.

## Findings

1. **The OpenClaw user runs a trading operation on cron, on Claude Opus 4.6 (thinking).** 11 scheduled jobs over about 36 hours. The three largest project to about **$9,400 a month at OpenRouter list price**:
   - a market and position monitor: 134 runs seen, about 8,500 a month, about 84k input tokens a run, **~$3,700/month**. Its last message is a decision (stay quiet or report). 49 of 134 runs stayed quiet. This is the cleanest replay target.
   - a strategy self-review loop: about 970 runs a month, about 590k input tokens a run, **~$3,000/month**.
   - an app auto-builder: about 1,800 runs a month, **~$2,700/month**. Coding, free text, not string-gradable.
   Caveat: the model id carries a `google-antigravity/` prefix, which suggests access through a subscription route, so this user may not pay list price. The pattern still matches the Bitdepth pitch exactly: frontier model, every few minutes, simple check.
2. **Unattended work is 16% of this OpenClaw user's spend, not most of it.** One interactive session alone (about 128M input tokens over 6 hours) outweighs every cron job. Above the 10% stop line in the brief, so replay is justified.
3. **The Hermes user already did Bitdepth's job by hand.** 246 of 278 sessions are a programmatic review pipeline, and every one runs on cheap open models (Kimi K2.6, GLM 5.1, MiniMax M2.7, DeepSeek V4 Pro). Whole set: about $13 at list price (a floor; the export has no token counts, so tokens are estimated from visible text). Power users who notice the bill move on their own.
4. **Coding-agent logs have no unattended work.** Both coding-only datasets show 0%. Consistent with risk 14: interactive coding is not the market.

## Replay estimate (stage 3, not yet sent)

- 2 gradable jobs (monitor, self-review loop), 20 sampled runs each, both decisions kept in the sample.
- 3 targets: cheapest allowed endpoint today for gpt-oss-120b, deepseek-v4.1-flash-1017, deepseek-v4-pro.
- Expected cost **$0.19**. Cap $1.00 by default (hard ceiling $3.00, also bounded by the nightly cap).

## Next

Run the workflow once: GitHub, Actions, "agent log savings", Run workflow, type RUN in confirm, leave the rest as is. https://github.com/unblinkr/bitdepth/actions/workflows/agent-logs.yml

## Housekeeping

- Nothing from any dataset is committed. Downloads and outputs live under `packets/agentlogs/` (git ignored) or in the workflow artifact.
- `pytest`: 125 pass. The 3 failures are the known `tests/test_actor_probe.py` failures on main (open item 5 in the Nov 18 decisions doc), unrelated to this task.
