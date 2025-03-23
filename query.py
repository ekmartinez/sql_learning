import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# SQL query to join customers and orders
query = """
SELECT 
    customers.CustomerID,
    customers.Name,
    customers.Email,
    orders.OrderID,
    orders.OrderDate,
    orders.Amount
FROM 
    orders
JOIN 
    customers
ON
    orders.CustomerID = customers.CustomerID
""" 

# Execute the query
cursor.execute(query)

# Fetch all results
order_ids = cursor.fetchall()

# Close the connection
conn.close()

# Print the results (optional)
for x in order_ids:
    print(x)

# Write results to a file
with open('data.txt', 'w') as data:
    for line in order_ids:
        data.write(', '.join(map(str, line)) + '\n')  # Convert tuple to string and write to file

