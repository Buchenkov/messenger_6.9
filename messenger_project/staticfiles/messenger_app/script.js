document.addEventListener('DOMContentLoaded', function() {
    const chatWindow = document.getElementById('chat-window');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    const chatName = 'general';  // Имя чата (можно динамически изменять)
    const username = 'user1';  // Имя пользователя (получить из аутентификации)

    const socket = new WebSocket(`ws://${window.location.host}/ws/chat/${chatName}/`);

    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const messageElement = document.createElement('div');
        messageElement.textContent = `${data.username}: ${data.message}`;
        chatWindow.appendChild(messageElement);
    };

    sendButton.addEventListener('click', function() {
        const message = messageInput.value;
        socket.send(JSON.stringify({
            'message': message,
            'username': username
        }));
        messageInput.value = '';
    });
});
