from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

hf_token = "___"

# Загрузка модели и токенизатора
# model_name = "IlyaGusev/saiga_llama3_8b"
model_name = "___"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, hf_token=hf_token)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/predict")
def predict(data: dict):
    text = data.get('prompt', '')
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"result": result}
