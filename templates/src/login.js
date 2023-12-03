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
        }
        console.log(data)
        window.open('http://localhost:63342/FSgame/templates/home.html', '_self');
    }
}

document.getElementById('login').addEventListener('submit', (evt) => {
    evt.preventDefault()
    login()
});

