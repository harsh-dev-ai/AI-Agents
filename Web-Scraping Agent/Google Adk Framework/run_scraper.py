import asyncio
from google.adk.runners import InMemoryRunner
from google.genai import types
from adk_web_scraper.agent import web_scraper_agent

async def main():
    runner = InMemoryRunner(agent=web_scraper_agent)
    session = await runner.session_service.create_session(
        app_name=web_scraper_agent.name, user_id="user"
    )

    print("🌐 ADK WebScraper ready! (type 'exit' to quit)\n")
    while True:
        q = input("You: ").strip()
        if q.lower() in {"exit", "quit"}:
            break

        full = ""
        async for event in runner.run_async("user", session.id, types.Content.from_text(q)):
            chunk = event.stringify_content()
            if chunk:
                print(chunk, end="")
                full += chunk
        if not full.endswith("\n"):
            print()

if __name__ == "__main__":
    asyncio.run(main())
