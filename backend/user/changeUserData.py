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
    # Get IP and username from database
    result = DBcall(f"""SELECT COUNT(1), IP FROM users WHERE username = '{username}';""")[0][0]
    finalData = {'match': None, 'message': None}  # Initialize return JSON format

    if result[0] == 1:  # If username exists
        if IP == result[1]:  # If IPs match return JSON with match True
            finalData['match'] = True

        else:  # If IPs do not match return match-False and a message
            finalData['match'], finalData['message'] = False, "IPs do not match with that username's account. Try again later!"

    else:  # If given username doesn't exist return match-False and a message
        finalData['match'], finalData['message'] = False, "There is no assigned account with that username. Try signing up!"

    return finalData


def resetPassword(username, newPassword):
    hashedPassword = hashPassword(newPassword)  # Hash the new password
    insertQuery = f"""UPDATE users SET password = "{hashedPassword}" where username = '{username}'"""
    # Implement the update of password

    if DBcall(insertQuery)[1] == 1:  # If 1 row was changed
        return {'message': "Password Reset was successful. Try logging in!"}  # Return message of success

    else:  # Otherwise return a message of failure
        return {'message': "Unfortunately Password Reset was unsuccessful, try again later."}
