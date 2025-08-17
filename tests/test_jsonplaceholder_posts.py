import json, requests
from jsonschema import validate

POST_SCHEMA = {
  "type":"object",
  "required":["userId","id","title","body"],
  "properties":{"userId":{"type":"number"},"id":{"type":"number"},"title":{"type":"string"},"body":{"type":"string"}}
}

def test_get_post_1(base_json):
    r = requests.get(f"{base_json}/posts/1", timeout=20)
    assert r.status_code == 200
    data = r.json()
    validate(instance=data, schema=POST_SCHEMA)
    assert data["id"] == 1
