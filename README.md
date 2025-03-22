# SQL Notes


## SELECT Statement

The `SELECT` statement is used to query data from a database. The `SELECT` statement allows you to specify which columns you want to retrieve from a table.

Syntax:

```sql
SELECT column1, column2, ...
FROM table_name;
```

Example: To select all columns from the customers table:

```sql
SELECT * FROM customers;
```

## WHERE Clause

The `WHERE` clause is used to filter records that meet certain conditions. It allows you to specify criteria for selecting rows.

Syntax:

```sql
SELECT from column1, column2, ...
FROM table_name
WHERE condition;
```

Example: To select customers with a specific name:

```sql
SELECT * FROM customers WHERE Name = 'Alice Smith';
```

## Using LIKE with Wildcards

Syntax:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name LIKE 'D%'
```
In the above example, `LIKE` 'D%' will match any names that start with the letter 'D', followed by any sequence of characters.

## HAVING Clause

Syntax:

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition
```

Example: To find customers who have made more than one order:

```sql
SELECT CustomerID, COUNT(OrderID)
FROM orders
GROUP BY CustomerID
HAVING COUNT(OrderID) > 1;
```

## JOINS
Joins are used to combine rows from two or more tables based on a related column between them. The most common types of joins are INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN.

Syntax:

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.common_column = table2.common_column;
```

Example: To get a list of customers along with their orders:

```sql
SELECT customers.Name, orders.OrderID, orders.Amount
FROM customers
INNER JOIN orders ON customers.CustomerID = orders.CustomersID; 
```

Summary:

1. SELECT Statement: Used to retrieve data from a table.
2. FROM Clause: Specifies the table from which to retrieve data.
3. WHERE Clause: Filters records based on specified conditions.
4. HAVING Clause: Filters records after aggregation, typically used with GROUP BY.
5. JOINS: Combines rows from two or more tables based on related columns.

