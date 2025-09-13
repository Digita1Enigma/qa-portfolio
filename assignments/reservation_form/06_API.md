# Валидация
- name: 1–100, не пусто; email: формат + уникальность; age: 0–120, integer.
# Негативы (JSON)
a) {"name": "", "email": "a@b.com", "age": 27} → 400  
b) {"name": "Анна", "email": "bad", "age": 27} → 400  
c) {"name": "Анна", "email": "dup@ex.com", "age": -1} → 400/422  
# Ожидаемые коды
201 (Location: /api/v1/users/{id}), 400/422 (валидация), 409 (дубликат email), 415 (неверный Content-Type).
# Заголовки
Request: Content-Type/Accept: application/json (+ Authorization при наличии).
Response: Content-Type: application/json, Cache-Control: no-store.
