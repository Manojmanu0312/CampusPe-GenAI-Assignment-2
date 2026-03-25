import os
import cohere

client = cohere.Client(os.environ.get(""))

try:
    prompt = input("Enter your prompt: ")
    response = client.chat(message=prompt)
    print("Cohere Response:", response.text)
except Exception as e:
    print(f"Error: {e}")