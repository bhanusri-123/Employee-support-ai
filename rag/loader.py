"""
Loads policy documents.
"""

from pathlib import Path


POLICY_FOLDER = Path("data/policies")


def load_documents():

    documents = []

    for file in POLICY_FOLDER.glob("*.txt"):

        with open(file, "r", encoding="utf-8") as f:

            documents.append({

                "name": file.stem,

                "text": f.read()

            })

    return documents