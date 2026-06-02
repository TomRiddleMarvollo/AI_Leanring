import os
import yaml
import ollama
from tools import search_web, fetch_content
from database import SessionLocal, NewsItem, LearningModule
from sources import AI_SOURCES
import json
import time
import concurrent.futures
import google.generativeai as genai

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
ollama_client = ollama.Client(host=OLLAMA_HOST, timeout=300.0)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "gemini").strip().lower()

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def get_llm_provider() -> str:
    """
    Returns 'gemini' if GEMINI_API_KEY is configured and MODEL_PROVIDER is 'gemini'.
    Otherwise returns 'ollama'.
    """
    if GEMINI_API_KEY and MODEL_PROVIDER == "gemini":
        return "gemini"
    return "ollama"

def get_ollama_models() -> list:
    """
    Returns a list of all model names pulled on the host Ollama.
    """
    try:
        models_resp = ollama_client.list()
        return [m['name'] for m in models_resp.get('models', [])]
    except Exception as e:
        print(f"Ollama list models error: {e}")
        return []

def get_active_model() -> str:
    """
    Checks the models available on the host Ollama.
    Falls back to the first available model if DEFAULT_MODEL is missing.
    """
    try:
        models_resp = ollama_client.list()
        models = [m['name'] for m in models_resp.get('models', [])]
        
        # Exact check
        if DEFAULT_MODEL in models:
            return DEFAULT_MODEL
            
        # Try :latest variant
        latest_variant = f"{DEFAULT_MODEL}:latest"
        if latest_variant in models:
            return latest_variant
            
        # Try fuzzy check
        for m in models:
            if DEFAULT_MODEL in m:
                return m
                
        # Fallback to first available model if any
        if models:
            print(f"Configured model '{DEFAULT_MODEL}' not found. Falling back to '{models[0]}'")
            return models[0]
            
        # No models found, but return DEFAULT_MODEL so it can fail gracefully
        return DEFAULT_MODEL
    except Exception as e:
        print(f"Ollama list models error: {e}")
        return DEFAULT_MODEL


def get_file_path(env_var, local_rel_path):
    path = os.getenv(env_var)
    if path and os.path.exists(path):
        return path
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    return os.path.join(base_dir, local_rel_path)

config_path = get_file_path('CONFIG_PATH', 'config.yaml')
try:
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        DEFAULT_MODEL = config.get('model', 'llama3')
except Exception as e:
    print(f"Warning: Could not load config.yaml: {e}")
    DEFAULT_MODEL = "llama3"

prompt_path = get_file_path('PROMPT_PATH', 'prompts/system_prompts/default_system.txt')
try:
    with open(prompt_path, 'r') as f:
        SYSTEM_PROMPT = f.read().strip()
except Exception as e:
    print(f"Warning: Could not load prompt file: {e}")
    SYSTEM_PROMPT = "You are a helpful AI assistant."

