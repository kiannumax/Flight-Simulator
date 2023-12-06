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

function signedIn() {
    document.getElementById('notSigned').setAttribute('class', 'absent');

    const nav = document.getElementById('homeNav');
    const a = document.createElement('a');
    a.href = 'profile.html';
    a.innerText = "Profile";
    nav.appendChild(a)

    const button = document.createElement('button');
    button.innerText = "Sign Out";
    button.addEventListener('click', signout);
    nav.appendChild(button)

    if (localStorage.getItem('gameInMiddle') == '1') {
        document.getElementById('gameState').innerText = "You have an unfinished game!";
        document.getElementById('gameStateButton').innerText = "Continue";
    }
}


if(localStorage.getItem('token')) {
    signedIn();
} else {
    document.getElementById('signedIn').setAttribute('class', 'absent');
}


async function globalLeaderboard() {
        try{
           const response = await fetch('http://127.0.0.1:5000/globalLeaderboard');
           const data = await response.json();

           var list = document.createElement('ol');

           for(let i = 0; i < data['length']; i++) {
               let string = `Username: ${data['username'][i]}, Distance traveled: ${data['dstnc_traveled'][i].toFixed(2)}km, 
               Amount of Airports visited: ${data['airports_count'][i]}, Initial Airport: ${data['init_airport'][i]}, 
               Date played: ${new Date(data['date_played'][i]).toLocaleString().replaceAll('/', '.').split(',')[0]}`

               const li = document.createElement('li');
               const p = document.createElement('p');
               p.innerText = string;

               li.appendChild(p);
               list.appendChild(li);
           }


        } catch (error) {
          console.log("Error occured:" + error.message);

        } finally {
            document.getElementById('globalLeaderboard').appendChild(list);
    }
}

document.getElementById('gameStateButton').addEventListener('click', () => {
    window.open('http://localhost:63342/FSgame/templates/game.html', '_self');
});

globalLeaderboard();
