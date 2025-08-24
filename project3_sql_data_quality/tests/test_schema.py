import pytest
import sqlite3

def test_foreign_keys_enabled(conn):
    val = conn.execute("PRAGMA foreign_keys;").fetchone()[0]
    assert val == 1

def test_users_email_unique(conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO users(id,email,name,created_at) VALUES (3,'alice@example.com','Dup','2025-08-04T12:00:00Z')"
        )

def test_orders_user_fk(conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO orders(id,user_id,status,total,created_at) VALUES (102,999,'new',0,'2025-08-03T12:00:00Z')"
        )

def test_order_items_fks(conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO order_items(id,order_id,product_id,qty,price) VALUES (2000,999,1,1,9.99)"
        )
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO order_items(id,order_id,product_id,qty,price) VALUES (2001,100,999,1,9.99)"
        )
