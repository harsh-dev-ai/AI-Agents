import asyncio
from google.adk.runners import InMemoryRunner
from google.genai import types
from math_agent.agent import root_agent

async def main():
    runner = InMemoryRunner(agent=root_agent)
    session = await runner.session_service.create_session(
        app_name=root_agent.name, user_id="harsh"
    )

    print("Ask anything (Ctrl+C to exit).")
    while True:
        user_text = input("\nYou: ")
        async for event in runner.run_async("harsh", session.id, types.Content.from_text(user_text)):
            # Stream assistant output as it arrives
            chunk = event.stringify_content()
            if chunk:
                print(chunk, end="")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBye!")
