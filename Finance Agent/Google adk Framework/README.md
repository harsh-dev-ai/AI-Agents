# 💹 Finance Ticker Agent (Google ADK)

A minimal **Google ADK** agent that maps a **company name → stock ticker symbol** using a search-backed tool and a single LLM agent.

---

## ✨ Features

- **Company → Ticker**: enter any company name (e.g., *Amazon*, *Reliance Industries*) and get the likely ticker (e.g., `AMZN`, `RELIANCE.NS`).
- **Search‑backed tool**: DuckDuckGo search + simple heuristics to extract and rank tickers from finance sites.
- **Streaming CLI**: interactive command line app with streamed model output.
- **Zero-config defaults**: ships with OpenAI via LiteLLM; easily swap to Gemini.

---

## 📂 Project Structure

```
.
├── run_finance.py            # CLI entry point (InMemoryRunner + streaming)
├── finance_agent/            # Package
│   ├── agent.py              # Tools + ADK LlmAgent definition
│   └── __init__.py           # Package initializer
└── README.md
```
- **run_finance.py** — starts an ADK `InMemoryRunner`, creates a session, and streams agent replies as they arrive. fileciteturn7file0
- **finance_agent/agent.py** — implements `ticker_lookup(company_name)` with DuckDuckGo and a regex for tickers, and wires the `finance_agent` (`openai/gpt-4o-mini` via LiteLLM). fileciteturn7file1
- **finance_agent/__init__.py** — marks the folder as a Python package. fileciteturn7file2

---

## 🛠️ Installation

1) **Clone & enter** the project:
```bash
git clone https://github.com/your-username/adk-finance-ticker.git
cd adk-finance-ticker
```

2) **Create a virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

3) **Install dependencies**:
```bash
pip install -r requirements.txt
```
**Minimal requirements**:
```
google-adk
litellm
duckduckgo-search
```

4) **Set your LLM API key** (OpenAI by default via LiteLLM):
```bash
# Linux/Mac
export OPENAI_API_KEY=your_api_key_here

# Windows
setx OPENAI_API_KEY "your_api_key_here"
```

> To use **Gemini** instead, change the model in `finance_agent/agent.py` to `gemini-2.0-flash` and configure the Google AI key accordingly. fileciteturn7file1

---

## 🚀 Usage

Run the interactive CLI:
```bash
python run_finance.py
```
Example session:
```
Finance Ticker Agent (type 'exit' to quit)

Company: Amazon
AMZN

Company: Reliance Industries
RELIANCE.NS
```
(CLI banner and `Company:` prompt from `run_finance.py`.) fileciteturn7file0

---

## ⚙️ How It Works

- The **ADK runner** streams content events from the agent to the console. fileciteturn7file0
- The **`ticker_lookup` tool**:
  - Queries DuckDuckGo with prompts biased to **Yahoo Finance** and **MarketWatch**.
  - Extracts ticker candidates using a regex supporting formats like `AAPL`, `BRK.B`, `RDS-A`.
  - Scores candidates (trusted domain bonus, shorter tickers favored) and returns the top pick. fileciteturn7file1
- The **`finance_agent`** is an ADK `LlmAgent` (OpenAI via LiteLLM) instructed to return **only** the ticker text (or “No ticker found”). fileciteturn7file1

---

## 🔒 Notes & Limitations

- Heuristic extraction may misidentify tickers for companies with multiple listings—consider adding exchange filters.
- Network access is required for web search.
- This project **does not** fetch quotes or fundamentals—only **tickers**.

---

## 🧪 Quick Checks

Try a few names in the CLI:
- **Apple** → `AAPL`
- **Alphabet** → `GOOGL` (or `GOOG`)
- **Berkshire Hathaway B** → `BRK.B`

---

## 📜 License

MIT License © 2025
