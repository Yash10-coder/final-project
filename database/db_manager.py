import sqlite3
import bcrypt
from pathlib import Path

DB_FILE = "college_review.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        department TEXT NOT NULL
    )
    ''')
    
    # Create reviews table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        rating INTEGER NOT NULL,
        attendance_regular BOOLEAN,
        understanding_level BOOLEAN,
        feedback TEXT,
        submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def create_user(username, password, full_name, email, department):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    try:
        cursor.execute(
            'INSERT INTO users (username, password, full_name, email, department) VALUES (?, ?, ?, ?, ?)',
            (username, hashed_password, full_name, email, department)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return dict(user)
    return None

def save_review(user_id, subject, rating, attendance_regular, understanding_level, feedback):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO reviews (user_id, subject, rating, attendance_regular, understanding_level, feedback)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, subject, rating, attendance_regular, understanding_level, feedback))
    
    conn.commit()
    conn.close()

def get_user_reviewed_subjects(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT DISTINCT subject FROM reviews WHERE user_id = ?', (user_id,))
    reviewed_subjects = [row['subject'] for row in cursor.fetchall()]
    
    conn.close()
    return reviewed_subjects