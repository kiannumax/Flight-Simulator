'use strict';

function signout() {
    const gameInMiddle = localStorage.getItem('gameInMiddle');
    let message = "Are you sure you want to sign out?";

    if (gameInMiddle == '1') {
        message += " The progress of your current game will be lost!"
    }

    const decision = confirm(message);

    if (decision) {
        localStorage.removeItem('token');
        localStorage.removeItem('gameInMiddle');
        localStorage.removeItem('gameData');
        window.open('http://localhost:63342/FSgame/templates/home.html', '_self');
    }
}


async function changeUsername() {
    const newUsername = prompt("Enter your new username");

    try {
        const response = await fetch(`http://127.0.0.1:5000/changeUsername/${localStorage.getItem('token')}/${newUsername}`);
        var data = await response.json();

    } catch (e) {
        console.log("An Error occured:" + e);

    } finally {
        if(!data['success']) {
            console.log("Username change failed")
        } else {
            window.open('http://localhost:63342/FSgame/templates/profile.html', '_self')
        }
    }
}


async function changePassword() {
    const newPassword = prompt("Enter your new password");

    try {
        const response = await fetch(`http://127.0.0.1:5000/changePassword/${localStorage.getItem('token')}/${newPassword}`);
        var data = await response.json();

    } catch (e) {
        console.log("An Error occured:" + e);

    } finally {
        if(!data['success']) {
            console.log("Password change failed")
        } else {
            window.open('http://localhost:63342/FSgame/templates/profile.html', '_self')
        }
    }
}


async function profileData() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/playerInfo/${localStorage.getItem('token')}`);
        const data = await response.json();

        var string = `Username: ${data['username']} 
        Date registered: ${new Date(data['date_registered']).toLocaleString().replaceAll('/', '.').split(',')[0]} 
        IP adress: ${data['IP']}`;
        var list = document.createElement('ol');

           for(let game of data['games']) {
               let string = `Distance traveled: ${game['dstnc_traveled'].toFixed(2)}km, 
               Amount of Airports visited: ${game['airports_count']}, Initial Airport: ${game['init_airport']}, 
               Date played: ${new Date(game['date_played']).toLocaleString().replaceAll('/', '.').split(',')[0]}`

               const li = document.createElement('li');
               const p = document.createElement('p');
               p.innerText = string;

               li.appendChild(p);
               list.appendChild(li);
           }

    } catch(e) {
        console.log("An Error occured: " + e);
    } finally {
        document.getElementById('playerData').innerText = string;
        document.getElementById('playerInfo').appendChild(list);
    }
}

document.getElementById('signout').addEventListener('click', signout);
document.getElementById('changeUsername').addEventListener('click', changeUsername);
document.getElementById('changePassword').addEventListener('click', changePassword);

profileData();
