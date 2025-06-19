import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

class DisplayResult:
    def __init__(self, graph, user_message):
        self.graph = graph
        self.user_message = user_message
        
    def display_result_on_ui(self):
        try:
            user_message = self.user_message
            initial_state = {"messages": [user_message]}
            res = self.graph.invoke(initial_state)

            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
        except Exception as e:
            raise ValueError(f"Error: Error displaying result with Exception: {e}")