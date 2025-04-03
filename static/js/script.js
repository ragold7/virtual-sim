async function sendMessage() {
    const userInput = document.getElementById("userInput").value;

    const response = await fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();

    // Append user input and response to the chat
    const chatBox = document.getElementById("chatBox");
    const userMessage = document.createElement("p");
    userMessage.textContent = "You: " + userInput;
    const botMessage = document.createElement("p");
    botMessage.textContent = "Bot: " + data.response;

    chatBox.appendChild(userMessage);
    chatBox.appendChild(botMessage);

    document.getElementById("userInput").value = ""; // Clear input field
}
function startVoiceRecognition() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.onresult = function(event) {
        const userInput = event.results[0][0].transcript;
        document.getElementById("userInput").value = userInput;
        sendMessage();  // Automatically process the voice input
    };

    recognition.onerror = function(event) {
        alert("Error recognizing speech: " + event.error);
    };

    recognition.start();
}
