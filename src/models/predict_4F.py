import joblib
from src.utils.preprocessing_4F import preprocess

model = joblib.load("src/models/model_ocsvm_4f.pkl")

def predict_proba(input_dict):
    x = preprocess(input_dict)
    score = model.decision_function(x)  # or model.predict(x)
    return float(score)  # ensure it's JSON serializable
