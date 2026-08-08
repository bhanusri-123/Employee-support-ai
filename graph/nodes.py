"""
LangGraph Nodes
"""
import time
from rag.rag_chain import answer_policy_question
from graph import state
import intents
from intents.hybrid import detect_intents
from chatbot.intent_router import IntentRouter
from chatbot.response_formatter import format_response

from utils.data_loader import load_json, load_text


# -------------------------------------------------
# Load mock data once
# -------------------------------------------------

EMPLOYEE = load_json("employees.json")[0]

TICKETS = load_json("tickets.json")

POLICIES = {

    "leave_policy":
        load_text("data/policies/leave_policy.txt"),

    "office_policy":
        load_text("data/policies/office_policy.txt"),

    "travel_policy":
        load_text("data/policies/travel_policy.txt"),

    "wfh_policy":
        load_text("data/policies/wfh_policy.txt"),

    "insurance_policy":
        load_text("data/policies/insurance_policy.txt")
}


ROUTER = IntentRouter(
    EMPLOYEE,
    TICKETS,
    POLICIES
)


# -------------------------------------------------
# Intent Detection Node
# -------------------------------------------------

def intent_node(state):

    start = time.perf_counter()

    result = detect_intents(state["query"])

    state["intent_result"] = result

    state["method"] = result.get("method", "rule_based")

    intents = result.get("intents", [])

    if intents:

        state["intent"] = intents[0]["intent"]

        if "confidence" in intents[0]:

            state["confidence"] = round(
                intents[0]["confidence"] * 100,
                2
            )

        else:

            score = intents[0].get("score", 0)

            state["confidence"] = min(
                score * 25,
                100
            )

    else:

        state["intent"] = "unknown"

        state["confidence"] = 0

    state["response_time"] = (
        time.perf_counter() - start
    )

    return state

# -------------------------------------------------
# Tool Execution Node
# -------------------------------------------------

def tool_node(state):

    # ---------------------------------------------
    # Unknown query -> return friendly response
    # ---------------------------------------------

    if (
        state["intent"] == "unknown"
        and "response" in state["intent_result"]
    ):

        state["tool_result"] = [

            {

                "tool": "unknown",

                "message": state["intent_result"]["response"]

            }

        ]

        return state

    # ---------------------------------------------
    # Execute tools normally
    # ---------------------------------------------

    intents = state["intent_result"]["intents"]

    ROUTER.query = state["query"]

    results = ROUTER.execute(intents)

    state["tool_result"] = results

    return state

# -------------------------------------------------
# Policy Node
# (RAG will replace this later)
# -------------------------------------------------

def policy_node(state):

    result = answer_policy_question(
        state["query"]
    )

    state["tool_result"] = [result]

    state["method"] = "rag"

    return state


# -------------------------------------------------
# Response Formatter Node
# -------------------------------------------------
def formatter_node(state):

    state["response"] = format_response(
        state["tool_result"]
    )

    return state


# -------------------------------------------------
# Routing Function
# -------------------------------------------------

def route_after_intent(state):

    intents = state["intent_result"]["intents"]

    if not intents:

        return "tool"

    first_intent = intents[0]["intent"]

    if first_intent == "policy_query":

        return "policy"

    return "tool"