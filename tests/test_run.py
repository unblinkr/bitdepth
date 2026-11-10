import json
from pathlib import Path

import pytest

from probe import run as run_mod
from probe.run import Spend, make_row, send_all


def _endpoint(tag="full/bf16", provider="Full", quant="bf16", seed=True):
    return {
        "provider_name": provider, "tag": tag, "quantization": quant,
        "price_in": 0.000001, "price_out": 0.000002, "context_length": 1000,
        "max_completion_tokens": 100, "supported_parameters": ["seed"] if seed else [], "status": 0,
    }


def _prompt(pid="fixed-math-001"):
    return {"id": pid, "family": "math", "prompt": "What is 2 plus 2? Reply with the integer only.", "answer": "4"}


def _ok(provider="Full", text="4"):
    return {"status": "ok", "error": "", "text": text, "provider": provider,
            "usage": {"prompt_tokens": 10, "completion_tokens": 1, "cost": 0.00001},
            "latency_ms": 50, "finish_reason": "stop", "reasoning_mode": "disabled", "raw": {}}


def test_misroute_is_marked_when_returned_provider_differs():
    row = make_row("r", "alpha", "a/b", _endpoint(), _prompt(), _ok(provider="Other"))
    assert row["status"] == "misrouted"
    assert row["misrouted"] is True
    row2 = make_row("r", "alpha", "a/b", _endpoint(), _prompt(), _ok(provider="full"))
    assert row2["status"] == "ok"
    assert row2["misrouted"] is False


def test_cost_falls_back_to_tokens_when_usage_has_no_cost():
    res = _ok()
    res["usage"] = {"prompt_tokens": 100, "completion_tokens": 10}
    row = make_row("r", "alpha", "a/b", _endpoint(), _prompt(), res)
    assert row["cost_source"] == "estimated"
    assert abs(row["cost_usd"] - (100 * 0.000001 + 10 * 0.000002)) < 1e-9


