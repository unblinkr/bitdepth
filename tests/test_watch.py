import json

from probe import watch


def _model(tag_rows, model="deepseek/deepseek-v4-pro"):
    return {"model": model, "label": model.split("/")[1], "as_of": "2026-11-06", "endpoints": tag_rows}


def _write(tmp_path, endpoints):
    pub = tmp_path / "pub"
    (pub / "or" / "deepseek").mkdir(parents=True)
    (pub / "or" / "deepseek" / "deepseek-v4-pro.json").write_text(json.dumps(_model(endpoints)))
    (pub / "index.json").write_text(json.dumps({"models": [{"model": "deepseek/deepseek-v4-pro", "path": "or/deepseek/deepseek-v4-pro.json"}]}))
    return pub


def _ep(tag, state="within", quant="fp8", pin=1.0, pout=2.0):
    return {"tag": tag, "state": state, "declared_quant": quant, "price_in_per_m": pin, "price_out_per_m": pout}


def test_first_night_is_a_baseline_with_no_changes(tmp_path):
    pub = _write(tmp_path, [_ep("a/fp8")])
    doc = watch.run_changes(pub, tmp_path / "state.json")
    assert doc["baseline"] is True and doc["changes"] == []
    assert (pub / "changes.json").exists()


def test_detects_state_quant_price_new_and_removed(tmp_path):
    state = tmp_path / "state.json"
    pub = _write(tmp_path, [_ep("a/fp8"), _ep("b/fp8"), _ep("gone/fp8")])
    watch.run_changes(pub, state)
    pub = _write(tmp_path / "n2", [_ep("a/fp8", state="outside"), _ep("b/fp8", quant="fp4", pout=2.5), _ep("new/bf16")])
    doc = watch.run_changes(pub, state)
    got = {(c["tag"], c["field"]) for c in doc["changes"]}
    assert got == {
        ("a/fp8", "state"),
        ("b/fp8", "declared_quant"),
        ("b/fp8", "price_out_per_m"),
        ("gone/fp8", "listed"),
        ("new/bf16", "listed"),
    }


def test_tiny_price_moves_are_ignored(tmp_path):
    state = tmp_path / "state.json"
    watch.run_changes(_write(tmp_path, [_ep("a/fp8", pout=2.0)]), state)
    doc = watch.run_changes(_write(tmp_path / "n2", [_ep("a/fp8", pout=2.001)]), state)
    assert doc["changes"] == []


def test_parse_and_match_respect_model_and_quantity():
    specs = watch.parse_endpoints("deepseek/deepseek-v4-pro:a/fp8, b/fp8\nc/fp8")
    assert specs == ["deepseek/deepseek-v4-pro:a/fp8", "b/fp8", "c/fp8"]
    changes = [
        {"model": "deepseek/deepseek-v4-pro", "tag": "a/fp8", "field": "state"},
        {"model": "openai/gpt-oss-120b", "tag": "a/fp8", "field": "state"},
        {"model": "openai/gpt-oss-120b", "tag": "b/fp8", "field": "state"},
        {"model": "openai/gpt-oss-120b", "tag": "c/fp8", "field": "state"},
    ]
    got = watch.changes_for(specs, 2, changes)
    assert [(c["model"], c["tag"]) for c in got] == [
        ("deepseek/deepseek-v4-pro", "a/fp8"),
        ("openai/gpt-oss-120b", "b/fp8"),
    ]


def test_notify_skips_without_keys(monkeypatch, capsys):
    for k in ("STRIPE_SECRET_KEY", "RESEND_API_KEY", "WATCH_PAYMENT_LINK"):
        monkeypatch.delenv(k, raising=False)
    assert watch.notify({"changes": [{"x": 1}], "as_of": "d"}) == 0
    assert "skipped" in capsys.readouterr().out


def test_email_body_has_no_em_dash():
    body = watch.email_body("2026-11-10", [{"label": "m", "tag": "a/fp8", "field": "price_out_per_m", "from": 2.0, "to": 2.5}])
    assert "\u2014" not in body and "$2.500/M" in body
