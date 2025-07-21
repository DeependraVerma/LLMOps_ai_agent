import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    ALLOWED_MODEL_NAME = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]


setting = Settings()
