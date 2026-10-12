"""sqlite3 из стандартной библиотеки. Параметры только через ? — никаких f-строк в SQL."""

import sqlite3
from pathlib import Path

db_path = Path("_cheat.db")
if db_path.exists():
    db_path.unlink()

con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row          # строки как dict: row["email"]
cur = con.cursor()

cur.execute("""
CREATE TABLE users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    age   INTEGER NOT NULL
)
""")
cur.execute("""
CREATE TABLE tasks (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    title    TEXT NOT NULL,
    user_id  INTEGER NOT NULL REFERENCES users(id)
)
""")

cur.execute("INSERT INTO users (email, age) VALUES (?, ?)", ("anya@test.ru", 25))
cur.execute("INSERT INTO users (email, age) VALUES (?, ?)", ("boris@test.ru", 30))
uid = cur.execute("SELECT id FROM users WHERE email = ?", ("anya@test.ru",)).fetchone()["id"]
cur.executemany(
    "INSERT INTO tasks (title, user_id) VALUES (?, ?)",
    [("хлеб", uid), ("молоко", uid)],
)
con.commit()

row = cur.execute("SELECT email, age FROM users WHERE age >= ?", (26,)).fetchone()
print(dict(row))                       # {'email': 'boris@test.ru', 'age': 30}

print("JOIN:")
for r in cur.execute("""
    SELECT u.email, t.title
    FROM users u
    JOIN tasks t ON t.user_id = u.id
    ORDER BY u.email, t.title
"""):
    print(r["email"], r["title"])

# LEFT JOIN: все пользователи, даже без задач
print("LEFT + COUNT:")
for r in cur.execute("""
    SELECT u.email, COUNT(t.id) AS n
    FROM users u
    LEFT JOIN tasks t ON t.user_id = u.id
    GROUP BY u.id
    HAVING COUNT(t.id) >= 0
"""):
    print(r["email"], r["n"])

con.close()
db_path.unlink()

# con.commit() после записи; при ошибке con.rollback()
# executemany — пачка INSERT
# fetchone / fetchall / for row in cur.execute(...)
print("SQL руками здесь; ORM — 09_fastapi/07_sqlalchemy.py")