def process_news_source(source):
    db = SessionLocal()
    try:
        query = f"Latest AI advancements news site:{source}"
        # Limit to 2 per source to prevent model overload
        res = search_web(query, max_results=2)
        
        for item in res:
            title = item.get('title')
            url = item.get('href')
            snippet = item.get('body')
            
            exists = db.query(NewsItem).filter(NewsItem.url == url).first()
            if exists:
                continue
                
            content = fetch_content(url)
            text_to_summarize = content if content else snippet
            
            prompt = f"""
            You are an AI assistant for an 'AI Learning Hub'. Evaluate and summarize the following news article.
            Title: {title}
            Content: {text_to_summarize}
            
            Evaluate the quality of this article from 1 to 10 based on its VALUE FOR AI LEARNERS AND DEVELOPERS:
            - Technical & Educational Value (50%): Does it teach a new concept, algorithm, prompt technique, or release open-source code? (Give low scores to generic business/legal/PR news).
            - Actionability (30%): Can the reader practice or use this immediately? (e.g. contains code snippets, HuggingFace links, tutorials).
            - Clarity (20%): Is it explained clearly with facts/benchmarks rather than clickbait hype?
            
            Provide a concise, easy-to-read summary of the key technical points (under 200 words).
            Respond ONLY with a valid JSON object in this exact format, with no markdown code blocks or extra text:
            {{"summary": "your summary here", "rating": 8}}
            """
            
            try:
                provider = get_llm_provider()
                content_resp = None
                if provider == "gemini":
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        response = model.generate_content(
                            prompt,
                            generation_config=genai.types.GenerationConfig(
                                response_mime_type="application/json"
                            )
                        )
                        content_resp = response.text.strip()
                        print("News summarized successfully using Google Gemini 2.5 Flash.")
                    except Exception as gemini_err:
                        print(f"Gemini news summarization error: {gemini_err}. Falling back to Ollama...")
                        provider = "ollama"
                
                if provider == "ollama" or not content_resp:
                    active_model = get_active_model()
                    response = ollama_client.chat(model=active_model, messages=[
                        {'role': 'user', 'content': prompt}
                    ])
                    content_resp = response['message']['content'].strip()
                    content_resp = content_resp.removeprefix("```json").removesuffix("```").strip()
                    print(f"News summarized using Ollama model '{active_model}'.")
                
                parsed = json.loads(content_resp)
                summary = parsed.get("summary", "No summary provided.")
                rating = parsed.get("rating", 0)
                
                news_item = NewsItem(title=title, summary=summary, url=url, rating=rating)
                db.add(news_item)
                db.commit()
            except Exception as e:
                print(f"Error summarizing news from {source}: {e}")
                db.rollback()
    finally:
        db.close()

def process_learning_source(source):
    db = SessionLocal()
    try:
        query = f"AI best practices guide site:{source}"
        res = search_web(query, max_results=1)
        
        for item in res:
            title = item.get('title')
            url = item.get('href')
            snippet = item.get('body')
            
            exists = db.query(LearningModule).filter(LearningModule.title == title).first()
            if exists:
                continue
                
            content = fetch_content(url)
            text_to_summarize = content if content else snippet
            
            prompt = f"""
            Extract the core best practices from the following text to create a bite-sized learning module.
            Title: {title}
            Text: {text_to_summarize}
            
            Format your response as a clear markdown list of actionable tips.
            """
            
            try:
                provider = get_llm_provider()
                learning_content = None
                if provider == "gemini":
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        response = model.generate_content(prompt)
                        learning_content = response.text.strip()
                        print("Learning module generated successfully using Google Gemini 2.5 Flash.")
                    except Exception as gemini_err:
                        print(f"Gemini learning module error: {gemini_err}. Falling back to Ollama...")
                        provider = "ollama"
                
                if provider == "ollama" or not learning_content:
                    active_model = get_active_model()
                    response = ollama_client.chat(model=active_model, messages=[
                        {'role': 'user', 'content': prompt}
                    ])
                    learning_content = response['message']['content'].strip()
                    print(f"Learning module generated using Ollama model '{active_model}'.")
                
                category = "Prompt Engineering" if "prompt" in title.lower() else "General AI"
                
                module = LearningModule(title=title, content=learning_content, category=category)
                db.add(module)
                db.commit()
            except Exception as e:
                print(f"Error generating learning module from {source}: {e}")
                db.rollback()
    finally:
        db.close()

