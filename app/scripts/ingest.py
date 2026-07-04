from langchain_qdrant import QdrantVectorStore

from app.ai.loader import load_documents
from app.ai.embeddings import embedding_model

documents = load_documents()

QdrantVectorStore.from_documents(
    documents=documents,
    embedding=embedding_model,
    url="http://qdrant:6333",
    collection_name="ecommerce_docs",
)

print("Documents indexed successfully.")