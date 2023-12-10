'use strict';

async function startGame() {
    try {  // API call to Flask to get initial airport's information
        const response = await fetch('http://127.0.0.1:5000/getInitialAirport');
        var initAirport = await response.json();

    } catch (e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred: " + e);

    } finally {
        const gameData = {'money': 2000, 'totalDstnc': 0, 'airportCount': 0, 'currentAirport': initAirport, 'all_airports': [initAirport['name']]};
        localStorage.setItem('gameData', JSON.stringify(gameData));  // Initialize initial game state and save it
        localStorage.setItem('gameInMiddle', '1');  // Change the Game in Middle state to True (1)
        continueGame();  // Continue the game with initial game state
    }
}


async function updateNearBy(gameData) {
    // Show the loading information
    document.getElementById('loader').setAttribute('class', 'svgLoader');
    document.getElementById('loaderPath').setAttribute('class', 'svgLoaderPath');

    try {  // API call to Flask to get a list of nearby airports
        const link = `http://127.0.0.1:5000/getClosestAirports/${gameData['currentAirport']['latitude']}/${gameData['currentAirport']['longitude']}/${gameData['all_airports']}`;
        const response = await fetch(link);
        var data = await response.json();

    } catch (e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred: " + e);

    } finally {
        const ul = document.createElement('ul');
        // Create a list and fill it while traversing through fetched airports
        for (let airport of data['airports']) {
            const li = document.createElement('li');

            const p = document.createElement('p');
            p.innerText = `Name: ${airport['name'].replaceAll('?', '')}, ${airport['ICAO']}
            Country: ${airport['country']} | Distance: ${airport['dstnc'].toFixed(2)}km | Type: ${airport['type'].replace('_', ' ')}`;
            li.appendChild(p);  // Append information about the airport to the list element

            const button = document.createElement('button');
            button.innerText = "Go Here!";  // Create a button for each element
            button.id = `${airport['ICAO']}/${airport['dstnc']}`;
            button.addEventListener('click', () => {
                goToAirport(airport, gameData);  // If pressed, game will be updated according to the chosen airport
            });
            li.appendChild(button);

            ul.appendChild(li);  // Update the list
        }
        // Stop and hide the loading animation
        document.getElementById('loader').setAttribute('class', 'svgLoaderHide');
        document.getElementById('loaderPath').setAttribute('class', 'svgLoaderPathStop');
        // Update the section with a list of airports
        document.getElementById('closestAirports').appendChild(ul);
    }
}


async function stopGame(gameData) {
    localStorage.setItem('gameInMiddle', '0');  // Change the state of Game in Middle to false (0)
    localStorage.removeItem('gameData');  // Remove game data

    const article = document.createElement('article');
    // Create an article which will contain game stats and play again button
    const gameOverP = document.createElement('p');
    gameOverP.innerText = "Game Over! No money left!";
    gameOverP.className = 'loss';  // Create game over <p> and append it to the article
    article.appendChild(gameOverP);

    const gameDataP = document.createElement('p');
    gameDataP.innerText = `Distance traveled: ${gameData['totalDstnc'].toFixed(2)}km 
                   Airports visited: ${gameData['airportCount']}`;
    article.appendChild(gameDataP);  // Create game stats <p> and append it to the article

    try {  // API call to Flask to save the game
        const link = `http://127.0.0.1:5000/saveGame/${gameData['totalDstnc']}/${localStorage.getItem('token')}/${gameData['airportCount']}/${gameData['all_airports'][0]}`;
        const response = await fetch(link);
        var data = await response.json();

    } catch (e) {  // Show error in console, more useful for developing state
        console.log("An Error occurred: " + e);

    } finally {
        const p = document.createElement('p');

        if(!data['success']) {  // If game save failed, inform the player about it
            p.innerText = "Unfortunately, Game had failed to be saved into your account. Try playing again!";

        } else {  // Likewise, but about the successful save
            p.innerText = "Game successfully saved!";
        }

        const button = document.createElement('button');
        button.innerText = "Play again!";  // Create a button that will reload the game
        button.addEventListener('click', () => {
           location.reload();
        });
        // Hide the Restart the Game button from nav
        document.getElementById('restartGame').className = 'hidden';
        const section = document.getElementById('game');
        section.innerHTML = '';  // Delete all HTML from section

        article.appendChild(p);  // Update HTML structure
        article.appendChild(button);
        section.appendChild(article);
    }
}



function goToAirport(airport, gameData) {  // Remove the list of closest airports
    document.getElementById('closestAirports').removeChild(document.querySelector('ul'));
    // Chance of getting money gain relying on airport type
    const sustainability = {'small_airport': 8, 'large_airport': 3, 'medium_airport': 6, 'seaplane_base': 10};
    const moneyOptions = [0, 50, 100, 150, 200];  // Possible money changes

    const p = document.getElementById('moneyChange');
    let money;
    // If a chance worked out
    if (Math.floor(Math.random() * 10) + 1 <= sustainability[airport['type']]) {
        const moneyChange = moneyOptions[Math.floor(Math.random() * 5)];
        money = gameData['money'] + moneyChange - (2 * airport['dstnc']);
        // Increase money by random change and decrease by the traveled distance
        p.innerText = `You gained ${moneyChange}€!`;  // Inform player about it
        p.className = 'gain';  // CSS styling

    } else {  // Otherwise, identical procedure but money is taken away
        const moneyChange = moneyOptions[Math.floor(Math.random() * 5)];
        money = gameData['money'] - moneyChange - (2 * airport['dstnc']);

        p.innerText = `You lost ${moneyChange}€!`;
        p.className = 'loss';
    }

    const totalDstnc = gameData['totalDstnc'] + airport['dstnc'];
    const airportCount = gameData['airportCount'] + 1;
    const allAirports = [...gameData['all_airports'], airport['name']];
    // Update current state of the game using JSON format
    const newGameData = {'money': money, 'totalDstnc': totalDstnc, 'airportCount': airportCount, 'currentAirport': airport, 'all_airports': allAirports};

    if (money <= 0) {  // Stop the game if no money left
        stopGame(newGameData);

    } else {  // Otherwise, update the current state of the game and continue
        localStorage.setItem('gameData', JSON.stringify(newGameData));
        continueGame();
    }
}


function restartGame() {
    localStorage.setItem('gameInMiddle', '0');  // Change the Game in Middle state to 0
    localStorage.removeItem('gameData');  // Remove game data

    location.reload(); // Update the page
}


function continueGame() {
    const gameData = JSON.parse(localStorage.getItem('gameData'));  // Get game's current state
    // Show information about the game in a string
    const currentState = `Money left: ${Math.round(gameData['money'])}€ | Total distance traveled: ${gameData['totalDstnc'].toFixed(2)}km
                                Amount of Airports visited: ${gameData['airportCount']}`;
    // Show information about the current airport in a string
    const currentAirport = `Current Airport: ${gameData['currentAirport']['name'].replaceAll('?', '')}, ${gameData['currentAirport']['ICAO']}
                                    Country: ${gameData['currentAirport']['country']}`;

    // Update HTML <p> elements with information about the current game state
    document.getElementById('currentStatus').innerText = currentState;
    document.getElementById('currentAirport').innerText = currentAirport;

    updateNearBy(gameData);  // Start the fetching of nearby airports
}


// Continue the game if user had game mid-saved, otherwise start a new one
if (localStorage.getItem('gameInMiddle') == '1') {
    continueGame();
} else {
    startGame();
}

// Add event listener to a Restart Game button
document.getElementById('restartGame').addEventListener('click', restartGame);
