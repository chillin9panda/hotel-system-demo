// Select the elements
const homeLink = document.getElementById('home-link');
const roomStatusLink = document.getElementById('room-status-link');
const searchBookingLink = document.getElementById('search-booking-link');
const bookRoomLink = document.getElementById('book-room-link'); // Book Room link
const contentWrapper = document.getElementById('content-wrapper');
const currentDate = document.getElementById('current-date');

// Select sections within the content wrapper
const roomStatusSection = document.querySelector('.status-overview');
const searchSection = document.querySelector('.search');
const bookRoomSection = document.querySelector('.book-room'); // Book Room section

// Function to show the content wrapper and set the current date
function showContentWrapper() {
    contentWrapper.style.display = 'block';
    const date = new Date().toLocaleDateString();
    currentDate.textContent = date;
}

// Function to hide the content wrapper
function hideContentWrapper() {
    contentWrapper.style.display = 'none';
}

// Show specific sections
function showRoomStatus() {
    roomStatusSection.style.display = 'block';
    searchSection.style.display = 'block';
    bookRoomSection.style.display = 'none'; // Hide Book Room
}

function showSearchBooking() {
    roomStatusSection.style.display = 'none';
    searchSection.style.display = 'block';
    bookRoomSection.style.display = 'none'; // Hide Book Room
}

function showBookRoom() {
    roomStatusSection.style.display = 'none';
    searchSection.style.display = 'none';
    bookRoomSection.style.display = 'block'; // Show Book Room
}

// Add event listeners to the navigation links
homeLink.addEventListener('click', function() {
    hideContentWrapper();
});

roomStatusLink.addEventListener('click', function() {
    showContentWrapper();
    showRoomStatus();
});

searchBookingLink.addEventListener('click', function() {
    showContentWrapper();
    showSearchBooking();
});

bookRoomLink.addEventListener('click', function() {
    showContentWrapper();
    showBookRoom();
});
