from app.models.classification import classify_text

test_texts = [
    "I am feeling really happy today.",
    "I can't stop feeling anxious about my job.",
    "I am so depressed and lonely."
]

for text in test_texts:
    category = classify_text(text)
    print(f"Text: {text} => Category: {category}")
