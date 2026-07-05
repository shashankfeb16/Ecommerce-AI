from app.ai.llm import llm
from app.ai.prompts import RAG_PROMPT
from app.ai.retriever import retrieve


def ask(question: str):

    context = retrieve(question)

    prompt = RAG_PROMPT.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    response = llm.invoke(prompt)

    return response.content