import mysql.connector as mysql
import random
from geopy import distance

con = mysql.connect(host='localhost', user='root', password='password', database='flight_game')
cursor = con.cursor()
current_airport = None
startingairport = None
print('<game description>')
# create table credentials(name varchar(20),password varchar(20));
start = 1000
distanc = 0
l = [100, 50, 0, -50, -100]


def starting_airport():
    global current_airport
    a = random.randint(1, 70942)
    querry = 'select name from airport;'
    cursor.execute(querry)
    b = cursor.fetchall()
    current_airport = b[a][0]
    return current_airport


def airportscloseby():
    global current_airport, start, distanc, startingairport
    querry1 = 'select name,latitude_deg,longitude_deg from airport;'
    cursor.execute(querry1)
    a = cursor.fetchall()
    startingairport = starting_airport()
    querry2 = f'select latitude_deg,longitude_deg from airport where name="{startingairport}"'
    cursor.execute(querry2)
    data = cursor.fetchone()
    for i in a:
        loc1 = data
        loc2 = (i[1], i[2])
        distanc = distance.distance(loc1, loc2).miles
        if distanc < 10:
            print(i[0])
    current_airport = input('copy and paste the airport you want to go to')
    start = start - (distance1() * 50)
    x = money_add()
    print(f'money status from new airport:{x}')
    start = start + x
    print(f'money remaining={int(start)}')


def distance1():
    global current_airport
    querry2 = f'select latitude_deg,longitude_deg from airport where name="{startingairport}"'
    cursor.execute(querry2)
    loc1 = cursor.fetchone()
    querry = f'select latitude_deg,longitude_deg from airport where name="{current_airport}"'
    cursor.execute(querry)
    loc2 = cursor.fetchone()
    x = distance.distance(loc1, loc2).miles
    return x


def money_add():
    x = random.randint(0, 4)
    return l[x]