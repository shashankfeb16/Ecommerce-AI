from app.agents.ecommerce_agent import EcommerceAgent

agent = EcommerceAgent()


class ChatService:

    @staticmethod
    def ask_question(question: str) -> str:
        return agent.invoke(question)