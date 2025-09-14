from crew import FinanceCrew

if __name__ == "__main__":
    crew = FinanceCrew().crew()

    while True:
        company = input("\nCompany name (or 'exit'): ").strip()
        if company.lower() in ("exit", "quit"):
            break

        result = crew.kickoff(inputs={"question": company})
        print("Ticker:", result)