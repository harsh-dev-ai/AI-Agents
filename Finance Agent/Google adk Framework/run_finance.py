import asyncio
from google.adk.runners import InMemoryRunner
from google.genai import types
from finance_agent.agent import finance_agent

async def main():
    runner = InMemoryRunner(agent=finance_agent)
    session = await runner.session_service.create_session(
        app_name=finance_agent.name, user_id="user"
    )

    print("Finance Ticker Agent (type 'exit' to quit)\n")
    while True:
        q = input("Company: ").strip()
        if q.lower() in {"exit", "quit"}:
            break

        # Stream the response
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
