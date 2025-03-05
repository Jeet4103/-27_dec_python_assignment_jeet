import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
    )
''')

cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", ("Alice", 30, "HR"))
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", ("Bob", 25, "IT"))
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", ("Charlie", 28, "Finance"))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print("\n🔹 Employee Records:")
for row in rows:
    print(row)

conn.close()
