"""
Rule-Based Intent Classifier.
"""

from intents.matcher import match_intents


def detect_intents(query: str) -> dict:
    """
    Detect intents using the Rule-Based matcher.

    Returns:
        {
            "query": "...",
            "normalized_query": "...",
            "intents": [
                {
                    "intent": "...",
                    "score": ...,
                    "matched_keywords": [...]
                }
            ]
        }
    """

    return match_intents(query)