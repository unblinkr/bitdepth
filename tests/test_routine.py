import json

import httpx
import pytest

from probe import openrouter
from probe import routine as rt

DATE = "2026-11-13"
EM_DASH = chr(8212)


def answer_for(job, wrong=False):
    """The reply a correct model would give, built from the expected answer."""
    e = job["expect"]
    name = job["job"]
    if name == "heartbeat":
        return "DUE: " + ("T-1" if wrong else rt._fmt_ids(e["DUE"]))
    if name == "monitor":
        return "FLAGGED: " + ("S-1" if wrong else rt._fmt_ids(e["FLAGGED"]))
    if name == "digest":
        total = "1.00" if wrong else e["INVOICE_TOTAL"]
        return f"ACTION: {rt._fmt_ids(e['ACTION'])}\nINVOICE_TOTAL: {total}"
    if name == "briefing":
        top = "Nobody" if wrong else e["TOP_REVENUE"]
        return f"TOP_REVENUE: {top}\nOLDEST: {e['OLDEST']}\nTOTAL_HEADCOUNT: {e['TOTAL_HEADCOUNT']}"
    tags = dict(e["TAGS"])
    if wrong:
        for k in list(tags)[:5]:
            tags[k] = "BUG" if tags[k] != "BUG" else "LOGIN"
    return "\n".join(f"{k}={v}" for k, v in tags.items())


def test_overhead_is_deterministic_and_agent_sized():
    a, b = rt.overhead(), rt.overhead()
    assert a == b
    assert 13_000 <= len(a) // 4 <= 15_000
    assert EM_DASH not in a


def test_jobs_are_deterministic_with_unique_ids():
    a, b = rt.build_jobs(3), rt.build_jobs(3)
    assert a == b
    assert len(a) == 15
    assert len({j["id"] for j in a}) == 15
    assert {j["job"] for j in a} == set(rt.JOBS)


def test_every_job_passes_on_its_own_answer_and_fails_on_a_wrong_one():
    for job in rt.build_jobs(3):
        good = rt.grade(job, answer_for(job))
        assert good["passed"] is True, (job["id"], good)
        assert good["score"] == 1.0
        bad = rt.grade(job, answer_for(job, wrong=True))
        assert bad["passed"] is False, (job["id"], bad)


def test_heartbeat_has_a_nothing_due_instance():
    jobs = [j for j in rt.build_jobs(3) if j["job"] == "heartbeat"]
    empty = [j for j in jobs if not j["expect"]["DUE"]]
    assert len(empty) == 1
    assert rt.grade(empty[0], "DUE: NONE")["passed"] is True
    assert rt.grade(empty[0], "Nothing is due right now.")["passed"] is False


def test_grader_tolerates_formatting_marks_case_and_spacing():
    job = next(j for j in rt.build_jobs(1) if j["job"] == "monitor")
    ids = job["expect"]["FLAGGED"]
    text = "Here is the result.\n**flagged:**  " + " , ".join(reversed(ids)) + "\n"
    assert rt.grade(job, text)["passed"] is True


def test_briefing_accepts_a_note_after_the_name_and_commas_in_numbers():
    job = next(j for j in rt.build_jobs(1) if j["job"] == "briefing")
    e = job["expect"]
    text = (f"TOP_REVENUE: {e['TOP_REVENUE']} (highest)\nOLDEST: {e['OLDEST']}\n"
            f"TOTAL_HEADCOUNT: {int(e['TOTAL_HEADCOUNT']):,}")
    assert rt.grade(job, text)["passed"] is True


def test_tagging_passes_at_nineteen_of_twenty_and_fails_at_eighteen():
    job = next(j for j in rt.build_jobs(1) if j["job"] == "tagging")
    tags = dict(job["expect"]["TAGS"])
    keys = list(tags)

    def reply(n_wrong):
        t = dict(tags)
        for k in keys[:n_wrong]:
            t[k] = "BUG" if t[k] != "BUG" else "LOGIN"
        return "\n".join(f"{k}={v}" for k, v in t.items())

    assert rt.grade(job, reply(1))["passed"] is True
    assert rt.grade(job, reply(2))["passed"] is False


def test_resolve_baseline_exact_then_newest_then_none():
    models = [
        {"id": "anthropic/claude-sonnet-4.6", "created": 10, "pricing": {"prompt": "0.000003", "completion": "0.000015"}},
        {"id": "anthropic/claude-sonnet-5.5", "created": 30, "pricing": {"prompt": "0.000003", "completion": "0.000015"}},
        {"id": "anthropic/claude-sonnet-5.5:batch", "created": 40, "pricing": {"prompt": "0.0000015", "completion": "0.0000075"}},
        {"id": "other/model", "created": 99, "pricing": {}},
    ]
    exact = rt.resolve_baseline("anthropic/claude-sonnet-4.6", models)
    assert exact["slug"] == "anthropic/claude-sonnet-4.6" and exact["resolved_from"] is None
    assert exact["price_in"] == pytest.approx(3e-6)
    newest = rt.resolve_baseline("anthropic/claude-sonnet-9", models)
    assert newest["slug"] == "anthropic/claude-sonnet-5.5"
    assert newest["resolved_from"] == "anthropic/claude-sonnet-9"
    assert rt.resolve_baseline("x/y", [{"id": "other/model"}]) is None


