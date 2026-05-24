"""psycopg2-sample.py

Sample code demonstrating how to use the psycopg2 Python library to 
connect to a database and execute a query.
"""

import psycopg2 as ps
from psycopg2 import sql

from Data import datasource as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_animal(connection, animal: str) -> list:
    """Retrieves all dates (and all the weather information associated with those dates) where the high temperature was above a specified threshold.

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (float) - the minimum high temperature

    Returns:
        list - a list of all dates where the high temperature is greater or equal to temp, or None if the query fails.
    """
    try:
        #cursor_1 = connection.cursor()
        
        #query = "SELECT observer FROM birds WHERE common_name = %s;"

        for item in ["birds","mammals","reptiles","insects","insects","amphibians"]:
            user_list = []
            birds = "birds"
            cursor = connection.cursor()
            cursor.execute(sql.SQL("SELECT observer,COUNT(*) FROM {table} WHERE common_name = (%s) GROUP BY observer ORDER BY COUNT(*) DESC").format(table = sql.Identifier(item)), (animal,))
            user_list = cursor.fetchall()
    
            if user_list != []:                      
                return user_list[:10]



    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None


def main():
    connection = connect()
    results = get_animal(connection, "American Toad")
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    connection.close()

main()