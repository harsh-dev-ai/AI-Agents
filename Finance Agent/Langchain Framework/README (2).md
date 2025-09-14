# 💹 Finance Ticker Agent (LangChain)

A minimal **LangChain** agent that maps a **company name → stock ticker symbol** using a DuckDuckGo-powered lookup tool and an OpenAI LLM.

---

## ✨ Features

- **Company → Ticker**: ask for a company's ticker (e.g., *Amazon* → `AMZN`).  
- **Search-backed tool**: queries DuckDuckGo and attempts to parse a MarketWatch lookup line.  
- **One-file demo**: simple, readable starting point for LangChain agents.

---

## 📂 Project Structure

```
.
├── finance_agent.py   # Main LangChain agent with custom search tool
└── README.md
```
The agent defines a custom `search_ticker` tool, instantiates `ChatOpenAI`, and initializes a Zero-Shot ReAct agent that runs a single prompt at the bottom of the file.

---

## 🛠️ Installation

1) **Clone & enter** the project:
```bash
git clone https://github.com/your-username/langchain-finance-agent.git
cd langchain-finance-agent
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
langchain
langchain-community
langchain-openai
duckduckgo-search
python-dotenv
```

4) **Set your OpenAI key** (required by `ChatOpenAI`):
```bash
# .env file
OPENAI_API_KEY=your_api_key_here
```

---

## 🚀 Usage

Run the script:
```bash
python finance_agent.py
```
Expected behavior: it will ask the agent **“what is the ticker of Amazon”** and print the result to the console.

---

## ⚙️ How It Works

- **Tool**: `search_ticker(company_name: str) -> str` calls DuckDuckGo and looks for a **MarketWatch** “Stock Ticker Symbol Lookup” line, returning the last token (assumed ticker).  
- **LLM**: `ChatOpenAI(temperature=0.0)` provides deterministic reasoning over the tools.  
- **Agent**: `initialize_agent(..., agent_type=ZERO_SHOT_REACT_DESCRIPTION, verbose=True)` composes the LLM and tools to answer the prompt.

---

## 🔒 Notes & Limitations (and quick fixes)

- **Custom tool loading**: if the code uses `load_tools(["search_ticker"], ...)`, note `load_tools` only loads **built-in** tools. For a custom tool, pass it directly:
  ```python
  tools = [search_ticker]
  ```
- **DuckDuckGo return type**: `DuckDuckGoSearchRun().run(...)` often returns a **string** rather than a list of dicts. If you need structured results, consider `DuckDuckGoSearchAPIWrapper` or parse the returned string.  
- **Heuristic parsing**: scraping a single MarketWatch line may miss tickers or return wrong ones; refine by querying finance domains and validating ticker formats (e.g., `AAPL`, `BRK.B`, `RELIANCE.NS`).

---

## 🧪 Quick Checks

Try replacing the hard-coded prompt with console input or additional test cases:
- **Apple** → expect `AAPL`  
- **Alphabet** → expect `GOOGL` (or `GOOG`)  
- **Berkshire Hathaway B** → expect `BRK.B`

---

## 📜 License

MIT License © 2025 Your Name
