from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_ID = "tiiuae/falcon-7b-instruct"

def load_falcon():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map="cuda", torch_dtype=torch.float16)
    return model, tokenizer