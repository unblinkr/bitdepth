from probe import MODELS, is_active


def labels(date):
    return [m["label"] for m in MODELS if is_active(m, date)]


def test_core_models_run_every_night():
    for d in ("2026-11-13", "2026-11-15", "2026-11-17"):
        assert {"gpt-oss-120b", "deepseek-v4-pro", "deepseek-v4.1-flash-1017"} <= set(labels(d))


def test_newer_models_run_monday_and_thursday_only():
    newer = {"mistral-large-4-0", "glm-5.3-flash", "gemma-4-31b-it", "mimo-v2.6-pro"}
    assert newer <= set(labels("2026-11-16"))  # Monday
    assert newer <= set(labels("2026-11-19"))  # Thursday
    assert not newer & set(labels("2026-11-17"))  # Tuesday


def test_selfcheck_night_keeps_full_set():
    assert len(labels("2026-11-14")) == len(MODELS)


def test_from_date_still_applies():
    assert "glm-5.3-flash" not in labels("2026-11-09")
