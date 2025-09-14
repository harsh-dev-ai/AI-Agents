from typing import List
from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

from tools import TickerLookupTool

@CrewBase
class FinanceCrew:
    """Crew for finding stock tickers from company names."""

    agents: List[Agent]
    tasks: List[Task]

    @agent
    def finance_researcher(self) -> Agent:
        # Loads config from config/agents.yaml
        return Agent(
            config=self.agents_config["finance_researcher"],
            tools=[TickerLookupTool()],
        )

    @task
    def lookup_ticker(self) -> Task:
        # Loads config from config/tasks.yaml
        return Task(
            config=self.tasks_config["lookup_ticker"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.finance_researcher()],
            tasks=[self.lookup_ticker()],
            verbose=True,
        )