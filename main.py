from flight_simulator.user.signup import signup
from flight_simulator.user.login import login
from sys import exit

print("Hello and Welcome to our Flight Simulator game!\n"
      "At this point of the program you can either view the global leaderboard "
      "or signup/login in order to play the game and view your own profile.\n")

decided = False
while not decided:
    option = input("Choose your option: View leaderboard, Login or Quit? (v, l, q) >> ").lower()

    if option == 'v':
        print("f")

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

        if result == 'exists':
            print("Account with this username already exists, please use a login option!\n")
            continue

        elif result == 'fail':
            print("Unfortunately Signup failed. Try again later!\n")

        else:
            print("Signup successful! We are happy to have you as our new user!\nEnjoy your game!")
            signed = True

    elif option == 'l':
        result = login()

        if result:
            print("Login successfull! Enjoy your game!")
            signed = True

        else:
            continue

    elif option == 'q':
        print("Exiting the program...")
        break

    else:
        print('\n')
