from crew import WebScraperCrew

if __name__ == "__main__":
    crew = WebScraperCrew().crew()
    print("🌐 WebScraperCrew ready! (type 'exit' to quit)\n")

    while True:
        q = input("You: ").strip()
        if q.lower() in {"exit", "quit"}:
            break

        result = crew.kickoff(inputs={"question": q})
        print("\nAgent:\n", result, "\n")
