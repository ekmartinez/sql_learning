import sqlite3
import random

# Connect to your SQLite database
conn = sqlite3.connect('test.db')  # Replace with your database file
cursor = conn.cursor()

# Fetch all Order IDs
cursor.execute("SELECT OrderID FROM orders;")
order_ids = cursor.fetchall()

# Generate random amounts and update the database
for order_id in order_ids:
    random_amount = round(random.uniform(100, 2000), 0)  # Generate a random float and round it
    cursor.execute("UPDATE orders SET Amount = ? WHERE OrderID = ?", (random_amount, order_id[0]))

# Commit the changes and close the connection
conn.commit()
conn.close()

