import sqlite3, csv, os

def create_db(db_path=":memory:"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    cur.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, customer TEXT)")
    cur.execute("CREATE TABLE order_items(order_id INTEGER, product_id INTEGER, qty INTEGER)")
    # load CSVs
    base = os.path.join(os.path.dirname(__file__), "data")
    with open(os.path.join(base, "products.csv"), newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cur.execute("INSERT INTO products VALUES(?,?,?)", (int(row["id"]), row["name"], float(row["price"])))
    with open(os.path.join(base, "orders.csv"), newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cur.execute("INSERT INTO orders VALUES(?,?)", (int(row["id"]), row["customer"]))
    with open(os.path.join(base, "order_items.csv"), newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cur.execute("INSERT INTO order_items VALUES(?,?,?)", (int(row["order_id"]), int(row["product_id"]), int(row["qty"])))
    conn.commit()
    return conn
