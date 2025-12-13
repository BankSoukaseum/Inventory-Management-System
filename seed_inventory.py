import sqlite3

items = [
    # Tea & Powders
    ("Ceylon Tea", "Tea & Powders", 0, "bags", 2),
    ("Green Tea", "Tea & Powders", 0, "bags", 2),
    ("Yuchi Black Tea", "Tea & Powders", 0, "bags", 2),
    ("Oolong Tea", "Tea & Powders", 0, "bags", 2),
    ("Buckwheat Tea", "Tea & Powders", 0, "bags", 2),
    ("Pearls", "Tea & Powders", 0, "bags", 3),
    ("A+ Powder", "Tea & Powders", 0, "bags", 2),
    ("Coffee Jelly Powder", "Tea & Powders", 0, "bags", 2),
    ("Coffee Powder", "Tea & Powders", 0, "bags", 2),
    ("Matcha Powder", "Tea & Powders", 0, "bags", 2),
    ("Coconut Powder", "Tea & Powders", 0, "bags", 2),
    ("Milk Powder", "Tea & Powders", 0, "bags", 2),
    ("Raw Sugar", "Tea & Powders", 0, "bags", 2),
    ("Plum", "Tea & Powders", 0, "bags", 2),
    ("Kanten Jelly", "Tea & Powders", 0, "bags", 2),
    ("Creme Brulee Powder", "Tea & Powders", 0, "bags", 2),
    ("Choc Brulee", "Tea & Powders", 0, "bags", 2),

    # Syrups & Liquids
    ("Fried Sugar", "Syrups & Liquids", 0, "bottle", 2),
    ("Sucrose", "Syrups & Liquids", 0, "bottle", 2),
    ("Brown Sugar", "Syrups & Liquids", 0, "bottle", 2),
    ("Dragon Fruit Juice", "Syrups & Liquids", 0, "bottle", 2),
    ("Strawberry Syrup", "Syrups & Liquids", 0, "bottle", 2),
    ("Plum Syrup", "Syrups & Liquids", 0, "bottle", 2),
    ("Grapefruit Syrup", "Syrups & Liquids", 0, "bottle", 2),
    ("Passionfruit Syrup", "Syrups & Liquids", 0, "bottle", 2),
    ("Longan Syrup", "Syrups & Liquids", 0, "bottle", 2),
    ("Yoghurt Syrup", "Syrups & Liquids", 0, "bottle", 2),
    ("Orange Syrup", "Syrups & Liquids", 0, "bottle", 2),
    ("Coconut Jelly", "Syrups & Liquids", 0, "bottle", 2),
    ("Mango Jam", "Syrups & Liquids", 0, "bottle", 2),

    # Dairy
    ("Long Life Milk", "Dairy & Milk", 0, "carton", 6),
    ("Oat Milk", "Dairy & Milk", 0, "carton", 6),
    ("Condensed Milk", "Dairy & Milk", 0, "tray", 1),

    # Toppings & Fruits
    ("Diced Mango", "Toppings & Fruits", 0, "cans", 4),
    ("Grapefruit Sacs", "Toppings & Fruits", 0, "cans", 4),
    ("Red Bean", "Toppings & Fruits", 0, "cans", 4),

    # Cups & Straws
    ("Cold Cups (Medium)", "Cups & Straws", 0, "stack", 3),
    ("Cold Cups (Large)", "Cups & Straws", 0, "stack", 3),
    ("Hot Cups (Medium)", "Cups & Straws", 0, "stack", 3),
    ("Hot Cups (Large)", "Cups & Straws", 0, "stack", 3),
    ("Clear Lids", "Cups & Straws", 0, "stack", 3),
    ("White Lids", "Cups & Straws", 0, "stack", 3),
    ("Straws (Thick)", "Cups & Straws", 0, "stack", 3),
    ("Straws (Thin)", "Cups & Straws", 0, "stack", 3),
    ("Paper Straws (Thick)", "Cups & Straws", 0, "stack", 3),
    ("Paper Straws (Thin)", "Cups & Straws", 0, "stack", 3),
    ("Panna Cotta Bottles", "Cups & Straws", 0, "box", 1),

    # Packaging
    ("Cup Sealing Roll", "Packaging & Consumables", 0, "roll", 1),
    ("Cup Label Stickers", "Packaging & Consumables", 0, "roll", 1),
    ("Receipt Paper Rolls", "Packaging & Consumables", 0, "roll", 1),
    ("Trays", "Packaging & Consumables", 0, "bags", 2),
    ("1-cup Plastic Bags", "Packaging & Consumables", 0, "bags", 2),
    ("2-cup Plastic Bags", "Packaging & Consumables", 0, "bags", 2),
    ("4-cup Plastic Bags", "Packaging & Consumables", 0, "bags", 2),
    ("Napkins", "Packaging & Consumables", 0, "stack", 2),
    ("Paper Towel", "Packaging & Consumables", 0, "rolls", 2),
    ("Fruit Picks", "Packaging & Consumables", 0, "bags", 2),
]

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.executemany(
    "INSERT INTO inventory (name, category, quantity, unit, min_level) VALUES (?, ?, ?, ?, ?)",
    items
)

conn.commit()
conn.close()

print("Inventory seeded successfully.")
