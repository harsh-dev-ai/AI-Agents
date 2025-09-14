from typing import List
from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

from tools import ScrapePageTool, ListLinksTool, WebSearchTool

@CrewBase
class WebScraperCrew:
    """Crew for scraping and summarizing web content."""

    agents: List[Agent]
    tasks: List[Task]

    @agent
    def web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config["web_scraper"],
            tools=[
                ScrapePageTool(),
                ListLinksTool(),
                WebSearchTool(),
            ],
        )

    @task
    def scrape_and_summarize(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_and_summarize"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.web_scraper()],
            tasks=[self.scrape_and_summarize()],
            verbose=True,
        )
