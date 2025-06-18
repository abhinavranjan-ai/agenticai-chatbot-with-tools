import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

class DisplayResult:
    def __init__(self, graph, user_message):
        self.graph = graph
        self.user_message = user_message
        
    def display_result_on_ui(self):
        graph = self.graph
        user_message = self.user_message

        for event in graph.stream({"messages": (HumanMessage(content=user_message))}):
            print(event.values())
            for value in event.values():
                with st.chat_message("user"):
                    st.write(user_message)
                with st.chat_message("assistant"):
                    st.write(value["messages"].content)