def run_all_background_tasks():
    """
    Main orchestration function to run all scraping tasks in the background.
    Uses ThreadPoolExecutor to run tasks concurrently but limits to 2 workers to prevent VRAM overflow.
    Adds sleep delays to avoid DuckDuckGo rate limiting.
    """
    all_sources = [url for category in AI_SOURCES.values() for url in category]
    
    print(f"Starting background scrape for {len(all_sources)} sources...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for source in all_sources:
            executor.submit(process_news_source, source)
            executor.submit(process_learning_source, source)
            # Add a 2-second delay between enqueuing/triggering duckduckgo search tools
            time.sleep(2)
    print("Background scrape completed.")

# Retained for legacy backwards compatibility in other modules if any
def summarize_news():
    pass
def fetch_best_practices():
    pass

import base64
import re

_SAFE_FILE_TYPES = {
    "text/plain", "text/markdown", "text/csv", "text/html",
    "application/json", "application/xml", "text/xml",
    "image/png", "image/jpeg", "image/gif", "image/webp",
    "audio/mpeg", "audio/wav", "video/mp4",
    "application/pdf",
}
_MAX_FILE_TEXT_CHARS = 12_000

def _sanitize_file_text(text: str) -> str:
    # Strip null bytes and limit length to prevent oversized prompts
    text = text.replace("\x00", "")
    return text[:_MAX_FILE_TEXT_CHARS]

def practice_chat(prompt: str, provider: str = None, model_name: str = None, system_prompt: str = None, file_data: str = None, file_name: str = None, file_type: str = None) -> str:
    if not provider:
        provider = get_llm_provider()
    else:
        provider = provider.lower().strip()
        
    active_sys_prompt = system_prompt if system_prompt is not None else SYSTEM_PROMPT
    
    has_file = file_data is not None and file_name is not None and file_type is not None
    is_binary = False

    if has_file:
        normalized_type = file_type.split(";")[0].strip().lower()
        if normalized_type not in _SAFE_FILE_TYPES:
            return f"Loại tệp '{normalized_type}' không được hỗ trợ."
        file_type = normalized_type
        is_binary = any(file_type.startswith(p) for p in ("image/", "audio/", "video/")) or file_type == "application/pdf"
        
    if provider == "gemini":
        try:
            model = genai.GenerativeModel(
                model_name='gemini-2.5-flash',
                system_instruction=active_sys_prompt
            )
            
            if has_file:
                file_bytes = base64.b64decode(file_data)
                if is_binary:
                    # Use Gemini native multimodal capability
                    file_part = {
                        "mime_type": file_type,
                        "data": file_bytes
                    }
                    contents = [file_part, prompt]
                    response = model.generate_content(contents)
                else:
                    try:
                        decoded_text = _sanitize_file_text(file_bytes.decode('utf-8'))
                        augmented_prompt = f"Tài liệu đính kèm ({file_name}):\n```\n{decoded_text}\n```\n\nYêu cầu người dùng:\n{prompt}"
                        response = model.generate_content(augmented_prompt)
                    except Exception:
                        file_part = {
                            "mime_type": file_type,
                            "data": file_bytes
                        }
                        contents = [file_part, prompt]
                        response = model.generate_content(contents)
            else:
                response = model.generate_content(prompt)
                
            return response.text.strip()
        except Exception as gemini_err:
            print(f"Gemini chat error: {gemini_err}. Falling back to Ollama...")
            provider = "ollama"
            
    if provider == "ollama":
        try:
            if model_name:
                active_model = model_name
            else:
                active_model = get_active_model()
                
            active_prompt = prompt
            if has_file:
                file_bytes = base64.b64decode(file_data)
                if is_binary:
                    return f"Mô hình Local Ollama hiện tại chưa hỗ trợ phân tích trực tiếp các tệp tin nhị phân (PDF, Hình ảnh, Âm thanh, Video). Vui lòng chuyển sang mô hình Google Gemini ở dưới để phân tích tài liệu đính kèm '{file_name}'."
                else:
                    try:
                        decoded_text = _sanitize_file_text(file_bytes.decode('utf-8'))
                        active_prompt = f"Tài liệu đính kèm ({file_name}):\n```\n{decoded_text}\n```\n\nYêu cầu người dùng:\n{prompt}"
                    except Exception:
                        return f"Không thể giải mã văn bản của tệp '{file_name}'. Vui lòng đảm bảo tệp sử dụng định dạng mã hóa văn bản UTF-8 hoặc chuyển sang sử dụng Google Gemini."
                        
            response = ollama_client.chat(model=active_model, messages=[
                {'role': 'system', 'content': active_sys_prompt},
                {'role': 'user', 'content': active_prompt}
            ])
            return response['message']['content'].strip()
        except Exception as ollama_err:
            print(f"Ollama chat error: {ollama_err}")
            return f"Error connecting to AI models. (Gemini API failed, and local Ollama '{model_name or DEFAULT_MODEL}' is unreachable: {ollama_err})"

