from typing import Any, Dict, List
from crewai.tools import BaseTool
import requests, re
from bs4 import BeautifulSoup

# --- Helper functions ---
def _fetch_html(url: str, timeout: int = 12) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.text

def _html_to_text(html: str, selector: str = None) -> str:
    soup = BeautifulSoup(html, "html.parser")
    scope = soup.select_one(selector) if selector else soup
    if not scope:
        return "Selector not found on page."
    for tag in scope(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

# --- Tools ---
class ScrapePageTool(BaseTool):
    name: str = "scrape_page"
    description: str = (
        "Scrape a web page. Input: URL (required), selector (optional), max_chars (optional). "
        "Extracts text and returns a cleaned summary-ready string."
    )

    def _run(self, url: str, selector: str = "", max_chars: int = 6000) -> str:
        try:
            html = _fetch_html(url)
            text = _html_to_text(html, selector or None)
            if len(text) > max_chars:
                text = text[:max_chars] + "\n... [truncated]"
            return f"{text}\n\n[Source] {url}"
        except Exception as e:
            return f"Scrape error: {e}"

class ListLinksTool(BaseTool):
    name: str = "list_links"
    description: str = "List up to N absolute links from a page."

    def _run(self, url: str, limit: int = 20) -> str:
        try:
            html = _fetch_html(url)
            soup = BeautifulSoup(html, "html.parser")
            out: List[str] = []
            for a in soup.find_all("a", href=True):
                href = a.get("href")
                if href and href.startswith("http"):
                    out.append(href)
                if len(out) >= int(limit):
                    break
            return "\n".join(out) if out else "No links found."
        except Exception as e:
            return f"List-links error: {e}"

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web using DuckDuckGo. Input: natural-language query."

    def _run(self, query: str) -> str:
        try:
            from duckduckgo_search import DDGS
            results = []
            with DDGS() as ddg:
                for r in ddg.text(query, max_results=5):
                    title = r.get("title", "")
                    href = r.get("href", "")
                    results.append(f"{title}: {href}")
            return "\n".join(results) if results else "No results found."
        except Exception as e:
            return f"Search error: {e}"