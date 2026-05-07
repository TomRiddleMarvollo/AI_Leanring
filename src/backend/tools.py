from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
import re

def search_web(query: str, max_results: int = 5) -> list:
    """
    Searches the web using DuckDuckGo and returns a list of results.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            return results
    except Exception as e:
        print(f"Error searching web for {query}: {e}")
        return []

def fetch_content(url: str) -> str:
    """
    Fetches the textual content of a given URL.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
            
        text = soup.get_text(separator=' ')
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limit the text length to avoid token limits for basic local models
        return text[:4000]
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return ""

if __name__ == "__main__":
    # Test
    res = search_web("Latest AI advancements in May 2024", max_results=1)
    if res:
        print("Search Result:", res[0])
        content = fetch_content(res[0]['href'])
        print("Content Snippet:", content[:200])
