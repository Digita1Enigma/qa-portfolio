import json
import os
from typing import Dict

def load_schema(name: str) -> Dict:
    here = os.path.dirname(__file__)
    path = os.path.join(here, "schemas", name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
