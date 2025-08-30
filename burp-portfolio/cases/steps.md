# Кейс 01 — httpbin + Burp Repeater

## Окружение
- Burp v2024.5.x (или твоя версия)
- Встроенный браузер Burp (Open browser)
- Scope: `httpbin.org` (Target → Scope → Add)

## Шаги
1) Открыл `https://httpbin.org/get` → запрос появился в Proxy → HTTP history.  
2) ПКМ → Send to Repeater.  
3) В Repeater отправил исходный:

GET /get HTTP/1.1
Host: httpbin.org

→ статус 200 (см. скрин `03_repeater_200.png`).

4) Скопировал вкладку (Duplicate tab) и изменил путь:


GET /status/418 HTTP/1.1
Host: httpbin.org

→ статус 418 “I'm a teapot” (см. скрин `04_repeater_418.png`).

5) Сравнил ответы в Comparer (см. `05_comparer.png`).

6) Сделал POST с JSON:


POST /post HTTP/1.1
Host: httpbin.org
Content-Type: application/json

{"sample":"data","user":"Vlad"}

→ httpbin отразил тело и заголовки.

## Артефакты
- `screenshots/*` — скриншоты шагов
- `requests/*` — сохранённые запросы/ответы
- `burp/project.burp` — состояние проекта (опционально)

## Повторяемость
Любой желающий может повторить шаги и получить те же статусы (200/418).