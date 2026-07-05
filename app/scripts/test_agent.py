from app.ai.rag import ask

response = ask(
    "When are orders dispatched? and What is the delivery time?"
)

print(response)