from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, TextClassificationPipeline

model_name = "distilbert-base-uncased"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)
pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)

def generate_response(prompt: str) -> str:
    response = pipeline(prompt)
    return response
