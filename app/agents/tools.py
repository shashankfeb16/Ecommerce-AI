from langchain_core.tools import tool

from app.ai.retriever import retrieve
from app.services.product_service import ProductService


def documentation_tool(question: str) -> str:
    """
    Search the ecommerce documentation and return the relevant context.
    """
    return retrieve(question)


def product_tool(question: str) -> str:
    """
    Search products in the ecommerce catalog.
    """

    products = ProductService.search_products(question)

    if not products:
        return "No products found."

    response = "Available Products:\n\n"

    for product in products:
        response += (
            f"- {product['name']} "
            f"(Category: {product['category']}, "
            f"Price: ₹{product['price']})\n"
        )

    return response