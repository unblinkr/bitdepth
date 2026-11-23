import json
from pathlib import Path

from probe import emit, trust
from probe import run as run_mod

SLUG = "deepseek/deepseek-v4.1-flash-1017"
LABEL = "deepseek-v4.1-flash-1017"
BLOG = "https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/"


def _listing(root: Path, date: str, eps: list[tuple[str, str]], slug: str = SLUG) -> None:
    p = root / "trust" / "listed" / f"{date}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"date": date, "models": {slug: [{"tag": t, "provider_name": n} for t, n in eps]}}))


def _zdr(root: Path, date: str, entries: list[tuple[str, str]]) -> None:
    p = root / "trust" / "zdr" / f"{date}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"date": date, "entries": [{"model_id": m, "tag": t, "provider_name": "X"} for m, t in entries]}))


def _incidents(root: Path, items: list[dict]) -> None:
    (root / "incidents.json").write_text(json.dumps({"incidents": items}))


BASE = [("alpha", "Alpha"), ("beta/fp8", "Beta"), ("gmicloud/fp8", "GMICloud")]


def test_norm_model_matches_zdr_ids_without_date_suffix():
    assert trust.norm_model("deepseek/deepseek-v4.1-flash-1017") == "deepseek/deepseek-v4.1-flash"
    assert trust.norm_model("thinkingmachines/inkling-2-mini-20261120") == "thinkingmachines/inkling-2-mini"
    assert trust.norm_model("openai/gpt-oss-120b") == "openai/gpt-oss-120b"
    assert trust.norm_model("mistralai/mistral-large-4-0") == "mistralai/mistral-large-4-0"


def test_zdr_matches_on_tag_plus_normalized_model(tmp_path):
    # The ZDR list names the model without the -1017 suffix our slug carries.
    _listing(tmp_path, "2026-11-22", BASE)
    _zdr(tmp_path, "2026-11-22", [("deepseek/deepseek-v4.1-flash", "alpha"), ("deepseek/deepseek-v4.1-flash", "beta/fp8")])
    _zdr(tmp_path, "2026-11-23", [("deepseek/deepseek-v4.1-flash", "alpha"), ("other/model", "beta/fp8")])
    flags = trust.trust_flags(SLUG, data_dir=tmp_path)
    assert flags == {"beta/fp8": "lost ZDR 2026-11-23"}


def test_delisted(tmp_path):
    _listing(tmp_path, "2026-11-21", BASE)
    _listing(tmp_path, "2026-11-22", BASE[:2])
    assert trust.delisted(SLUG, {"alpha", "gmicloud/fp8"}, {"alpha"}) == {"gmicloud/fp8"}
    assert trust.trust_flags(SLUG, data_dir=tmp_path) == {"gmicloud/fp8": "delisted 2026-11-22"}
    # Same answer with tonight's live listing passed in, as the nightly run does.
    live = [{"tag": t, "provider_name": n} for t, n in BASE[:2]]
    _listing(tmp_path, "2026-11-22", BASE)  # an older record for tonight is replaced by the live list
    assert trust.trust_flags(SLUG, live, date="2026-11-22", data_dir=tmp_path) == {"gmicloud/fp8": "delisted 2026-11-22"}


def test_relisted_needs_fresh_nights_on_routes_but_is_probed(tmp_path):
    _listing(tmp_path, "2026-11-20", BASE)
    _listing(tmp_path, "2026-11-21", BASE[:2])
    _listing(tmp_path, "2026-11-22", BASE)
    assert trust.trust_flags(SLUG, data_dir=tmp_path, probing=True) == {}
    flags = trust.trust_flags(SLUG, data_dir=tmp_path, probing=False, fresh_nights={"gmicloud/fp8": 1})
    assert flags["gmicloud/fp8"].startswith("delisted 2026-11-21; listed again 2026-11-22, 1 of 7")
    assert trust.trust_flags(SLUG, data_dir=tmp_path, probing=False, fresh_nights={"gmicloud/fp8": 7}) == {}


