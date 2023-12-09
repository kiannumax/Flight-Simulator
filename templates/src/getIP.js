'use strict';

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
