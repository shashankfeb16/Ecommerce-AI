from qdrant_client import QdrantClient


def get_client():
    return QdrantClient(
        url="http://qdrant:6333",
    )