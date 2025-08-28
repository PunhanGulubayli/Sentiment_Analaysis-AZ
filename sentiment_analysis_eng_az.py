# sentiment_analysis_eng_az.py
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from deep_translator import GoogleTranslator

# --- Data load və model train ---
df = pd.read_csv('../ML/training.1600000.processed.noemoticon.csv', encoding='latin-1', header=None)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df = df[[0, 5]]
df.columns = ['label', 'text']

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www.\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text

df['clean_text'] = df['text'].apply(clean_text)

y = df['label']
X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'], y, test_size=0.2, random_state=42, stratify=df["label"]
)

vectorizer = TfidfVectorizer(max_features=15000, ngram_range=(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=10000, C=10, penalty="l2")
model.fit(X_train_tfidf, y_train)

# LabelEncoder 0 və 4 üçün
le = LabelEncoder()
le.fit([0,4])

# Translator
def az_to_en(text):
    try:
        return GoogleTranslator(source='az', target='en').translate(text)
    except:
        return text

# Funksiya
def predict_sentiment(input_text, threshold=70):
    input_en = az_to_en(input_text)
    input_vector = vectorizer.transform([input_en])
    proba = model.predict_proba(input_vector)[0]
    idx = proba.argmax()
    confidence = proba[idx] * 100
    sentiment_label = le.inverse_transform([idx])[0]
    if confidence < threshold:
        return "Neutral", confidence
    if sentiment_label == 0:
        return "Negative", confidence
    elif sentiment_label == 4:
        return "Positive", confidence
    else:
        return "Neutral", confidence
