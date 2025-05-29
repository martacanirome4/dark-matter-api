from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.main import app


client = TestClient(app)

def test_predict_endpoint_returns_score():
    payload = {
        "E_peak": 2.1,
        "Beta": -0.9,
        "Sigma": 0.45,
        "Beta_rel": 0.22
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "dark_matter_score" in data
    assert isinstance(data["dark_matter_score"], float)
