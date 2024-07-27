
try:
    from app.models.rag import generate_response
    from app.models.classification import classify_text
    print("Imports are successful.")
except ImportError as e:
    print(f"Import error: {e}")
