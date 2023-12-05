# from backend.user.signup import signup
# from backend.user.login import login
# from backend.user.profile import showProfile
# from backend.game.game import game
# from backend.leaderboard import showLeaderboard
# from sys import exit
#
# currentUser = None
#
# print("Hello and Welcome to our AIR Dominance game!\n"
#       "At this point of the program you can either view the global leaderboard "
#       "or signup/login in order to play the game and view your own profile.\n")
#
# decided = False
# while not decided:
#     option = input("Choose your option: View leaderboard, Login or Quit? (v, l, q) >> ").lower()
#
#     if option == 'v':
#         showLeaderboard()
#         print('\n')
#
#     elif option == 'l':
#         print("Alright! You will be taken to another input..\n")
#         decided = True
#
#     elif option == 'q':
#         print("Exiting the program...")
#         exit(0)
#
#     else:
#         print('\n')
#
#
# signed = False
# while not signed:
#     option = input("Choose your option: Signup, Login or Quit? (s, l, q) >> ").lower()
#
#     if option == 's':
#         result = signup()
#
#         if result[0] == 'exists':
#             print("Account with this username already exists, please use a login option!\n")
#             continue
#
#         elif result[0] == 'fail':
#             print("Unfortunately Signup failed. Try again later!\n")
#
#         else:
#             print("Signup successful! We are happy to have you as our new user!\n")
#             currentUser = result[1]
#             signed      = True
#
#     elif option == 'l':
#         result = login()
#
#         if result[0]:
#             print("Login successfull!")
#             currentUser = result[1]
#             signed      = True
#
#         else:
#             continue
#
#     elif option == 'q':
#         print("Exiting the program...")
#         exit(0)
#
#     else:
#         print('\n')
#
#
# print("\nNow, since you are logged in, you have 4 options what to do next:")
#
# finishedGame = False
# while not finishedGame:
#     option = input("You can view your own profile (p);\n"
#                    "You can read the rules of the game (recommended if playing for the first time) (r);\n"
#                    "You can exit the program (q);\nOr you can start the GAME itself! (g)\n"
#                    "Choose your option (p, r, q, g) >> ").lower()
#
#     if option == 'p':
#         showProfile(currentUser)
#
#     elif option == 'r':
#         print("\nYou will be dropped in an random airport and will be given a wallet with initial amount of 2000euros.\n"
#               "You will have to travel to nearby airports scavenging for money and try your luck in getting as far as possible!\n")
#
#     elif option == 'q':
#         print("Exiting the program...")
#         exit(0)
#
#     elif option == 'g':
#         print("Alright! Game will start in a bit. Enjoy!\n")
#         updated = game(currentUser)
#
#         if updated:
#             print("\nGame finished and saved to you profile, where you can later view it.\n"
#                   "If it was your best game so far, then expect to see it in a leaderboard!")
#         else:
#             print("Game finished, but unfortunately did not get saved to your profile due to uknown reasons.\n"
#                   "Try playing again later!")
#
#         finishedGame = True
#
#     else:
#         print('\n')


from flask import Flask, Response
from flask_cors import CORS
import json

from backend.leaderboard import showLeaderboard
from backend.user.signup import signup
from backend.user.login import login
from backend.user.profile import profileData
from backend.user.changeUserData import changeUsername
from backend.user.changeUserData import changePassword
from backend.user.changeUserData import checkIP
from backend.user.changeUserData import resetPassword

app = Flask(__name__)
CORS(app)



@app.route('/signup/<username>/<password>/<IP>')
def signUP(username, password, IP):
    return signup(username, password, IP)


@app.route('/changeUsername/<token>/<newUsername>', methods=['GET'])
def usernameChange(token, newUsername):
    return changeUsername(token, newUsername)


@app.route('/changePassword/<token>/<newPassword>', methods=['GET'])
def passwordChange(token, newPassword):
    return changePassword(token, newPassword)


@app.route('/checkIP/<username>/<IP>', methods=['GET'])
def IPcheck(username, IP):
    return checkIP(username, IP)


@app.route('/resetPassword/<username>/<newPassword>', methods=['GET'])
def passwordReset(username, newPassword):
    return resetPassword(username, newPassword)


@app.route('/playerInfo/<token>', methods=['GET'])
def getProfileData(token):
    return profileData(token)


@app.route('/login/<username>/<password>', methods=['GET'])
def doLogin(username, password):
    return login(username, password)


@app.route('/globalLeaderboard', methods=['GET'])
def showGlobalLeaderboard():
    return showLeaderboard()




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000, )
