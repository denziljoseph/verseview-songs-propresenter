import sqlite3
from config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def fetch_data(query, params=()):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        return cur.fetchall()

def list_tables():
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    return fetch_data(query)
