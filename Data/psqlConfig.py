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
    """ This gives the sorted top users in a specific animal sighting.

    Args:
        connection (psycopg2) - This connects use to the datebase.
        animal (str) - This gives gives us the common_name of the animal that people are looking for.

    Returns:
        user_list (list) - This is the list of all of the 
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



def get_top_species(conenction, animal):
        printout_number = 3
        lat_upper = 44.0115
        lat_lower = 47.3043200834
        lon_upper = -92.64152795
        long_lower = -90.8924674988


        total_db_list = []
        for item in ["birds","mammals","reptiles","insects","insects","amphibians"]:
            user_list = []
            cursor = connection.cursor()
            cursor.execute(sql.SQL("SELECT common_name,COUNT(*) FROM {table} WHERE ((lat BETWEEN %s AND %s)) and (lon BETWEEN %s AND %s)) GROUP BY common_name ORDER BY COUNT(*) DESC").format(table = sql.Identifier(item)), (lat_upper,lat_lower,lon_upper,long_lower,))
            user_list = cursor.fetchall()

    #SELECT common_name,COUNT(*) FROM birds WHERE latitude BETWEEN 45.01 AND 49 AND WHERE longitude BETWEEN -90 AND -92 GROUP BY common_name ORDER BY COUNT(*) DESC;
            if user_list != []:                      
                total_db_list.append(user_list[:printout_number])
        return total_db_list

def main():
    connection = connect()
    results = get_animal(connection, "American Toad")
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    connection.close()

main()