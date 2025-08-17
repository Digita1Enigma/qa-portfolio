import requests

def test_list_users(base_reqres):
    r = requests.get(f"{base_reqres}/users?page=2", timeout=20)
    assert r.status_code == 200
    data = r.json()
    assert "data" in data and len(data["data"]) > 0

def test_create_user(base_reqres):
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post(f"{base_reqres}/users", json=payload, timeout=20)
    assert r.status_code in (200, 201)
    data = r.json()
    for k, v in payload.items():
        assert data.get(k) == v
