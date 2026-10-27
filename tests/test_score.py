from probe.score import build_reference, endpoint_metrics, noise_floor


def _ep(tag, quant):
    return {"provider_name": tag.split("/")[0], "tag": tag, "quantization": quant, "supported_parameters": ["seed"],
            "price_in": 0, "price_out": 0}


def _row(tag, pid, out, status="ok", finish="stop"):
    return {"pinned_tag": tag, "prompt_id": pid, "output": out, "status": status, "finish_reason": finish,
            "latency_ms": 10, "cost_usd": 0.0, "model": "m"}


def test_reference_plurality_among_bf16_wins():
    eps = [_ep("a/bf16", "bf16"), _ep("b/bf16", "bf16"), _ep("c/fp16", "fp16"), _ep("d/fp4", "fp4")]
    rows = [_row("a/bf16", "p1", "4"), _row("b/bf16", "p1", "4"), _row("c/fp16", "p1", "5"), _row("d/fp4", "p1", "5")]
    ref, rule, no_ref, tags = build_reference(eps, rows)
    assert ref == {"p1": "4"}
    assert "bf16" in rule
    assert no_ref == 0
    assert set(tags) == {"a/bf16", "b/bf16", "c/fp16"}


def test_reference_tie_yields_no_reference():
    eps = [_ep("a/bf16", "bf16"), _ep("b/bf16", "bf16")]
    rows = [_row("a/bf16", "p1", "4"), _row("b/bf16", "p1", "5")]
    ref, rule, no_ref, tags = build_reference(eps, rows)
    assert ref == {}
    assert no_ref == 1


def test_reference_falls_back_to_all_when_fewer_than_two_full_precision():
    eps = [_ep("a/bf16", "bf16"), _ep("d/fp4", "fp4"), _ep("e/fp8", "fp8")]
    rows = [_row("a/bf16", "p1", "4"), _row("d/fp4", "p1", "5"), _row("e/fp8", "p1", "5")]
    ref, rule, no_ref, tags = build_reference(eps, rows)
    assert ref == {"p1": "5"}
    assert "all endpoints" in rule
    assert set(tags) == {"a/bf16", "d/fp4", "e/fp8"}


def test_misrouted_rows_excluded_from_metrics():
    ep = _ep("d/fp4", "fp4")
    prompts = {"p1": {"id": "p1", "family": "math", "prompt": "", "answer": "4"},
               "p2": {"id": "p2", "family": "math", "prompt": "", "answer": "4"}}
    rows = [_row("d/fp4", "p1", "4"), _row("d/fp4", "p2", "4", status="misrouted")]
    m = endpoint_metrics(ep, rows, {"p1": "4", "p2": "4"}, prompts)
    assert m["compared"] == 1
    assert m["exact_pct"] == 100.0
    assert m["misrouted"] == 1
    assert m["math"] == 100.0


def test_divergence_and_truncation_counted():
    ep = _ep("d/fp4", "fp4")
    prompts = {"p1": {"id": "p1", "family": "echo", "prompt": "", "answer": "a b c"}}
    rows = [_row("d/fp4", "p1", "a b d", finish="length")]
    m = endpoint_metrics(ep, rows, {"p1": "a b c"}, prompts)
    assert m["exact_pct"] == 0.0
    assert m["divergence_median"] == 2
    assert m["truncated"] == 1
    assert m["echo"] == 0.0


def test_noise_floor_agreement():
    rows = [
        dict(_row("d/fp4", "p1", "x"), **{"pass": "A"}),
        dict(_row("d/fp4", "p1", "x"), **{"pass": "B"}),
        dict(_row("d/fp4", "p2", "x"), **{"pass": "A"}),
        dict(_row("d/fp4", "p2", "y"), **{"pass": "B"}),
    ]
    nf = noise_floor(rows)
    a = nf["m|d/fp4"]
    assert a["n"] == 2 and a["agree"] == 1 and a["agree_pct"] == 50.0
