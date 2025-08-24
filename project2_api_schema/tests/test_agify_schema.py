from jsonschema import validate
from project2_api_schema.utils import load_schema  # ← вот так
import pytest

AGIFY = "https://api.agify.io"

@pytest.mark.parametrize("name", ["michael", "sarah", "vlad", "olga", "alex"])
def test_agify_schema_and_ranges(http, name):
    schema = load_schema("agify_schema.json")
    r = http.get(f"{AGIFY}?name={name}", timeout=15)
    assert r.status_code == 200, f"Unexpected status: {r.status_code}"
    data = r.json()
    validate(instance=data, schema=schema)

    assert data["name"].lower() == name.lower()
    if data["age"] is not None:
        assert 0 <= data["age"] <= 120
    assert data["count"] >= 0

def test_agify_empty_name_behaviour(http):
    schema = load_schema("agify_schema.json")
    r = http.get(f"{AGIFY}?name=", timeout=15)
    assert r.status_code == 200
    data = r.json()
    validate(instance=data, schema=schema)

    assert data["name"] == ""
    assert data["age"] is None
    assert data["count"] == 0
