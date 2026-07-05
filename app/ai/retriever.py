from langchain_qdrant import QdrantVectorStore

from app.ai.embeddings import embedding_model

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://qdrant:6333",
    collection_name="ecommerce_docs",
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3},
)


def retrieve(question: str) -> str:
    docs = retriever.invoke(question)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )