import json
from pathlib import Path

from probe import site

DATA = Path(__file__).resolve().parent.parent / "data" / "public" / "v1"


def _model(endpoints, primary="string"):
    return {"model": "a/test-model", "as_of": "2026-11-04", "primary_columns": [primary], "endpoints": endpoints}


def _ep(tag, state, agree, pin, pout, nights=9):
    return {"tag": tag, "provider_slug": tag.split("/")[0], "state": state, "string": agree, "exact": agree,
            "self_agree": agree, "nights": nights, "price_in_per_m": pin, "price_out_per_m": pout,
            "declared_quant": "fp8", "movement": 0.0, "movement_flag": False}


def test_rank_is_quality_adjusted_and_outside_is_never_ranked():
    m = _model([
        _ep("cheap/fp4", "outside", 40.0, 0.1, 0.2),
        _ep("good/fp8", "within", 80.0, 0.5, 1.0),
        _ep("pricier/bf16", "within", 90.0, 1.0, 2.0),
        _ep("new/fp8", "no_data", 85.0, 0.2, 0.4, nights=2),
    ])
    r = site.rows(m)
    assert [e["tag"] for e in r["ranked"]] == ["good/fp8", "pricier/bf16"]
    assert [e["tag"] for e in r["outside"]] == ["cheap/fp4"]
    assert [e["tag"] for e in r["first"]] == ["new/fp8"]
    h = site.headline(m)
    assert "good/fp8" in h and "cheap/fp4" in h and "sits outside the reference" in h


def test_first_look_model_headline_has_no_rank():
    m = _model([_ep("x/fp8", "no_data", 70.0, 0.1, 0.2, nights=1)])
    assert site.headline(m).startswith("First look at")


def test_placeholder_names_no_real_provider():
    data = site.load(DATA)
    real = {e["provider_slug"] for m in data["models"] for e in m["endpoints"]}
    ph = site.placeholder(data)
    names = {e["provider_slug"] for m in ph["models"] for e in m["endpoints"]}
    assert names.isdisjoint(real)
    assert all(n.startswith("host-") for n in names)


def test_preview_build_is_noindex_and_carries_no_real_name(tmp_path):
    data = site.load(DATA)
    real = {e["provider_slug"] for m in data["models"] for e in m["endpoints"]}
    site.build(site.placeholder(data), tmp_path, "/lab", True, site.SITE + "/lab", home=True)
    html = "".join(p.read_text() for p in tmp_path.rglob("*.html"))
    assert 'content="noindex,nofollow"' in html
    assert "placeholder data" in html
    for name in real:
        assert f'class="ep">{name}/' not in html and f'class="ep">{name}<' not in html
    assert "—" not in html
    assert (tmp_path / "og" / "board.png").exists()
