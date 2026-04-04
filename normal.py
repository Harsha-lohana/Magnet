import requests
agentState = {}

class superAgent:
    def __init__(self, name, role, instructions):
        self.name = name
        self.role = role
        self.instructions = instructions
        self.agents = []

    def agent_creation(self, agent_name, agent_role, agent_instructions):
        new_agent = SwarmAgent(agent_name, agent_role, agent_instructions)
        return new_agent

class SwarmAgent:
    def __init__(self, name, role, instructions):
        self.name = name
        self.role = role
        self.instructions = instructions
        

    def chat(self, message):
        
        # 2. Prepare the prompt with their Role
        full_prompt = f"""You are {self.name}, You are  {self.role}. Here is an Ad: {self.instructions}Analyze if you would buy this.Return your answer in exactly this format: SCORE: [0-100] | REASON: [Short text] \n\nContext: {message} """
                
        # 3. Call your local Ollama
        response = requests.post("http://localhost:11434/api/generate", 
            json={"model": "llama3", "prompt": full_prompt, "stream": False,"options": {
        }})
        
        answer = response.json()['response']
        agentState["history"].append(answer)
        
        return answer

agent1 = SwarmAgent("helper","a helpful assistant","")

topic = "Just behave like normal agent"
agentState={"topic": topic, "history": [], "user_input":[]}

msg = topic
# --- SIMULATION START ---
def research(state,user,msg)->dict:
        state['user_input'].append(user)
        msg = agent1.chat(msg + "\n\nUser Argument: " + user)
        print(f"harsha_ai: {msg}")

while True:
    user = input("Enter your argument (or 'exit' to stop): ")
    if user.lower() == 'exit':
            break
    research(agentState,user,msg)

    
    print(agentState)