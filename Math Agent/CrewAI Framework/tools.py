from typing import Any, Dict
from crewai.tools import BaseTool

class CalculatorTool(BaseTool):
    name: str = "calculator"
    description: str = (
        "Evaluate a numeric math expression only (no text). "
        "Examples: '2*(3+4)^2/7', 'sqrt(2)', 'sin(pi/2)'."
    )

    def _run(self, expression: str) -> str:
        try:
            from sympy import sympify
            val = sympify(expression).evalf()
            return str(val)
        except Exception as e:
            return f"Error: {e}"

class WikipediaSummaryTool(BaseTool):
    name: str = "wikipedia_summary"
    description: str = (
        "Fetch a short summary for a general topic from Wikipedia. "
        "Args: query (topic string), sentences (int, optional)."
    )

    def _run(self, query: str, sentences: int = 2) -> Dict[str, Any]:
        try:
            import wikipedia
            wikipedia.set_lang("en")
            summary = wikipedia.summary(
                query, sentences=int(sentences), auto_suggest=True, redirect=True
            )
            return {"status": "success", "summary": summary}
        except Exception as e:
            return {"status": "error", "error_message": f"Wikipedia lookup failed: {e}"}
