import sqlite3
from datetime import datetime, timedelta

# Connect to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create the Customers table (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);
''')

# Create the Orders table (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT NOT NULL,
    Amount REAL NOT NULL,
    CustomerID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
''')

# Insert dummy data into the Customers table (10 entries)
customers_data = [
    (1, 'Alice Smith', 'alice@example.com'),
    (2, 'Bob Johnson', 'bob@example.com'),
    (3, 'Charlie Brown', 'charlie@example.com'),
    (4, 'Diana Prince', 'diana@example.com'),
    (5, 'Ethan Hunt', 'ethan@example.com'),
    (6, 'Fiona Gallagher', 'fiona@example.com'),
    (7, 'George Costanza', 'george@example.com'),
    (8, 'Hannah Baker', 'hannah@example.com'),
    (9, 'Ian Malcolm', 'ian@example.com'),
    (10, 'Julia Roberts', 'julia@example.com')
]

cursor.executemany('''
INSERT INTO Customers (CustomerID, Name, Email) VALUES (?, ?, ?);
''', customers_data)

# Insert dummy data into the Orders table (10 entries per customer)
orders_data = []
order_id = 1
base_date = datetime(2023, 1, 1)

for customer_id in range(1, 11):  # For each customer
    for i in range(5):  # Create 5 orders for each customer
        order_date = base_date + timedelta(days=i)
        amount = round(100 + (i * 10.25), 2)  # Varying amounts
        orders_data.append((order_id, order_date.strftime('%Y-%m-%d'), amount, customer_id))
        order_id += 1

cursor.executemany('''
INSERT INTO Orders (OrderID, OrderDate, Amount, CustomerID) VALUES (?, ?, ?, ?);
''', orders_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Dummy data has been inserted into the database.")

