import sqlite3
from pathlib import Path

DB_PATH = Path("data/quit_tracker.db")

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            quit_date TEXT,
            cigarettes_per_day INTEGER,
            daily_cost REAL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS daily_log (
            id INTEGER PRIMARY KEY,
            date TEXT,
            cravings INTEGER,
            notes TEXT
        )
    """)

    conn.commit()
    conn.close()
