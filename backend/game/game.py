from ..database import DBcall
from random import randint
from geopy import distance


def getClosestAirports(latitude, longitude, pastAirports):
    allAirports = DBcall("SELECT name, ident, latitude_deg, longitude_deg, type, iso_country FROM airport;")[0]
    results = {'airports': []}  # Initialize a list which is being returned
    i = 0
    for airport in allAirports:  # Traverse through all airports
        if i > 10:  # If list is 10 airports long, stop the loop
            break

        if (airport[0] in pastAirports) or (airport[4] == 'closed') or (airport[4] == 'balloonport') or (airport[4] == 'heliport'):
            continue  # Continue the loop if airport was already used by the player, or its type is closed/balloonport/heliport

        dstnc = distance.distance((airport[2], airport[3]), (latitude, longitude)).km
        # Calculate distance to the airport from current point and if it's less than 200km, append the airport to the list
        if dstnc < 200:
            country = DBcall(f"SELECT name FROM country WHERE iso_country = '{airport[5]}';")[0][0][0]
            # Save airports information in JSON format
            airportJson = {'name': airport[0], 'ICAO': airport[1], 'latitude': airport[2], 'longitude': airport[3],
            'country': country, 'dstnc': dstnc, 'type': airport[4]}

            i += 1  # Append the airport and update the counter
            results['airports'].append(airportJson)

    return results


def getInitialAirport():
    initialAirportIndex = randint(0, 70941)  # Random airport index
    airport = DBcall("SELECT name, ident, latitude_deg, longitude_deg, type, iso_country FROM airport;")[0][initialAirportIndex]
    # Select random airport from database
    country = DBcall(f"SELECT name FROM country WHERE iso_country = '{airport[5]}';")[0][0][0]
    # Return its information in JSON format
    return {'name': airport[0], 'ICAO': airport[1], 'latitude': airport[2], 'longitude': airport[3], 'country': country, 'type': airport[4]}
