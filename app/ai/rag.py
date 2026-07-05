from langchain_qdrant import QdrantVectorStore

from app.ai.embeddings import embedding_model
from app.ai.llm import llm
from app.ai.prompts import RAG_PROMPT

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://qdrant:6333",
    collection_name="ecommerce_docs",
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


def ask(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = RAG_PROMPT.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    response = llm.invoke(prompt)

    return response.content