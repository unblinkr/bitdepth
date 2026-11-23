import pytest

from probe import trust


@pytest.fixture(autouse=True)
def _no_zdr_network(monkeypatch):
    """No test reaches OpenRouter: the ZDR fetch fails as if offline unless a test patches it."""
    def offline(*a, **k):
        raise RuntimeError("offline in tests")
    monkeypatch.setattr(trust, "fetch_zdr", offline)
