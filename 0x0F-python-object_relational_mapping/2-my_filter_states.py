#!/usr/bin/python3
"""
This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
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
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            state_name
        )
        cursor.execute(query)

        # get response data
        rows = cursor.fetchall()

        # print the retrieved records
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error retrieving data!", e)

    finally:
        # close the cursor and database connection
        cursor.close()
        connection.close()
