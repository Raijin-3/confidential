// document.addEventListener('DOMContentLoaded', function() {
//     const buttons = document.querySelectorAll('.btn');
//     buttons.forEach(button => {
//         button.addEventListener('click', function() {
//             alert('You clicked: ' + this.textContent);
//             // Here you can add the logic to handle button clicks, e.g., show specific information or start a conversation
//         });
//     });

//     const sendBtn = document.getElementById('send-btn');
//     sendBtn.addEventListener('click', function() {
//         const chatInput = document.getElementById('chat-input');
//         if (chatInput.value.trim() !== '') {
//             // Display the user's message
//             displayMessage(chatInput.value, 'user');
//             // Simulate an AI response
//             simulateAiResponse(chatInput.value);
//             chatInput.value = ''; // Clear the input field
//         }
//     });
// });

// function displayMessage(message, sender) {
//     const chatMessages = document.querySelector('.chat-messages');
//     const messageElement = document.createElement('p');
//     messageElement.textContent = message;
//     messageElement.classList.add(sender); // Add a class to differentiate user and AI messages
//     chatMessages.appendChild(messageElement);

//     // Automatically scroll to the bottom of the chat messages container
//     chatMessages.scrollTop = chatMessages.scrollHeight;
// }

// function simulateAiResponse(userMessage) {
//     // This is a simple echo response. Replace this with your AI logic or API call.
//     const response = `You said: ${userMessage}`;
//     displayMessage(response, 'ai');
// }
