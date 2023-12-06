'use strict';

async function startGame() {
    try {
        const response = await fetch('http://127.0.0.1:5000/getInitialAirport');
        var initAirport = await response.json();

    } catch (e) {
        console.log("An Error occurred: " + e);

    } finally {
        const gameData = {'money': 2000, 'totalDstnc': 0, 'airportCount': 0, 'currentAirport': initAirport, 'all_airports': [initAirport['name']]};
        localStorage.setItem('gameData', JSON.stringify(gameData));
        localStorage.setItem('gameInMiddle', 1);
        continueGame();
    }
}


async function goToAirport(airport, gameData) {
    document.getElementById('closestAirports').innerHTML = '';

    const sustainability = {'small_airport': 8, 'large_airport': 3, 'medium_airport': 6, 'seaplane_base': 10};
    const moneyOptions = [0, 50, 100, 150, 200];
    const p = document.getElementById('monayChange');
    let money;

    if (Math.floor(Math.random() * 10) + 1 <= sustainability[airport['type']]) {
        const moneyChange = moneyOptions[Math.floor(Math.random() * 5)];
        money = gameData['money'] + moneyChange - (5 * airport['dstnc']);
        p.innerText = `You gained ${moneyChange}€!`;

    } else {
        const moneyChange = moneyOptions[Math.floor(Math.random() * 5)];
        money = gameData['money'] - moneyChange - (5 * airport['dstnc']);
        p.innerText = `You lost ${moneyChange}€!`;
    }

    const totalDstnc = gameData['totalDstnc'] + airport['dstnc']
    const airportCount = gameData['airportCount'] + 1
    const allAirports = [...gameData['all_airports'], airport['name']]

    const newGameData = {'money': money, 'totalDstnc': totalDstnc, 'airportCount': airportCount, 'currentAirport': airport, 'all_airports': allAirports};

    if (money <= 0) {
        stopGame(newGameData);

    } else {
        localStorage.setItem('gameData', JSON.stringify(newGameData));
        continueGame();
    }
}


async function updateNearBy(gameData) {
    document.getElementById('loader').className = 'loading';

    try {
        const link = `http://127.0.0.1:5000/getClosestAirports/${gameData['currentAirport']['latitude']}/${gameData['currentAirport']['longitude']}/${gameData['all_airports']}`;
        const response = await fetch(link);
        var data = await response.json();

    } catch (e) {
        console.log("An Error occurred: " + e);

    } finally {
        const ul = document.createElement('ul');
        console.log('done')
        for (let airport of data['airports']) {
            const li = document.createElement('li');
            const p = document.createElement('p');
            p.innerText = `Name: ${airport['name']}, ICAO: ${airport['ICAO']}, Distance: ${airport['dstnc'].toFixed(2)}km, Type: ${airport['type']}`;
            li.appendChild(p);

            if (airport['home_link']) {
                const iframe = document.createElement('iframge');
                iframe.src = airport['home_link'];
                li.appendChild(iframe);
            }

            if (airport['wiki_link']) {
                const iframe = document.createElement('iframge');
                iframe.src = airport['wiki_link'];
                li.appendChild(iframe);
            }

            const button = document.createElement('button');
            button.innerText = "Go Here!";
            button.id = `${airport['ICAO']}/${airport['dstnc']}`;
            button.addEventListener('click', (evt) => {
                goToAirport(airport, gameData);
            });
            li.appendChild(button);

            document.getElementById('loader').className = 'stopLoading';
            ul.appendChild(li)
        }

        document.getElementById('closestAirports').appendChild(ul);
    }
}


async function stopGame(gameData) {
    localStorage.setItem('gameInMiddle', 0);
    localStorage.removeItem('gameData');

    const div = document.getElementById('game');
    div.innerHTML = '';

    const p = document.createElement('p');
    p.innerText = `Distance traveled: ${gameData['totalDstnc']}, Airports visited: ${gameData['airportCount']}`;
    div.appendChild(p);

    try {
        const link = `http://127.0.0.1:5000/saveGame/${gameData['totalDstnc']}/${localStorage.getItem('token')}/${gameData['airportCount']}/${gameData['all_airports'][0]}`;
        const response = await fetch(link);
        var data = await response.json();

    } catch (e) {
        console.log("An Error occurred: " + e);

    } finally {
        if(!data['success']) {
            console.log("problem")
        } else {
            const p = document.createElement('p');
            p.innerText = "Game succesfully saved!";

            const button = document.createElement('button');
            button.innerText = "Play again!";
            button.addEventListener('click', () => {
               location.reload();
            });

             div.appendChild(p);
             div.appendChild(button);
        }
    }
}



function restartGame() {
    localStorage.setItem('gameInMiddle', 0);
    localStorage.removeItem('gameData');

    location.reload();
}


function continueGame() {
    const gameData = JSON.parse(localStorage.getItem('gameData'));

    document.getElementById('money').innerText = `${Math.round(gameData['money'])}€`;
    document.getElementById('totalDstnc').innerText = `${gameData['totalDstnc'].toFixed(2)}km`;
    document.getElementById('airportCount').innerText = gameData['airportCount'];
    document.getElementById('airportName').innerText = gameData['currentAirport']['name'];
    document.getElementById('ICAO').innerText = gameData['currentAirport']['ICAO'];

    updateNearBy(gameData);
}



document.getElementById('restartGame').addEventListener('click', restartGame);



if (localStorage.getItem('gameInMiddle') == '1') {
    continueGame();
} else {
    startGame();
}
