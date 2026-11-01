import json
from pathlib import Path

from probe import trend
from probe.trend import THRESHOLDS, build, load_nights, movement, percentile, render

MODEL = "m"
TAGS = {"a/bf16": "bf16", "b/bf16": "bf16", "c/fp4": "fp4"}

# Four fixed prompts (two math, two string) and one fresh math prompt per night.
FIXED = [
    {"id": "fixed-math-001", "family": "math", "prompt": "", "answer": "4"},
    {"id": "fixed-string-001", "family": "string", "prompt": "", "answer": "abc"},
    {"id": "fixed-math-002", "family": "math", "prompt": "", "answer": "9"},
    {"id": "fixed-string-002", "family": "string", "prompt": "", "answer": "xyz"},
]
DATES = ["2026-11-01", "2026-11-02", "2026-11-03", "2026-11-04"]


def _endpoint(tag):
    return {"provider_name": tag.split("/")[0], "tag": tag, "quantization": TAGS[tag],
            "price_in": 0, "price_out": 0, "supported_parameters": ["seed"]}


def _row(tag, pid, family, out, status="ok", extra=None):
    r = {"model": MODEL, "slug": "m/m", "prompt_id": pid, "family": family, "pinned_tag": tag, "output": out,
         "status": status, "finish_reason": "stop", "latency_ms": 10, "cost_usd": 0.0}
    if extra:
        r.update(extra)
    return r


