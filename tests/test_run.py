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
    monkeypatch.setattr(run_mod, "resolve_models", lambda: called.__setitem__("n", called["n"] + 1) or {})
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
    monkeypatch.setattr(run_mod, "resolve_models", lambda: {"alpha": {"slug": "a/b", "endpoints": [ep], "short": True}})
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
