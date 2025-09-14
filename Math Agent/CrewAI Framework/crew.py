from typing import List
from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from tools import CalculatorTool, WikipediaSummaryTool

@CrewBase
class MathCrew:
    """Crew for solving math/logic questions and fetching concise facts."""

    agents: List[Agent]
    tasks: List[Task]

    @agent
    def math_reasoner(self) -> Agent:
        # Uses config from config/agents.yaml: math_reasoner
        return Agent(
            config=self.agents_config["math_reasoner"],
            tools=[
                CalculatorTool(),
                WikipediaSummaryTool(),
            ],
        )

    @task
    def answer_math_query(self) -> Task:
        # Uses config from config/tasks.yaml: answer_math_query
        return Task(
            config=self.tasks_config["answer_math_query"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.math_reasoner()],
            tasks=[self.answer_math_query()],
            verbose=True,
        )
