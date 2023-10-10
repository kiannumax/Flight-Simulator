from ..database import DBcall
from geopy import distance

def closestAirports(currentAirport):
    allAirports = DBcall("SELECT name,latitude_deg,longitude_deg FROM airport;")[0]

    print('\nAirports closest to you:')
    for airport in allAirports:
        dstnc = distance.distance((airport[1], airport[2]), (currentAirport[1], currentAirport[2])).km

        if dstnc < 20:
            print(airport[0])

    print("Done")