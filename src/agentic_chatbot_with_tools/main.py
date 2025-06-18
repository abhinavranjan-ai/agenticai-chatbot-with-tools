import streamlit as st
from src.agentic_chatbot_with_tools.ui.streamlit.loadui import LoadStreamlitUI
from src.agentic_chatbot_with_tools.llm.llms import LLM
from src.agentic_chatbot_with_tools.graph.graph_builder import GraphBuilder
from src.agentic_chatbot_with_tools.ui.streamlit.display_result import DisplayResult

# Main Function starts
def load_agentic_chatbot_app():
    """
    Loads and runs the Langgraph AgenticAI application with Streamlit UI.
    This funciton initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for roubustness.
    
    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    user_message = st.chat_input("Enter your message: ")

    if user_message:
        try:
            ## Configure LLM
            obj_llm_config = LLM(user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")

            # Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph()
                DisplayResult(graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: Graph set up failed with Exception: {e}")

        except Exception as e:
            raise ValueError(f"Error: Error occured with Exception: {e}")