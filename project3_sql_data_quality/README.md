# Project 3 — SQL Data Quality (SQLite + pytest)

Мини‑проект проверки качества данных: заказы/строки/товары. Тесты валидируют связи и суммы.

## Что проверяем
- Внешние ключи (`PRAGMA foreign_keys = ON`)
- Уникальность email, SKU
- Положительность цен и количеств
- Соответствие `orders.total` сумме позиций заказа
- Допустимые статусы заказов
- Ошибки при вставке некорректных записей (IntegrityError)



## Запуск
```bash
python -m pip install -r requirements.txt
pytest -s

cd project3_sql_data_quality
# создание/пересоздание БД
python scripts/init_db.py
# запуск тестов (из корня репо):
cd ..
pytest -v project3_sql_data_quality/tests --html=reports/sql_report.html --self-contained-html
```