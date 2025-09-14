# 💹 Finance Ticker Lookup Agent (CrewAI)

A minimal **CrewAI** project that maps a **company name → stock ticker symbol** using a purpose‑built tool and a single research agent.

---

## ✨ Features

- **Company → Ticker**: enter any company name (e.g., *Amazon*, *Reliance Industries*) and get the likely ticker (e.g., `AMZN`, `RELIANCE.NS`).  
- **Search‑backed tool**: lightweight DuckDuckGo search + heuristics to extract and rank tickers from finance sites.  
- **Config‑driven**: agent and task prompts in `config/agents.yaml` and `config/tasks.yaml`.  
- **CLI workflow**: type a company name; get a ticker.

---

## 📂 Project Structure

```
.
├── crew.py                 # CrewBase: wires agent + task, loads config
├── run_finance_cli.py      # Interactive CLI entry point
├── tools.py                # TickerLookupTool (search + extract heuristics)
├── config/
│   ├── agents.yaml         # Agent config (e.g., model, system prompts)
│   └── tasks.yaml          # Task config (e.g., instructions, expected outputs)
└── README.md
```

- **crew.py** — defines `FinanceCrew` with a `finance_researcher` agent and a `lookup_ticker` task; both read from the `config/` YAMLs. fileciteturn6file0  
- **run_finance_cli.py** — spins up the crew and prompts *“Company name (or 'exit')”*; each input is passed to `crew.kickoff(...)` and the result is printed as **Ticker:**. fileciteturn6file1  
- **tools.py** — implements `TickerLookupTool` using DuckDuckGo to query Yahoo Finance / MarketWatch and extract uppercase ticker candidates with regex + scoring. fileciteturn6file2

---

## 🛠️ Installation

1) **Clone & enter** the project:
```bash
git clone https://github.com/your-username/crewai-finance-agent.git
cd crewai-finance-agent
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
crewai
duckduckgo-search
pyyaml
```

> If your `agents.yaml` specifies a remote LLM (e.g., OpenAI), also install the vendor SDK and set API keys per your config.

---

## 🚀 Usage

Run the interactive CLI:

```bash
python run_finance_cli.py
```

Example session:
```
Company name (or 'exit'): Amazon
Ticker: AMZN

Company name (or 'exit'): Reliance Industries
Ticker: RELIANCE.NS
```

---

## ⚙️ How It Works

- The **FinanceCrew** loads its agent/task definitions from `config/agents.yaml` & `config/tasks.yaml`, then runs the single task with your input. fileciteturn6file0  
- The **TickerLookupTool**:
  - Queries DuckDuckGo with multiple prompts biased to Yahoo Finance / MarketWatch.  
  - Extracts possible tickers from titles/snippets/URLs using a regex that supports forms like `BRK.B` or `BABA-SW`.  
  - Ranks candidates: small bonus for trusted domains, shorter tickers preferred, then returns the best match. fileciteturn6file2

---

## 🔒 Notes & Limitations

- Heuristic extraction may misidentify tickers for companies with multiple listings; refine prompts or add exchange filters if needed. fileciteturn6file2  
- Network access is required for web search.  
- This project **does not** fetch prices or financial data—only **tickers**.

---

## 🧪 Quick Checks

Try a few names in the CLI:
- **Apple** → expect `AAPL`  
- **Alphabet** → expect `GOOGL` or `GOOG`  
- **Berkshire Hathaway B** → expect `BRK.B`

---

## 📜 License

MIT License © 2025 Your Name
