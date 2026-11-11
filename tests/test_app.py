from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_index():
    resp = client().get("/")
    assert resp.status_code == 200
    assert "Hello" in resp.get_json()["message"]


def test_health():
    resp = client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}
