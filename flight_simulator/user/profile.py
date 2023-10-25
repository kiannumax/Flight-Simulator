from ..database import DBcall
from .changeUserData import changeUsername

def showProfile(currentUser):
    user = DBcall(f"SELECT username, date_registered, IP FROM users WHERE id = {currentUser};")[0][0]

    print(f"\nHere is your profile:\n"
          f"Username: {user[0]}, assigned IP: {user[2]}, date_registered: {user[1]}")

    allGames = DBcall(f"SELECT date_played, initial_airport, airports_visited, distance FROM games WHERE user_id = {currentUser} GROUP BY distance DESC;")[0]

    print("\nHere are all your played games sorted from best to worst:")
    for game in allGames:
        print(f"Distance traveled: {game[3]:.2f}km, Amount of Airports visited: {game[2]}, "
              f"Initial Airport: {game[1]}, Date played: {game[0]}")

    print()
    decided = False
    while not decided:
        option = input("Do you want to change the username, or go back? (c, b) >> ")

        if option == 'b':
            print()
            decided = True

        elif option == 'c':
            changeUsername(currentUser)
            decided = True