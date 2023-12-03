from ..database import DBcall
from .closestAirports import closestAirports
from .saveGame import saveGame
from random import randint
from geopy import distance

def game(currentUser):
    initialAirportIndex = randint(1, 70942)
    randomMoney         = [0, 100, 200, -100, -200]
    money               = 2000
    totalDstnc          = 0
    airportCount        = 0

    currentAirport = initialAirport = DBcall("SELECT name, latitude_deg, longitude_deg FROM airport;")[0][initialAirportIndex]

    while money > 0:
        print("You are at:", currentAirport[0])
        print("Money left: ", int(money))
        print(f"Distance traveled so far: {totalDstnc:.2f}km")

        closestAirports(currentAirport)
        airportCount += 1

        prevAirport        = (currentAirport[1], currentAirport[2])
        currentAirportName = input("\nCopy and paste the airport you want to go to >> ")
        currentAirport     = DBcall(f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE name = '{currentAirportName}';")[0][0]

        dstnc = distance.distance(prevAirport, (currentAirport[1], currentAirport[2])).km
        moneyChange = randomMoney[randint(0, 4)]

        money = money - (dstnc * 50) + moneyChange
        totalDstnc += dstnc

        if(money < 0):
            break


        if moneyChange > 0:
            print("\nMoney gained: ", moneyChange)

        elif moneyChange < 0:
            print("\nMoney lost: ", moneyChange)

        else:
            print("\nNo loss and no Gain!")


    print("\nGAMEOVER (Unfortunately you ran out of money)\n"
          "Your game statistics:")

    print(f"Distance traveled: {totalDstnc:.2f} kilometers,\n"
          f"Amount of Airports visited: {airportCount}")

    updated = saveGame(totalDstnc, currentUser, airportCount, initialAirport[0])

    if updated:
        return True
    else:
        return False
