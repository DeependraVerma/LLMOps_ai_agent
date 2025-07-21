from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn


from fastapi.responses import JSONResponse
from app.core.ai_agent import get_response_from_ai_agents
from app.config.settings import setting
from app.common.logger import get_logger

from app.common.custom_exception import CustomException

app = FastAPI(title = "MULTI AI AGENT")

logger = get_logger(__name__)

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


@app.post("/chat")
def chat_endpoint(request:RequestState):
    logger.info(f"Recieved Request For Model: {request.model_name}")

    if request.model_name not in setting.ALLOWED_MODEL_NAME:
        logger.warning(f"Invalid Model Name")
        raise HTTPException(status_code = 400, detail= "Invalid model name")
    
    try:
        response = get_response_from_ai_agents(
            llm_id=request.model_name,
            query=request.messages,
            allow_search= request.allow_search,
            system_prompt=request.system_prompt
        )
        logger.info(f"Successfuly got resposne from AI Agent: {request.model_name}")
        return {"response": response}
    
    except Exception as e:
        logger.error(f"Some error occured while fetching response from the ai agent: {e}")
        raise HTTPException(status_code = 500, 
                            detail = str(CustomException("Failed to get AI response", error_detail=e)))

