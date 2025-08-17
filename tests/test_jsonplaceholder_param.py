import requests
import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3, 10, 50, 100])
def test_get_post_by_id(base_json, post_id):
    r = requests.get(f"{base_json}/posts/{post_id}", timeout=20)
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == post_id
    assert isinstance(data["title"], str) and data["title"].strip()
