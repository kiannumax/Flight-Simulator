'use strict';
// Function creating a custom Alert popup
export function openAlert(message) {
    return new Promise(resolve => { // Code will not go on until this Promise resolved (popup closed)
        const alertBox = document.createElement("div");
        alertBox.className = 'popup'; // Structural div

        const p = document.createElement('p');
        p.innerText = message; // Display message in <p> tag
        alertBox.appendChild(p);

        const alertClose = document.createElement("button");
        alertClose.className = 'popupButton'; // Create button which closes the alert
        alertClose.innerText = "Close";
        alertBox.appendChild(alertClose);

        alertClose.onclick = () => { // If button pressed
            alertBox.remove(); // Delete this entire HTML structure from the app
            resolve(null); // Resolve the Promise, continue the code
        };

        document.body.appendChild(alertBox); // Show Alert popup
    });
}


// Function creating a custom Prompt popup
export function openPrompt(message, type) {
    return new Promise(resolve => { // Code will not go on until Promise resolved
        const promptBox = document.createElement("div");
        promptBox.className = 'popup'; // Structural div

        const p = document.createElement('p');
        p.innerText = message; // Display message in <p> tag
        promptBox.appendChild(p);

        const input = document.createElement('input');
        input.id = 'resetUsername'; // Create input tag
        input.type = type; // Determine its type from attribute (text/password)
        input.placeholder = `Enter your ${type == 'text' ? "username" : "password"}`;
        promptBox.appendChild(input);

        const promptClose = document.createElement("button");
        promptClose.className = 'popupButton'; // Create a button which closes the Prompt
        promptClose.id = 'close';
        promptClose.innerText = "Close";
        promptBox.appendChild(promptClose);

        promptClose.onclick = () => {
            promptBox.remove(); // Delete this entire HTML structure from the app
            resolve(false); // Resolve a Promise, return false since closed
        };

        const promptSend = document.createElement("button");
        promptSend.className = 'popupButton'; // Create a button which sends the contents of input
        promptSend.id = 'promptSend';
        promptSend.innerText = "Send";
        promptBox.appendChild(promptSend);
        promptSend.onclick = () => {
            promptBox.remove(); // Delete this entire HTML structure from the app
            resolve(input.value.trim()); // Resolve a Promise, return input's trimmed value
        };

        document.body.appendChild(promptBox); // Show the Prompt popup
    });
}


// Function creating a custom Confirm popup
export function openConfirm(message) {
    return new Promise(resolve => { // Code will not go on until Promise resolved
        const confirmBox = document.createElement("div");
        confirmBox.className = 'popup'; // Structural div

        const p = document.createElement('p');
        p.innerText = message; // Display message in <p> tag
        confirmBox.appendChild(p);

        const confirmClose = document.createElement("button");
        confirmClose.className = 'popupButton'; // Create a button which serves as 'No'
        confirmClose.id = 'close';
        confirmClose.innerText = "No";
        confirmBox.appendChild(confirmClose);

        confirmClose.onclick = () => {
            confirmBox.remove(); // Delete this entire HTML structure from the app
            resolve(false); // Resolve a Promise, return false since user answered 'No'
        };

        const confirmYes = document.createElement("button");
        confirmYes.className = 'popupButton'; // Create a button which serves as 'Yes'
        confirmYes.id = 'confirmYes';
        confirmYes.innerText = "Yes";
        confirmBox.appendChild(confirmYes);

        confirmYes.onclick = () => {
            confirmBox.remove(); // Delete this entire HTML structure from the app
            resolve(true); // Resolve a Promise, return ture since user answered 'Yes'
        };

        document.body.appendChild(confirmBox); // Show the Confirm popup
    });
}
