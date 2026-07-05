from app.ai.rag import search

docs = search("How many days can I return a product?")

print("\nRetrieved Documents:\n")

for i, doc in enumerate(docs, start=1):
    print(f"Document {i}")
    print(doc.page_content)
    print("-" * 50)