def test_runtime_budget_stop_skips_remaining_rows(tmp_path):
    calls = []

    def completer(slug, tag, messages):
        calls.append(tag)
        r = _ok()
        r["usage"]["cost"] = 1.0
        return r

    models = {"alpha": {"slug": "a/b", "endpoints": [_endpoint()]}}
    prompts = [_prompt(f"fixed-math-{i:03d}") for i in range(1, 6)]
    spend = Spend(cap=2.0)
    rows = send_all("r", models, prompts, tmp_path / "responses.jsonl", spend, completer=completer)
    assert spend.stopped
    skipped = [r for r in rows if r["status"] == "skipped_budget"]
    assert skipped, "some rows should be skipped once the cap is hit"
    assert len(calls) + len(skipped) == 5
    written = [json.loads(l) for l in (tmp_path / "responses.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(written) == 5


def test_skip_when_run_exists(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    rd = Path("data/runs/2026-10-27")
    rd.mkdir(parents=True)
    (rd / "run.json").write_text("{}")
    called = {"n": 0}
    monkeypatch.setattr(run_mod, "resolve_models", lambda **k: called.__setitem__("n", called["n"] + 1) or {})
    rc = run_mod.main(["--date", "2026-10-27", "--source", "local"])
    assert rc == 0
    assert "run exists for 2026-10-27, skipping" in capsys.readouterr().out
    assert called["n"] == 0


def test_abort_on_estimate_sends_nothing_and_records_estimate(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("data/prompts").mkdir(parents=True)
    # one very expensive endpoint so the estimate is far over the cap
    ep = _endpoint()
    ep["price_in"] = 1.0
    ep["price_out"] = 1.0
    monkeypatch.setattr(run_mod, "resolve_models", lambda **k: {"alpha": {"slug": "a/b", "endpoints": [ep], "short": True}})
    monkeypatch.setattr(run_mod, "load_jsonl", lambda path: [_prompt()])
    monkeypatch.setattr(run_mod, "fresh_set", lambda date: [])
    Path("data/prompts/fixed.jsonl").write_text("{}\n")
    sent = {"n": 0}
    monkeypatch.setattr(run_mod.openrouter, "complete", lambda *a, **k: sent.__setitem__("n", sent["n"] + 1))
    rc = run_mod.main(["--date", "2026-10-27", "--source", "local"])
    assert rc == 0
    assert sent["n"] == 0
    rec = json.loads(Path("data/runs/2026-10-27/run.json").read_text())
    assert rec["aborted_on_estimate"] is True
    assert rec["estimate"]["usd"] > 5.0
    assert not Path("data/runs/2026-10-27/responses.jsonl").exists()


def test_selfcheck_sends_n_prompts_per_endpoint_per_pass_and_records_them(tmp_path):
    calls = []

    def completer(slug, tag, messages):
        calls.append(tag)
        return _ok()

    models = {"alpha": {"slug": "a/b", "endpoints": [_endpoint(), _endpoint(tag="cheap/fp4", provider="Cheap", quant="fp4")]}}
    fixed = [_prompt(f"fixed-math-{i:03d}") for i in range(1, 41)]
    spend = Spend(cap=5.0)
    block = run_mod.run_selfcheck("r", models, fixed, 36, tmp_path / "selfcheck.jsonl", spend, wait_seconds=0, completer=completer)
    assert block["prompts"] == 36
    assert block["prompt_ids"] == [f"fixed-math-{i:03d}" for i in range(1, 37)]
    assert len(calls) == 36 * 2 * 2
    rows = [json.loads(line) for line in (tmp_path / "selfcheck.jsonl").read_text().splitlines()]
    assert sum(1 for r in rows if r["pass"] == "A") == 72
    assert sum(1 for r in rows if r["pass"] == "B") == 72
    assert block["pass_a"]["rows"] == 72 and block["pass_b"]["rows"] == 72


def test_resolve_models_skips_models_before_their_from_date(monkeypatch):
    monkeypatch.setattr(run_mod, "MODELS", [
        {"label": "old", "slug": "a/old"},
        {"label": "new", "slug": "a/new", "from": "2026-11-10"},
    ])
    before = run_mod.resolve_models(lister=lambda slug: [], on="2026-11-09")
    after = run_mod.resolve_models(lister=lambda slug: [], on="2026-11-10")
    assert list(before) == ["old"]
    assert list(after) == ["old", "new"]


def test_deadline_stops_new_requests_and_keeps_prompt_order(tmp_path, monkeypatch):
    import time as _t
    from probe import run as R
    calls = []

    def completer(slug, tag, msgs):
        calls.append(msgs[0]["content"])
        return {"status": "ok", "text": "x", "provider": tag.split("/")[0], "usage": {}, "latency_ms": 1,
                "finish_reason": "stop", "reasoning_mode": None}

    spend = R.Spend(100.0, deadline=_t.monotonic() - 1)
    models = {"m": {"slug": "a/m", "endpoints": [{"tag": "p/fp8", "provider_name": "P", "quantization": "fp8", "price_in": 0, "price_out": 0, "supported_parameters": []}]}}
    prompts = [{"id": "p1", "prompt": "one", "family": "math"}, {"id": "p2", "prompt": "two", "family": "math"}]
    rows = R.send_all("r", models, prompts, tmp_path / "out.jsonl", spend, completer=completer)
    assert calls == []
    assert spend.time_stopped and all(r["status"] == "skipped_budget" for r in rows)


def test_concurrency_override(monkeypatch):
    from probe import run as R
    monkeypatch.setenv("PROBE_CONCURRENCY", "8")
    assert R.concurrency() == 8
    monkeypatch.setenv("PROBE_CONCURRENCY", "50")
    assert R.concurrency() == 8
    monkeypatch.setenv("PROBE_CONCURRENCY", "")
    assert R.concurrency() == R.CONCURRENCY


def _two_models():
    return {
        "alpha": {"slug": "a/alpha", "endpoints": [_endpoint("full/bf16", "Full")], "short": True},
        "beta": {"slug": "b/beta", "endpoints": [_endpoint("q/fp8", "Quant", "fp8"), _endpoint("q2/fp8", "Quant2", "fp8")], "short": True},
    }


def _setup_parts(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("data/prompts").mkdir(parents=True)
    Path("data/prompts/fixed.jsonl").write_text("{}\n")
    monkeypatch.setattr(run_mod, "resolve_models", lambda **k: _two_models())
    monkeypatch.setattr(run_mod, "load_jsonl", lambda path: [_prompt()] if "fixed" in str(path) else
                        [json.loads(l) for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()])
    monkeypatch.setattr(run_mod, "fresh_set", lambda date: [])
    monkeypatch.setattr(run_mod, "MODELS", [{"label": "alpha", "slug": "a/alpha"}, {"label": "beta", "slug": "b/beta"}])
    sent = []

    def fake_complete(slug, tag, messages):
        sent.append((slug, tag))
        return _ok(provider={"full/bf16": "Full", "q/fp8": "Quant", "q2/fp8": "Quant2"}[tag])

    orig = run_mod.send_all
    monkeypatch.setattr(run_mod, "send_all", lambda *a, **k: orig(*a, completer=fake_complete, **k))
    return sent


def test_part_runs_one_model_with_its_share_of_the_cap(tmp_path, monkeypatch):
    sent = _setup_parts(tmp_path, monkeypatch)
    rc = run_mod.main(["--date", "2026-11-10", "--source", "live", "--model", "beta"])
    assert rc == 0
    assert {s for s, _ in sent} == {"b/beta"}
    rec = json.loads(Path("data/runs/2026-11-10/parts/beta/run.json").read_text())
    assert rec["part"] == "beta"
    # beta has two of three endpoints at equal prices, so about two thirds of the cap
    assert run_mod.BUDGET_USD * 0.5 < rec["cap_usd"] < run_mod.BUDGET_USD
    assert not Path("data/runs/2026-11-10/run.json").exists()


def test_merge_joins_parts_into_night_files(tmp_path, monkeypatch):
    sent = _setup_parts(tmp_path, monkeypatch)
    assert run_mod.main(["--date", "2026-11-10", "--source", "live", "--model", "alpha"]) == 0
    assert run_mod.main(["--date", "2026-11-10", "--source", "live", "--model", "beta"]) == 0
    assert len(sent) == 3
    assert run_mod.main(["--date", "2026-11-10", "--merge"]) == 0
    rd = Path("data/runs/2026-11-10")
    rec = json.loads((rd / "run.json").read_text())
    assert rec["summary"]["rows"] == 3
    assert set(rec["parts"]) == {"alpha", "beta"}
    assert rec["missing_parts"] == []
    assert rec["cap_usd"] == run_mod.BUDGET_USD
    assert rec["parts"]["beta"]["rows"] == 2 and rec["parts"]["alpha"]["rows"] == 1
    assert set(json.loads((rd / "endpoints.json").read_text())["models"]) == {"alpha", "beta"}
    assert len((rd / "responses.jsonl").read_text().splitlines()) == 3
    assert len((rd / "prompts.jsonl").read_text().splitlines()) == 1
    # a second part run after the merge is skipped
    assert run_mod.main(["--date", "2026-11-10", "--source", "live", "--model", "alpha"]) == 0
    assert len(sent) == 3


def test_merge_records_missing_parts(tmp_path, monkeypatch):
    _setup_parts(tmp_path, monkeypatch)
    assert run_mod.main(["--date", "2026-11-10", "--source", "live", "--model", "alpha"]) == 0
    assert run_mod.main(["--date", "2026-11-10", "--merge"]) == 0
    rec = json.loads(Path("data/runs/2026-11-10/run.json").read_text())
    assert rec["missing_parts"] == ["beta"]


def test_list_models_respects_from_dates(monkeypatch, capsys):
    monkeypatch.setattr(run_mod, "MODELS", [{"label": "a", "slug": "x/a"}, {"label": "b", "slug": "x/b", "from": "2026-11-10"}])
    assert run_mod.main(["--date", "2026-11-09", "--list-models"]) == 0
    assert json.loads(capsys.readouterr().out) == ["a"]
    assert run_mod.main(["--date", "2026-11-10", "--list-models"]) == 0
    assert json.loads(capsys.readouterr().out) == ["a", "b"]
