import json

from probe import agentlogs as al


def _session(sid, first, final, start, tools=1, tin=1000, tout=10, model="anthropic/claude-opus-4.6", extra_user=0):
    msgs = [{"role": "user", "content": first}]
    msgs += [{"role": "user", "content": "more"} for _ in range(extra_user)]
    msgs.append({"role": "assistant", "content": "",
                 "tool_uses": [{"tool": "exec", "input": {"command": "uptime"}, "output": {"text": "up 3 days"}}] * tools})
    if final is not None:
        msgs.append({"role": "assistant", "content": final})
    return {"session_id": sid, "model": model, "start_time": start, "source": "openclaw",
            "stats": {"user_messages": 1 + extra_user, "input_tokens": tin, "output_tokens": tout}, "messages": msgs}


def _write(tmp_path, rows, name="fixture.jsonl"):
    p = tmp_path / name
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
    return str(p)


def _cron_rows(n=12):
    rows = []
    for i in range(n):
        final = al.NO_REPLY if i % 2 else "Position closed, equity up 30."
        rows.append(_session(f"c{i}", "[cron:0274287d-5308-4bb4 Watch] Check, report only changes.", final,
                             f"2026-02-26T{10 + i // 6:02d}:{(i % 6) * 10:02d}:00Z"))
    return rows


def test_cron_key_and_mask():
    key, name, cron = al.job_key("[cron:ab12-cd34 Server Health] check it")
    assert key == "cron:ab12-cd34" and name == "Server Health" and cron
    k1, _, c1 = al.job_key("Summarise ticket 4512 opened 2026-01-02 at https://x.y/z")
    k2, _, _ = al.job_key("Summarise ticket 99 opened 2026-03-09 at https://a.b/c")
    assert k1 == k2 and not c1


def test_parse_estimates_tokens_when_missing(tmp_path):
    row = _session("s1", "hello", "done", "2026-02-26T10:00:00Z", tin=0, tout=0)
    s = al.load([_write(tmp_path, [row])])[0]
    assert s["tokens_estimated"] and s["input_tokens"] > 0
    assert s["decision"] == "report"


def test_jobs_flag_unattended_and_project_cron(tmp_path):
    rows = _cron_rows() + [_session("i1", "can you fix my build", "fixed", "2026-02-26T09:00:00Z", extra_user=3,
                                    tin=50000)]
    sessions = al.load([_write(tmp_path, rows)])
    prices = {"anthropic/claude-opus-4.6": (5e-6, 25e-6)}
    jobs = al.build_jobs(sessions, prices)
    cron = next(j for j in jobs if j["cron"])
    inter = next(j for j in jobs if not j["cron"])
    assert cron["kind"] == "unattended" and cron["gradable"] and cron["runs_per_month"]
    assert cron["cost_per_month_usd"] and cron["all_priced"]
    assert inter["kind"] == "interactive" and inter["runs_per_month"] is None
    sh = al.shares(jobs)
    assert 0 < sh["unattended_share"] < 1


def test_price_match_strips_harness_prefix():
    prices = {"anthropic/claude-opus-4.6": (1, 2), "anthropic/claude-opus-4.6:batch": (0.5, 1)}
    mid, pr = al.match_price("google-antigravity/claude-opus-4-6-thinking", prices)
    assert mid == "anthropic/claude-opus-4.6" and pr == (1, 2)


def test_decision_strings():
    assert al.decision_of("NO_REPLY") == al.NO_REPLY
    assert al.decision_of("`NO_REPLY`") == al.NO_REPLY
    assert al.decision_of("Trade opened") == "report"
    assert al.decision_of("") == "none"


def test_samples_keep_both_decisions(tmp_path):
    sessions = al.load([_write(tmp_path, _cron_rows(30))])
    jobs = al.build_jobs(sessions, {})
    picked = al.pick_samples(jobs, sessions, max_samples=10)
    got = {p["session"]["decision"] for p in picked}
    assert got == {al.NO_REPLY, "report"} and len(picked) == 10


def test_replay_respects_cap_and_grades(tmp_path, monkeypatch):
    sessions = al.load([_write(tmp_path, _cron_rows())])
    jobs = al.build_jobs(sessions, {"anthropic/claude-opus-4.6": (5e-6, 25e-6)})
    samples = al.pick_samples(jobs, sessions, max_samples=4)
    targets = [{"label": "cheap", "slug": "x/cheap", "tag": "h1", "price_in": 1e-7, "price_out": 1e-7,
                "provider_name": "H1"}]

    def fake(slug, tag, messages, params, reasoning_modes=None):
        assert "Tool results:" in messages[1]["content"]
        return {"status": "ok", "text": al.NO_REPLY, "usage": {"cost": 0.0001}, "provider": "H1"}

    rows = al.send(samples, targets, al.routine.HardCap(1.0), tmp_path / "r.jsonl", "t", completer=fake)
    assert len(rows) == 4 and sum(r["passed"] for r in rows) == 2
    capped = al.send(samples, targets, al.routine.HardCap(0.0), tmp_path / "r2.jsonl", "t", completer=fake)
    assert all(r["status"] == "skipped_budget" for r in capped)
    summ = al.replay_summary(rows, jobs, targets)
    assert summ[0]["pass_rate"] == 0.5 and summ[0]["option_per_month_usd"] is not None


def test_effective_cap_never_above_ceiling(tmp_path, monkeypatch):
    monkeypatch.setattr(al.routine, "night_billed", lambda d: 0.0)
    monkeypatch.setattr(al.routine, "routine_billed", lambda d: 0.0)
    monkeypatch.setattr(al, "OUT_DIR", tmp_path)
    assert al.effective_cap(10.0, "2026-11-19") == al.HARD_CEILING
    monkeypatch.setattr(al.routine, "night_billed", lambda d: 7.0)
    assert al.effective_cap(10.0, "2026-11-19") == 0.75
