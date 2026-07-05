from app.ai.rag import ask


class ChatService:

    @staticmethod
    def ask_question(question: str) -> str:
        return ask(question)