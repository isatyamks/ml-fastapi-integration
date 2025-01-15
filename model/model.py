import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

nltk.download('stopwords')
nltk.download('wordnet')

data = pd.read_csv('data\\train.csv')

stop_words = stopwords.words('english')
lem = WordNetLemmatizer()

def fun_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    text = ' '.join([lem.lemmatize(word) for word in text.split() if word not in stop_words])
    return text

data['cleaned_text'] = data['text'].apply(fun_text)

X = data['cleaned_text']
Y = data['label']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=45)

vectorizer = TfidfVectorizer(max_features=5000)
X_train_vect = vectorizer.fit_transform(X_train).toarray()
X_test_vect = vectorizer.transform(X_test).toarray()

model = LogisticRegression()
model.fit(X_train_vect, Y_train)

# with open('saved_model\\model.pkl', 'wb') as file:
#     pickle.dump(model, file)
# with open('saved_model\\vectorizer.pkl', 'wb') as file:
#     pickle.dump(vectorizer, file)

def predict(text):
    cleaned_text = fun_text(text)
    vect_text = vectorizer.transform([cleaned_text]).toarray()
    prediction = model.predict(vect_text)
    return prediction[0]

# Example usage
input_text = "i am sad"
print(f"Prediction: {predict(input_text)}")
