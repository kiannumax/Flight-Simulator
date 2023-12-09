'use strict';

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


async function signup(username, password) {
    try {
         const IP =  await getIP();
         const response = await fetch(`http://127.0.0.1:5000/signup/${username}/${password}/${IP}`);
         var data = await response.json();

    } catch(e) {
         console.log("An Error occurred: " + e);

     } finally {
        if (data['success']) {
            localStorage.setItem('token', data['token']);
            localStorage.setItem('gameInMiddle', 0)
            window.open('http://localhost:63342/FSgame/templates/home.html', '_self');
        } else {
            alert(data['message']);
        }
    }
}


function checkCredentials() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const password2 = document.getElementById('password2').value;
    const p = document.getElementById('warning');

    if (username.length > 15) {
        p.className = 'warning';
        p.innerText = "Username should be less than 15 characters!"

    } else if (password != password2) {
        p.className = 'warning';
        p.innerText = "Passwords do not match!"

    } else {
        signup(username, password);
    }
}

document.getElementById('signupForm').addEventListener('submit', (evt) => {
    evt.preventDefault()
    checkCredentials()
});
