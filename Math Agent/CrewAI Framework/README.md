# ➗ Math & Research Agent (CrewAI)

An AI-powered **math and facts** agent built on the [CrewAI](https://docs.crewai.com) framework.  
It can **solve numeric expressions** safely (via SymPy) and **fetch concise topic summaries** from Wikipedia—exposed as tools to a single reasoning agent.

---

## ✨ Features

- **Numeric math evaluator**: evaluate expressions like `2*(3+4)^2/7`, `sqrt(2)`, `sin(pi/2)` using SymPy.  
- **Wikipedia summaries**: quick, 1–3 sentence overviews for general topics.  
- **Config‑driven**: agent and task prompts live in `config/agents.yaml` and `config/tasks.yaml`.  
- **Interactive CLI**: chat with the agent from your terminal.

---

## 📂 Project Structure

```
.
├── crew.py                 # CrewBase: agent + task wiring
├── run_math_cli.py         # Interactive CLI entry point
├── tools.py                # Calculator & Wikipedia tools
├── config/
│   ├── agents.yaml         # Agent config (e.g., model, system prompts)
│   └── tasks.yaml          # Task config (e.g., instructions, expected outputs)
└── README.md               # Project documentation
```

- **crew.py** – defines `MathCrew` with a `math_reasoner` agent and `answer_math_query` task, wiring tools and loading YAML config.  
- **run_math_cli.py** – boots the crew, opens a REPL (`exit`/`quit` to leave), and routes your input into the crew via `kickoff`.  
- **tools.py** – implements two tools: `CalculatorTool` (SymPy-backed evaluator) and `WikipediaSummaryTool` (using `wikipedia` PyPI).  
- **__init__.py** – package initializer (empty).  

> 🔧 The agent reads its configuration from **`config/agents.yaml`** (`math_reasoner` key) and **`config/tasks.yaml`** (`answer_math_query` key).

---

## 🛠️ Installation

1) **Clone & enter** the project:
```bash
git clone https://github.com/your-username/crewai-math-agent.git
cd crewai-math-agent
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
sympy
wikipedia
pyyaml
```

> If your `agents.yaml` uses an external LLM (e.g., OpenAI), also install the relevant SDKs and set API keys as required by your config.

---

## 🚀 Usage

Run the interactive CLI:
```bash
python run_math_cli.py
```

Example session:
```
Math & Research Crew ready! (type 'exit' to quit)

You: 2*(3+4)^2/7
Agent:
 14

You: wikipedia_summary: "Pythagoras" 2
Agent:
 {"status": "success", "summary": "Pythagoras was an ancient Greek philosopher ..."}  # trimmed
```

> The agent may decide when to call tools. You can also hint it with explicit phrasing like:  
> “Compute: sin(pi/2) + sqrt(2)” or “Give me a 2‑sentence summary of Bayes’ theorem.”

---

## ⚙️ Configuration

- **Agent prompt & model** live under `config/agents.yaml` → `math_reasoner`.  
- **Task instructions** live under `config/tasks.yaml` → `answer_math_query`.  
- **Tools** available to the agent:
  - `calculator(expression: str)` → returns evaluated numeric result.  
  - `wikipedia_summary(query: str, sentences: int = 2)` → returns a short topic summary.  

You can tune tone, guardrails, and output format entirely via YAML—no code changes required.

---

## 🔒 Notes & Limitations

- The **calculator** only accepts **numeric expressions** (no text); invalid input returns an error string.  
- Wikipedia lookups may fail for misspellings/ambiguous topics; errors are returned in a structured dict.  
- If your agent config uses a remote LLM, ensure network access and credentials are set before running.

---

## 🧪 Quick Tests

Try a few prompts in the CLI:
- `Compute: (1/3 + 2/5)`  
- `Evaluate: sqrt(2)^4 - 7`  
- `Give me a 3-sentence summary of the Central Limit Theorem`

---

## 📜 License

MIT License © 2025
