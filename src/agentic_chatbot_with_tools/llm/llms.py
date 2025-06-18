from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
import streamlit as st

class LLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            selected_llm = self.user_controls_input["selected_llm"]

            if selected_llm == "Groq":
                groq_api_key = self.user_controls_input["GROQ_API_KEY"]
                selected_groq_model = self.user_controls_input["selected_groq_model"]

                if groq_api_key=='' and os.environ["GROQ_API_KEY"]:
                    st.error("Please enter the Groq API Key")

                llm = ChatGroq(model=selected_groq_model, api_key=groq_api_key)

            elif selected_llm=="OpenAI":
                openai_api_key = self.user_controls_input["OPENAI_API_KEY"]
                selected_openai_model = self.user_controls_input["selected_openai_model"]

                if selected_openai_model=='' and os.environ["OPENAI_API_KEY"]=='':
                    st.error("Please enter the Openai Api Key")
                
                llm = ChatOpenAI(api_key=openai_api_key, model=selected_openai_model)

        except Exception as e:
            raise ValueError(f"Error: Error occurer with Exception: {e}")

        return llm