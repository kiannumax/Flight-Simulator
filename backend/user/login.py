from ..database import DBcall
from .hash import checkPassword

def login(username, password):
    query = f"""SELECT COUNT(1) FROM users WHERE username = '{username}';"""
    result = {'result': False, 'token': None}

    if DBcall(query)[0][0][0] == 1:
        data = DBcall(f"""SELECT password, id FROM users WHERE username = '{username}';""")[0][0]

        if checkPassword(password, data[0]):
            result['result'] = True
            result['token'] = data[1]

    return result
