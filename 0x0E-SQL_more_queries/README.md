# ALX — SQL More queries
0x0E. SQL - More queries

## Overview
This will cover various aspects including user management, permissions, constraints, query techniques, and join operations.

## Creating a New User and Granting Permissions in MySQL
To create a new user in MySQL and grant permissions, you can use the **CREATE USER** and **GRANT** statements. 
Here's a basic example:

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
```
This code creates a new user named *'newuser'* with the password *'password'* and grants all privileges on all databases and tables.

## Using MySQL GRANT Statement To Grant Privileges To a User
The **GRANT** statement in MySQL is used to grant specific privileges to users.
Here's a syntax example:
```sql
GRANT privilege_type ON database_name.table_name TO 'username'@'hostname';
```
For instance, to grant **SELECT** and **INSERT** privileges on a specific table to a user:
```sql
GRANT SELECT, INSERT ON database_name.table_name TO 'username'@'hostname';
```

## MySQL Constraints
MySQL constraints are rules applied to columns to enforce data integrity. Common constraints include **PRIMARY KEY**, **FOREIGN KEY**, **NOT NULL**, **UNIQUE**, and **CHECK**.

## SQL Technique: Subqueries
Subqueries in SQL are queries nested within another query. They can be used in **SELECT**, **INSERT**, **UPDATE**, or **DELETE** statements to perform operations based on the result of another query.

## Basic Query Operation: The JOIN
The **JOIN** operation is used to combine rows from two or more tables based on a related column between them. Common types of joins include **INNER JOIN**, **LEFT JOIN**, **RIGHT JOIN**, and **FULL JOIN**.

## Join Types
Join types determine how rows from one table are combined with rows from another table. Each join type (INNER, LEFT, RIGHT, FULL) has its own behavior regarding matching and non-matching rows.

## The Seven Types of SQL Joins
- **INNER JOIN**: Retrieves records that have matching values in both tables involved in the join. It returns rows when there is at least one match in both tables.

- **LEFT JOIN** (or LEFT OUTER JOIN): Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.

- **RIGHT JOIN** (or RIGHT OUTER JOIN): Opposite of a LEFT JOIN. It returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.

- **FULL JOIN** (or FULL OUTER JOIN): Returns all records when there is a match in either left or right table. If there is no match, the result is NULL in the columns from the table that lacks a match.

- **CROSS JOIN**: Produces a Cartesian product of the two tables involved in the join. It returns all possible combinations of rows from the tables.

- **SELF JOIN**: Joins a table with itself. It is used to compare rows within the same table.

- **NATURAL JOIN**: Joins two tables based on the columns with the same name and datatype. It implicitly performs an INNER JOIN on the common columns.

Each type of join serves a specific purpose and can be used to retrieve data based on different criteria and relationships between tables in a database.

## Let's connect
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
