# ➗ Math & Reasoning Agent (LangChain)

An AI-powered **math and reasoning assistant** built with the [LangChain](https://python.langchain.com/) framework and [Chainlit](https://docs.chainlit.io/).  
This agent can **solve numeric expressions**, **reason through word problems**, and **fetch Wikipedia summaries**, all through a conversational interface.

---

## ✨ Features

- **Math Calculator** – evaluates symbolic and numeric expressions using LangChain’s `LLMMathChain`.  
- **Reasoning Tool** – step-by-step logical reasoning for word problems.  
- **Wikipedia lookup** – retrieves factual summaries for general knowledge questions.  
- **Interactive UI** – powered by Chainlit (`chainlit run mathematics_agent.py`).  

---

## 📂 Project Structure

```
.
├── mathematics_agent.py      # Main LangChain math agent
└── README.md                 # Project documentation
```

- **mathematics_agent.py** – defines the agent, tools (`Calculator`, `Reasoning Tool`, `Wikipedia`), and Chainlit chat events.  

---

## 🛠️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/langchain-math-agent.git
   cd langchain-math-agent
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
   langchain
   langchain-openai
   langchain-community
   wikipedia
   chainlit
   python-dotenv
   ```

4. **Set your OpenAI API key** in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

---

## 🚀 Usage

Launch the Chainlit app:

```bash
chainlit run mathematics_agent.py
```

Then open the provided **localhost URL** in your browser to chat with the agent.

---

## 💡 Example Interactions

**Numeric Calculation:**
```
You: 2*(3+4)^2 / 7
Agent:
 • Step 1: Compute inside parentheses → (3+4) = 7
 • Step 2: Multiply → 2*7^2 = 2*49 = 98
 • Step 3: Divide by 7 → 98/7 = 14
 • ✅ Final Answer: 14
```

**Reasoning / Word Problem:**
```
You: A train travels 60 miles in 2 hours. What is its average speed?
Agent:
 • Step 1: Distance = 60 miles, Time = 2 hours
 • Step 2: Speed = Distance / Time = 60 / 2
 • ✅ Final Answer: 30 mph
```

**Wikipedia Summary:**
```
You: Who was Pythagoras?
Agent:
 • Pythagoras was an ancient Greek philosopher and mathematician...
```

---

## ⚡ Configuration

- **LLM**: Uses `gpt-3.5-turbo-instruct` by default, configurable in `mathematics_agent.py`.  
- **Tools**:
  - `Calculator` → numeric math only.  
  - `Reasoning Tool` → step-by-step logical reasoning.  
  - `Wikipedia` → general knowledge lookup.  

---

## 🔒 Notes & Limitations

- The calculator only accepts pure math expressions (no text).  
- Wikipedia tool may return errors on ambiguous queries.  
- Requires an OpenAI API key in `.env` for LLM access.  

---

## 📜 License

MIT License © 2025 Your Name
