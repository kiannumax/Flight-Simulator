from ..database import DBcall
from .hash import hashPassword
import datetime

def signup(username, password, IP):
    query = f"SELECT COUNT(1) FROM users WHERE username = '{username}';"  # Check if username already exists

    if DBcall(query)[0][0][0] == 0:  # If there is no account with same username
        hashedPassword = hashPassword(password)  # Hash the password
        currentDate    = datetime.date.today()  # Get today's date

        # Insert new row to users table with all the user data
        insertQuery = (f"INSERT INTO users (username, password, date_registered, IP)"
                       f"""VALUES ('{username}', "{hashedPassword}", '{currentDate}', '{IP}');""")

        if DBcall(insertQuery)[1] == 1:  # If Insert was successful
            token = DBcall(f"SELECT id FROM users WHERE username = '{username}';")[0]
            # return True as 'success' and user's token
            return {'success': True, 'token': token, 'message': None}

        else:  # If Insert to database failed, return Fail as 'success' and a message
            return {'success': False, 'token': None, 'message': "Unfortunately Sign up failed. Try again later!"}

    else:  # If username already exists, return Fail as 'success' and a message
        return {'success': False, 'token': None, 'message': "Account with that username already exists. Try Logging in!"}
