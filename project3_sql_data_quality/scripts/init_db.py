import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "shop.db"

SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  sku TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  price REAL NOT NULL CHECK(price >= 0)
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('new','paid','shipped','cancelled')),
  total REAL NOT NULL CHECK(total >= 0),
  created_at TEXT NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
  id INTEGER PRIMARY KEY,
  order_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  qty INTEGER NOT NULL CHECK(qty > 0),
  price REAL NOT NULL CHECK(price >= 0),
  FOREIGN KEY(order_id) REFERENCES orders(id),
  FOREIGN KEY(product_id) REFERENCES products(id)
);
"""

SEED_SQL = """
INSERT INTO users(id,email,name,created_at) VALUES
  (1,'alice@example.com','Alice','2025-08-01T10:00:00Z'),
  (2,'bob@example.com','Bob','2025-08-02T11:00:00Z');

INSERT INTO products(id,sku,title,price) VALUES
  (1,'SKU-RED-1','Red Widget', 9.99),
  (2,'SKU-BLUE-1','Blue Widget', 12.50),
  (3,'SKU-GREEN-1','Green Widget', 5.00);

INSERT INTO orders(id,user_id,status,total,created_at) VALUES
  (100,1,'paid',  32.48,'2025-08-03T09:00:00Z'),
  (101,2,'new',    5.00,'2025-08-03T10:00:00Z');

INSERT INTO order_items(id,order_id,product_id,qty,price) VALUES
  (1000,100,1,2,9.99),    -- 2 * 9.99 = 19.98
  (1001,100,2,1,12.50),   -- 12.50
  (1002,101,3,1,5.00);    -- 5.00
"""

def rebuild_db():
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(SCHEMA_SQL)
        conn.executescript(SEED_SQL)
        conn.commit()
    finally:
        conn.close()
    return DB_PATH

if __name__ == "__main__":
    path = rebuild_db()
    print(f"DB rebuilt at: {path}")
