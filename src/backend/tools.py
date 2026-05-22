import requests
import xml.etree.ElementTree as ET
import random
import re
from bs4 import BeautifulSoup

def search_web(query: str, max_results: int = 5) -> list:
    import urllib.parse
    results = []
    try:
        response = requests.post(
            'https://html.duckduckgo.com/html/', 
            data={'q': query}, 
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
            timeout=15
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for result in soup.select('.result'):
            a_tag = result.select_one('.result__a')
            snippet_tag = result.select_one('.result__snippet')
            
            if not a_tag or not snippet_tag:
                continue
                
            href = a_tag.get('href', '')
            if 'uddg=' in href:
                href = urllib.parse.unquote(href.split('uddg=')[1].split('&')[0])
            elif href.startswith('//'):
                href = 'https:' + href
                
            title = a_tag.text
            snippet = snippet_tag.text
            
            if 'ad_domain' in href or not href.startswith('http'):
                continue
                
            results.append({"title": title, "href": href, "body": snippet})
            
            if len(results) >= max_results:
                break
    except Exception as e:
        print(f"Error fetching DDG for query '{query}': {e}")
    return results

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
