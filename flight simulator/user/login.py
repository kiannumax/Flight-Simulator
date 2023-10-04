def validation():
    username = input('enter username')
    password = input('enter password')
    querry='select * from credentials'
    cred=(username,password)
    cursor.execute(querry)
    data=cursor.fetchall()
    for i in data:
        if i==cred:
            return True
    else:
        return False
