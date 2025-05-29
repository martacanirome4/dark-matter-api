from fastapi import FastAPI
from pydantic import BaseModel
from src.models.predict_4F import predict_proba

app = FastAPI()

class Source(BaseModel):
    E_peak: float
    Beta: float
    Sigma: float
    Beta_rel: float

@app.post("/predict")
def predict(source: Source):
    score = predict_proba(source.dict())
    return {"dark_matter_score": score}
