from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import re

app = FastAPI()


with open('..\\saved_model\\model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('..\\saved_model\\vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

class TextData(BaseModel):
    text: str

@app.post("/predict")
async def predict(data: TextData):
    emotion_labels = {
        0: "sadness",
        1: "happy",
        2: "love",
        3: "anger",
        4: "fear",
        5: "surprise"
    }

    text_vector = vectorizer.transform([data.text]).toarray()
    prediction = model.predict(text_vector)[0]
    return {"prediction": emotion_labels.get(prediction, "Unknown label")}


