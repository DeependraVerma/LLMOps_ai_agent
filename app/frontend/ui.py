import streamlit as st
import requests
import os

from app.config.settings import setting
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(page_title="Multi AI Agent" , layout="centered")
st.title("Multi AI Agent using Groq and Tavily New")

system_prompt = st.text_area("Define your AI Agent: " , height=70)
selected_model = st.selectbox("Select your AI model: ", setting.ALLOWED_MODEL_NAME)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Enter your query : " , height=150)

API_URL = os.getenv("API_URL")

if st.button("Ask the agent") and user_query.strip():
    payload = {
        "model_name" : selected_model,
        "system_prompt" : system_prompt,
        "messages": [user_query],
        "allow_search" : allow_web_search,
        
    }
    try:
        logger.info("Sending request to backend")
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            agent_response = response.json().get("response","")
            logger.info("Succesfully recieved response from backend")
            st.subheader("Agent Respnse")
            st.markdown(agent_response.replace("\n","<br>"), unsafe_allow_html = True)
        else:
            logger.error("Backend Error")
            st.error("Model did not respond")
    except Exception as e:
        logger.error("Error Occured Due To :",e)
        st.error(str(CustomException(f"Error Occured Due To :{e}")))



