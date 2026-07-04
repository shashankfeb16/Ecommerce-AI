from app.ai.vector_store import vector_store

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


def search(query: str):
    return retriever.invoke(query)