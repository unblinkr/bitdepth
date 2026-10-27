import json

from probe.generators import (
    FIXED_COUNTS,
    FRESH_COUNTS,
    fixed_set,
    fresh_set,
    generate_set,
    grade,
    grade_echo,
    grade_json,
    grade_math,
    grade_needle,
    grade_string,
)


def test_fixed_set_is_deterministic_and_counts_match():
    a = fixed_set()
    b = fixed_set()
    assert a == b
    assert len(a) == sum(FIXED_COUNTS.values())
    by_fam = {}
    for p in a:
        by_fam[p["family"]] = by_fam.get(p["family"], 0) + 1
    assert by_fam == FIXED_COUNTS


def test_fresh_set_counts_and_differs_by_date():
    a = fresh_set("2026-10-27")
    b = fresh_set("2026-10-28")
    assert len(a) == sum(FRESH_COUNTS.values())
    assert a == fresh_set("2026-10-27")
    assert [p["prompt"] for p in a] != [p["prompt"] for p in b]


def test_seeds_change_content():
    a = generate_set(1, {"math": 3, "json": 1, "string": 1, "needle": 1, "echo": 1}, "x")
    b = generate_set(2, {"math": 3, "json": 1, "string": 1, "needle": 1, "echo": 1}, "x")
    assert [p["prompt"] for p in a] != [p["prompt"] for p in b]


def test_leading_slice_is_a_mix():
    first = fixed_set()[:12]
    fams = {p["family"] for p in first}
    assert fams == {"math", "json", "string", "needle", "echo"}


def test_no_em_dash_anywhere():
    for p in fixed_set() + fresh_set("2026-10-27"):
        assert chr(0x2014) not in p["prompt"]
        assert chr(0x2014) not in p["answer"]


def _one(family):
    return next(p for p in fixed_set() if p["family"] == family)


def test_grade_math_pass_and_fail():
    p = _one("math")
    assert grade_math(f"The answer is {p['answer']}.", p["answer"])
    assert grade_math(f"Working: 12 then 15. Final: {p['answer']}", p["answer"])
    assert not grade_math(f"{p['answer']}1", p["answer"])
    assert not grade_math("no number here", p["answer"])


def test_grade_json_pass_and_fail():
    p = _one("json")
    good = p["answer"]
    assert grade_json(good, good, p["schema"])
    assert grade_json("```json\n" + good + "\n```", good, p["schema"])
    bad = json.loads(good)
    bad["items"][0] = "something else"
    assert not grade_json(json.dumps(bad), good, p["schema"])
    extra = json.loads(good)
    extra["note"] = "x"
    assert not grade_json(json.dumps(extra), good, p["schema"])


def test_grade_string_pass_and_fail():
    p = _one("string")
    assert grade_string(f"\"{p['answer']}\"\n", p["answer"])
    assert not grade_string(p["answer"] + "x", p["answer"])


def test_grade_needle_pass_and_fail():
    p = _one("needle")
    assert grade_needle(f"The code is {p['answer']}", p["answer"])
    assert not grade_needle("I could not find it", p["answer"])


def test_grade_echo_pass_and_fail():
    p = _one("echo")
    assert grade_echo(p["answer"] + "\n", p["answer"])
    assert not grade_echo("\"" + p["answer"] + "\"", p["answer"])


def test_dispatch_matches_direct():
    for fam in ("math", "json", "string", "needle", "echo"):
        p = _one(fam)
        assert grade(fam, p["answer"] if fam != "math" else p["answer"], p["answer"], p.get("schema"))
