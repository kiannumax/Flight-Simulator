def starting_airport():
    global current_airport
    a=random.randint(1,70942)
    querry='select name from airport;'
    cursor.execute(querry)
    b=cursor.fetchall()
    current_airport=b[a][0]
    return current_airport
def airportscloseby():
    global current_airport
    querry1='select name,latitude_deg,longitude_deg from airport;'
    cursor.execute(querry1)
    a=cursor.fetchall()
    querry2=f'select latitude_deg,longitude_deg from airport where name="{starting_airport()}"'
    cursor.execute(querry2)
    data=cursor.fetchone()
    for i in a:
        loc1 = data
        loc2 = (i[1], i[2])
        distanc=distance.distance(loc1, loc2).miles
        if distanc<10:
            print(i[0])
    current_airport=input('copy and paste the airport you want to go to')
