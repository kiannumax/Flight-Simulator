'use strict';

import { openConfirm } from "./customPopups.js";  // Import a custom Confirm popup function


async function signout() {
    const gameInMiddle = localStorage.getItem('gameInMiddle');
    let message = "Are you sure you want to sign out?";
    // If user has a game in the middle, add that information to Confirm message
    if (gameInMiddle == '1') {
        message += " The progress of your current game will be lost!";
    }

    try {
        var decision = await openConfirm(message);  // Call a custom Confirm popup

    } finally {
        if (decision) {  // If answered yes, remove all data from localStorage and open a Home page
            localStorage.removeItem('token');
            localStorage.removeItem('gameInMiddle');
            localStorage.removeItem('gameData');
            window.open('http://localhost:63342/FSgame/templates/home.html', '_self');
       }
    }
}


async function globalLeaderboard() {
        try{  // Call Flask API to get a list of games in a Global Leaderboard
           const response = await fetch('http://127.0.0.1:5000/globalLeaderboard');
           const data = await response.json();

           var list = document.createElement('ol');  // Initialize <ol> element

           for(let i = 0; i < data['length']; i++) {  // Traverse through the games list
               const string = `Username: ${data['username'][i]} | Distance traveled: ${data['dstnc_traveled'][i].toFixed(2)}km 
               Amount of Airports visited: ${data['airports_count'][i]} | Initial Airport: ${data['init_airport'][i]} 
               Date played: ${new Date(data['date_played'][i]).toLocaleString().replaceAll('/', '.').split(',')[0]}`;
               // Create a text describing game stats
               const li = document.createElement('li');
               const p = document.createElement('p');
               p.innerText = string;

               if (i == 0) {  // Extra styling for the first place
                   li.className = 'first';

               } else if (i == 1) {  // Extra styling for the second place
                   li.className = 'second';

               } else if (i == 2) {  // Extra styling for the third place
                   li.className = 'third';
               }

               li.appendChild(p);  // Append game to the list
               list.appendChild(li);
           }


        } catch (e) {  // Show error in console, more useful for developing state
          console.log("Error occurred:" + e);

        } finally {  // Append completed list to the page HTML structure
            document.getElementById('globalLeaderboard').appendChild(list);
    }
}



function signedIn() {
    // Show hidden sections
    document.getElementById('notSigned').setAttribute('class', 'absent');

    const nav = document.getElementById('homeNav');
    const a = document.createElement('a');
    a.href = 'profile.html';
    a.innerText = "Profile";
    nav.appendChild(a);
    // Fill <nav> with a link to Profile page and a Sign-out button
    const button = document.createElement('button');
    button.innerText = "Sign Out";
    button.addEventListener('click', signout);  // Assign a function to the Sign-out button
    nav.appendChild(button);

    if (localStorage.getItem('gameInMiddle') == '1') {
        // If game in middle, modify the  section which leads to a Game page
        document.getElementById('gameState').innerText = "You have an unfinished game!";
        document.getElementById('gameStateButton').innerText = "Continue";
    }
}



if(localStorage.getItem('token')) {
    signedIn();  // If token exists, show Home page assigned for logged users
} else {  // Otherwise, hide sections meant for logged users
    document.getElementById('signedIn').setAttribute('class', 'absent');
}

// Open a game page if corresponding button is clicked
document.getElementById('gameStateButton').addEventListener('click', () => {
    window.open('http://localhost:63342/FSgame/templates/game.html', '_self');
});

// Show Global Leaderboard
globalLeaderboard();
