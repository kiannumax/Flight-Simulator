from ..database import DBcall
import datetime

def saveGame(distance, user, airportCount, initialAirport):
    currentDate = datetime.date.today()

    insertQuery = (f"INSERT INTO games (distance, date_played, initial_airport, airports_visited, user_id)"
                   f"""VALUES ('{distance}', '{currentDate}', '{initialAirport}', '{airportCount}', '{user}');""")

    if DBcall(insertQuery)[1] == 1:
        return True

    else:
        return False
