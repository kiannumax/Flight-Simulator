from ..database import DBcall
from .hash import checkPassword
from .resetPassword import resetPaswrd

def check(username, password):
    query = f"""SELECT COUNT(1) FROM users WHERE username = '{username}';"""

    if DBcall(query)[0][0][0] == 1:
        actualPaswd = DBcall(f"""SELECT password FROM users WHERE username = '{username}'""")[0][0][0]

        if checkPassword(password, actualPaswd):
            return True

        else:
            return False
    else:
        return False


def login():
    username = input("Enter your username >> ")
    password = input("Enter your password >> ")

    result = check(username, password)

    if result:
        return True

    else:
        while True:
            option = input(("Invalid username or password. Go back or Reset Password? (b, r) >> ")).lower()

            if option == 'b':
                print('\n')
                return False

            elif option == 'r':
                result = resetPaswrd()

                if result:
                    return True

                else:
                    return False

