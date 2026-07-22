import sqlite3

DB_NAME = "expenses.db"


def get_connection():
    # connects to the database file, creates it if it doesn't exist yet
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # creates the expenses table if it doesn't already exist
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

    def add_expense(title, amount, category, date):
    conn = get_connection()
    conn.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
        (title, amount, category, date)
    )
    conn.commit()
    conn.close()


def get_all_expenses():
    conn = get_connection()
    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY date DESC"
    ).fetchall()
    conn.close()
    return expenses

def get_total():
    conn = get_connection()
    result = conn.execute("SELECT SUM(amount) AS total FROM expenses").fetchone()
    conn.close()
    return result["total"] if result["total"] else 0


def get_totals_by_category():
    conn = get_connection()
    results = conn.execute(
        "SELECT category, SUM(amount) AS total FROM expenses GROUP BY category"
    ).fetchall()
    conn.close()
    return results