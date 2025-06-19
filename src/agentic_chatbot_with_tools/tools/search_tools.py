from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """

    tool = TavilySearchResults(max_result=2)

    return [tool]

def create_tool_node(tools):
    """
    Create and returns a tool node for the graph.
    """

    return ToolNode(tools=tools)