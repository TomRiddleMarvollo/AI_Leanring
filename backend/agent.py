import os
import ollama
from tools import search_web, fetch_content
from database import SessionLocal, NewsItem, LearningModule
from sources import get_random_sources
import json

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama3")

# Set ollama client to point to host if needed, but normally ollama library picks up OLLAMA_HOST
# or we can use the default global client.

def summarize_news():
    """
    Finds news from prioritized sources, reads content, asks Ollama to summarize, and saves to DB.
    """
    db = SessionLocal()
    try:
        sources = get_random_sources(2)
        all_results = []
        for source in sources:
            query = f"Latest AI advancements news site:{source}"
            res = search_web(query, max_results=2)
            all_results.extend(res)
            
        for res in all_results:
            title = res.get('title')
            url = res.get('href')
            snippet = res.get('body')
            
            exists = db.query(NewsItem).filter(NewsItem.url == url).first()
            if exists:
                continue
                
            content = fetch_content(url)
            text_to_summarize = content if content else snippet
            
            prompt = f"""
            You are an AI assistant. Summarize the following news article about AI.
            Title: {title}
            Content: {text_to_summarize}
            
            Provide a concise, easy-to-read summary of the key advancements mentioned.
            Respond ONLY with the summary. Keep it under 200 words.
            """
            
            try:
                response = ollama.chat(model=DEFAULT_MODEL, messages=[
                    {'role': 'user', 'content': prompt}
                ])
                summary = response['message']['content'].strip()
                
                news_item = NewsItem(title=title, summary=summary, url=url)
                db.add(news_item)
                db.commit()
            except Exception as e:
                print(f"Error summarizing with Ollama: {e}")
                
    finally:
        db.close()

def fetch_best_practices():
    """
    Finds learning resources from prioritized sources, summarizes them, and saves to DB.
    """
    db = SessionLocal()
    try:
        sources = get_random_sources(2)
        all_results = []
        for source in sources:
            query = f"AI best practices guide site:{source}"
            res = search_web(query, max_results=2)
            all_results.extend(res)
            
        for res in all_results:
            title = res.get('title')
            url = res.get('href')
            snippet = res.get('body')
            
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
                response = ollama.chat(model=DEFAULT_MODEL, messages=[
                    {'role': 'user', 'content': prompt}
                ])
                learning_content = response['message']['content'].strip()
                
                category = "Prompt Engineering" if "prompt" in title.lower() else "General AI"
                
                module = LearningModule(title=title, content=learning_content, category=category)
                db.add(module)
                db.commit()
            except Exception as e:
                print(f"Error generating learning module with Ollama: {e}")
    finally:
        db.close()

def practice_chat(prompt: str) -> str:
    """
    Sends user prompt to Ollama for the Practice tab.
    """
    try:
        response = ollama.chat(model=DEFAULT_MODEL, messages=[
            {'role': 'system', 'content': 'You are a helpful AI assistant. Answer the user strictly but concisely. If they want to practice prompt engineering, act as the requested persona.'},
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content'].strip()
    except Exception as e:
        print(f"Ollama chat error: {e}")
        return f"Error connecting to local AI model '{DEFAULT_MODEL}'. Please check if Ollama is running."
