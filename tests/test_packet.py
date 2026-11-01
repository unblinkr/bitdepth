import json
from pathlib import Path

from probe import packet

DATE = "2026-11-01"


def _trend():
    def ep(tag, quant, exact, string, agree, move=0.0, flag=False, nights=6):
        return {
            "tag": tag, "declared_quant": quant, "declared_changed": False, "nights": nights,
            "exact_by_night": {DATE: exact}, "exact_mean": exact, "exact_sd": 1.0, "exact_min": exact,
            "exact_max": exact, "movement": move, "movement_overlap": False, "movement_flag": flag,
            "families": {"math": 100.0, "json": 100.0, "string": string, "needle": 100.0, "echo": 100.0},
            "self": {"pairs": 10, "agree_pct": agree, "by_family": {}},
            "selfcheck": {},
        }

    fam = {f: {"endpoints": 3, "median_agree_pct": 100.0, "p75_disagree_pct": 0.0, "noise_floor": 100.0, "stable": True}
           for f in ("math", "json", "string", "needle", "echo")}
    return {
        "dates": ["2026-10-30", "2026-10-31", DATE],
        "selfcheck_dates": [],
        "thresholds": {"STABLE_MIN": 95.0, "MOVE_MIN": 10.0},
        "window": 3,
        "models": [{
            "label": "m", "slug": "o/m", "rules": ["plurality among endpoints declaring bf16 or fp16"],
            "families": fam,
            "endpoints": [
                ep("a/bf16", "bf16", 97.0, 85.0, 97.0),
                ep("b/fp4", "fp4", 95.0, 80.0, 95.0),
                ep("c/fp8", "fp8", 90.0, 70.0, 90.0, move=-12.0, flag=True),
            ],
        }],
    }


def _write(root: Path):
    (root / "trend").mkdir()
    (root / "trend" / "latest.json").write_text(json.dumps(_trend()))
    run = root / "runs" / DATE
    run.mkdir(parents=True)
    run.joinpath("endpoints.json").write_text(json.dumps({"date": DATE, "models": {"m": {"slug": "o/m", "endpoints": [
        {"tag": "a/bf16", "price_in": 1e-7, "price_out": 5e-7},
        {"tag": "b/fp4", "price_in": 2e-7, "price_out": 6e-7},
    ]}}}))
    (root / "scorecard").mkdir()
    (root / "scorecard" / f"{DATE}.md").write_text(
        "# x\n\n## m (`o/m`)\n\n| a |\n\nReference rule: plurality among endpoints declaring bf16 or fp16. Reference endpoints: a/bf16. Prompts with no plurality (excluded from exact match): 0.\n")


def test_buyer_packet_marks_and_orders(tmp_path):
    _write(tmp_path)
    date, md, rows = packet.build("Acme", "buyer", ["b"], None, tmp_path / "runs", tmp_path / "trend", tmp_path / "scorecard")
    assert date == DATE
    assert rows[0]["endpoint"] == "b/fp4" and rows[0]["marked"]
    assert [r["endpoint"] for r in rows] == ["b/fp4", "a/bf16", "c/fp8"]
    assert rows[0]["price_in_per_m"] == 0.2 and rows[2]["price_in_per_m"] is None
    assert f"| {packet.MARK} | b/fp4 |" in md
    assert "-12.0 *" in md
    assert "Reference endpoints on 2026-11-01: a/bf16" in md
    assert "—" not in md


def test_provider_packet_names_only_its_own_rows(tmp_path):
    _write(tmp_path)
    _, md, rows = packet.build("C Corp", "provider", ["c"], None, tmp_path / "runs", tmp_path / "trend", tmp_path / "scorecard")
    assert [r["endpoint"] for r in rows] == ["c/fp8"]
    assert "a/bf16" not in md and "b/fp4" not in md
    assert "c/fp8: 3 of 3 by Exact, 3 of 3 by String." in md
    assert "Field by Exact: top 97.0, median 95.0, bottom 90.0" in md


def test_csv_and_slug(tmp_path):
    _write(tmp_path)
    _, _, rows = packet.build("Acme", "buyer", [], None, tmp_path / "runs", tmp_path / "trend", tmp_path / "scorecard")
    out = tmp_path / "p.csv"
    packet.write_csv(out, rows)
    lines = out.read_text().splitlines()
    assert lines[0].split(",") == packet.COLUMNS
    assert len(lines) == 4
    assert packet.slugify("Nano GPT, Inc.") == "nano-gpt-inc"
