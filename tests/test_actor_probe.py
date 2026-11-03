"""Tests for the Apify probe actor logic. Reads the latest night from data/ on disk,
no network, no money."""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from actor import probe_one
from actor.probe_one import ProbeInputError

DATA = Path("data")


def _local_client() -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:
        rel = request.url.path.split("/main/data/", 1)[1]
        p = DATA / rel
        if not p.exists():
            return httpx.Response(404)
        return httpx.Response(200, content=p.read_bytes())
    return httpx.Client(transport=httpx.MockTransport(handler))


@pytest.fixture(scope="module")
def ref_oss():
    return probe_one.load_reference("openai/gpt-oss-120b", client=_local_client())


def _target(ref, tag):
    night = json.loads((DATA / "runs" / ref["night"] / "endpoints.json").read_text())
    return next(e for e in night["models"][ref["label"]]["endpoints"] if e["tag"] == tag)


def test_reference_is_fixed_prompts_only(ref_oss):
    assert ref_oss["night"] == json.loads((DATA / "public/v1/index.json").read_text())["as_of"]
    assert ref_oss["reference"]
    assert all(pid.startswith("fixed") for pid in ref_oss["reference"])
    assert ref_oss["nightly_fixed"]


def test_ungraded_model_is_refused():
    with pytest.raises(ProbeInputError):
        probe_one.load_reference("meta/llama-9", client=_local_client())


def test_perfect_endpoint_scores_100_and_is_chargeable(ref_oss, tmp_path):
    answers = {p["id"]: ref_oss["reference"][p["id"]] for p in ref_oss["prompts"] if p["id"] in ref_oss["reference"]}
    by_prompt = {p["prompt"]: answers[p["id"]] for p in ref_oss["prompts"] if p["id"] in answers}
    target = _target(ref_oss, "deepinfra/fp8")

    def completer(slug, tag, messages):
        return probe_one.openrouter._result("ok", "disabled", text=by_prompt[messages[0]["content"]],
                                            provider=target["provider_name"], usage={"cost": 0.0001}, latency_ms=10)

    out = probe_one.run_probe(ref_oss, target, completer, tmp_path, "openrouter")
    assert out["schema"] == "bitdepth.probe.v1"
    assert out["result"]["exact_pct"] == 100.0
    assert out["result"]["compared"] == len(answers)
    assert out["chargeable"] is True
    assert out["footer"] == probe_one.FOOTER
    col = out["against_last_night"]["columns"]["exact"]
    assert col["rank_among_last_night"] == f"1 of {len(ref_oss['nightly_fixed'])}"
    assert out["last_night_row"]["tag"] == "deepinfra/fp8"


def test_dead_endpoint_is_not_chargeable(ref_oss, tmp_path):
    target = _target(ref_oss, "deepinfra/fp8")
    dead = lambda slug, tag, messages: probe_one.openrouter._result("error", "none", error="http 503")
    out = probe_one.run_probe(ref_oss, target, dead, tmp_path, "openrouter")
    assert out["chargeable"] is False
    assert out["result"]["ok"] == 0


def test_misrouted_answers_are_counted(ref_oss, tmp_path):
    target = _target(ref_oss, "deepinfra/fp8")
    other = lambda slug, tag, messages: probe_one.openrouter._result("ok", "disabled", text="x", provider="SomeoneElse")
    out = probe_one.run_probe(ref_oss, target, other, tmp_path, "openrouter")
    assert out["result"]["misrouted"] == out["result"]["rows"]
    assert out["chargeable"] is False


def test_openrouter_tag_must_exist():
    lister = lambda slug: [{"tag": "a/fp8", "provider_name": "A"}]
    assert probe_one.openrouter_target("x", "a/fp8", lister=lister)["tag"] == "a/fp8"
    with pytest.raises(ProbeInputError):
        probe_one.openrouter_target("x", "b/fp4", lister=lister)


@pytest.mark.parametrize("url", ["http://example.com/v1", "https://127.0.0.1/v1", "https://10.0.0.5/v1",
                                 "https://169.254.169.254/v1", "ftp://example.com"])
def test_custom_url_refuses_unsafe_hosts(url):
    with pytest.raises(ProbeInputError):
        probe_one.custom_target(url, "m", None)


def test_custom_completer_sends_the_nightly_request_and_keeps_the_key_private():
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        seen.append((request.headers.get("authorization"), body))
        if "reasoning_effort" in body:
            return httpx.Response(400, json={"error": "unknown field reasoning_effort"})
        return httpx.Response(200, json={"choices": [{"message": {"content": "42"}, "finish_reason": "stop"}],
                                         "usage": {"prompt_tokens": 5, "completion_tokens": 1}})

    c = httpx.Client(transport=httpx.MockTransport(handler))
    complete = probe_one.custom_completer("https://inference.example.com/v1", "secret-key", "my-model", client=c)
    r = complete("s", "t", [{"role": "user", "content": "hi"}])
    assert r["status"] == "ok" and r["text"] == "42"
    assert seen[0][0] == "Bearer secret-key"
    assert seen[0][1]["reasoning_effort"] == "low" and "reasoning_effort" not in seen[1][1]
    for k, v in {"temperature": 0, "top_p": 1, "max_tokens": probe_one.MAX_TOKENS, "seed": probe_one.SEED, "model": "my-model"}.items():
        assert seen[1][1][k] == v
    assert "secret-key" not in json.dumps(r)
