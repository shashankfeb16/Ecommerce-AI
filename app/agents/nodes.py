from app.agents.tools import documentation_tool, product_tool
from app.agents.state import AgentState


def router_node(state: AgentState):
    question = state["question"].lower()

    product_keywords = [
        "product",
        "products",
        "laptop",
        "mobile",
        "phone",
        "price",
        "category",
    ]

    if any(keyword in question for keyword in product_keywords):
        state["route"] = "product"
    else:
        state["route"] = "documentation"

    return state


def product_node(state: AgentState):
    state["answer"] = product_tool(state["question"])
    return state


def documentation_node(state: AgentState):
    state["answer"] = documentation_tool(state["question"])
    return state