def test_lost_zdr_and_clearing():
    a, b = ("m", "a"), ("m", "b")
    assert trust.lost_zdr({a}, {a, b}) == {b}
    snaps = [("2026-11-01", {a, b}), ("2026-11-02", {a})]
    assert trust.zdr_flags(snaps) == {b: "2026-11-02"}
    back = [(f"2026-11-{d:02d}", {a, b}) for d in range(3, 9)]  # six nights back
    assert trust.zdr_flags(snaps + back) == {b: "2026-11-02"}
    assert trust.zdr_flags(snaps + back + [("2026-11-09", {a, b})]) == {}
    # A night off the list again resets the count.
    gap = back[:3] + [("2026-11-06", {a})] + [(f"2026-11-{d:02d}", {a, b}) for d in range(7, 13)]
    assert trust.zdr_flags(snaps + gap) == {b: "2026-11-06"}


def test_first_night_has_no_prior_snapshot(tmp_path):
    assert trust.lost_zdr([{"model_id": "m", "tag": "a"}], None) == set()
    _listing(tmp_path, "2026-11-23", BASE)
    _zdr(tmp_path, "2026-11-23", [("deepseek/deepseek-v4.1-flash", "alpha")])
    assert trust.trust_flags(SLUG, data_dir=tmp_path) == {}


def test_open_incident_flags_every_endpoint_of_the_provider(tmp_path):
    _listing(tmp_path, "2026-11-22", BASE + [("gmicloud/fp4", "GMICloud")])
    _incidents(tmp_path, [{"provider_name": "GMICloud", "opened": "2026-11-21", "closed": None, "source_url": BLOG,
                           "note": "Provider security notice; see source"}])
    flags = trust.trust_flags(SLUG, data_dir=tmp_path)
    want = f"open incident: GMICloud 2026-11-21 {BLOG}"
    assert flags == {"gmicloud/fp8": want, "gmicloud/fp4": want}
    assert trust.source_url(want, SLUG) == BLOG


def test_closed_incident_flags_nothing(tmp_path):
    _listing(tmp_path, "2026-11-22", BASE)
    _incidents(tmp_path, [{"provider_name": "GMICloud", "opened": "2026-11-21", "closed": "2026-11-30", "source_url": BLOG,
                           "note": "Provider security notice; see source"}])
    assert trust.trust_flags(SLUG, data_dir=tmp_path) == {}


def test_incident_reason_wins_over_delisted(tmp_path):
    _listing(tmp_path, "2026-11-21", BASE)
    _listing(tmp_path, "2026-11-22", BASE[:2])
    _incidents(tmp_path, [{"provider_name": "GMICloud", "opened": "2026-11-21", "closed": None, "source_url": BLOG, "note": ""}])
    assert trust.trust_flags(SLUG, data_dir=tmp_path)["gmicloud/fp8"].startswith("open incident: GMICloud")


def test_zdr_snapshot_refuses_a_collapsed_list(tmp_path):
    _zdr(tmp_path, "2026-11-22", [("m", f"t{i}") for i in range(10)])
    try:
        trust.snapshot_zdr("2026-11-23", tmp_path, fetcher=lambda: [{"model_id": "m", "tag": "t0", "provider_name": "X"}])
        raise AssertionError("expected a refusal")
    except RuntimeError:
        pass
    assert not (tmp_path / "trust" / "zdr" / "2026-11-23.json").exists()
    p = trust.snapshot_zdr("2026-11-23", tmp_path, fetcher=lambda: [{"model_id": "m", "tag": f"t{i}", "provider_name": "X"} for i in range(9)])
    assert json.loads(p.read_text())["count"] == 9


def _row(tag, state="within", nights=10, price=1.0):
    return {"tag": tag, "state": state, "nights": nights, "declared_quant": "fp8",
            "price_in_per_m": price, "price_out_per_m": price}


def _doc(rows, untrusted=()):
    return {"model": SLUG, "label": LABEL, "as_of": "2026-11-23", "endpoints": rows, "untrusted": list(untrusted)}


def test_routes_exclude_untrusted_with_reason_word_for_word():
    why = f"open incident: Together 2026-11-22 {BLOG}"
    r = _row("together")
    r.update(state="untrusted", graded_state="within", trust_reason=why)
    d = emit.route_doc(_doc([_row("alpha"), r], [{"tag": "together", "reason": why, "source_url": BLOG},
                                                  {"tag": "phala", "reason": "delisted 2026-11-22", "source_url": None}]))
    assert d["allow"] == ["alpha"]
    ex = {x["tag"]: x["why"] for x in d["excluded"]}
    assert ex == {"together": why, "phala": "delisted 2026-11-22"}
    assert "no trust flag (delisted, lost ZDR, open incident)" in d["rule"]
    assert not emit.routable(r)


