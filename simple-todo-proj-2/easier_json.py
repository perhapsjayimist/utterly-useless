import json
from pathlib import Path

# folder where this file lives
BASE_DIR = Path(__file__).parent

# lists folder next to it
LISTS_DIR = BASE_DIR / "lists"


def load(name):
    file = LISTS_DIR / f"{name}.json"

    if not file.exists():
        print(f"File does not exist. Creating '{name}.json'")
        file.write_text("[]")
        return []

    print(f"Loading existing file '{name}.json'")

    with open(file, "r") as f:
        return json.load(f)


def save(name, data):
    file = LISTS_DIR / f"{name}.json"

    with open(file, "w") as f:
        json.dump(data, f, indent=4)