def _write_night(root: Path, date: str, outputs: dict, selfcheck=None):
    """outputs: tag -> {prompt_id: output}. Every fixed prompt plus one fresh math prompt."""
    d = root / date
    d.mkdir(parents=True)
    fresh = {"id": f"fresh-{date}-math-001", "family": "math", "prompt": "", "answer": "7"}
    prompts = FIXED + [fresh]
    (d / "endpoints.json").write_text(json.dumps({"date": date, "models": {MODEL: {"slug": "m/m", "endpoints": [_endpoint(t) for t in TAGS]}}}))
    (d / "prompts.jsonl").write_text("\n".join(json.dumps(p) for p in prompts) + "\n")
    rows = []
    for tag, outs in outputs.items():
        for p in prompts:
            rows.append(_row(tag, p["id"], p["family"], outs.get(p["id"], f"{date} 7")))  # fresh output: right answer, wording differs nightly
    (d / "responses.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    (d / "run.json").write_text(json.dumps({"run_id": f"{date}-local", "date": date}))
    if selfcheck:
        (d / "selfcheck.jsonl").write_text("\n".join(json.dumps(r) for r in selfcheck) + "\n")


def _fixture(tmp_path: Path) -> Path:
    runs = tmp_path / "runs"
    good = {"fixed-math-001": "4", "fixed-string-001": "abc", "fixed-math-002": "9", "fixed-string-002": "xyz"}
    for i, date in enumerate(DATES):
        a = dict(good)
        b = dict(good)
        c = dict(good)
        if i == 1:
            b["fixed-string-001"] = "abd"  # b flips one fixed string prompt on night two
        if i >= 2:
            c["fixed-math-001"] = "5"  # c moves on the last two nights: wrong on one math prompt
            c["fixed-string-002"] = "xyy"
        selfcheck = None
        if i == 0:
            selfcheck = [
                _row("a/bf16", "fixed-math-001", "math", "4", extra={"pass": "A"}),
                _row("a/bf16", "fixed-math-001", "math", "4", extra={"pass": "B"}),
                _row("a/bf16", "fixed-string-001", "string", "abc", extra={"pass": "A"}),
                _row("a/bf16", "fixed-string-001", "string", "abd", extra={"pass": "B"}),
            ]
        _write_night(runs, date, {"a/bf16": a, "b/bf16": b, "c/fp4": c}, selfcheck=selfcheck)
    return runs


def _ep(t, tag):
    return next(e for e in t["models"][0]["endpoints"] if e["tag"] == tag)


def test_load_nights_respects_date_and_order(tmp_path):
    runs = _fixture(tmp_path)
    nights = load_nights(runs, "2026-11-02")
    assert [n["date"] for n in nights] == DATES[:2]
    assert len(load_nights(runs, "2026-12-01")) == 4


def test_exact_history_mean_and_sd(tmp_path):
    t = build(load_nights(_fixture(tmp_path), "2026-11-04"))
    a = _ep(t, "a/bf16")
    assert a["nights"] == 4
    assert list(a["exact_by_night"].values()) == [100.0, 100.0, 100.0, 100.0]
    assert a["exact_mean"] == 100.0 and a["exact_sd"] == 0.0
    c = _ep(t, "c/fp4")
    # reference is the plurality among a and b (both bf16); c differs on two of five prompts on nights three and four
    assert list(c["exact_by_night"].values()) == [100.0, 100.0, 60.0, 60.0]
    assert c["exact_min"] == 60.0 and c["exact_max"] == 100.0


def test_movement_overlaps_below_six_nights_and_flags_at_move_min(tmp_path):
    assert movement([100.0, 100.0, 60.0, 60.0]) == (-13.3, True)
    assert movement([1.0]) == (None, False)
    t = build(load_nights(_fixture(tmp_path), "2026-11-04"))
    c = _ep(t, "c/fp4")
    assert c["movement"] == -13.3 and c["movement_overlap"] is True
    assert abs(c["movement"]) >= THRESHOLDS["MOVE_MIN"]
    assert c["movement_flag"] is True
    assert _ep(t, "a/bf16")["movement_flag"] is False


def test_self_agreement_counts_fixed_pairs_only(tmp_path):
    t = build(load_nights(_fixture(tmp_path), "2026-11-04"))
    a = _ep(t, "a/bf16")
    # four fixed prompts, three consecutive-night pairs; the fresh prompt changes nightly and is excluded
    assert a["self"]["pairs"] == 12
    assert a["self"]["agree_pct"] == 100.0
    b = _ep(t, "b/bf16")
    # b's flip on night two disagrees with night one and with night three: two of twelve pairs
    assert b["self"]["pairs"] == 12
    assert b["self"]["agree_pct"] == round(100 * 10 / 12, 1)
    assert b["self"]["by_family"]["math"] == {"pairs": 6, "agree_pct": 100.0}
    assert b["self"]["by_family"]["string"] == {"pairs": 6, "agree_pct": round(100 * 4 / 6, 1)}
    c = _ep(t, "c/fp4")
    # c changes two prompts between night two and night three only: two of twelve pairs disagree
    assert c["self"]["agree_pct"] == round(100 * 10 / 12, 1)


def test_family_means_and_noise_floor(tmp_path):
    t = build(load_nights(_fixture(tmp_path), "2026-11-04"))
    c = _ep(t, "c/fp4")
    # math: three prompts a night (two fixed, one fresh), c wrong on one on two of four nights
    assert c["families"]["math"] == round((100 + 100 + 66.7 + 66.7) / 4, 1)
    assert c["families"]["string"] == 75.0
    fam = t["models"][0]["families"]
    assert fam["math"]["endpoints"] == 3
    assert fam["math"]["median_agree_pct"] == 100.0
    # string self-agreement: a 100, b 66.7, c 83.3 -> disagreement 0, 33.3, 16.7 -> p75 of [0, 16.7, 33.3] = 25.0
    assert fam["string"]["p75_disagree_pct"] == 25.0
    assert fam["string"]["noise_floor"] == 75.0
    assert fam["string"]["stable"] is False
    assert fam["needle"]["endpoints"] == 0 and fam["needle"]["noise_floor"] is None


def test_stable_flips_at_threshold(tmp_path, monkeypatch):
    nights = load_nights(_fixture(tmp_path), "2026-11-04")
    monkeypatch.setitem(trend.THRESHOLDS, "STABLE_MIN", 80.0)
    fam = build(nights)["models"][0]["families"]
    assert fam["string"]["median_agree_pct"] == 83.3
    assert fam["string"]["stable"] is True
    monkeypatch.setitem(trend.THRESHOLDS, "STABLE_MIN", 90.0)
    assert build(nights)["models"][0]["families"]["string"]["stable"] is False


def test_selfcheck_joined_by_night(tmp_path):
    t = build(load_nights(_fixture(tmp_path), "2026-11-04"))
    assert t["selfcheck_dates"] == ["2026-11-01"]
    a = _ep(t, "a/bf16")
    assert a["selfcheck"]["2026-11-01"]["agree_pct"] == 50.0
    assert a["selfcheck"]["2026-11-01"]["n"] == 2
    assert _ep(t, "b/bf16")["selfcheck"]["2026-11-01"] is None


def test_render_has_tables_and_footer(tmp_path):
    t = build(load_nights(_fixture(tmp_path), "2026-11-04"))
    text = render("2026-11-04", t)
    assert "# Bitdepth trend through 2026-11-04" in text
    assert "| Endpoint | Declared quant | Nights | 11-01 | 11-02 | 11-03 | 11-04 | Mean | SD | Min | Max | Movement |" in text
    assert "| c/fp4 | fp4 | 4 | 100.0 | 100.0 | 60.0 | 60.0 | 80.0 | 20.0 | 60.0 | 100.0 | -13.3 * |" in text
    assert "Self-check 11-01 |" in text
    assert "### Noise floor by family (night-to-night)" in text
    assert "- Nights found: 4. Self-check nights found: 1 (2026-11-01)." in text
    assert "Numbers against a stated reference. Not a claim about intent." in text
    assert chr(0x2014) not in text  # no em dash anywhere in the rendered file


def test_percentile_interpolates():
    assert percentile([], 75) is None
    assert percentile([5.0], 75) == 5.0
    assert percentile([0.0, 10.0, 20.0, 30.0], 50) == 15.0
    assert percentile([0.0, 16.7, 33.3], 75) == 25.0


def test_main_writes_files_and_latest(tmp_path):
    runs = _fixture(tmp_path)
    out = tmp_path / "trend"
    assert trend.main(["--date", "2026-11-04", "--runs", str(runs), "--out", str(out)]) == 0
    assert (out / "2026-11-04.md").exists() and (out / "2026-11-04.json").exists()
    assert (out / "latest.md").read_text() == (out / "2026-11-04.md").read_text()
    assert trend.main(["--date", "2026-10-01", "--runs", str(runs), "--out", str(out)]) == 2
