from ..database import DBcall
from .hash import hashPassword
import socket

def changeUsername(token, newUsername):
    insertQuery = f"""UPDATE users SET username = "{newUsername}" where id = '{token}'"""

    return {'success': DBcall(insertQuery)[1] == 1}


def changePassword(token, newPassword):
    hashedPaswd = hashPassword(newPassword)
    insertQuery = f"""UPDATE users SET password = "{hashedPaswd}" where id = '{token}'"""

    return {'success': DBcall(insertQuery)[1] == 1}


def resetPassword():
    print("Program will ask you to type your username, and if it exists: "
          "it will compare your IP adress with the assigned one\n")

    username = input("Please enter your username >> ")

    result = DBcall(f"""SELECT COUNT(1), IP FROM users WHERE username = '{username}';""")[0][0]

    if result[0] == 1:
        assignedIP = result[1]

        hostname = socket.gethostname()
        hostIP = socket.gethostbyname(hostname)

        if assignedIP == hostIP:
            password = input("IP's match! Type a new password for the account >> ")
            hashedPaswd = hashPassword(password)

            insertQuery = f"""UPDATE users SET password = "{hashedPaswd}" where username = '{username}'"""

            if DBcall(insertQuery)[1] == 1:
                print("Password Reset successfull! You will be logged in. ")
                return (True, DBcall(f"SELECT id FROM users WHERE username = '{username}';")[0][0][0])

            else:
                print("Unfortunately password reset failed. Try again later!\n")
                return (False, None)

        else:
            print("IP's do not match with that username's account. Try again later!\n")
            return (False, None)

    else:
        print("There is no assigned account with that username. Try signing up!\n")
        return (False, None)
