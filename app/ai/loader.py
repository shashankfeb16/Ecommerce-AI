from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = BASE_DIR / "documents"


def load_documents():
    loader = DirectoryLoader(
        str(DOCUMENTS_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    return splitter.split_documents(documents)