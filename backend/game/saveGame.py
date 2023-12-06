from ..database import DBcall
import datetime

def saveGame(distance, token, airportCount, initialAirport):
    currentDate = datetime.date.today()

    insertQuery = (f"INSERT INTO games (distance, date_played, initial_airport, airports_visited, user_id)"
                   f"""VALUES ('{distance}', '{currentDate}', '{initialAirport}', '{airportCount}', '{token}');""")

    return {'success': DBcall(insertQuery)[1] == 1}

