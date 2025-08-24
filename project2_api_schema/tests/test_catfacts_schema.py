from jsonschema import validate
from project2_api_schema.utils import load_schema  # ← вот так
CAT_BASE = "https://catfact.ninja"

def test_catfact_single_shape(http):
    schema = load_schema("cat_fact_schema.json")
    r = http.get(f"{CAT_BASE}/fact", timeout=15)
    assert r.status_code == 200, f"Status {r.status_code}, body: {r.text[:300]}"
    data = r.json()
    validate(instance=data, schema=schema)
    assert len(data["fact"].strip()) > 0
    assert data["length"] >= 1

def test_catfacts_list_basic(http):
    r = http.get(f"{CAT_BASE}/facts?limit=5", timeout=15)
    assert r.status_code == 200
    payload = r.json()
    assert "data" in payload and isinstance(payload["data"], list)

    schema = load_schema("cat_fact_schema.json")
    for item in payload["data"]:
        validate(instance=item, schema=schema)

