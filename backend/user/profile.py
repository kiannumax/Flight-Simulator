from ..database import DBcall

def profileData(token):
    # Fetch all information about the user from database
    user = DBcall(f"SELECT username, date_registered, IP FROM users WHERE id = {token};")[0][0]
    finalData = {'username': user[0], 'IP': user[2], 'date_registered': user[1], 'games': []}
    # Initialize return JSON format

    allGames = DBcall(f"SELECT date_played, initial_airport, airports_visited, distance FROM games WHERE user_id = {token} GROUP BY distance DESC;")[0]
    # Fetch all user's played games from best to worst and traverse through the list
    for game in allGames:
        gameStat = {'dstnc_traveled': game[3], 'airports_count': game[2], 'init_airport': game[1], 'date_played': game[0]}
        # Append a game with all of its data into the list of returned games
        finalData['games'].append(gameStat)


    return finalData
