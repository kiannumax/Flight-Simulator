from sys import exit
import mysql.connector as database

connection = database.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_simulator',
    user = 'root',
    password = 'mkiannu2005#!',
    autocommit = True
)

#import pyodbc

#server   = 'tcp:fsgame.database.windows.net, 1433'
#database = 'FSgame'
#username = 'FSgameUser'
#password = 'aiRbuS320!'
#driver = '{ODBC Driver 18 for SQL Server}'

def DBcall(query):
    try:
        #cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        #cursor = cnxn.cursor()
        cursor = connection.cursor()

        cursor.execute(query)

        data = cursor.fetchall()
        return (data, cursor.rowcount)

    except Exception as err:
        print(f"Sorry, but our program encountered an Error! "
              f"Contact our developers to quickly fix this issue!\n"
              f"Error Message:\n{str(err)}")
        exit(0)
