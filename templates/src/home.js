'use strict';

function signout() {
    const decision = confirm("Are you sure?");

    if (decision) {
        localStorage.removeItem('token');
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
}

function notSignedIn() {
     document.getElementById('signedIn').setAttribute('class', 'absent');
}


if(localStorage.getItem('token')) {
    signedIn();
} else {
    notSignedIn();
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

globalLeaderboard();
