# Object Relational Mapping — Alx Higher Level Programming
0x0F. Python - Object-relational mapping

## Overview
This document provides a brief overview of different methods to connect to databases in Python, focusing on two popular approaches: ``MySQLdb`` and ``ORM`` (SQLAlchemy).

## MySQLdb Module
MySQLdb is a Python module that provides a way to interact with MySQL databases from Python code. It allows you to perform various operations such as connecting to a MySQL database, executing SQL queries, fetching data, and managing database transactions.
#### Examples:
```python
import MySQLdb

# Connect to the MySQL database
connection = MySQLdb.connect(host="your_host",
                             user="your_username",
                             passwd="your_password",
                             db="your_database")

# Create a cursor object to execute queries
cursor = connection.cursor()

try:
    # Execute the query to select all records from the states table
    cursor.execute("SELECT * FROM states")
    
    # Fetch all the rows from the result set
    rows = cursor.fetchall()
    
    # Print the retrieved records
    for row in rows:
        print(row)

except MySQLdb.Error as e:
    print("Error retrieving data from MySQL table:", e)

finally:
    # Close the cursor and database connection
    cursor.close()
    connection.close()
```

## What ORM means?
ORM stands for **Object-Relational Mapping**. It's a programming technique that allows you to convert data between incompatible systems by mapping objects in your code to tables in a relational database. With ORM, you can interact with databases using objects and methods, rather than writing raw SQL queries.

## SQLAlchemy ORM
``SQLAlchemy`` is a powerful and popular Python ORM library that provides a high-level interface for interacting with relational databases. It supports various database systems, including MySQL, SQLite, PostgreSQL and others. SQLAlchemy offers both ORM (Object-Relational Mapping) and Core (SQL Expression Language) components, giving developers flexibility in how they interact with databases.

### Usage:
The following example demonstrates how to define database tables using SQLAlchemy's ORM, insert data into the database, query data from the database, and establish relationships between tables. With SQLAlchemy ORM, you can work with databases in a more Pythonic and object-oriented way.
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create an engine to connect to the MySQL database
engine = create_engine('mysql+mysqldb://username:password@host/database_name', echo=True)

# Define a base class for declarative class definitions
Base = declarative_base()

# Define a User class representing a table in the database
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    addresses = relationship("Address", back_populates="user")
    
# Define an Address class representing another table in the database
class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="addresses")

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Inserting data into the database
new_user = User(name='el_ouardy')
session.add(new_user)

new_address = Address(email='el_ouardy@example.com', user=new_user)
session.add(new_address)

# commit pending changes
session.commit()

# Example: Querying data from the database
user = session.query(User).filter_by(name='el_ouardy').first()
print(user.name)
for address in user.addresses:
    print(address.email)

# Close the session
session.close()
```

## MySQLdb Module VS ORM
Both MySQLdb and ORM are popular choices for connecting to databases in Python. MySQLdb is suitable for direct SQL queries and low-level database operations, while ORM offers a higher-level abstraction for working with databases in an object-oriented manner. The choice between the two depends on the specific requirements and preferences of the project.
#### MySQLdb Module advantages:
- Direct interaction with the MySQL database.
- Efficient for executing raw SQL queries.
#### Object-relational mapping advantages:
- Object-oriented approach to database interaction.
- Provides abstraction over SQL queries and database operations.
- Offers features like automatic schema generation and data validation.

## Let's connect
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
