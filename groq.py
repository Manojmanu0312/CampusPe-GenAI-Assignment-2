import os
from groq import Groq

client = Groq(api_key=os.environ.get(""))

try:
    prompt = input("Enter your prompt: ")
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    print("Groq Response:", response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")