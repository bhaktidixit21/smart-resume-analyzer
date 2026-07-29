import sqlite3

def create_database():
    connection = sqlite3.connect("database/users.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()
    print("Database Created Successfully")