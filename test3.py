import requests

class SwarmAgent:
    def __init__(self, name, role, instructions):
        self.name = name
        self.role = role
        self.instructions = instructions
        self.history = []

    def chat(self, message):
        # 1. Add message to memory
        self.history.append({"role": "user", "content": message})
        
        # 2. Prepare the prompt with their Role
        full_prompt = f"You are {self.name}, a {self.role}. {self.instructions}\n\nContext: {message} "
        
        # 3. Call your local Ollama
        response = requests.post("http://localhost:11434/api/generate", 
            json={"model": "llama3", "prompt": full_prompt, "stream": False,"options": {
          
    }})
        
        answer = response.json()['response']
        self.history.append({"role": "assistant", "content": answer})
        return answer

# --- SIMULATION START ---
agent1 = SwarmAgent()

topic = ""
# The "Sand Table" Loop
msg = topic

while True:

    user = input("Enter your argument (or 'exit' to stop): ")
    if user.lower() == 'exit':
        break
    msg = agent1.chat(msg + "\n\nUser Argument: " + user)
    print(f"harsha_ai: {msg}")
