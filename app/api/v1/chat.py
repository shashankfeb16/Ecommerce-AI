from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):

    answer = ChatService.ask_question(request.question)

    return ChatResponse(
        answer=answer
    )