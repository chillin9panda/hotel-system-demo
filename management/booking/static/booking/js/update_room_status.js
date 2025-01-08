const RoomStatusSocket = new WebSocket('ws://' + window.location.host + '/ws/room_status/');

RoomStatusSocket.onmessage = function(event) {
    const data = JSON.parse(event.data);

    // Update room status when the message is received
    if (data.event === 'room_status_update') {  // assuming event is 'room_status_update'
        const room_number = data.room_number;
        const room_status = data.room_status;

        // Correctly using template literals for room number
        const roomElement = document.querySelector(`#room-${room_number}`);

        if (roomElement) {
            roomElement.textContent = `Status: ${room_status}`;
        }
    }
};

// Handle WebSocket closure
RoomStatusSocket.onclose = function() {
    console.log('WebSocket connection closed.');
};

// Handle WebSocket errors (optional)
RoomStatusSocket.onerror = function(error) {
    console.log('WebSocket error:', error);
};
