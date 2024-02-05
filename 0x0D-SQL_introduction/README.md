# ALX — SQL Introduction
0x0D. SQL - Introduction

## What are Databases?
Databases are like organized collections of information that you can easily access, manage, and update. Think of them as digital filing cabinets where you store all your data neatly arranged in tables.

## Famous Types of Databases
- **Relational Databases**: These are the most common type. They organize data into tables with rows and columns, and they use structured query language (``SQL``) for managing and querying data.

- **NoSQL Databases**: These databases handle unstructured or semi-structured data. They're great for handling large volumes of data quickly and are often used in big data and real-time web applications.

- **Document Databases**: They store data in a document format, like JSON or XML. This makes it easy to handle data with complex structures.

- **Graph Databases**: Perfect for relationships between data. They store data in nodes and edges, making it easy to represent and query complex relationships.

## What is SQL?
**SQL** stands for `Structured Query Language`. It's the language used to communicate with relational databases. With SQL, you can perform various operations like querying data, updating records, inserting new data, and deleting unwanted data from the database.

SQL is super powerful because it allows you to retrieve specific information from a database without needing to know how the data is stored internally. You just tell it what you want, and SQL figures out the best way to get it for you!

Here are some simple examples of SQL queries:
```sql
-- Create User Table: Define the structure of the 'users' table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255)
);
-- Selecting Data: Retrieve all columns from the 'users' table
SELECT * FROM users;

-- Filtering Data: Retrieve users who are older than 18
SELECT * FROM users WHERE age > 18;

-- Inserting Data: Add a new user into the 'users' table
INSERT INTO users (name, age, email) VALUES ('Wadi3 El Wardy', 25, 'wadi3@elwardy.io');

-- Updating Data: Update the age of the user named 'Wadi3 El Wardy'
UPDATE users SET age = 30 WHERE name = 'Wadi3 El Wardy';

-- Deleting Data: Remove the user named 'Wadi3 El Wardy' from the 'users' table
DELETE FROM users WHERE name = 'Wadi3 El Wardy';

-- Joining Tables: Retrieve user names and their corresponding orders
SELECT users.name, orders.product FROM users
JOIN orders ON users.id = orders.user_id;

-- Aggregating Data: Count the total number of users in the 'users' table
SELECT COUNT(*) FROM users;
```

### Subqueries
Subqueries, also known as nested queries or inner queries, are SQL queries that are embedded within another query. They are used to retrieve data from one or more tables based on the results of a separate query.

Subqueries can be used in various parts of a SQL statement, including the **SELECT**, **INSERT**, **UPDATE**, and **DELETE** statements. They are commonly used to filter results, perform calculations, or retrieve data from related tables.
```sql
SELECT name, age
FROM users
WHERE age > (SELECT AVG(age) FROM users);
```

## Functions (MySQL functions)
Using MySQL functions is quite straightforward. You can use functions in various parts of your SQL queries to perform calculations, manipulate data, or format output. Here's a basic overview of how to use MySQL functions:

``Function Syntax``: Most MySQL functions follow a standard syntax. They start with the function name, followed by parentheses ( ), which may contain one or more arguments. For example:
```sql
FUNCTION_NAME(argument1, argument2, ...);
```
``Scalar Functions``: These functions operate on a single value and return a single value. They can be used in ***SELECT*** statements, ***WHERE*** clauses, ***ORDER BY*** clauses, etc. Examples include ***ROUND()***, ***UPPER()***, ***LOWER()***, ***CONCAT()***, ***LEN()***, etc.
```sql
SELECT UPPER(name) AS uppercase_name FROM users;
```
``Aggregate Functions``: These functions operate on sets of values and return a single value summarizing the set. They are commonly used with the ***GROUP BY*** clause. Examples include ***SUM()***, ***AVG()***, ***COUNT()***, ***MIN()***, ***MAX()***, etc.
```sql
SELECT COUNT(*) AS total_users FROM users;
```
``Date and Time Functions``: MySQL provides various functions for working with date and time values. Examples include ***NOW()***, ***DATE()***, ***YEAR()***, ***MONTH()***, ***DAY()***, ***HOUR()***, ***MINUTE()***, ***SECOND()***, ***DATE_FORMAT()***, etc.
```sql
SELECT DATE_FORMAT(date_column, '%Y-%m-%d') AS formatted_date FROM table_name;
```
``Mathematical Functions``: MySQL supports a range of mathematical functions for performing arithmetic operations. Examples include ***ABS()***, ***ROUND()***, ***CEILING()***, ***FLOOR()***, ***POWER()***, ***SQRT()***, etc.
```sql
SELECT ROUND(price, 2) AS rounded_price FROM products;
```
``Conditional Functions``: MySQL provides conditional functions like ***IF()***, ***CASE***, ***COALESCE()***, etc., which allow you to perform conditional logic within SQL queries.
```sql
SELECT IF(age > 18, 'Adult', 'Minor') AS age_group FROM users;
```
``User-Defined Functions (UDFs)``: MySQL also supports the creation of user-defined functions using the ***CREATE FUNCTION*** statement, allowing you to extend the functionality of MySQL with custom functions.
```sql
CREATE FUNCTION custom_function_name (parameters)
RETURNS return_type
BEGIN
    -- Function body
END;
```

## Author:
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
