from ..database import DBcall
from random import randint
from geopy import distance


def getClosestAirports(latitude, longitude, pastAirports):
    allAirports = DBcall("SELECT name, ident, latitude_deg, longitude_deg, home_link, wikipedia_link, type FROM airport;")[0]
    results = {'airports': []}
    i = 0
    for airport in allAirports:
        if i > 10:
            break

        if (airport[0] in pastAirports) or (airport[6] == 'closed') or (airport[6] == 'balloonport') or (airport[6] == 'heliport'):
            continue

        dstnc = distance.distance((airport[2], airport[3]), (latitude, longitude)).km

        if dstnc < 200:
            airportJson = {'name': airport[0], 'ICAO': airport[1], 'latitude': airport[2], 'longitude': airport[3],
             'home_link': airport[4], 'wiki_link': airport[5], 'dstnc': dstnc, 'type': airport[6]}

            i += 1
            results['airports'].append(airportJson)

    return results


def getInitialAirport():
    initialAirportIndex = randint(0, 70941)
    airport = DBcall("SELECT name, ident, latitude_deg, longitude_deg, home_link, wikipedia_link, type FROM airport;")[0][initialAirportIndex]

    return {'name': airport[0], 'ICAO': airport[1], 'latitude': airport[2], 'longitude': airport[3], 'home_link': airport[4], 'wiki_link': airport[5], 'type': airport[6]}
