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


def test_route_list_follows_check_before_route(tmp_path):
    built = emit.build(_write(tmp_path) / "trend", tmp_path / "runs", None)
    r = built["routes"][0]
    assert r["schema"] == "bitdepth.routelist.v1"
    assert r["allow"] == ["a/bf16"]
    assert r["openrouter"] == {"provider": {"only": ["a/bf16"], "sort": "price", "allow_fallbacks": True}}
    why = {x["tag"]: x["why"] for x in r["excluded"]}
    assert why == {"b/fp4": "only 6 nights; 7 needed", "c/fp8": "outside"}
    rows = {e["tag"]: e for e in built["models"][0]["endpoints"]}
    for tag, row in rows.items():
        assert (tag in r["allow"]) == (row["state"] == "within" and row["nights"] >= emit.MIN_ROUTE_NIGHTS)
    assert built["index"]["models"][0]["routes_path"] == "routes/o/m.json"
    paths = emit.write(tmp_path / "out", built)
    assert (tmp_path / "out" / "routes" / "o" / "m.json") in paths


def test_route_list_rule_matches_mcp():
    root = Path(__file__).resolve().parents[1] / "site" / "api"
    lib = (root / "_lib" / "routes.js").read_text()
    assert f"export const MIN_ROUTE_NIGHTS = {emit.MIN_ROUTE_NIGHTS};" in lib
    assert 'e.state === "within"' in lib
    assert 'from "./_lib/routes.js"' in (root / "mcp.js").read_text()


def test_empty_route_list_has_no_provider_block(tmp_path):
    root = _write(tmp_path)
    t = json.loads((root / "trend" / "latest.json").read_text())
    t["models"][0]["endpoints"] = [t["models"][0]["endpoints"][2]]
    (root / "trend" / "latest.json").write_text(json.dumps(t))
    r = emit.build(root / "trend", root / "runs", None)["routes"][0]
    assert r["allow"] == [] and r["openrouter"] is None


def test_route_list_leaves_out_a_slug_that_shadows_a_left_out_endpoint(tmp_path):
    root = _write(tmp_path)
    t = json.loads((root / "trend" / "latest.json").read_text())
    eps = t["models"][0]["endpoints"]
    eps.append(_ep("c", 97.0, 97.0))  # bare slug "c" would also match "c/fp8", which is outside
    (root / "trend" / "latest.json").write_text(json.dumps(t))
    r = emit.build(root / "trend", root / "runs", None)["routes"][0]
    assert "c" not in r["allow"]
    assert {x["tag"]: x["why"] for x in r["excluded"]}["c"] == "would also match c/fp8"


def test_gap_threshold_is_fifteen():
    from probe.emit import state_of
    assert state_of(7, 80.0, 94.0, "2026-11-10", "2026-11-10") == "within"
    assert state_of(7, 80.0, 95.5, "2026-11-10", "2026-11-10") == "outside"


def test_floor_test_marks_far_below_pack_outside():
    from probe.emit import apply_floor
    rows = [{"tag": t, "nights": 13, "exact": v, "state": "within"} for t, v in
            [("a", 96.0), ("b", 95.0), ("c", 97.0), ("d", 94.0), ("low", 85.9), ("edge", 88.5)]]
    rows.append({"tag": "young", "nights": 3, "exact": 50.0, "state": "no_data"})
    apply_floor(rows, "exact")
    states = {r["tag"]: r["state"] for r in rows}
    # median of the 13-night endpoints is 94.5; floor is 86.5
    assert states["low"] == "outside"
    assert states["edge"] == "within"
    assert states["young"] == "no_data"
    assert states["a"] == "within"


def test_flash_is_pinned_to_exact():
    from probe.emit import primary_columns
    assert primary_columns("deepseek/deepseek-v4.1-flash-1017", {"math": {"stable": False}}) == ["exact"]
