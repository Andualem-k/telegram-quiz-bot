import sqlite3

DB_NAME = "bot_data.db"

def init_db():
    """Database, paid_users እና all_users tables መፍጠር"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 1. Table for paid users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paid_users (
            user_id INTEGER PRIMARY KEY,
            approved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 2. Table for tracking all users (for broadcast)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS all_users (
            user_id INTEGER PRIMARY KEY,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def add_all_user(user_id: int):
    """ቦቱን የጀመረን ማንኛውንም ተጠቃሚ መመዝገብ"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO all_users (user_id) VALUES (?)
    ''', (user_id,))
    conn.commit()
    conn.close()

def get_all_users() -> list:
    """የሁሉም ተጠቃሚዎች ID ዝርዝር ማግኘት"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM all_users')
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

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

def get_total_users_count() -> int:
    """የጠቅላላ ተጠቃሚዎችን ብዛት ማወቅ"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM all_users')
    count = cursor.fetchone()[0]
    conn.close()
    return count
