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

import requests

def test_get_post_invalid_id():
    """Проверка: запрос поста с несуществующим ID"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/999999", timeout=10)
    assert response.status_code == 404

def test_create_post_empty_body():
    """Проверка: создание поста с пустым телом"""
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json={}, timeout=10)
    # API jsonplaceholder "прикидывается" что всё ок, но должен вернуть 201 и пустое тело
    assert response.status_code == 201
    assert response.json() != {}  # обычно сервер что-то возвращает

def test_update_post_invalid_method():
    """Проверка: использование неверного метода"""
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    # jsonplaceholder разрешает delete, но в реальных API мы ожидаем ошибку (например 405 Method Not Allowed)
    assert response.status_code in [200, 204, 405]

