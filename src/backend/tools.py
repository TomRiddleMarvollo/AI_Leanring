import os
import requests
import xml.etree.ElementTree as ET
import random
import re
from bs4 import BeautifulSoup

SEARXNG_URL = os.getenv("SEARXNG_URL", "http://localhost:8888").rstrip("/")

def search_web(query: str, max_results: int = 5) -> list:
    """
    Searches the web via a self-hosted SearXNG instance (JSON API) — no
    search-engine account/key needed, and not subject to the scraping
    blocks/CAPTCHAs a public site's HTML would eventually trigger for
    an unattended, repeated caller like this one.
    Falls back to scraping DuckDuckGo's HTML results if SearXNG is
    unreachable (e.g. its container isn't running in this environment).
    """
    try:
        response = requests.get(
            f"{SEARXNG_URL}/search",
            # Explicit engine list instead of SearXNG's full default set:
            # duckduckgo/brave/startpage/qwant/yahoo all came back blocked
            # (CAPTCHA/rate-limit) when tested from this environment, while
            # these four consistently returned real results. Google is kept
            # in the mix even though it currently returns nothing here — it
            # fails silently rather than erroring, so there's no downside.
            params={"q": query, "format": "json", "engines": "google,bing,yandex,mwmbl,gmx"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        results = [
            {"title": r.get("title", ""), "href": r.get("url", ""), "body": r.get("content", "")}
            for r in data.get("results", [])
            if r.get("url", "").startswith("http")
        ]
        if results:
            return results[:max_results]
        # Empty result set — worth a fallback attempt rather than trusting
        # a possibly-misconfigured SearXNG instance over an empty answer.
        print(f"SearXNG returned no results for '{query}', falling back to DuckDuckGo.")
    except Exception as e:
        print(f"Error querying SearXNG for '{query}': {e}. Falling back to DuckDuckGo.")
    return _search_web_ddg_fallback(query, max_results)

def _search_web_ddg_fallback(query: str, max_results: int = 5) -> list:
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

def _is_safe_url(url: str) -> bool:
    from urllib.parse import urlparse
    import ipaddress
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False
        host = parsed.hostname or ""
        # Block private/loopback addresses (SSRF prevention)
        try:
            addr = ipaddress.ip_address(host)
            if addr.is_private or addr.is_loopback or addr.is_link_local:
                return False
        except ValueError:
            # hostname, not IP — block known internal names
            if host in ("localhost", "metadata.google.internal") or host.endswith(".local"):
                return False
        return True
    except Exception:
        return False

def fetch_content(url: str) -> str:
    """
    Fetches the textual content of a given URL.
    """
    if not _is_safe_url(url):
        print(f"Blocked potentially unsafe URL: {url}")
        return ""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
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
