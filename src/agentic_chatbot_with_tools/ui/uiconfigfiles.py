from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file= r"E:\chatbot_withtools_agenticai\src\agentic_chatbot_with_tools\ui\uiconfigs.ini"):
        self.config=ConfigParser()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        confile_file_path = os.path.join(current_dir, "uiconfigs.ini")
        self.config.read(confile_file_path)
        print("Config file path is: ", confile_file_path)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_openai_model_options(self):
        return self.config["DEFAULT"].get("OPENAI_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
