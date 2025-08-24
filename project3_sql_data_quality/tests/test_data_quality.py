from db_loader import create_db

def test_foreign_keys_and_totals():
    conn = create_db()
    c = conn.cursor()
    # 1) orphan items check: все product_id должны существовать
    c.execute("""
        SELECT oi.product_id
        FROM order_items oi
        LEFT JOIN products p ON p.id = oi.product_id
        WHERE p.id IS NULL
    """)
    assert c.fetchall() == [], "Найдены строки без существующего product_id"

    # 2) заказ с суммой > 0 и корректным подсчетом
    c.execute("""
        SELECT o.id, SUM(oi.qty * p.price) AS total
        FROM orders o
        JOIN order_items oi ON oi.order_id = o.id
        JOIN products p ON p.id = oi.product_id
        GROUP BY o.id
        ORDER BY o.id
    """)
    totals = c.fetchall()
    assert totals[0][1] > 0
    assert totals[1][1] > 0
    conn.close()
