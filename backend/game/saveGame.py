from ..database import DBcall
import datetime

def saveGame(distance, token, airportCount, initialAirport):
    currentDate = datetime.date.today()
    # Get game's stats and information and Insert them into the database
    insertQuery = (f"INSERT INTO games (distance, date_played, initial_airport, airports_visited, user_id)"
                   f"""VALUES ('{distance}', '{currentDate}', '{initialAirport}', '{airportCount}', '{token}');""")

    return {'success': DBcall(insertQuery)[1] == 1}  # return True if the amount of modified rows os 1, False otherwise
