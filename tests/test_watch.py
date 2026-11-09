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


def test_resolve_flags_unknown_and_over_quantity(tmp_path):
    pub = _write(tmp_path, [_ep("a/fp8"), _ep("b/fp8")])
    _, rows = watch.load_current(pub)
    specs = ["deepseek/deepseek-v4-pro:a/fp8", "nope/fp8", "b/fp8", "a/fp8"]
    matched, unknown, extra = watch.resolve(specs, 3, rows)
    assert [r["tag"] for r in matched] == ["a/fp8", "b/fp8"]
    assert unknown == ["nope/fp8"]
    assert extra == ["a/fp8"]
    body = watch.welcome_body("2026-11-09", matched, unknown, extra)
    assert "nope/fp8" in body and "not being watched" in body and "past the number" in body
    assert "\u2014" not in body


def test_payment_links_reads_both_secrets(monkeypatch):
    monkeypatch.setenv("WATCH_PAYMENT_LINK", "plink_A")
    monkeypatch.setenv("WATCH_TEST_PAYMENT_LINK", "plink_B, plink_C")
    assert watch.payment_links() == ["plink_A", "plink_B", "plink_C"]


def test_welcome_emails_each_subscription_once(tmp_path, monkeypatch):
    pub = _write(tmp_path, [_ep("a/fp8")])
    ledger = tmp_path / "welcomed.json"
    for k, v in (("STRIPE_SECRET_KEY", "k"), ("RESEND_API_KEY", "r"), ("WATCH_PAYMENT_LINK", "plink_A")):
        monkeypatch.setenv(k, v)
    monkeypatch.setattr(watch, "list_watchers", lambda key, links: [{"email": "x@y.z", "quantity": 3, "specs": ["a/fp8"], "sub": "sub_1"}])
    sent = []
    monkeypatch.setattr(watch, "send_email", lambda key, to, subj, body: sent.append((to, subj)))
    assert watch.welcome(pub, ledger) == 1
    assert watch.welcome(pub, ledger) == 0
    assert len(sent) == 1
    assert "x@y.z" not in ledger.read_text() and "sub_1" not in ledger.read_text()


def test_picker_specs_join_chunks_in_order():
    meta = {"bitdepth_watch": "1", "endpoints_1": "c/fp8", "endpoints_0": "m/x:a/fp8,b/fp8"}
    assert watch.picker_specs(meta) == ["m/x:a/fp8", "b/fp8", "c/fp8"]
    assert watch.picker_specs(None) == []


def test_weekly_reaches_every_watcher_even_with_no_change(tmp_path, monkeypatch):
    pub = _write(tmp_path, [_ep("a/fp8")])
    for k, v in (("STRIPE_SECRET_KEY", "k"), ("RESEND_API_KEY", "r")):
        monkeypatch.setenv(k, v)
    monkeypatch.setattr(watch, "list_watchers", lambda key, links: [
        {"email": "x@y.z", "quantity": 3, "specs": ["a/fp8", "nope/fp8"], "sub": "s1"},
        {"email": "q@y.z", "quantity": 3, "specs": ["a/fp8"], "sub": "s2"}])
    sent = []
    monkeypatch.setattr(watch, "send_email", lambda key, to, subj, body: sent.append((to, body)))
    assert watch.weekly(pub) == 2
    assert "nope/fp8" in sent[0][1] and "tested every night" in sent[0][1]
    assert "—" not in sent[0][1]


def test_mint_key_matches_the_site():
    # Same literal is pinned in tests/site_api.test.mjs: the email and the API must agree.
    assert watch.mint_key("sub_TEST123", "s3cret") == "bdw_c3ViX1RFU1QxMjM_986e5f11cc1358cb980d1c841178f452"


def test_existing_subscriber_gets_one_key_email(tmp_path, monkeypatch):
    pub = _write(tmp_path, [_ep("a/fp8")])
    ledger = tmp_path / "welcomed.json"
    ledger.write_text('{"welcomed": ["%s"]}' % watch._hash("sub_1"))
    for k, v in (("STRIPE_SECRET_KEY", "k"), ("RESEND_API_KEY", "r"), ("WATCH_KEY_SECRET", "s3cret")):
        monkeypatch.setenv(k, v)
    monkeypatch.setattr(watch, "list_watchers", lambda key, links: [{"email": "x@y.z", "quantity": 3, "specs": ["a/fp8"], "sub": "sub_1"}])
    sent = []
    monkeypatch.setattr(watch, "send_email", lambda key, to, subj, body: sent.append((subj, body)))
    assert watch.welcome(pub, ledger) == 1
    assert watch.welcome(pub, ledger) == 0
    assert sent[0][0] == "Bitdepth Watch: your API key"
    assert watch.mint_key("sub_1", "s3cret") in sent[0][1]
    assert "\u2014" not in sent[0][1]
