import json
from pathlib import Path

from probe import budget


def _endpoints():
    return json.loads((Path(__file__).parent / "fixtures" / "endpoints_small.json").read_text())


def _prompts():
    return [
        {"id": "fixed-math-001", "family": "math", "prompt": "x" * 400, "answer": "1"},
        {"id": "fixed-needle-001", "family": "needle", "prompt": "y" * 4000, "answer": "A"},
        {"id": "fresh-2026-10-27-echo-001", "family": "echo", "prompt": "z" * 200, "answer": "z"},
    ]


def test_estimate_matches_hand_computation():
    eps = _endpoints()
    prompts = _prompts()
    # input tokens: 400/4+24=124, 4000/4+24=1024, 200/4+24=74 -> 1222
    # output tokens: math 96 + needle 64 + echo 256 = 416
    est = budget.estimate(eps, prompts)
    assert est["input_tokens_per_endpoint"] == 1222
    assert est["output_tokens_per_endpoint"] == 416
    cheap = 1222 * 0.0000001 + 416 * 0.0000005
    full = 1222 * 0.000001 + 416 * 0.000002
    assert abs(est["usd"] - round(cheap + full, 4)) < 1e-6
    assert est["per_model"]["alpha"] == round(cheap + full, 4)


def test_cap_drops_needle_then_fresh_then_aborts():
    eps = _endpoints()
    prompts = _prompts()
    full_est = budget.estimate(eps, prompts)["usd"]
    # cap just below the full estimate: needle goes first
    kept, dropped, est, aborted = budget.apply_cap(eps, prompts, cap=full_est - 1e-6)
    assert not aborted
    assert [p["id"] for p in dropped] == ["fixed-needle-001"]
    assert {p["family"] for p in kept} == {"math", "echo"}
    # cap below needle-less estimate: fresh goes next
    no_needle_est = budget.estimate(eps, [p for p in prompts if p["family"] != "needle"])["usd"]
    kept, dropped, est, aborted = budget.apply_cap(eps, prompts, cap=no_needle_est - 1e-6)
    assert not aborted
    assert [p["id"] for p in dropped] == ["fixed-needle-001", "fresh-2026-10-27-echo-001"]
    assert [p["id"] for p in kept] == ["fixed-math-001"]
    # cap below everything: abort, nothing kept, estimate reported
    kept, dropped, est, aborted = budget.apply_cap(eps, prompts, cap=0.0)
    assert aborted
    assert kept == []
    assert len(dropped) == 3
    assert est["usd"] > 0


def test_cap_passes_when_under():
    eps = _endpoints()
    prompts = _prompts()
    kept, dropped, est, aborted = budget.apply_cap(eps, prompts, cap=100.0)
    assert not aborted and not dropped and len(kept) == 3
