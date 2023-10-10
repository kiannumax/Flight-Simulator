from .database import DBcall

def showLeaderboard():
    allGames = DBcall("SELECT date_played, initial_airport, airports_visited, distance, user_id FROM games GROUP BY distance DESC;")[0]
    usedUsers = []

    print("\nHere is the leaderboard that contains each user's best game:")

    i = 1
    for game in allGames:
        if game[4] in usedUsers:
            continue

        else:
            usedUsers.append(game[4])
            user = DBcall(f"SELECT username FROM users WHERE id = {game[4]};")[0][0][0]

            print(f"{i}. Username: {user}, Distance traveled: {game[3]:.2f}km, Amount of Airports visited: {game[2]}, "
                  f"Initial Airport: {game[1]}km, Date played: {game[0]}")
            i += 1
