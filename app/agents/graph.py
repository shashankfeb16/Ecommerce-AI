from langgraph.graph import END, StateGraph

from app.agents.state import AgentState
from app.agents.nodes import (
    router_node,
    product_node,
    documentation_node,
)


builder = StateGraph(AgentState)

builder.add_node("router", router_node)
builder.add_node("product", product_node)
builder.add_node("documentation", documentation_node)


builder.set_entry_point("router")


def route(state: AgentState):
    return state["route"]


builder.add_conditional_edges(
    "router",
    route,
    {
        "product": "product",
        "documentation": "documentation",
    },
)

builder.add_edge("product", END)
builder.add_edge("documentation", END)

graph = builder.compile()