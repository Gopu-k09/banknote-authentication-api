from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("model.pkl")

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bank Note Authentication API is running!"}

@app.post("/predict")
def predict(note: BankNote):
    features = [[note.variance, note.skewness, note.curtosis, note.entropy]]
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
