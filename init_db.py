import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    quantity INTEGER,
    unit TEXT,
    min_level INTEGER
)
""")

cursor.execute("""
INSERT INTO inventory (name, category, quantity, unit, min_level)
VALUES ('Large Cups', 'Cups', 4, 'boxes', 5)
""")

conn.commit()
conn.close()

print("Database initialized successfully.")