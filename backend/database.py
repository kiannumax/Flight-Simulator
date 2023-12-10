import mysql.connector as db
# Connect to a local flight_simulator database located on the computer
connection = db.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_simulator',
    user = 'root',
    password = 'mkiannu2005#!',
    autocommit = True
)


def DBcall(query):
    try:
        cursor = connection.cursor()
        # Connect and execute a given query
        cursor.execute(query)

        data = cursor.fetchall()  # Return fetched data and row count
        return data, cursor.rowcount

    except Exception as err:  # Print an exception, more useful for development state
        print(f"Sorry, but our program encountered an Error! "
              f"Contact our developers to quickly fix this issue!\n"
              f"Error Message:\n{str(err)}")
