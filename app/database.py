import sqlite3

class Database:
    def __init__(self, db_name="finance.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY,
            amount REAL,
            date TEXT,
            description TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS expense (
            id INTEGER PRIMARY KEY,
            amount REAL,
            date TEXT,
            description TEXT
        )
        """)
        self.connection.commit()

db=Database()
db.create_tables()