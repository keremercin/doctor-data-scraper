from fastapi.testclient import TestClient

from doctor_scraper.api.main import app


def test_health() -> None:
    c = TestClient(app)
    r = c.get("/health")
    assert r.status_code == 200
