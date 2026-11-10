import json
from pathlib import Path

from probe import report


def _public(tmp_path):
    pub = tmp_path / "public" / "x"
    pub.mkdir(parents=True)
    doc = {"model": "x/m", "label": "m", "as_of": "2026-11-08", "primary_columns": ["exact"], "endpoints": [
        {"tag": "good/fp8", "provider_slug": "good", "nights": 13, "exact": 96.0, "state": "within", "price_in_per_m": 0.1, "price_out_per_m": 0.2},
        {"tag": "cheap/fp8", "provider_slug": "cheap", "nights": 13, "exact": 95.0, "state": "within", "price_in_per_m": 0.05, "price_out_per_m": 0.1},
        {"tag": "bad/int4", "provider_slug": "bad", "nights": 13, "exact": 80.0, "state": "outside", "price_in_per_m": 0.3, "price_out_per_m": 0.6},
    ]}
    (pub / "m.json").write_text(json.dumps(doc))
    return tmp_path / "public", tmp_path / "runs"


def test_report_splits_spend_by_state_and_prices_the_alternative(tmp_path):
    public, runs = _public(tmp_path)
    grades = report.load_grades(public, runs)
    act = [
        {"date": "2026-11-05", "model": "x/m", "provider_name": "Bad", "usage": 10, "prompt_tokens": 1_000_000, "completion_tokens": 1_000_000},
        {"date": "2026-11-06", "model": "x/m", "provider_name": "Good", "usage": 30},
        {"date": "2026-11-06", "model": "y/closed", "provider_name": "Lab", "usage": 60},
    ]
    r = report.build(act, grades)
    assert r["total"] == 100
    assert r["by_state"] == {"outside": 10, "within": 30, "not_graded": 60}
    bad = [x for x in r["rows"] if x["provider"] == "Bad"][0]
    assert bad["alt_tag"] == "cheap/fp8"
    assert abs(bad["alt_cost"] - 0.15) < 1e-9
    md = report.render("Acme", r)
    assert "Outside the pack: $10.00 (10.0%)" in md
    assert "Not a claim about intent." in md


def test_main_reads_an_activity_file(tmp_path, monkeypatch):
    public, runs = _public(tmp_path)
    act = tmp_path / "act.json"
    act.write_text(json.dumps({"data": [{"date": "2026-11-07", "model": "x/m", "provider_name": "Good", "usage": 5}]}))
    out = tmp_path / "out"
    assert report.main(["--activity", str(act), "--for", "Acme", "--out", str(out), "--public", str(public), "--runs", str(runs)]) == 0
    assert (out / "acme-spend-2026-11-07.md").exists()
    assert (out / "acme-spend-2026-11-07.csv").exists()


def test_activity_rows_named_by_endpoint_tag_match_exactly(tmp_path):
    public, runs = _public(tmp_path)
    grades = report.load_grades(public, runs)
    r = report.build([{"date": "2026-11-06", "model": "x/m", "provider_name": "bad/int4", "usage": 7}], grades)
    assert r["rows"][0]["state"] == "outside"
    assert r["rows"][0]["tags"] == ["bad/int4"]
