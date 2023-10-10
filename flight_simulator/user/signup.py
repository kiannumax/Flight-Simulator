from ..database import DBcall
from .hash import hashPassword
import datetime
import socket

def check(username, password):
    query = f"SELECT COUNT(1) FROM users WHERE username = '{username}';"

    if DBcall(query)[0][0][0] == 0:
        hashedPaswd = hashPassword(password)
        currentDate = datetime.date.today()

        hostname = socket.gethostname()
        hostIP   = socket.gethostbyname(hostname)

        insertQuery = (f"INSERT INTO users (username, password, date_registered, IP)"
                       f"""VALUES ('{username}', "{hashedPaswd}", '{currentDate}', '{hostIP}');""")

        if DBcall(insertQuery)[1] == 1:
            return 'success'

        else:
            return 'fail'

    else:
        return 'exists'


def signup():
    print("To complete the signup process you will be asked to enter a username and a password\n")

    username = None
    password = None
    essentialsDone = False

    while not essentialsDone:
        username = input("Please enter a username (max 15 characters) >> ")

        if len(username) > 15:
            print("Too long!\n")
            continue

        password = input("Please enter a password (be sure to remember it!) >> ")
        essentialsDone = True

    result = check(username, password)

    if result == 'exists':
        return 'exists'

    elif result == 'fail':
        return 'fail'

    else:
        return 'success'