def test_prefix_shadowing_still_works_when_a_parent_slug_is_untrusted():
    parent = _row("novita")
    parent.update(state="untrusted", trust_reason="lost ZDR 2026-11-23")
    child = _row("novita/fp8")
    d = emit.route_doc(_doc([parent, child]))
    # "novita/fp8" cannot match "novita", so the child stays; the parent is out with its reason.
    assert d["allow"] == ["novita/fp8"]
    assert {x["tag"]: x["why"] for x in d["excluded"]} == {"novita": "lost ZDR 2026-11-23"}
    # The other way round: an untrusted child shadows its allowed parent.
    child2 = _row("venice/fp8")
    child2.update(state="untrusted", trust_reason="delisted 2026-11-22")
    d2 = emit.route_doc(_doc([_row("venice"), child2]))
    assert d2["allow"] == []
    assert {x["tag"]: x["why"] for x in d2["excluded"]} == {"venice": "would also match venice/fp8",
                                                             "venice/fp8": "delisted 2026-11-22"}


def test_emit_marks_rows_untrusted_and_keeps_the_grade(tmp_path):
    root = tmp_path
    (root / "runs").mkdir()
    _listing(root, "2026-11-22", BASE)
    _incidents(root, [{"provider_name": "GMICloud", "opened": "2026-11-21", "closed": None, "source_url": BLOG, "note": ""}])
    rows = [dict(_row("alpha"), nightly_exact=[]), dict(_row("gmicloud/fp8"), nightly_exact=[])]
    out = emit.apply_trust(SLUG, rows, root, root / "runs")
    g = rows[1]
    assert g["state"] == "untrusted" and g["graded_state"] == "within" and g["trust_source_url"] == BLOG
    assert rows[0]["state"] == "within"
    assert out == [{"tag": "gmicloud/fp8", "reason": f"open incident: GMICloud 2026-11-21 {BLOG}", "source_url": BLOG}]


def test_nightly_run_skips_flagged_endpoints(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data = Path("data")
    data.mkdir()
    _incidents(data, [{"provider_name": "Novita", "opened": "2026-11-22", "closed": None, "source_url": BLOG, "note": ""}])
    extra = {"price_in": 1e-7, "price_out": 1e-7, "quantization": "fp8", "supported_parameters": []}
    eps = [{"tag": "alpha", "provider_name": "Alpha", **extra}, {"tag": "novita/fp8", "provider_name": "Novita", **extra}]
    models = {LABEL: {"slug": SLUG, "endpoints": list(eps), "short": False}}
    monkeypatch.setattr(trust, "fetch_zdr", lambda: [{"model_id": SLUG, "tag": "alpha", "provider_name": "Alpha"}])
    rec = run_mod.apply_trust(models, "2026-11-23")
    m = models[LABEL]
    assert [e["tag"] for e in m["endpoints"]] == ["alpha"]
    assert m["untrusted"] == [{"tag": "novita/fp8", "provider_name": "Novita", "state": "untrusted",
                               "reason": f"open incident: Novita 2026-11-22 {BLOG}"}]
    assert [e["tag"] for e in m["listed"]] == ["alpha", "novita/fp8"]
    assert rec["zdr"] == "ok" and rec["flagged"][LABEL] == {"novita/fp8": f"open incident: Novita 2026-11-22 {BLOG}"}
    # Nothing is sent to a flagged endpoint.
    sent = []
    run_mod.send_all("r", models, [{"id": "p1", "family": "math", "prompt": "x"}], Path("out.jsonl"),
                     run_mod.Spend(1.0), completer=lambda slug, tag, msgs: sent.append(tag) or
                     {"status": "ok", "text": "", "provider": "Alpha", "usage": {}, "latency_ms": 1,
                      "finish_reason": "stop", "reasoning_mode": "none"})
    assert sent == ["alpha"]
