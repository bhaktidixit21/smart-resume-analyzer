import sqlite3
import hashlib


DB_PATH = "database/users.db"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(name, email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, hash_password(password))
        )
        conn.commit()
        return True, "Registration Successful"

    except sqlite3.IntegrityError:
        return False, "Email already exists"

    finally:
        conn.close()


def login_user(email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )

    user = cursor.fetchone()
    conn.close()

    return user