import sqlite3
import os

DB_PATH = "bot_data.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    # Foydalanuvchilar jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Statistika jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total INTEGER DEFAULT 0,
            malicious INTEGER DEFAULT 0,
            suspicious INTEGER DEFAULT 0,
            safe INTEGER DEFAULT 0,
            feedback_correct INTEGER DEFAULT 0,
            feedback_wrong INTEGER DEFAULT 0
        )
    ''')

    # Statistika boshlang'ich qiymati
    cursor.execute("SELECT COUNT(*) FROM stats")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO stats VALUES (1, 0, 0, 0, 0, 0, 0)")

    conn.commit()
    conn.close()

def db_add_user(user_id, name):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)",
        (user_id, name)
    )
    conn.commit()
    conn.close()

def db_get_users():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]

def db_get_user_count():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def db_add_check(result_type):
    conn = get_conn()
    cursor = conn.cursor()
    if result_type == "malicious":
        cursor.execute("UPDATE stats SET total=total+1, malicious=malicious+1 WHERE id=1")
    elif result_type == "suspicious":
        cursor.execute("UPDATE stats SET total=total+1, suspicious=suspicious+1 WHERE id=1")
    else:
        cursor.execute("UPDATE stats SET total=total+1, safe=safe+1 WHERE id=1")
    conn.commit()
    conn.close()

def db_add_feedback(feedback_type):
    conn = get_conn()
    cursor = conn.cursor()
    if feedback_type == "correct":
        cursor.execute("UPDATE stats SET feedback_correct=feedback_correct+1 WHERE id=1")
    else:
        cursor.execute("UPDATE stats SET feedback_wrong=feedback_wrong+1 WHERE id=1")
    conn.commit()
    conn.close()

def db_get_stats():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats WHERE id=1")
    row = cursor.fetchone()
    conn.close()
    return {
        "total": row[1],
        "malicious": row[2],
        "suspicious": row[3],
        "safe": row[4],
        "feedback_correct": row[5],
        "feedback_wrong": row[6],
        "users": db_get_user_count()
    }