"""
Keyword matching and scoring engine for Rule-Based Intent Detection.
"""

import re

from config import (
    PRIMARY_KEYWORD_SCORE,
    SECONDARY_KEYWORD_SCORE,
)

from intents.keywords import INTENT_KEYWORDS
from intents.normalizer import normalize_text


import re

def _contains_keyword(query: str, keyword: str) -> bool:
    """
    Flexible phrase matching.

    Allows extra words between keyword words.

    Example:
        keyword: "reset password"

        Matches:
            "reset my password"
            "reset the password"

        Doesn't match:
            "password reset"
    """

    words = keyword.split()

    pattern = r"\b"

    pattern += r"\b.*\b".join(
        re.escape(word)
        for word in words
    )

    pattern += r"\b"

    return re.search(pattern, query) is not None


def _remove_overlapping_keywords(matched_keywords: list[str]) -> list[str]:
    """
    Longest phrase wins.

    Example:

        matched:
            password
            forgot password

        result:
            forgot password
    """

    matched_keywords = sorted(
        set(matched_keywords),
        key=len,
        reverse=True
    )

    filtered = []

    for keyword in matched_keywords:

        keep = True

        for existing in filtered:

            if keyword in existing:
                keep = False
                break

        if keep:
            filtered.append(keyword)

    return filtered


def _calculate_score(
    primary_matches: list[str],
    secondary_matches: list[str]
) -> tuple[int, list[str]]:
    """
    Calculate the intent score.

    Duplicate keywords are ignored.

    Overlapping phrases are removed before scoring.
    """

    primary_matches = _remove_overlapping_keywords(primary_matches)
    secondary_matches = _remove_overlapping_keywords(secondary_matches)

    # Prevent secondary keywords that are part of
    # already matched primary phrases.

    filtered_secondary = []

    for secondary in secondary_matches:

        overlap = False

        for primary in primary_matches:

            if secondary in primary:
                overlap = True
                break

        if not overlap:
            filtered_secondary.append(secondary)

    score = (
        len(primary_matches) * PRIMARY_KEYWORD_SCORE +
        len(filtered_secondary) * SECONDARY_KEYWORD_SCORE
    )

    matched_keywords = primary_matches + filtered_secondary

    return score, matched_keywords


def match_intents(query: str) -> dict:
    """
    Match all intents against the user query.

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

    normalized_query = normalize_text(query)

    detected_intents = []

    for intent, keyword_groups in INTENT_KEYWORDS.items():

        primary_matches = []

        secondary_matches = []

        # ---------- Primary ----------

        for keyword in keyword_groups["primary"]:

            if _contains_keyword(normalized_query, keyword):
                primary_matches.append(keyword)

        # ---------- Secondary ----------

        for keyword in keyword_groups["secondary"]:

            if _contains_keyword(normalized_query, keyword):
                secondary_matches.append(keyword)

        score, matched_keywords = _calculate_score(
            primary_matches,
            secondary_matches
        )

        if score > 0:

            detected_intents.append({

                "intent": intent,

                "score": score,

                "matched_keywords": matched_keywords

            })

    detected_intents.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return {

        "query": query,

        "normalized_query": normalized_query,

        "intents": detected_intents

    }