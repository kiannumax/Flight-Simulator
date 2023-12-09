from ..database import DBcall
from .hash import checkPassword


def login(username, password):
    query  = f"""SELECT COUNT(1) FROM users WHERE username = '{username}';"""  # Checks if user exists
    result = {'result': False, 'token': None}  # Initial return JSON

    if DBcall(query)[0][0][0] == 1:  # If user exists
        data = DBcall(f"""SELECT password, id FROM users WHERE username = '{username}';""")[0][0]
        # Get user's id(token) and password

        if checkPassword(password, data[0]):  # Compare hashes of passwords
            result['result'] = True  # If passwords match, return true and user's token in JSON format
            result['token'] = data[1]

    return result
