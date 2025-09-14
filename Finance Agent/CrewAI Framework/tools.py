from typing import Any
from crewai.tools import BaseTool

class TickerLookupTool(BaseTool):
    name: str = "ticker_lookup"
    description: str = (
        "Given a company name, search the web and return the most likely stock ticker symbol. "
        "Prefers Yahoo Finance / MarketWatch. Returns only the ticker (e.g., AMZN)."
    )

    # Implementation notes:
    # - Uses `duckduckgo_search` to fetch top results.
    # - Tries to extract tickers from titles/snippets/URLs.
    # - Heuristics favor common finance sites and uppercase tickers.
    def _run(self, company_name: str) -> str:
        try:
            import re
            from duckduckgo_search import DDGS  # pip install duckduckgo-search

            # Search queries that bias toward reliable finance sites
            queries = [
                f'{company_name} ticker site:finance.yahoo.com',
                f'{company_name} stock ticker site:finance.yahoo.com',
                f'{company_name} ticker site:marketwatch.com',
                f'{company_name} stock symbol',
            ]

            candidates = []

            def extract_tickers(text: str) -> list[str]:
                if not text:
                    return []
                # Common ticker shapes (incl. dots for e.g. BRK.B; dashes for foreign listings)
                pattern = r'\b[A-Z]{1,5}(?:\.[A-Z]{1,3}|-[A-Z]{1,3})?\b'
                return re.findall(pattern, text.upper())

            with DDGS() as ddg:
                for q in queries:
                    for r in ddg.text(q, max_results=8):
                        title = r.get("title", "")
                        snippet = r.get("body", "") or r.get("href", "")
                        url = r.get("href", "")

                        # Try extracting from title, snippet, and URL
                        hits = (
                            extract_tickers(title)
                            + extract_tickers(snippet)
                            + extract_tickers(url)
                        )

                        # Light heuristics: prefer Yahoo/MarketWatch, de-dup, keep short tickers
                        domain_bonus = 2 if ("yahoo" in url.lower() or "marketwatch" in url.lower()) else 0
                        for h in hits:
                            # Skip obvious non-tickers
                            if h in ("HTTP", "HTTPS", "WWW", "COM"):
                                continue
                            score = domain_bonus + (5 - len(h))  # shorter often better (AAPL > XXXXX)
                            candidates.append((h, score))

            if not candidates:
                return "No ticker found"

            # Aggregate by ticker and choose best score
            best = {}
            for tkr, score in candidates:
                best[tkr] = max(score, best.get(tkr, -999))
            winner = sorted(best.items(), key=lambda x: x[1], reverse=True)[0][0]

            # Very light final sanity check: keep it uppercase, 1–5 letters (allow dot/dash)
            import re
            if re.fullmatch(r'[A-Z]{1,5}([.-][A-Z]{1,3})?', winner):
                return winner

            return "No ticker found"
        except Exception as e:
            return f"No ticker found"
