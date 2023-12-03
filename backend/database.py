import mysql.connector as db

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

        cursor.execute(query)

        data = cursor.fetchall()
        return (data, cursor.rowcount)

    except Exception as err:
        print(f"Sorry, but our program encountered an Error! "
              f"Contact our developers to quickly fix this issue!\n"
              f"Error Message:\n{str(err)}")

