import sqlite3

conn = sqlite3.connect("inventory.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS audit_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user TEXT,
  action TEXT,
  item_name TEXT,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()
