from crewai import Agent, Task, Crew, LLM
print("initialised")
# 1. Connect to your local Llama via Ollama
local_llm = LLM(
    model="ollama/llama3",
    base_url="http://localhost:11434"
)
print("connected to local LLM")
# 2. Define your Agent
researcher = Agent(
    role='Researcher',
    goal='Find the latest news about AI',
    backstory='You are a tech-savvy researcher.',
    llm=local_llm
)
print("agent defined")
# 3. Define a Task
task = Task(description='Summarize AI trends in 2026', agent=researcher, expected_output="A 1-bullet point summary upto 10 words.")
print("task defined")
while True:
    print("task started")
    user=input("Enter your argument:")
    if user == "exit":
        break
    # 4. Kick it off
    crew = Crew(agents=[researcher], tasks=[task])
    result = crew.kickoff(inputs={'user_input': user})
    print(result)
    