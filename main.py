import pyodbc

print(pyodbc.drivers())

server = 'tcp:fsgame.database.windows.net, 1433'
database = 'FSgame'
username = 'FSgameUser'
password = '{aiRbuS320!}'
driver = '{ODBC Driver 18 for SQL Server}'

try:
    cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

    cursor = cnxn.cursor()

   # cursor.execute("CREATE TABLE Persons (ID int NOT NULL PRIMARY KEY IDENTITY, FirstName varchar(255), LastName varchar(255));")
    cursor.execute("SELECT * FROM Persons;")
    test = cursor.fetchall()[0]
    print(test)
except Exception as err:
    print('Cannot connect to SQL server' + str(err))
