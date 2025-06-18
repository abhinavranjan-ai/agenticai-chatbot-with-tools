from src.agentic_chatbot_with_tools.state.state import State

class ChatbotNode:
    def __init__(self, model):
        self.model = model
    
    def process(self, state: State) -> dict:
        """
        Process the input state and generate a chatbot response.
        """
        
        return {"messages": self.model.invoke(state["messages"])}