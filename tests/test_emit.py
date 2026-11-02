import json
from pathlib import Path

from probe import badge, emit, packet

DATE = "2026-11-02"


def _ep(tag, exact, agree, nights=7, move=0.0, flag=False):
    return {
        "tag": tag, "declared_quant": tag.split("/")[-1], "declared_changed": False, "nights": nights,
        "exact_by_night": {DATE: exact}, "exact_mean": exact, "exact_sd": 1.0, "exact_min": exact,
        "exact_max": exact, "movement": move, "movement_overlap": False, "movement_flag": flag,
        "families": {"math": 100.0, "json": 100.0, "string": 80.0, "needle": 100.0, "echo": 100.0},
        "self": {"pairs": 10, "agree_pct": agree, "by_family": {}},
        "selfcheck": {},
    }


def _write(root: Path) -> Path:
    fam = {f: {"endpoints": 3, "median_agree_pct": 100.0, "p75_disagree_pct": 0.0, "noise_floor": 100.0, "stable": True}
           for f in emit.FAMILIES}
    t = {
        "dates": [DATE], "selfcheck_dates": [], "thresholds": {"STABLE_MIN": 95.0, "MOVE_MIN": 10.0}, "window": 3,
        "models": [{
            "label": "m", "slug": "o/m", "rules": ["plurality among endpoints declaring bf16 or fp16"], "families": fam,
            "endpoints": [
                _ep("a/bf16", 97.0, 97.0),
                _ep("b/fp4", 95.0, 95.0, nights=6),
                _ep("c/fp8", 50.0, 80.0, move=-12.0, flag=True),
            ],
        }],
    }
    (root / "trend").mkdir()
    (root / "trend" / "latest.json").write_text(json.dumps(t))
    (root / "runs" / DATE).mkdir(parents=True)
    (root / "runs" / DATE / "endpoints.json").write_text(json.dumps({"models": {"m": {"endpoints": [
        {"tag": "a/bf16", "price_in": 1e-7, "price_out": 5e-7}]}}}))
    return root


def test_schema_and_states(tmp_path):
    root = _write(tmp_path)
    built = emit.build(root / "trend", root / "runs", None)
    d = built["models"][0]
    for k in ("schema", "model", "as_of", "nights", "reference_rule", "method_url", "primary_columns",
              "noise_floor", "endpoints", "footer", "state_rule"):
        assert k in d
    states = {e["tag"]: e["state"] for e in d["endpoints"]}
    assert states == {"a/bf16": "within", "b/fp4": "no_data", "c/fp8": "outside"}
    a = next(e for e in d["endpoints"] if e["tag"] == "a/bf16")
    assert a["price_in_per_m"] == 0.1 and a["price_out_per_m"] == 0.5


def test_stale():
    assert emit.state_of(7, 97.0, 97.0, "2026-11-01", "2026-11-05") == "stale"
    assert emit.state_of(7, 97.0, 97.0, "2026-11-01", "2026-11-04") == "within"


def test_drift_matches_flags_and_files(tmp_path):
    root = _write(tmp_path)
    built = emit.build(root / "trend", root / "runs", None)
    assert [i["tag"] for i in built["drift"]["items"]] == ["c/fp8"]
    paths = emit.write(tmp_path / "out", built)
    assert (tmp_path / "out" / "or" / "o" / "m.json") in paths
    idx = json.loads((tmp_path / "out" / "index.json").read_text())
    assert idx["models"][0]["path"] == "or/o/m.json"


def test_attestation_and_badge(tmp_path):
    root = _write(tmp_path)
    rc = packet.main(["--attestation", "--buyer", "Acme", "--providers", "a,c", "--month", "2026-11",
                      "--trend", str(root / "trend"), "--runs", str(root / "runs"),
                      "--scorecards", str(root / "sc"), "--out", str(tmp_path / "p")])
    assert rc == 0
    md = (tmp_path / "p" / "acme-attestation-2026-11.md").read_text()
    assert "| m | a/bf16 | bf16 | 1 of 1 |" in md
    assert "| m | c/fp8 | fp8 | 0 of 1 |" in md
    assert "\u2014" not in md
    t = json.loads((root / "trend" / "latest.json").read_text())
    assert badge.nights_inside(t, "a", "o/m", "2026-11") == (1, 1)
