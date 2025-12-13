import sqlite3

conn = sqlite3.connect("inventory.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE,
  password TEXT,
  role TEXT
)
""")

# Example users
c.execute("INSERT OR IGNORE INTO users VALUES (NULL, 'admin', 'admin123', 'admin')")
c.execute("INSERT OR IGNORE INTO users VALUES (NULL, 'staff', 'staff123', 'staff')")

conn.commit()
conn.close()
