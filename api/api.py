from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

# Initialize FastAPI app
app = FastAPI()

# Load stopwords and lemmatizer
stop_words = stopwords.words('english')
lem = WordNetLemmatizer()

# Load the saved model and vectorizer
with open('..\\saved_model\\model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('..\\saved_model\\vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define input data schema
class TextData(BaseModel):
    text: str

# Text preprocessing function
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\\s]', '', text.lower())
    text = ' '.join([lem.lemmatize(word) for word in text.split() if word not in stop_words])
    return text

@app.post("/predict")
async def predict(data: TextData):
    try:
        # Preprocess the input text
        cleaned_text = preprocess_text(data.text)

        # Transform the text using the vectorizer
        text_vector = vectorizer.transform([cleaned_text]).toarray()

        # Predict using the loaded model
        prediction = model.predict(text_vector)

        # Return the prediction
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Text Prediction API! Use /predict endpoint to get predictions."}
