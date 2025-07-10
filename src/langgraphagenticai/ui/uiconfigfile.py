from configparser import ConfigParser

class Config:
    def __init__(self,config_file=r"src\langgraphagenticai\ui\uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def getllm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def getusecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def getgroq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
