from src.agentic_chatbot_with_tools.state.state import State
from langgraph.graph import StateGraph, START, END
from src.agentic_chatbot_with_tools.node.chatbot_with_tool_node import ChatbotWithToolNode
from src.agentic_chatbot_with_tools.tools.search_tools import create_tool_node, get_tools
from langgraph.prebuilt import tools_condition

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)


    def chatbot_with_tools_build_graph(self):
        """
        Build an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilities, and sets up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.
        
        """

        # Define the tool and toolsnode
        try:
            tools = get_tools()
            tool_nodel = create_tool_node(tools)

            obj_chatbot_with_tools_node = ChatbotWithToolNode(self.llm)
            chatbot_node = obj_chatbot_with_tools_node.create_chatbot(tools)

            self.graph_builder.add_node("chatbot", chatbot_node)
            self.graph_builder.add_node("tools", tool_nodel)
            
            # Define conditional and direct edges
            self.graph_builder.add_edge(START, "chatbot")
            self.graph_builder.add_conditional_edges("chatbot", tools_condition)
            self.graph_builder.add_edge("tools", "chatbot")

        except Exception as e:
            raise ValueError(f"Error: Error occured with Exception: {e}")
        
        
    def setup_graph(self):
        self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()