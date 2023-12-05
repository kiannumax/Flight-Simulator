'use strict';

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch(`http://127.0.0.1:5000/login/${username}/${password}`);
        var data = await response.json();

    } catch (e) {
        console.log("An Error occured: " + e);

    } finally {
        if (data['result']) {
            localStorage.setItem('token', data['token']);
            window.open('http://localhost:63342/FSgame/templates/home.html', '_self');
        } else {
            document.getElementById('resetButton').className = 'wrongCredentials';
            document.getElementById('resetPassword').className = 'wrongCredentials';
        }
    }
}


async function getIP() {
    try {
        const response = await fetch("https://api.ipify.org/?format=json");
        var data = await response.json();

    } catch(e) {
        console.log("An Error occured: " + e);

    } finally {
        return data['ip'];
    }
}


async function resetPassword(username) {
    const newPassword = prompt("Type a new password");

    try {
        const response = await fetch(`http://127.0.0.1:5000/resetPassword/${username}/${newPassword}`);
        var data = await response.json();

    } catch (e) {
        console.log("An Error occured: " + e);

    } finally {
        console.log(data)
        if (data['success']) {
            alert("Password reset was successful, try signing in!")
            window.open('http://localhost:63342/FSgame/templates/home.html', '_self');
        }
    }
}


async function checkIP() {
    var username = prompt("Type your username. You will be able to reset the password if " +
        "your current IP matches with the assigned one to the username.");


    try {
         const IP =  await getIP();
         const response = await fetch(`http://127.0.0.1:5000/checkIP/${username}/${IP}`);
         var data = await response.json();

    } catch(e) {
         console.log("An Error occured: " + e);

     } finally {
        if (data['match']) {
            resetPassword(username);
        } else {
            alert(data['message']);
        }
    }
}

document.getElementById('login').addEventListener('submit', (evt) => {
    evt.preventDefault()
    login()
});

document.getElementById('resetButton').addEventListener('click', checkIP)

