"""
Hybrid Intent Classifier.

Uses Rule-Based classification whenever possible.
Falls back to Gemini if the Rule-Based score is too low.
"""

from config import RULE_BASED_SCORE_THRESHOLD

from intents.rule_based import detect_intents as detect_rule_based_intents
from intents.llm_classifier import classify_with_llm


def _highest_score(rule_result: dict) -> int:
    """
    Return the highest Rule-Based score.
    """

    intents = rule_result.get("intents", [])

    if not intents:
        return 0

    return max(
        intent["score"]
        for intent in intents
    )


def detect_intents(query: str) -> dict:
    """
    Hybrid Intent Detection.

    1. Try Rule-Based classification.
    2. If no intent is detected, use Gemini.
    3. If Rule-Based score is high enough, use Rule-Based.
    4. Otherwise, use Gemini.
    """

    rule_result = detect_rule_based_intents(query)

    # No intent detected → Use Gemini
    if not rule_result["intents"]:
        return classify_with_llm(query)

    highest_score = _highest_score(rule_result)

    # High-confidence Rule-Based result
    if highest_score >= RULE_BASED_SCORE_THRESHOLD:

        return {
            "method": "rule_based",
            "query": query,
            "normalized_query": rule_result["normalized_query"],
            "intents": rule_result["intents"]
        }

    # Low-confidence Rule-Based result → Use Gemini
    return classify_with_llm(query)