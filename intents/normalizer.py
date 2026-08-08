"""
Text normalization utilities for intent detection.
"""

import re


def normalize_text(text: str) -> str:
    """
    Normalize user input before intent matching.

    Steps:
    1. Convert to lowercase.
    2. Normalize repeated letters.
    3. Remove punctuation.
    4. Collapse multiple spaces.
    5. Strip leading/trailing spaces.
    """

    text = text.lower()

    # Normalize repeated letters
    # hellooo -> hello
    # hiiii -> hi
    # byeeee -> bye
    # thankssss -> thanks

    text = re.sub(r'([a-z])\1{2,}', r'\1', text)

    # Keep only letters, numbers and spaces
    text = re.sub(r"[^\w\s]", " ", text)

    # Replace multiple spaces with one space
    text = re.sub(r"\s+", " ", text)

    return text.strip()