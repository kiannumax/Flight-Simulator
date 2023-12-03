from ..database import DBcall

def profileData(token):
    user = DBcall(f"SELECT username, date_registered, IP FROM users WHERE id = {token};")[0][0]
    finalData = {'username': user[0], 'IP': user[2], 'date_registered': user[1], 'games': []}

    allGames = DBcall(f"SELECT date_played, initial_airport, airports_visited, distance FROM games WHERE user_id = {token} GROUP BY distance DESC;")[0]

    for game in allGames:
        gameStat = {'dstnc_traveled': game[3], 'airports_count': game[2], 'init_airport': game[1], 'date_played': game[0]}
        finalData['games'].append(gameStat)


    return finalData