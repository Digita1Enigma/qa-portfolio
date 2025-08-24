import json, os, pytest, requests

@pytest.fixture(scope="session")
def http():
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    return s

def load_schema(name: str) -> dict:
    here = os.path.dirname(__file__)
    path = os.path.join(here, "schemas", name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)