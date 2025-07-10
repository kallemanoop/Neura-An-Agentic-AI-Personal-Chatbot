import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.title(self.config.get_page_title())

        with st.sidebar:
            llm_options=self.config.getllm_options()
            usecase_options=self.config.getusecase_options()

            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.getgroq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                groq_api_key = st.text_input("API Key", type="password")
                if not groq_api_key:
                    st.warning("Please enter your Groq API Key to proceed.")
                    return None
                self.user_controls["GROQ_API_KEY"] = groq_api_key
                # if not self.user_controls["GROQ_API_KEY"]:
                #     st.warning("Please enter your Groq API Key to proceed.") 

            
            self.user_controls["selected_usecase"]=st.selectbox("Select Use Case", usecase_options)

        return self.user_controls
    
    
                