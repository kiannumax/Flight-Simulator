from .database import DBcall

def showLeaderboard():
    allGames = DBcall("SELECT date_played, initial_airport, airports_visited, distance, user_id FROM games GROUP BY distance DESC;")[0]
    usedUsers = []
    finalData = {'length': 0, 'username': [], 'dstnc_traveled': [], 'airports_count': [], 'init_airport': [], 'date_played': []}

    for game in allGames:
        if game[4] in usedUsers:
            continue

        else:
            usedUsers.append(game[4])
            finalData['length'] += 1
            user = DBcall(f"SELECT username FROM users WHERE id = {game[4]};")[0][0][0]

            finalData['username'].append(user)
            finalData['dstnc_traveled'].append(game[3])
            finalData['airports_count'].append(game[2])
            finalData['init_airport'].append(game[1])
            finalData['date_played'].append(game[0])

    return finalData
