import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# ❌ Тест 1: получение несуществующего пользователя
def test_get_invalid_user():
    r = requests.get(f"{BASE_URL}/users/9999")
    assert r.status_code == 404 or r.json() == {}, "Ожидаем 404 или пустой ответ"

# ❌ Тест 2: получение пользователя с некорректным ID
def test_get_user_with_string_id():
    r = requests.get(f"{BASE_URL}/users/abc")
    assert r.status_code in [400, 404], "Должна быть ошибка"

# ❌ Тест 3: удаление несуществующего поста
def test_delete_nonexistent_post():
    r = requests.delete(f"{BASE_URL}/posts/9999")
    assert r.status_code in [404, 200], "Некорректный ID поста"

# ❌ Тест 4: POST без данных
def test_create_post_empty_body():
    r = requests.post(f"{BASE_URL}/posts", json={})
    assert r.status_code in [400, 201], "API должно вернуть ошибку или хотя бы невалидный объект"

# ❌ Тест 5: использование неподдерживаемого метода
def test_invalid_method():
    r = requests.patch(f"{BASE_URL}/posts/1")
    assert r.status_code in [400, 404, 405], "Метод не должен поддерживаться"
