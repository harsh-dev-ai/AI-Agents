import os
import re
import requests
from typing import List, Optional
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.callbacks.manager import get_openai_callback  # optional (cost debug)
from bs4 import BeautifulSoup

# --- Env ---
load_dotenv()
# expects OPENAI_API_KEY

# --- Helpers ---
def _fetch_html(url: str, timeout: int = 12) -> str:
    """Fetch raw HTML with a browser-like User-Agent and small timeout."""
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

def _html_to_text(html: str, selector: Optional[str] = None) -> str:
    """Convert HTML to readable text; optional CSS selector scope."""
    soup = BeautifulSoup(html, "html.parser")
    scope = soup.select_one(selector) if selector else soup
    if not scope:
        return "Selector not found on page."
    # Remove script/style/nav/footer
    for tag in scope(["script", "style", "noscript"]):
        tag.decompose()
    text = scope.get_text(separator="\n", strip=True)
    # Normalize whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

# --- Tools ---
def scrape(url: str, selector: str = "", max_chars: int = 6000) -> str:
    """
    Fetch a web page, optionally scope by a CSS selector, and return cleaned text.
    Args:
      url: Full URL (https://...).
      selector: Optional CSS selector (e.g., 'article', '#content', '.post').
      max_chars: Truncate long pages to keep answers focused.
    Returns:
      Clean text excerpt, ending with the source URL for citation.
    """
    try:
        html = _fetch_html(url)
        text = _html_to_text(html, selector or None)
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... [truncated]"
        return f"{text}\n\n[Source] {url}"
    except Exception as e:
        return f"Scrape error: {e}"

def list_links(url: str, limit: int = 20) -> str:
    """
    Return up to N absolute links from a page. Helpful for site exploration.
    """
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
        if not out:
            return "No links found."
        return "\n".join(out)
    except Exception as e:
        return f"List-links error: {e}"

# LangChain’s built-in DuckDuckGo search tool
search = DuckDuckGoSearchRun()

scrape_tool = Tool.from_function(
    name="ScrapePage",
    func=scrape,
    description=(
        "Fetch and parse a web page. Input must be a JSON-like string or text containing:\n"
        "url (required), selector (optional), max_chars (optional).\n"
        "Use this to extract article text, product details, or page content. "
        "Always include the URL you scraped in your final answer."
    ),
)

links_tool = Tool.from_function(
    name="ListLinks",
    func=list_links,
    description=(
        "List up to N absolute links from a given page URL. "
        "Useful for discovering detail pages before scraping."
    ),
)

search_tool = Tool.from_function(
    name="WebSearch",
    func=search.run,
    description=(
        "Search the web (DuckDuckGo). Input is a natural-language query. "
        "Use this first to find candidate URLs to scrape."
    ),
)

# --- LLM ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- Agent ---
agent = initialize_agent(
    tools=[search_tool, links_tool, scrape_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

if __name__ == "__main__":
    print("🌐 WebScraper Agent ready! (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            break
        try:
            response = agent.run(user_input)
            print(f"\nAgent: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
