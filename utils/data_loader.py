import json
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directory
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    """
    Load data from a JSON file.
    """
    file_path = DATA_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(filename, data):
    """
    Save data to a JSON file.
    """
    file_path = DATA_DIR / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_text(filepath):
    """
    Load text from a file.
    """

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

