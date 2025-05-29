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
