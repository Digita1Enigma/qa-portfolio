from db_loader import create_db
from math import isclose

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


    from math import isclose

def test_required_user_fields_not_null(conn):
    row = conn.execute("SELECT COUNT(*) FROM users WHERE email IS NULL OR name IS NULL OR created_at IS NULL").fetchone()[0]
    assert row == 0

def test_product_prices_non_negative(conn):
    row = conn.execute("SELECT COUNT(*) FROM products WHERE price < 0").fetchone()[0]
    assert row == 0

def test_order_totals_match_items(conn):
    # проверим, что total = сумма (qty*price) по order_items
    for (order_id,) in conn.execute("SELECT id FROM orders"):
        sum_items = conn.execute("""
            SELECT COALESCE(SUM(qty*price),0) FROM order_items WHERE order_id=?
        """,(order_id,)).fetchone()[0]
        total = conn.execute("SELECT total FROM orders WHERE id=?", (order_id,)).fetchone()[0]
        assert isclose(sum_items, total, rel_tol=1e-9), f"Order {order_id}: items={sum_items}, total={total}"

def test_orders_status_enforced(conn):
    bad = conn.execute("SELECT COUNT(*) FROM orders WHERE status NOT IN ('new','paid','shipped','cancelled')").fetchone()[0]
    assert bad == 0

def test_cannot_insert_negative_price_or_qty(conn,):
    import sqlite3, pytest
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute("INSERT INTO products(id,sku,title,price) VALUES (99,'SKU-NEG','Bad',-1)")
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute("INSERT INTO order_items(id,order_id,product_id,qty,price) VALUES (3000,100,1,0,9.99)")

