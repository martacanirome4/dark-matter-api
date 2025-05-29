import requests

payload = {
    "E_peak": 2.1,
    "Beta": -0.9,
    "Sigma": 0.45,
    "Beta_rel": 0.22
}

res = requests.post("http://localhost:8000/predict", json=payload)
print(res.json())
