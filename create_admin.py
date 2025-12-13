from werkzeug.security import generate_password_hash
import sqlite3

username = "admin"
password = "peanut"   # CHANGE THIS AFTER TESTING
role = "admin"

conn = sqlite3.connect("inventory.db")

conn.execute(
    """
    INSERT OR IGNORE INTO users (username, password_hash, role)
    VALUES (?, ?, ?)
    """,
    (username, generate_password_hash(password), role)
)

conn.commit()
conn.close()

print("Admin user created (if not already present).")
