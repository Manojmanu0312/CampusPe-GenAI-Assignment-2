import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get(""))

try:
    prompt = input("Enter your prompt: ")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    print("Gemini Response:", response.text)
except Exception as e:
    print(f"Error: {e}")