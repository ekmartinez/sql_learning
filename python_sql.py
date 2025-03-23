import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

query = """
SELECT
    customers.CustomerID,
    customers.Name,
    Customers.Email,
    orders.OrderId,
    orders.OrderDate,
    orders.Amount
FROM 
    customers
LEFT JOIN
    orders
ON
    customers.CustomerID = orders.CustomerID;
    """

cursor.execute(query)
results = cursor.fetchall()

with open('orders_and customers.txt', 'w') as file:
    file.write("CustomerID|Name|Email|OrderID|OrderDate|Amount\n")
    for row in results:
        file.write("|".join(map(str, row)) + "\n")

cursor.close()
connection.close()

print("Results have been written to orders_and_customers.txt")
