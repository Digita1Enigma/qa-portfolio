# QA Portfolio — Владислав Горбачёв

Добро пожаловать в моё портфолио по тестированию.  
Здесь собраны учебные проекты, демонстрирующие навыки в **API, SQL и UI тестировании**, а также интеграцию с CI/CD.

---

##  Стек
- Python (pytest, requests, jsonschema)
- SQLite (data quality проверки)
- Playwright (TypeScript, E2E UI-тесты)
- HTML-отчёты, GitHub Actions

---

##  Проекты

### [Project 1 — API QA Boost](./project1_api_qa_boost)
**Стек:** Python + pytest + requests  
- Тесты публичного API JSONPlaceholder  
- Проверка статус-кодов и JSON-структуры  
- HTML-отчёты (`pytest-html`)

Основное: `tests/test_jsonplaceholder_posts.py`

---

### [Project 2 — API Schema Validation](./project2_api_schema)
**Стек:** Python + pytest + requests + jsonschema  
- Проверка API `catfact.ninja` и `agify.io`  
- Валидация ответов по JSON Schema  
- Позитивные и негативные проверки  

Основное: `tests/test_catfacts_schema.py`, `tests/test_agify_schema.py`

---

### [Project 3 — SQL / Data Quality](./project3_sql_data_quality)
**Стек:** Python + pytest + SQLite  
- Проверка ограничений и связей в БД  
- Валидация бизнес-правил:  
  - `orders.total = сумма позиций`  
  - уникальные email/sku  
  - положительные цены/количество  
- Нарушения вызывают `IntegrityError`  

Основное: `scripts/init_db.py`, `tests/test_data_quality.py`

---

### [Project 4 — UI E2E Tests (Playwright)](./project2_ui_playwright_smoke)
**Стек:** Playwright + TypeScript  
- E2E-тесты магазина [saucedemo.com](https://www.saucedemo.com)  
- Сценарии:  
  - Успешный логин  
  - Негативный логин  
  - Добавление товара в корзину  
  - ↕Сортировка по цене и имени  
  - Логаут  
- Отчёты Playwright Report  
- CI/CD (GitHub Actions)

Основное: `tests/auth.spec.ts`, `tests/cart.spec.ts`, `tests/sort.spec.ts`, `tests/logout.spec.ts`

---

##  Как запускать локально

```bash
# установка зависимостей
pip install -r requirements.txt

# запуск тестов
pytest -v <папка_проекта>/tests --html=reports/report.html --self-contained-html
```

### UI проект (Playwright)
```bash
cd project2_ui_playwright_smoke
npm install
npx playwright install
npx playwright test
npx playwright show-report
```

