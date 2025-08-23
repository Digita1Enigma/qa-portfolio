# API Testing Project — JSONPlaceholder

Учебный проект по автоматизации REST API на Python.

## Стек
Python 3.11 · pytest · requests · jsonschema · pytest-html · GitHub

## Что покрыто
- **Позитивные:** `GET /posts`, `GET /posts/{id}`, `POST /posts`.
- **Негативные:** несуществующий ресурс (404), некорректный ID/метод, пустое тело запроса.
- Параметризация тестов, базовые фикстуры, JSON Schema валидация.

Скриншоты:
![bandicam 2025-08-17 13-12-04-613](https://github.com/user-attachments/assets/842efc91-f0e3-4cfd-9c08-65bdf53d37b8)
![bandicam 2025-08-17 13-15-48-878](https://github.com/user-attachments/assets/d64bdcb5-f48d-483a-a84a-fe821c42f624)
![bandicam 2025-08-17 13-13-30-918](https://github.com/user-attachments/assets/8b7214de-24ab-43b1-807c-89749e8a330e)

## UI автотесты (Playwright + TypeScript)

В репозитории есть мини-смоук по UI в папке [`ui-playwright-ts`](./ui-playwright-ts).

**Что проверяет:** логин на https://www.saucedemo.com и наличие списка товаров.  
**Стек:** Playwright, TypeScript, HTML-отчёт.

### Локальный запуск
```bash
cd ui-playwright-ts
npm i
npx playwright install
npx playwright test



## Быстрый старт
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -v

HTML-отчёт:
pytest -v --html=reports/report.html --self-contained-html

Структура:
tests/                  # тесты (позитив/негатив/параметризация/схемы)
conftest.py             # фикстуры и опции
pytest.ini              # конфигурация pytest
requirements.txt        # зависимости

Примечание:
```bash
git add README.md .gitignore
git commit -m "Docs: add README and .gitignore"
git push
