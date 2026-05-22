import os
import sys
import time
import json

# Add backend directory to path
sys.path.append("/app")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/backend')))

print("==================================================")
print("     DIAGNOSTIC TEST: GEMINI API & OLLAMA FALLBACK ")
print("==================================================")

try:
    import agent
    print("[+] SUCCESS: Imported backend agent module.")
except Exception as e:
    print(f"[-] ERROR: Failed to import agent module: {e}")
    sys.exit(1)

def run_provider_check():
    provider = agent.get_llm_provider()
    print(f"\n[*] Active Provider: {provider.upper()}")
    print(f"    - GEMINI_API_KEY: {'[CONFIGURED]' if agent.GEMINI_API_KEY else '[EMPTY]'}")
    print(f"    - MODEL_PROVIDER: {agent.MODEL_PROVIDER}")
    return provider

def test_chat_interface(expected_provider):
    print(f"\n[*] Testing chat interface (Expecting provider: {expected_provider.upper()})...")
    start_time = time.time()
    response = agent.practice_chat("Output the word 'HELLO' and nothing else.")
    elapsed = time.time() - start_time
    
    print(f"[+] Response time: {elapsed:.2f} seconds")
    print(f"[+] Response content: {repr(response)}")
    
    # Simple validation
    if not response or "Error connecting" in response:
        print("[-] FAILED: Chat interface returned error or empty response.")
        return False
    print("[+] SUCCESS: Chat interface is operational.")
    return True

def test_json_summarization():
    print("\n[*] Testing structured JSON news summarization...")
    prompt = """
    You are an AI assistant for an 'AI Learning Hub'. Summarize this news article:
    Title: Google Releases Gemini 1.5 Flash
    Content: Google has announced Gemini 1.5 Flash, a lighter-weight, faster model designed for high-frequency and speed-sensitive tasks, featuring a massive context window of up to 1 million tokens.
    
    Respond ONLY with a valid JSON object in this exact format:
    {"summary": "your summary here", "rating": 9}
    """
    
    # We will invoke the logic inside process_news_source or test it directly.
    # To avoid DB side-effects, we test LLM response parsing directly or mock the db part.
    # Let's test the active provider's behavior directly.
    provider = agent.get_llm_provider()
    print(f"[*] Calling provider {provider.upper()} for JSON output...")
    
    start_time = time.time()
    try:
        if provider == "gemini":
            import google.generativeai as genai
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    response_mime_type="application/json"
                )
            )
            content_resp = response.text.strip()
        else:
            active_model = agent.get_active_model()
            response = agent.ollama_client.chat(model=active_model, messages=[
                {'role': 'user', 'content': prompt}
            ])
            content_resp = response['message']['content'].strip()
            content_resp = content_resp.removeprefix("```json").removesuffix("```").strip()
            
        elapsed = time.time() - start_time
        print(f"[+] Response received in {elapsed:.2f}s")
        print(f"[+] Raw Response: {repr(content_resp)}")
        
        parsed = json.loads(content_resp)
        print(f"[+] Parsed JSON successfully: {parsed}")
        if "summary" in parsed and "rating" in parsed:
            print("[+] SUCCESS: Structured JSON summarization works.")
            return True
        else:
            print("[-] FAILED: JSON structure missing required fields.")
            return False
    except Exception as e:
        print(f"[-] FAILED: JSON generation or parsing error: {e}")
        return False

def main():
    # 1. Run with current env
    current_provider = run_provider_check()
    test_chat_interface(current_provider)
    test_json_summarization()
    
    # Keep track of old env
    old_key = agent.GEMINI_API_KEY
    old_provider = agent.MODEL_PROVIDER
    
    # 2. Test fallback by forcing Ollama provider
    print("\n==================================================")
    print("      MOCKING OLLAMA FALLBACK MODE (OFFLINE)      ")
    print("==================================================")
    
    agent.GEMINI_API_KEY = ""
    agent.MODEL_PROVIDER = "ollama"
    
    try:
        mocked_provider = run_provider_check()
        assert mocked_provider == "ollama", "Failed to mock Ollama fallback provider."
        test_chat_interface("ollama")
    finally:
        # Restore
        agent.GEMINI_API_KEY = old_key
        agent.MODEL_PROVIDER = old_provider
        
    # 3. Test active Gemini Mode with fake key to verify exception handling & Ollama fallback
    print("\n==================================================")
    print("      MOCKING GEMINI API MODE (WITH FAKE KEY)     ")
    print("==================================================")
    
    agent.GEMINI_API_KEY = "AIzaSyFakeKey_ForTestingOnly"
    agent.MODEL_PROVIDER = "gemini"
    import google.generativeai as genai
    genai.configure(api_key=agent.GEMINI_API_KEY)
    
    try:
        mocked_provider = run_provider_check()
        assert mocked_provider == "gemini", "Failed to mock Gemini active provider."
        print("[*] Sending chat request (Gemini should fail on fake key, falling back to Ollama)...")
        test_chat_interface("gemini")
    finally:
        # Restore
        agent.GEMINI_API_KEY = old_key
        agent.MODEL_PROVIDER = old_provider
        
    print("\n==================================================")
    print("             DIAGNOSTICS COMPLETED                ")
    print("==================================================")

if __name__ == "__main__":
    main()
