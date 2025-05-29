import numpy as np
from pydantic import BaseModel

class SourceFeatures(BaseModel):
    E_peak: float
    Beta: float
    Sigma: float
    Beta_rel: float


def preprocess(input_dict):
    ordered = [
        input_dict["E_peak"],
        input_dict["Beta"],
        input_dict["Sigma"],
        input_dict["Beta_rel"]
    ]
    return np.array(ordered).reshape(1, -1)

