import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get(""))

try:
    prompt = input("Enter your prompt: ")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print("OpenAI Response:", response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")