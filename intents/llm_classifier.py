"""
LLM-based Intent Classifier.
"""

import json

from config import llm, DEBUG
from intents.prompt import INTENT_CLASSIFIER_PROMPT
from intents.parser import parse_llm_response


def classify_with_llm(query: str) -> dict:
    """
    Classify the user's intent using Gemini.
    """

    prompt = f"""
{INTENT_CLASSIFIER_PROMPT}

User Query:
{query}
"""

    try:

        response = llm.invoke(prompt)

        raw_response = response.content

        # LangChain Gemini may return a list instead of a string
        if isinstance(raw_response, list):

            raw_response = "".join(
                item.get("text", "")
                for item in raw_response
                if isinstance(item, dict)
            )

        parsed_response = parse_llm_response(raw_response)

        # ---------------------------------------------
        # Debug Logs
        # ---------------------------------------------

        if DEBUG:

            print("\n========== LLM PARSED RESULT ==========")

            print(
                json.dumps(
                    parsed_response,
                    indent=4
                )
            )

            print("=======================================\n")

        intents = parsed_response.get("intents", [])

        # ---------------------------------------------
        # Friendly fallback for unsupported queries
        # ---------------------------------------------

        if (
            not intents
            or intents[0]["intent"] == "unknown"
        ):

            return {

                "method": "llm",

                "query": query,

                "intents": [

                    {

                        "intent": "unknown",

                        "confidence": 0.0

                    }

                ],

                "response":

"""I'm sorry, I couldn't understand or support that request.

I can currently help you with:

• Password Reset
• Account Unlock
• Leave Management
• Employee Profile
• Support Tickets
• Company Policies

Please try rephrasing your question."""

            }

        return {

            "method": "llm",

            "query": query,

            "intents": intents

        }

    except Exception as e:

        print("\n========== LLM ERROR ==========")
        print(e)
        print("===============================\n")

        return {

            "method": "llm",

            "query": query,

            "intents": [

                {

                    "intent": "unknown",

                    "confidence": 0.0

                }

            ],

            "response":

"""Sorry, I'm unable to process your request right now.

Please try again later."""

        }