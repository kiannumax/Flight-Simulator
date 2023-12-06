from flask import Flask, Response
from flask_cors import CORS
import json

from backend.leaderboard import showLeaderboard
from backend.game.game import getInitialAirport
from backend.game.game import getClosestAirports
from backend.game.saveGame import saveGame
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


@app.route('/getInitialAirport', methods=['GET'])
def initialAirport():
    return getInitialAirport()


@app.route('/getClosestAirports/<latitude>/<longitude>/<pastAirports>', methods=['GET'])
def closestAirports(latitude, longitude, pastAirports):
    return getClosestAirports(latitude, longitude, pastAirports)


@app.route('/saveGame/<distance>/<token>/<airportCount>/<initialAirport>')
def gameSave(distance, token, airportCount, initialAirport):
    return saveGame(distance, token, airportCount, initialAirport)



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
