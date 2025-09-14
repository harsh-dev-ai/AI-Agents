# math_agent/agent.py
from typing import Dict
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm  # OpenAI via LiteLLM

# --- Tool: Calculator (safe symbolic evaluation) ---
def calculate(expression: str) -> Dict[str, str]:
    """
    Evaluate a numeric math expression safely.
    Args:
      expression: A pure math expression such as "2*(3+4)^2 / 7".
    Returns:
      dict with 'status' and 'result' or 'error_message'.
    """
    try:
        from sympy import sympify
        expr = sympify(expression)
        val = expr.evalf()
        return {"status": "success", "result": str(val)}
    except Exception as e:
        return {"status": "error", "error_message": f"Calculation failed: {e}"}

# --- Tool: Wikipedia summary ---
def wikipedia_summary(query: str, sentences: int = 2) -> Dict[str, str]:
    """
    Fetch a short summary from Wikipedia.
    Args:
      query: Topic to search.
      sentences: Number of summary sentences.
    Returns:
      dict with 'status' and 'summary' or 'error_message'.
    """
    try:
        import wikipedia
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=sentences, auto_suggest=True, redirect=True)
        return {"status": "success", "summary": summary}
    except Exception as e:
        return {"status": "error", "error_message": f"Wikipedia lookup failed: {e}"}

# --- ADK Agent using OpenAI (via LiteLLM) ---
# Model strings follow "openai/<model_name>" per ADK+LiteLLM docs.
# Examples: "openai/gpt-4o-mini", "openai/gpt-4o", "openai/gpt-4.1-mini"
root_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4o-mini"),
    name="math_wiki_agent_openai",
    description="Answers logic-based questions, performs calculations, and looks up facts.",
    instruction=(
        "You are a reasoning agent tasked with solving the user's logic and numeric questions.\n"
        "Think step by step, be factual, and clearly detail the steps involved, then provide the final answer.\n"
        "Format the response as bullet points. For numeric questions, call the 'calculate' tool with a pure math "
        "expression (no extra text). For general knowledge, consider calling 'wikipedia_summary'."
    ),
    tools=[calculate, wikipedia_summary],
)
