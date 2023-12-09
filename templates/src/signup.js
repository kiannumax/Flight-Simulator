'use strict';

import { getIP } from "./getIP.js";  // Import function which return user's public IP
import { openAlert } from "./customPopups.js";  // Import custom Alert


async function signup(username, password) {
    try {
         const IP =  await getIP();  // Get user's public IP
         const response = await fetch(`http://127.0.0.1:5000/signup/${username}/${password}/${IP}`);
         var data = await response.json();  // Call Flask's Sign Up API

    } catch(e) {  // Show error in console, more useful for developing state
         console.log("An Error occurred: " + e);

     } finally {
        if (data['success']) {  // If Sign up successful
            localStorage.setItem('token', data['token']);
            // Store user's token in local Storage to let know the app that user is logged in
            localStorage.setItem('gameInMiddle', '0');  // Initialize other user data about game state

            await openAlert("Sign up was successful! You will be taken to a Home page.")
            window.open('http://localhost:63342/FSgame/templates/home.html', '_self');
            // Redirect to a Home page and inform the user about it with custom Alert

        } else {  // If Sign up failed, show a message to user with custom Alert
            openAlert(data['message']);
        }
    }
}



function checkCredentials() {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const password2 = document.getElementById('password2').value.trim();
    const p = document.getElementById('warning');

    if (!username || !password || !password2) { // If either of the inputs is empty
        p.className = 'warning';
        p.innerText = "Prompts should be filled!";

    } else if (username.length > 15) {  // If username is too long
        p.className = 'warning';
        p.innerText = "Username should be less than 15 characters!";

    } else if (password != password2) {  // If passwords do not match
        p.className = 'warning';
        p.innerText = "Passwords do not match!";

    } else {
        p.className = 'hide';
        signup(username, password);  // Otherwise send a call to API
    }
}


// Start the process of Signing up if from is submitted
document.getElementById('signupForm').addEventListener('submit', (evt) => {
    evt.preventDefault();
    checkCredentials();
});
