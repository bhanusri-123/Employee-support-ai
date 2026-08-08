"""
Defines the LangGraph workflow.
"""

from langgraph.graph import StateGraph, START, END

from graph.state import ChatState
from graph.nodes import (
    intent_node,
    tool_node,
    policy_node,
    formatter_node,
    route_after_intent
)


def build_graph():

    workflow = StateGraph(ChatState)

    workflow.add_node("intent", intent_node)
    workflow.add_node("tool", tool_node)
    workflow.add_node("policy", policy_node)
    workflow.add_node("formatter", formatter_node)

    workflow.add_edge(START, "intent")

    workflow.add_conditional_edges(
        "intent",
        route_after_intent,
        {
            "tool": "tool",
            "policy": "policy"
        }
    )

    workflow.add_edge("tool", "formatter")
    workflow.add_edge("policy", "formatter")

    workflow.add_edge("formatter", END)

    return workflow.compile()