def _ep(tag, pin=1e-7, pout=5e-7, provider="P"):
    return {"provider_name": provider, "tag": tag, "quantization": "fp8", "price_in": pin, "price_out": pout,
            "context_length": 100000, "max_completion_tokens": 4096, "supported_parameters": [], "status": 0}


def _routes(tmp_path):
    for slug, allow, excluded in [
        ("openai/gpt-oss-120b", ["a/fp4", "gone/fp4", "b/fp8", "c/bf16"],
         [{"tag": "new/fp4", "why": "only 2 nights; 7 needed"}, {"tag": "out/int4", "why": "outside"}]),
        ("deepseek/deepseek-v4.1-flash-1017", ["d/fp8", "e/fp8"], []),
    ]:
        p = tmp_path / "routes" / f"{slug}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"as_of": DATE, "allow": allow, "excluded": excluded}), encoding="utf-8")
    return tmp_path / "routes"


def _lister(slug):
    if slug == "openai/gpt-oss-120b":
        return [_ep("a/fp4", provider="A"), _ep("b/fp8", provider="B"), _ep("c/bf16", provider="C"),
                _ep("new/fp4", provider="New"), _ep("out/int4", provider="Out")]
    return [_ep("d/fp8", provider="D"), _ep("e/fp8", pin=0.0, provider="E")]


def test_lane_targets_take_cheapest_listed_allowed_and_one_outside(tmp_path):
    t = rt.lane_targets(_lister, hosts=2, outside=True, routes_dir=_routes(tmp_path))
    got = [(x["kind"], x["label"], x["tag"]) for x in t]
    assert got == [
        ("lane", "gpt-oss-120b", "a/fp4"),
        ("lane", "gpt-oss-120b", "b/fp8"),       # gone/fp4 is on the list but no longer listed
        ("outside", "gpt-oss-120b", "out/int4"),  # new/fp4 is excluded for nights, not as outside
        ("lane", "deepseek-v4.1-flash-1017", "d/fp8"),  # e/fp8 has no price
    ]
    assert all(x["kind"] != "outside" for x in rt.lane_targets(_lister, 2, False, _routes(tmp_path)))


def test_hard_cap_never_lets_reserved_plus_spent_pass_the_cap():
    cap = rt.HardCap(1.00)
    assert cap.reserve(0.60) is True
    assert cap.reserve(0.50) is False
    cap.settle(0.60, 0.20)
    assert cap.spent == pytest.approx(0.20)
    assert cap.reserve(0.80) is True
    assert cap.reserve(0.01) is False


def test_effective_cap_is_the_lowest_of_request_ceiling_and_night_headroom():
    assert rt.effective_cap(3.00, 2.44) == 3.00
    assert rt.effective_cap(9.00, 0.0) == rt.HARD_CEILING
    assert rt.effective_cap(3.00, 6.75) == 1.00
    assert rt.effective_cap(3.00, 8.00) == 0.0


def _models():
    return [{"id": "anthropic/claude-sonnet-5.5", "created": 1, "pricing": {"prompt": "0.000003", "completion": "0.000015"}}]


def _night(tmp_path, billed=2.44):
    p = tmp_path / "runs" / DATE
    p.mkdir(parents=True, exist_ok=True)
    (p / "run.json").write_text(json.dumps({"total_billed_usd": billed}), encoding="utf-8")
    return tmp_path / "runs"


def _args(tmp_path, *extra):
    return ["--date", DATE, "--instances", "3", "--out-dir", str(tmp_path / "routine"),
            "--routes-dir", str(_routes(tmp_path)), "--runs-dir", str(tmp_path / "runs"), *extra]


def _completer(jobs, calls):
    by_user = {j["user"]: j for j in jobs}

    def complete(slug, tag, messages, params=None, client=None):
        calls.append((slug, tag, params))
        job = by_user[messages[1]["content"]]
        assert messages[0]["role"] == "system" and len(messages[0]["content"]) > 50_000
        assert params == {"max_tokens": job["max_tokens"]}
        provider = {None: "Anthropic", "a/fp4": "A", "b/fp8": "B", "out/int4": "Out", "d/fp8": "D"}[tag]
        text = answer_for(job, wrong=(tag == "out/int4"))
        cost = 0.04 if tag is None else 0.002
        return {"status": "ok", "error": "", "text": text, "provider": provider,
                "usage": {"prompt_tokens": 14500, "completion_tokens": 20, "cost": cost},
                "latency_ms": 10, "finish_reason": "stop", "reasoning_mode": "disabled", "raw": {}}

    return complete


def _no_send(*a, **k):
    raise AssertionError("a dry run or a refused run must not send anything")


def test_main_refuses_without_the_nights_run_record(tmp_path, capsys):
    rc = rt.main(_args(tmp_path), lister=_lister, model_lister=_models, completer=_no_send)
    assert rc == 2
    assert "no nightly run record" in capsys.readouterr().out
    assert not (tmp_path / "routine").exists()


