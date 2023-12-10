import bcrypt  # Import external package

def checkPassword(attempt, real):
    hashedPassword = attempt.encode('utf-8')
    # Encode given password to the same format as the real one and compare them
    return bcrypt.checkpw(hashedPassword, real[2:-1].encode('utf-8'))


def hashPassword(password):
    salt = bcrypt.gensalt()  # Generate a hash salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Generate and return a hashed password
    return hashed
