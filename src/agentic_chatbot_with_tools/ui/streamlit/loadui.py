import streamlit as st
from src.agentic_chatbot_with_tools.ui.uiconfigfiles import Config
import os

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def initialize_session(self):
        return {
            "current_step": "initializing"
        }
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 "+ self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        
        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()

            ## LLM Selection
            self.user_controls["selected_llm"]=st.selectbox("Select LLM", llm_options)
            
            if self.user_controls["selected_llm"] == "Groq":
                # Model Selection
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", groq_model_options)
                # API Key Input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                # Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your Groq API Key to proceed. Don't have? refer : https://console.groq.com/keys ")

            if self.user_controls["selected_llm"] == "OpenAI":
                # Model Selection
                openai_model_options = self.config.get_openai_model_options()
                self.user_controls["selected_openai_model"] = st.selectbox("Select Model", openai_model_options)
                # API Key Input
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"] = st.text_input("API KEY", type="password")

                # Validate API Key
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("⚠️ Please enter your OpeanAI API Key to proceed. Don't have? refer : https://platform.openai.com/settings/organization/api-keys ")

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

        return self.user_controls