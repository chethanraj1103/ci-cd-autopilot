import json
from app import app


def test_home():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    j = r.get_json()
    assert "message" in j


def test_predict():
    client = app.test_client()
    r = client.post("/predict", json={"x": 3})
    assert r.status_code == 200
    j = r.get_json()
    assert j["y"] == 6
