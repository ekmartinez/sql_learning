import sqlite3

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

# Insert dummy data into the Orders table (10 entries)
orders_data = [
    (1, '2023-01-15', 100.50, 1),  # Order for Alice
    (2, '2023-01-16', 200.75, 2),  # Order for Bob
    (3, '2023-01-17', 150.00, 1),  # Another order for Alice
    (4, '2023-01-18', 300.00, 3),  # Order for Charlie
    (5, '2023-01-19', 250.25, 4),  # Order for Diana
    (6, '2023-01-20', 400.00, 5),  # Order for Ethan
    (7, '2023-01-21', 350.50, 6),  # Order for Fiona
    (8, '2023-01-22', 450.75, 7),  # Order for George
    (9, '2023-01-23', 500.00, 8),  # Order for Hannah
    (10, '2023-01-24', 600.25, 9)   # Order for Ian
]

cursor.executemany('''
INSERT INTO Orders (OrderID, OrderDate, Amount, CustomerID) VALUES (?, ?, ?, ?);
''', orders_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Dummy data has been inserted into the database.")

