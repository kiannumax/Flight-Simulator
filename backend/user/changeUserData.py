from ..database import DBcall
from .hash import hashPassword

def changeUsername(token, newUsername):
    insertQuery = f"""UPDATE users SET username = "{newUsername}" where id = '{token}'"""

    return {'success': DBcall(insertQuery)[1] == 1}


def changePassword(token, newPassword):
    hashedPaswd = hashPassword(newPassword)
    insertQuery = f"""UPDATE users SET password = "{hashedPaswd}" where id = '{token}'"""

    return {'success': DBcall(insertQuery)[1] == 1}


def checkIP(username, IP):
    result = DBcall(f"""SELECT COUNT(1), IP FROM users WHERE username = '{username}';""")[0][0]
    finalData = {'match': None, 'message': None}

    if result[0] == 1:
        if IP == result[1]:
            finalData['match'] = True

        else:
            finalData['match'], finalData['message'] = False, "IP's do not match with that username's account. Try again later!"

    else:
        finalData['match'], finalData['message'] = False, "There is no assigned account with that username. Try signing up!"

    return finalData


def resetPassword(username, newPassword):
    hashedPaswd = hashPassword(newPassword)
    insertQuery = f"""UPDATE users SET password = "{hashedPaswd}" where username = '{username}'"""

    return {'success': DBcall(insertQuery)[1] == 1}
