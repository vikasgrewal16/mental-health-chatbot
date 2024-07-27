
from fastapi import FastAPI
from models.rag import generate_response
from models.classification import classify_text

app = FastAPI()

@app.post("/rag")
async def rag_endpoint(prompt: str):
    try:
        response = generate_response(prompt)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

@app.post("/classification")
async def classification_endpoint(text: str):
    try:
        category = classify_text(text)
        return {"category": category}
    except Exception as e:
        return {"error": str(e)}
