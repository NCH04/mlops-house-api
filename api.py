# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("regression.joblib")

class House(BaseModel):
    size: float
    nb_rooms: int
    garden: int

@app.post("/predict")
def predict(house: House):
    X = pd.DataFrame([house.model_dump()])
    y_pred = model.predict(X)[0]
    return {"y_pred": float(y_pred)}