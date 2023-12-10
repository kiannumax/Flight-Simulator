'use strict';

import { openConfirm } from "./customPopups.js";  // Import a custom Confirm popup function


export async function signout() {
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


export async function getIP() {
    try {  // Fetch data from public API which returns current public IP of a user
        const response = await fetch('https://api.ipify.org/?format=json');
        var data = await response.json();

    } catch(e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred: " + e);

    } finally {
        return data['ip'];  // Return user's public IP
    }
}
