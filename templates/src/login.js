'use strict';

import { openAlert, openPrompt } from "./customPopups.js"; // Import custom Alert and Prompt functions
import { getIP } from "./sharedFunctions.js";  // Import function which return user's public IP


async function login() {
    // Get trimmed values from prompts
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!username.length || !password.length) {
        return;  // Stop the function from continuing if either of inputs is empty
    }

    try { // API call to Flask which includes credentials entered by user
        const response = await fetch(`http://127.0.0.1:5000/login/${username}/${password}`);
        var data = await response.json();

    } catch (e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred: " + e);

    } finally {
        if (data['result']) { // If login credentials entered correctly
            localStorage.setItem('token', data['token']);
            // Store user's token in local Storage to let know the app that user is logged in
            localStorage.setItem('gameInMiddle', '0');  // Initialize other user data about game state
            window.open('http://localhost:63342/FSgame/templates/home.html', '_self'); // Move to Home page

        } else { // If credentials entered wrong, show message and button with reset password feature
            document.getElementById('resetPassword').className = 'wrongCredentials';
        }
    }
}


async function resetPassword(username) {
    try {
        const newPassword = await openPrompt("Type a new password", 'password');
        var data;  // Ask user to type a new password using custom Prompt with type 'password'

        if (!newPassword) {  // If Prompt was closed or its input was empty, cancel database fetch and show message
            data = {'message': "Password Reset Canceled."};

        } else {
            const response = await fetch(`http://127.0.0.1:5000/resetPassword/${username}/${newPassword}`);
            data = await response.json();  // Update user's password with API call
        }

    } catch (e) {  // If IPs match start the process of Password resetting
        console.log("An Error occurred: " + e);

    } finally {
        await openAlert(data['message']);  // Show message to user using custom Alert
        window.open('http://localhost:63342/FSgame/templates/login.html', '_self');
        // Reload the page no matter the outcome of Password reset
    }
}


async function checkIP() {
    try {  // Ask user for username using custom Prompt
         var username = await openPrompt("Type your username. You will be able to reset the password if " +
        "your current IP matches with the assigned one to the username.", 'text');
         var data;

         if (!username) {  // If Prompt was closed or its input was empty, cancel database fetch and show message
             data = {'match': false, 'message': "Password Reset Canceled."};

         } else {
             const IP =  await getIP();  // Get user's public IP address
             const response = await fetch(`http://127.0.0.1:5000/checkIP/${username}/${IP}`);
             data = await response.json();  // API call to compare IPs with database data
         }

    } catch(e) {  // Show error in console, more useful for developing state
         console.log("An Error occurred: " + e);

     } finally {
        if (data['match']) {  // If IPs match start the process of Password resetting
            resetPassword(username);

        } else {  // If IPs do not match or username doesn't exist, alert user with message and reload the page
            await openAlert(data['message']);
            window.open('http://localhost:63342/FSgame/templates/login.html', '_self');
        }
    }
}


// Start a login function when form submitted
document.getElementById('loginForm').addEventListener('submit', (evt) => {
    evt.preventDefault();
    login();
});

document.getElementById('resetButton').addEventListener('click', checkIP);
// Start a Reset Password procedure if clicked by user
