from ..database import DBcall
from .hash import hashPassword
import datetime

def signup(username, password, IP):
    query = f"SELECT COUNT(1) FROM users WHERE username = '{username}';"

    if DBcall(query)[0][0][0] == 0:
        hashedPaswd = hashPassword(password)
        currentDate = datetime.date.today()

        insertQuery = (f"INSERT INTO users (username, password, date_registered, IP)"
                       f"""VALUES ('{username}', "{hashedPaswd}", '{currentDate}', '{IP}');""")

        if DBcall(insertQuery)[1] == 1:
            token = DBcall(f"SELECT id FROM users WHERE username = '{username}';")[0]

            return {'success': True, 'token': token, 'message': None}

        else:
            return {'success': False, 'token': None, 'message': "Unfortunately, signup failed, try again later!"}

    else:
        return {'success': False, 'token': None, 'message': "Sorry but this account already exists, try logging in!"}
