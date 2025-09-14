# finance_agent/agent.py
from typing import Dict, List, Tuple
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm  # OpenAI via LiteLLM

# --- Tool: Ticker lookup via DuckDuckGo ---
def ticker_lookup(company_name: str) -> Dict[str, str]:
    """
    Find the most likely stock ticker for a given company name using DuckDuckGo results.
    Prefers results from Yahoo Finance and MarketWatch. Returns {"status": "...", "ticker": "..."}.
    """
    try:
        import re
        from duckduckgo_search import DDGS  # pip install duckduckgo-search

        def extract_tickers(text: str) -> List[str]:
            if not text:
                return []
            # Allow e.g. BRK.B or RDS-A besides plain AAPL/AMZN
            pattern = r'\b[A-Z]{1,5}(?:[.-][A-Z]{1,3})?\b'
            return re.findall(pattern, text.upper())

        queries = [
            f'{company_name} ticker site:finance.yahoo.com',
            f'{company_name} stock ticker site:finance.yahoo.com',
            f'{company_name} ticker site:marketwatch.com',
            f'{company_name} stock symbol',
        ]

        candidates: List[Tuple[str, int]] = []
        with DDGS() as ddg:
            for q in queries:
                for r in ddg.text(q, max_results=8) or []:
                    title = r.get("title", "")
                    snippet = r.get("body", "") or r.get("href", "")
                    url = r.get("href", "")

                    hits = extract_tickers(title) + extract_tickers(snippet) + extract_tickers(url)
                    domain_bonus = 2 if ("yahoo" in url.lower() or "marketwatch" in url.lower()) else 0

                    for h in hits:
                        if h in {"HTTP", "HTTPS", "WWW", "COM"}:
                            continue
                        score = domain_bonus + (5 - len(h))  # shorter often better
                        candidates.append((h, score))

        if not candidates:
            return {"status": "not_found", "ticker": "No ticker found"}

        best: Dict[str, int] = {}
        for tkr, s in candidates:
            best[tkr] = max(best.get(tkr, -999), s)
        winner = sorted(best.items(), key=lambda x: x[1], reverse=True)[0][0]

        if re_full := __import__("re").fullmatch(r'[A-Z]{1,5}([.-][A-Z]{1,3})?', winner):
            return {"status": "success", "ticker": winner}

        return {"status": "not_found", "ticker": "No ticker found"}

    except Exception:
        # Keep it quiet for the agent; ADK will reason with the return value.
        return {"status": "error", "ticker": "No ticker found"}


# --- ADK Agent (OpenAI via LiteLLM) ---
# To switch to Gemini later: model="gemini-2.0-flash" and use google AI key instead.
finance_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4o-mini"),
    name="finance_ticker_agent",
    description="Given a company name, return only its stock ticker symbol.",
    instruction=(
        "You are a precise finance lookup agent.\n"
        "Use the `ticker_lookup` tool to map a company name to a stock ticker.\n"
        "Return **only** the ticker (e.g., AMZN). If not found, return 'No ticker found'."
    ),
    tools=[ticker_lookup],
)