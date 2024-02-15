#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Protected against SQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # get user input arguments
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    try:
        # connect to the MySQL database
        connection = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database_name
        )

        # create a cursor object to execute queries
        cursor = connection.cursor()

        # execute SQL query
        query = "SELECT c.name FROM cities c JOIN states s ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id ASC"
        cursor.execute(query, (state_name,))

        # get response data
        rows = cursor.fetchall()

        # print the retrieved records
        rows = [row[0] for row in rows]  # convert to list of strings
        print(", ".join(rows))

    except MySQLdb.Error as e:
        print("Error retrieving data!", e)

    finally:
        # close the cursor and database connection
        cursor.close()
        connection.close()
