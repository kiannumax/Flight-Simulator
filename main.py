from flight_simulator.user.signup import signup
from flight_simulator.user.login import login
from flight_simulator.user.profile import showProfile
from flight_simulator.game.game import game
from flight_simulator.leaderboard import showLeaderboard
from sys import exit

currentUser = None

print("Hello and Welcome to our Flight Simulator game!\n"
      "At this point of the program you can either view the global leaderboard "
      "or signup/login in order to play the game and view your own profile.\n")

decided = False
while not decided:
    option = input("Choose your option: View leaderboard, Login or Quit? (v, l, q) >> ").lower()

    if option == 'v':
        showLeaderboard()
        print('\n')

    elif option == 'l':
        print("Alright! You will be taken to another input..\n")
        decided = True

    elif option == 'q':
        print("Exiting the program...")
        exit(0)

    else:
        print('\n')


signed = False
while not signed:
    option = input("Choose your option: Signup, Login or Quit? (s, l, q) >> ").lower()

    if option == 's':
        result = signup()

        if result[0] == 'exists':
            print("Account with this username already exists, please use a login option!\n")
            continue

        elif result[0] == 'fail':
            print("Unfortunately Signup failed. Try again later!\n")

        else:
            print("Signup successful! We are happy to have you as our new user!\n")
            currentUser = result[1]
            signed      = True

    elif option == 'l':
        result = login()

        if result[0]:
            print("Login successfull!")
            currentUser = result[1]
            signed      = True

        else:
            continue

    elif option == 'q':
        print("Exiting the program...")
        break

    else:
        print('\n')


print("\nNow, since you are logged in, you have 4 options what to do next: You can view your own profile (p);\n"
      "You can read the rules of the game (recommended if playing for the first time) (r);\n"
      "You can exit the program (q); Or you can start the GAME itself! (g)")

finishedGame = False
while not finishedGame:
    option = input("Choose your option (p, r, q, g) >> ").lower()

    if option == 'p':
        showProfile(currentUser)

    elif option == 'r':
        print('')

    elif option == 'q':
        print("Exiting the program...")
        exit(0)

    elif option == 'g':
        print("Alright! Game will start in a bit. Enjoy!\n")
        updated = game(currentUser)

        if updated:
            print("\nGame finished and saved to you profile, where you can later view it.\n"
                  "If it was your best game so far, then expect to see it in a leaderboard!")
        else:
            print("Game finished, but unoftunately did not get saved to your profile due to uknown reasons.\n"
                  "Try playing again later!")

        finishedGame = True

    else:
        print('\n')
