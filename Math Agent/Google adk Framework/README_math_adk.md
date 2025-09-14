# ➗ Math & Research Agent (Google ADK)

An AI-powered **math and research assistant** built with the [Google AI Development Kit (ADK)](https://ai.google.dev/) framework.  
It can **evaluate math expressions** (via SymPy) and **fetch concise summaries** from Wikipedia—exposed as tools for a reasoning LLM agent.

---

## ✨ Features

- **Safe math calculator** – evaluates symbolic math expressions using SymPy.  
- **Wikipedia summaries** – fetches short factual overviews for any topic.  
- **Config-free** – tools are wired directly into the ADK `LlmAgent`.  
- **Interactive CLI** – run locally with real-time streaming output.  

---

## 📂 Project Structure

```
.
├── run_local.py              # CLI entry point (starts InMemoryRunner)
├── math_agent/               # Package
│   ├── agent.py              # Defines tools + root LlmAgent
│   └── __init__.py           # Package initializer
└── README.md                 # Project documentation
```

- **run_local.py** – creates an ADK `InMemoryRunner`, starts a session, and streams agent replies interactively.  
- **math_agent/agent.py** – defines two tools (`calculate`, `wikipedia_summary`) and the `root_agent` (OpenAI GPT-4o-mini via LiteLLM).  
- **math_agent/__init__.py** – marks the folder as a Python package.  

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/adk-math-agent.git
   cd adk-math-agent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Minimal requirements:
   ```
   google-adk
   litellm
   sympy
   wikipedia
   ```

4. **Configure your OpenAI key** (if using OpenAI models with LiteLLM):
   ```bash
   export OPENAI_API_KEY=your_api_key_here   # Linux/Mac
   setx OPENAI_API_KEY "your_api_key_here"   # Windows
   ```

---

## 🚀 Usage

Run the interactive CLI:

```bash
python run_local.py
```

Example session:

```
Ask anything (Ctrl+C to exit).

You: 2*(3+4)^2 / 7
Agent:
 • Step 1: Compute inside parentheses → (3+4) = 7
 • Step 2: Multiply → 2*7^2 = 2*49 = 98
 • Step 3: Divide by 7 → 98/7 = 14
 • ✅ Final Answer: 14

You: Give me 2 sentences about Bayes' theorem
Agent:
 • Bayes' theorem is a fundamental result in probability theory...
 • It describes how to update beliefs based on new evidence.
```

---

## ⚡ Configuration

- **Model**: defaults to `openai/gpt-4o-mini` via LiteLLM (see `math_agent/agent.py`).  
- Swap models by editing:
  ```python
  model=LiteLlm(model="gemini-2.0-flash")
  ```
- **Tools**:
  - `calculate(expression: str)` → evaluates numeric expressions with SymPy.  
  - `wikipedia_summary(query: str, sentences: int = 2)` → fetches a short topic summary.  

---

## 🔒 Notes & Limitations

- The calculator only supports valid **numeric/math expressions** (e.g., `sqrt(2) + sin(pi/2)`).  
- Wikipedia lookups may fail on misspellings or ambiguous queries.  
- Requires internet access for Wikipedia and for LLM API calls.  

---

## 📜 License

MIT License © 2025 Your Name
