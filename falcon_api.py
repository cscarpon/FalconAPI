from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load Falcon model
from models.falcon_loader import load_falcon
model, tokenizer = load_falcon()

app = FastAPI()

# Serve frontend files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(request: PromptRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=200)
    return {"response": tokenizer.decode(output[0], skip_special_tokens=True)}