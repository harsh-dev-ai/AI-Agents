from typing import Dict, List
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm  # OpenAI via LiteLLM

# ------- Helpers (shared by tools) -------
def _fetch_html(url: str, timeout: int = 12) -> str:
    import requests
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

def _html_to_text(html: str, selector: str | None = None) -> str:
    import re
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    scope = soup.select_one(selector) if selector else soup
    if not scope:
        return "Selector not found on page."
    for tag in scope(["script", "style", "noscript"]):
        tag.decompose()
    text = scope.get_text(separator="\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

# ------- Tools -------
def web_search(query: str) -> str:
    """
    Search the web (DuckDuckGo). Input: natural language query.
    Returns a small list of 'Title: URL' lines.
    """
    try:
        from duckduckgo_search import DDGS  # pip install duckduckgo-search
        out: List[str] = []
        with DDGS() as ddg:
            for r in ddg.text(query, max_results=5) or []:
                title = r.get("title", "")
                href = r.get("href", "")
                out.append(f"{title}: {href}")
        return "\n".join(out) if out else "No results found."
    except Exception as e:
        return f"Search error: {e}"

def list_links(url: str, limit: int = 20) -> str:
    """
    Return up to N absolute links from a page (useful for exploration).
    """
    try:
        from bs4 import BeautifulSoup
        html = _fetch_html(url)
        soup = BeautifulSoup(html, "html.parser")
        links: List[str] = []
        for a in soup.find_all("a", href=True):
            href = a.get("href")
            if href and href.startswith("http"):
                links.append(href)
            if len(links) >= int(limit):
                break
        return "\n".join(links) if links else "No links found."
    except Exception as e:
        return f"List-links error: {e}"

def scrape_page(url: str, selector: str = "", max_chars: int = 6000) -> str:
    """
    Fetch a page, optionally scope by CSS selector, return cleaned text + source URL.
    """
    try:
        html = _fetch_html(url)
        text = _html_to_text(html, selector or None)
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... [truncated]"
        return f"{text}\n\n[Source] {url}"
    except Exception as e:
        return f"Scrape error: {e}"

# ------- ADK Agent (OpenAI via LiteLLM) -------
web_scraper_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4o-mini"),  # swap to "gemini-2.0-flash" to use Gemini
    name="web_scraper_agent",
    description="Search, scrape, and summarize web content.",
    instruction=(
        "You are a web-scraping assistant.\n"
        "If asked a general question, call `web_search` to find candidate URLs, then `scrape_page`.\n"
        "If given a URL, use `scrape_page` directly (optionally with a CSS selector like 'article' or '#content').\n"
        "When a site hub is provided, you may call `list_links` to find subpages before scraping.\n"
        "Summarize clearly and include the source URL in your final answer."
    ),
    tools=[web_search, list_links, scrape_page],
)
