def new_user():
    username = input('enter username')

    querry = 'select name from credentials;'
    cursor.execute(querry)
    data = cursor.fetchall()

    for i in data:
        if i[0] == username:
            return False
    else:
        password = input('enter password')
        querry=f'insert into credentials values("{username}","{password}");'
        cursor.execute(querry)
        con.commit()
        return True
