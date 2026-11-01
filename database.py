import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = sqlite3.connect('chatbot.db')
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                user_message TEXT NOT NULL,
                bot_response TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                intent TEXT,
                confidence REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS faq (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                category TEXT,
                keywords TEXT
            )
        ''')
        conn.commit()

def log_conversation(session_id, user_message, bot_response, intent, confidence):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO conversations (session_id, user_message, bot_response, intent, confidence)
            VALUES (?, ?, ?, ?, ?)
        ''', (session_id, user_message, bot_response, intent, confidence))
        conn.commit()

def get_conversations(session_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT user_message, bot_response, timestamp, intent, confidence
            FROM conversations 
            WHERE session_id = ?
            ORDER BY timestamp DESC
            LIMIT 50
        ''', (session_id,))
        return [
            {
                'user_message': conv[0],
                'bot_response': conv[1],
                'timestamp': conv[2],
                'intent': conv[3],
                'confidence': conv[4]
            }
            for conv in cursor.fetchall()
        ]

def get_faq():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT question, answer, category FROM faq ORDER BY category, question')
        return [
            {
                'question': faq[0],
                'answer': faq[1],
                'category': faq[2]
            }
            for faq in cursor.fetchall()
        ]
