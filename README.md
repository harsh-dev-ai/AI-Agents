# 🤖 AI-Agents Monorepo

A collection of small, focused AI agents built with **CrewAI**, **Google ADK**, and **LangChain**.  
Each agent lives in its own folder with a self-contained README and `requirements.txt`.

> TL;DR — **pick an agent → open the folder → follow its README**.

---

## 📦 What’s Inside

```
.
├── Finance Agent/
├── Math Agent/
└── Web-Scraping Agent/
```

Each folder contains multiple implementations (CrewAI / Google ADK / LangChain).  
You’ll find clear READMEs inside each subfolder with exact install & run steps.

---

## 🗺️ Repo Map & Entry Points

| Agent | Framework | Typical entry point | What it does |
|---|---|---|---|
| **Web-Scraping** | CrewAI | `run_scraper.py` | Scrape pages, list links, search via DuckDuckGo (tools wired to a Crew agent). |
|  | Google ADK | `run_scraper.py` | ADK `LlmAgent` with tools: `scrape_page`, `list_links`, `web_search` (streamed CLI). |
|  | LangChain | `web-scraping_agent.py` | Zero-shot ReAct agent with tools: scrape, list links, search. |
| **Math** | CrewAI | `run_math_cli.py` | SymPy calculator + Wikipedia summary tools; single Crew agent. |
|  | Google ADK | `run_local.py` | ADK `LlmAgent` exposing `calculate()` and `wikipedia_summary()` (streamed CLI). |
|  | LangChain | `mathematics_agent.py` | Chainlit app: LLMMathChain (calculator), reasoning chain, Wikipedia tool. |
| **Finance (Ticker Lookup)** | CrewAI | `run_finance_cli.py` | Heuristic company→ticker lookup via DuckDuckGo. |
|  | Google ADK | `run_finance.py` | ADK `LlmAgent` with `ticker_lookup` tool (streamed CLI). |
|  | LangChain | `finance_agent.py` | Minimal one-file demo asking “what is the ticker of Amazon”. |

> If filenames differ in your setup, use the subfolder README as the source of truth.

---

## 🧰 Prerequisites

- **Python 3.9+** recommended  
- A modern OS shell (macOS/Linux/Windows PowerShell or CMD)

**API keys (set only what you use):**
- `OPENAI_API_KEY` — required for OpenAI models (CrewAI / LangChain / ADK via LiteLLM)
- *(Optional)* Google AI key if you switch ADK to Gemini models

Create a `.env` in the subproject folder when needed:
```bash
OPENAI_API_KEY=your_api_key_here
```

---

## 🚀 Quick Start (per subproject)

Each subfolder ships with its own `requirements.txt`. Typical flow:

```bash
# 1) pick a subproject
cd "Web-Scraping Agent"/<framework-subfolder>

# 2) (recommended) create venv
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate     # Windows

# 3) install deps
pip install -r requirements.txt

# 4) run
python run_scraper.py          # or: run_local.py / run_finance.py / chainlit run mathematics_agent.py
```

See each subfolder’s README for exact commands and examples.

---

## 🧪 Example Commands

Some quick commands you’ll see across READMEs:
- **Web-Scraping (CrewAI/ADK):** `python run_scraper.py`
- **Web-Scraping (LangChain):** `python web-scraping_agent.py`
- **Math (CrewAI):** `python run_math_cli.py`
- **Math (ADK):** `python run_local.py`
- **Math (LangChain + Chainlit):** `chainlit run mathematics_agent.py`
- **Finance (CrewAI):** `python run_finance_cli.py`
- **Finance (ADK):** `python run_finance.py`
- **Finance (LangChain):** `python finance_agent.py`

---

## 📝 Notes & Limitations

- Web scrapers here are **static HTML** (no JS rendering).  
- Finance agents do **ticker lookup only** (no prices or fundamentals).  
- Math agents evaluate **numeric expressions** and fetch short Wikipedia summaries; invalid inputs return tool errors.

---

## 🧩 Contributing

PRs welcome! Suggested improvements:
- Add headless browser support for dynamic pages
- Strengthen ticker validation (exchange filters, symbol patterns)
- Add tests & CI for tool functions
- Add Dockerfiles for each subproject

---

## 📜 License

MIT © 2025 Harsh Dev (update as you prefer)
