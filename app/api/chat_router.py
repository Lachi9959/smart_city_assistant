from fastapi import APIRouter
from pydantic import BaseModel
from app.llm.granite_llm import ask_granite

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat/ask")
def ask_chat(req: ChatRequest):
    return {"response": ask_granite(req.prompt)}
