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


def test_findings_lead_and_delisted_marker():
    from probe import site
    def ep(tag, state, nights, last, mv=None, flag=False, string=60.0):
        series = [{"date": f"2026-11-{d:02d}", "exact": 90.0} for d in range(1, last + 1)]
        return {"tag": tag, "state": state, "nights": nights, "string": string, "exact": 90.0,
                "movement": mv, "movement_flag": flag, "nightly_exact": series,
                "price_in_per_m": 1.0, "price_out_per_m": 2.0}
    a = {"model": "x/a", "label": "A", "as_of": "2026-11-10", "primary_columns": ["string"],
         "endpoints": [ep("p1", "within", 10, 10), ep("p2", "within", 10, 10), ep("gone", "outside", 8, 3, string=20.0)]}
    b = {"model": "x/b", "label": "B", "as_of": "2026-11-10", "primary_columns": ["exact"],
         "endpoints": [ep("q1", "within", 10, 10), ep("drop", "outside", 10, 10, mv=-12.0, flag=True)]}
    ms = site.lead_order([b, a])
    assert ms[0] is a
    assert site.delisted(a, a["endpoints"][2]) == "2026-11-03"
    assert site.delisted(a, a["endpoints"][0]) is None
    m, e = site.drift_pick(ms)
    assert e["tag"] == "drop"
    html = site.findings(ms, "", "https://bitdepth.dev", "2026-11-10")
    assert "gone" in html and "not listed since" in html and "drop" in html
    assert "—" not in html
