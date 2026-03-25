import os
import requests

API_KEY = os.environ.get("")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

try:
    prompt = input("Enter your prompt: ")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    response.raise_for_status()
    print("Hugging Face Response:", response.json()[0]["generated_text"])
except Exception as e:
    print(f"Error: {e}")