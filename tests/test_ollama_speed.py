import os
import time
import requests
import ollama

def main():
    print("==================================================")
    print("     DIAGNOSTIC TEST: OLLAMA CONNECTION & SPEED   ")
    print("==================================================")
    
    # Read environment
    ollama_host = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")
    print(f"[*] Target Ollama Host: {ollama_host}")
    
    # 1. Test connection to Ollama Client
    try:
        start_time = time.time()
        client = ollama.Client(host=ollama_host, timeout=30.0)
        models_resp = client.list()
        models = [m['name'] for m in models_resp.get('models', [])]
        elapsed = time.time() - start_time
        print(f"[+] SUCCESS: Connected to Ollama server in {elapsed:.2f}s")
        print(f"[+] Available Models: {models}")
    except Exception as e:
        print(f"[-] ERROR: Failed to connect to Ollama server at {ollama_host}: {e}")
        return

    # 2. Identify active model
    default_model = "llama3"
    active_model = default_model
    if default_model in models:
        active_model = default_model
    elif f"{default_model}:latest" in models:
        active_model = f"{default_model}:latest"
    elif models:
        active_model = models[0]
        print(f"[*] Configured '{default_model}' not found. Selecting active fallback: '{active_model}'")
    else:
        print("[-] ERROR: No models downloaded on Ollama host. Run 'ollama pull llama3' on Mac host first.")
        return

    # 3. Test chat generation speed
    print(f"[*] Testing generation speed on model '{active_model}'...")
    try:
        start_time = time.time()
        response = client.chat(model=active_model, messages=[
            {'role': 'user', 'content': 'Output exact word "PONG" and nothing else.'}
        ])
        elapsed = time.time() - start_time
        answer = response['message']['content'].strip()
        print(f"[+] SUCCESS: Model answered: '{answer}'")
        print(f"[+] Generation time: {elapsed:.2f} seconds (Expected: < 5.0 seconds on GPU!)")
        if elapsed > 10.0:
            print("[-] WARNING: Response took more than 10 seconds. Check if host has hardware acceleration enabled.")
    except Exception as e:
        print(f"[-] ERROR: Chat generation failed: {e}")
        return

    # 4. Test Backend Endpoint
    print("\n[*] Testing Backend API Endpoint `/api/practice`...")
    backend_url = "http://localhost:8000/api/practice"
    # Fallback to backend container port if run on host
    try:
        start_time = time.time()
        payload = {"prompt": "Hello, who are you?"}
        res = requests.post(backend_url, json=payload, timeout=30.0)
        elapsed = time.time() - start_time
        if res.status_code == 200:
            data = res.json()
            print(f"[+] SUCCESS: Backend endpoint answered in {elapsed:.2f}s")
            print(f"[+] AI Response: {data.get('response')[:150]}...")
        else:
            print(f"[-] ERROR: Backend returned status code {res.status_code}: {res.text}")
    except Exception as e:
        print(f"[*] Backend not accessible at http://localhost:8000 directly from host (normal if inside docker with closed port). Let's try inside docker soon.")

    print("\n==================================================")
    print("             DIAGNOSTICS COMPLETED                ")
    print("==================================================")

if __name__ == "__main__":
    main()
