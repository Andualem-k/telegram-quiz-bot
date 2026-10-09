import sqlite3

DB_NAME = "bot_data.db"

def init_db():
    """Database እና Table መፍጠር"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paid_users (
            user_id INTEGER PRIMARY KEY,
            approved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_paid_user(user_id: int):
    """የከፈለ ተጠቃሚን መመዝገብ"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO paid_users (user_id) VALUES (?)
    ''', (user_id,))
    conn.commit()
    conn.close()

def is_user_paid(user_id: int) -> bool:
    """ተጠቃሚው መክፈሉን ማረጋገጥ"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT user_id FROM paid_users WHERE user_id = ?
    ''', (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row is not None

def get_paid_users_count() -> int:
    """የከፈሉ ተጠቃሚዎችን ብዛት ማወቅ"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM paid_users')
    count = cursor.fetchone()[0]
    conn.close()
    return count
