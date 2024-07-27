import joblib

def classify_text(text: str) -> str:
    vectorizer = joblib.load("app/data/vectorizer.pkl")
    model = joblib.load("app/data/model.pkl")
    X = vectorizer.transform([text])
    category = model.predict(X)[0]
    return category
