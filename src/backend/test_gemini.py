import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY", "").strip()
print(f"API Key loaded (first 5 chars): {api_key[:5]}... (Length: {len(api_key)})")

if not api_key:
    print("Error: GEMINI_API_KEY is empty!")
    exit(1)

genai.configure(api_key=api_key)

try:
    print("Testing connection to gemini-2.5-flash...")
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Hello, respond in exactly one word: Success.")
    print("Response text:")
    print(response.text)
    print("Gemini API connection test: SUCCESS!")
except Exception as e:
    print("Gemini API connection test: FAILED!")
    import traceback
    traceback.print_exc()
