from .database import DBcall

def showLeaderboard():
    # Fetch a list of all played games
    allGames = DBcall("SELECT date_played, initial_airport, airports_visited, distance, user_id FROM games GROUP BY distance DESC;")[0]
    usedUsers = []  # Initialize list containing duplicate users
    finalData = {'length': 0, 'username': [], 'dstnc_traveled': [], 'airports_count': [], 'init_airport': [], 'date_played': []}
    # Initialize return JSON format

    for game in allGames:  # Traverse through all games
        if game[4] in usedUsers:
            continue  # Continue the loop if game from this user is already used

        else:
            usedUsers.append(game[4])
            finalData['length'] += 1  # Amount of games being returned
            user = DBcall(f"SELECT username FROM users WHERE id = {game[4]};")[0][0][0]
            # Fill data about the game in JSON format and push it to lists
            finalData['username'].append(user)
            finalData['dstnc_traveled'].append(game[3])
            finalData['airports_count'].append(game[2])
            finalData['init_airport'].append(game[1])
            finalData['date_played'].append(game[0])

    return finalData