def test_main_dry_run_prints_the_estimate_and_sends_nothing(tmp_path, capsys):
    _night(tmp_path)
    rc = rt.main(_args(tmp_path, "--dry-run"), lister=_lister, model_lister=_models, completer=_no_send)
    out = capsys.readouterr().out
    assert rc == 0
    assert "cap $3.00" in out and "75 calls" in out   # 15 jobs x (1 baseline + 3 lane + 1 outside)
    assert not (tmp_path / "routine").exists()


def test_main_writes_record_rows_and_report_and_does_not_run_twice(tmp_path, capsys):
    _night(tmp_path)
    calls = []
    comp = _completer(rt.build_jobs(3), calls)
    rc = rt.main(_args(tmp_path, "--source", "dispatch"), lister=_lister, model_lister=_models, completer=comp)
    assert rc == 0
    out = tmp_path / "routine" / DATE
    rec = json.loads((out / "run.json").read_text())
    rows = [json.loads(x) for x in (out / "responses.jsonl").read_text().splitlines()]
    assert len(rows) == 75 == len(calls)
    assert rec["source"] == "dispatch" and rec["cap_usd"] == 3.00
    assert rec["total_billed_usd"] == pytest.approx(15 * 0.04 + 60 * 0.002)
    assert rec["total_billed_usd"] <= rec["cap_usd"]
    s = rec["summary"]
    assert s["groups"] == ["baseline", "lane:deepseek-v4.1-flash-1017", "lane:gpt-oss-120b", "outside:gpt-oss-120b"]
    hb = s["jobs"]["heartbeat"]
    assert hb["baseline"]["pass_rate"] == 1.0 and hb["baseline"]["monthly_usd"] == pytest.approx(0.04 * 1440)
    assert hb["lane:gpt-oss-120b"]["ok"] == 6 and hb["lane:gpt-oss-120b"]["pass_rate"] == 1.0
    assert hb["outside:gpt-oss-120b"]["pass_rate"] == 0.0
    assert s["monthly_total_usd"]["baseline"] == pytest.approx(0.04 * sum(rt.CALLS_PER_MONTH.values()))
    report = (out / "report.md").read_text()
    assert "lower. Passes: 30/30" in report and EM_DASH not in report
    assert (out / "system.txt").exists() and (out / "jobs.jsonl").exists()

    rc2 = rt.main(_args(tmp_path), lister=_lister, model_lister=_models, completer=_no_send)
    assert rc2 == 0 and "already has a run record" in capsys.readouterr().out


def test_main_shrinks_instances_then_stops_when_nothing_fits(tmp_path, capsys):
    _night(tmp_path, billed=7.00)   # 75 cents of headroom: fewer instances fit, three do not
    calls = []
    comp = _completer(rt.build_jobs(3), calls)
    rc = rt.main(_args(tmp_path), lister=_lister, model_lister=_models, completer=comp)
    assert rc == 0
    rec = json.loads((tmp_path / "routine" / DATE / "run.json").read_text())
    assert rec["cap_usd"] == 0.75 and rec["instances"] < 3
    assert rec["total_billed_usd"] <= 0.75

    tmp2 = tmp_path / "second"
    tmp2.mkdir()
    _night(tmp2, billed=7.70)       # 5 cents: one instance does not fit
    rc = rt.main(_args(tmp2), lister=_lister, model_lister=_models, completer=_no_send)
    assert rc == 2 and "does not fit under the cap" in capsys.readouterr().out


def test_a_misrouted_lane_row_is_not_counted_as_a_pass(tmp_path):
    _night(tmp_path)
    jobs = rt.build_jobs(1)
    base = _completer(jobs, [])

    def comp(slug, tag, messages, params=None, client=None):
        r = base(slug, tag, messages, params, client)
        if tag == "a/fp4":
            r["provider"] = "SomeoneElse"
        return r

    rt.main(_args(tmp_path, "--instances", "1"), lister=_lister, model_lister=_models, completer=comp)
    rows = [json.loads(x) for x in (tmp_path / "routine" / DATE / "responses.jsonl").read_text().splitlines()]
    mis = [r for r in rows if r["pinned_tag"] == "a/fp4"]
    assert mis and all(r["status"] == "misrouted" and r["passed"] is False for r in mis)


def _capture_body(tag):
    seen = {}

    def handler(request):
        seen["body"] = json.loads(request.content)
        return httpx.Response(200, json={"choices": [{"message": {"content": "ok"}, "finish_reason": "stop"}],
                                         "provider": "P", "usage": {}})

    client = httpx.Client(transport=httpx.MockTransport(handler))
    openrouter.complete("a/b", tag, [{"role": "user", "content": "hi"}], client=client)
    return seen["body"]


def test_complete_sends_no_provider_block_without_a_tag(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    assert "provider" not in _capture_body(None)
    assert _capture_body("x/fp8")["provider"] == {"order": ["x/fp8"], "allow_fallbacks": False}
