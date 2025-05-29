# Dark-Matter API 🚀

FastAPI micro-service that serves a pre-trained classifier for potential
dark-matter γ-ray sources (Fermi-LAT).

| Endpoint | Method | Input | Output |
|----------|--------|-------|--------|
| `/predict` | POST | JSON with source features | `{ "dark_matter_probability": 0.78 }` |

## Quickstart (locally)

```bash
docker build -t dark-matter .
docker run -p 8000:80 dark-matter
curl -X POST http://localhost:8000/predict -d '{"flux":0.3,...}'
```

## Tech stack
Python · scikit-learn · FastAPI · Docker · GitHub Actions


## Local Use Case
From terminal, navigate to the project and type:
```bash
uvicorn src.main:app --reload
```

Open another terminal and test the endpoint:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"E_peak": 2.1, "Beta": -0.9, "Sigma": 0.45, "Beta_rel": 0.22}'
```

I should return the anomaly score for the given input parameters (obtained from decision function), something like:
```bash
{"dark_matter_score":0.35423113674712003}%  
```

Or check out and explore the FastAPI UI while it's running! In your local browser, type:
```bash
http://localhost:8000/docs
```