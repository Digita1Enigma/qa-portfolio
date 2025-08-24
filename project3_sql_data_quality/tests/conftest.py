import pytest
import sqlite3
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pathlib import Path
from scripts.init_db import rebuild_db

@pytest.fixture(scope="session")
def db_path():
    return rebuild_db()

@pytest.fixture()
def conn(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    # включить внешние ключи на сессию
    conn.execute("PRAGMA foreign_keys = ON;")
    yield conn
    conn.close()

def q(conn, sql, *params):
    return conn.execute(sql, params).fetchall()
