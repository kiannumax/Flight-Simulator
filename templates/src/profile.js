'use strict';

import { signout } from "./sharedFunctions.js";  // Import a sign-out function
import { openAlert, openPrompt } from "./customPopups.js";  // Import custom Alert and Prompt popups


async function changeUsername() {
    try {
        const newUsername = await openPrompt("Enter your new username", 'text');
        // Ask user for a new username using custom Prompt popup
        if (!newUsername) {
            return;  // Stop the function if user's input is empty

        } else {  // Otherwise, API call to Flask to change the username
            const response = await fetch(`http://127.0.0.1:5000/changeUsername/${localStorage.getItem('token')}/${newUsername}`);
            var data = await response.json();
        }

    } catch (e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred:" + e);

    } finally {
        if(data['success']) {  // Refresh the page if username change was successful
            location.reload();

        } else {  // Otherwise alert the user that it failed
            await openAlert("Username change failed. Try again later!");
        }
    }
}


async function changePassword() {
    try {
        const newPassword = await openPrompt("Enter your new password", 'password');
        // Ask user for a new password using custom Prompt popup
        if (!newPassword) {
            return;  // Stop the function if user's input is empty

        } else {  // Otherwise, API call to Flask to change the password
            const response = await fetch(`http://127.0.0.1:5000/changePassword/${localStorage.getItem('token')}/${newPassword}`);
            var data = await response.json();
        }

    } catch (e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred:" + e);

    } finally {
        if(data['success']) {  // Alert the user if the Password change was successful
            await openAlert("Password change successful!");

        } else {  // Alert otherwise
            await openAlert("Password change failed. Try again later!");
        }
    }
}


async function profileData() {
    try {  // API call to Flask for getting user's data
        const response = await fetch(`http://127.0.0.1:5000/playerInfo/${localStorage.getItem('token')}`);
        const data = await response.json();

        // Create a string containing information about the user
        var string = `Username: ${data['username']} 
        Date registered: ${new Date(data['date_registered']).toLocaleString().replaceAll('/', '.').split(',')[0]} 
        Assigned IP address: ${data['IP']}`;
        var list = document.createElement('ol');
        // Initialize a list of user's past games and fill it while traversing through fetched list of games
       for(let game of data['games']) {
           let string = `Distance traveled: ${game['dstnc_traveled'].toFixed(2)}km 
           Amount of Airports visited: ${game['airports_count']} | Initial Airport: ${game['init_airport'].replaceAll('?', '')} 
           Date played: ${new Date(game['date_played']).toLocaleString().replaceAll('/', '.').split(',')[0]}`;
           // Create a string containing info about a game and append it to a list element
           const li = document.createElement('li');
           li.className = 'pastGamesLi';
           const p = document.createElement('p');
           p.innerText = string;
           p.className = 'pastGamesP';
           // Append p into a list element, and then the list element into the list itself
           li.appendChild(p);
           list.appendChild(li);
       }

    } catch(e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred: " + e);

    } finally {  // Append user's past games and information into HTMl structure
        document.getElementById('playerData').innerText = string;
        document.getElementById('playerGames').appendChild(list);
    }
}


// Assign event listeners to buttons and their corresponding functions
document.getElementById('signout').addEventListener('click', signout);
document.getElementById('changeUsername').addEventListener('click', changeUsername);
document.getElementById('changePassword').addEventListener('click', changePassword);

profileData();  // Fetch and show user's data
