from crew import MathCrew

if __name__ == "__main__":
    crew = MathCrew().crew()

    print("Math & Research Crew ready! (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        result = crew.kickoff(inputs={"question": user_input})
        print(f"Agent:\n{result}\n")
