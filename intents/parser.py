"""
Utilities for parsing LLM responses.
"""

import json
import re


def clean_json(text: str) -> str:
    """
    Remove markdown code fences from
    Gemini responses.
    """

    text = text.strip()

    # Remove ```json
    text = re.sub(
        r"^```json",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Remove ```
    text = re.sub(
        r"```$",
        "",
        text
    )

    return text.strip()


def parse_llm_response(response: str) -> dict:
    """
    Parse JSON returned by Gemini.
    """

    response = clean_json(response)

    try:
        return json.loads(response)

    except json.JSONDecodeError:

        return {

            "intents": [

                {

                    "intent": "unknown",

                    "confidence": 0.0

                }

            ]

        }