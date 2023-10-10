import mysql.connector as mysql
import random
from geopy import distance
con=mysql.connect(host='localhost', user='root',password='password',database='flight_game')
cursor=con.cursor()
start=2000
score=0
#Good Samaritan Hospital Heliport
l=[0,100,200,-100,-200]
a = random.randint(1, 70942)
querry = 'select name from airport;'
cursor.execute(querry)
b = cursor.fetchall()
current_airport = b[a][0]
while start>0:

    print('you are at:', current_airport)
    querry1 = 'select name,latitude_deg,longitude_deg from airport;'
    cursor.execute(querry1)
    a = cursor.fetchall()
    querry2 = f'select latitude_deg,longitude_deg from airport where name="{current_airport}"'
    cursor.execute(querry2)
    data = cursor.fetchone()
    for i in a:
        loc1 = data
        loc2 = (i[1], i[2])
        distanc=distance.distance(loc1, loc2).miles
        if distanc<15:
            print(i[0])
    current_airport = input('copy and paste the airport you want to go to')
    querry2 = f'select latitude_deg,longitude_deg from airport where name="{current_airport}"'
    cursor.execute(querry2)
    data1 = cursor.fetchone()
    loc1 = data


    loc2=data1
    distanc = distance.distance(loc1, loc2).miles
    x=random.randint(0,4)
    money=l[x]
    if money>0:
        print('money gained=',money)
    elif money<0:
        print('money lost=',money)
    else:
        print('no loss no gain')

    start=start-(distanc*100)+money
    if start<0:
        print('ran out of money')
    else:
        print('current wallet',int(start))


    score=score+distanc
    print(f'distance traveled: {score:.2f}')

