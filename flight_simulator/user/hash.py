import bcrypt

def checkPassword(attempt, real):
    hashedPaswd = attempt.encode('utf-8')

    return bcrypt.checkpw(hashedPaswd, real[2:-1].encode('utf-8'))


def hashPassword(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed
