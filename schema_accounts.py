import sqlite3
from settings import DBPATH

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        DROP_SQL = "DROP TABLE IF EXISTS accounts;"
        cursor.execute(DROP_SQL)

        CREATE_SQL = """CREATE TABLE accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number VARCHAR(10) NOT NULL,
            first_name VARCHAR(128),
            last_name VARCHAR(128),
            pin VARCHAR(4),
            balance FLOAT
        );"""
        cursor.execute(CREATE_SQL)

if __name__ == "__main__":
    schema()