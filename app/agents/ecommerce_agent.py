# from app.agents.tools import documentation_tool


# class EcommerceAgent:

#     def invoke(self, question: str) -> str:
#         return documentation_tool(question)

# from app.agents.tools import documentation_tool, product_tool


# class EcommerceAgent:
#     """
#     Ecommerce AI Agent.

#     Responsible for deciding which tool should
#     answer the user's question.
#     """

#     def invoke(self, question: str) -> str:
#         question_lower = question.lower()

#         # Product related questions
#         if any(
#             keyword in question_lower
#             for keyword in [
#                 "product",
#                 "products",
#                 "laptop",
#                 "mobile",
#                 "phone",
#                 "price",
#                 "category",
#             ]
#         ):
#             # return product_tool()
#             return product_tool(question)

#         # Everything else goes through RAG
#         return documentation_tool(question)

from app.agents.graph import graph


class EcommerceAgent:

    def invoke(self, question: str):

        result = graph.invoke(
            {
                "question": question,
                "route": "",
                "answer": "",
            }
        )

        return result["answer"]