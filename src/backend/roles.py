from langchain.agents import create_agent

class Manager:
    def __init__(self, llm):
       self.agent = create_agent(
                model=llm   
            )















