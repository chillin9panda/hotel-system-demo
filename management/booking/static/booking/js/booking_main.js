// Function to show the Home section
function showHome() {
    hideAllSections();  // Hide all sections first
    document.getElementById('home-section').style.display = 'block';  // Show the Home section
    document.getElementById('info-section').style.display = 'block';  // Show the Info Section (Room Status & Search)
}

// Function to show the Book Room section
function showBookRoom() {
    hideAllSections();  // Hide all sections first
    document.getElementById('book-room-section').style.display = 'block';  // Show the Book Room section
}

// Function to hide all sections
function hideAllSections() {
    document.getElementById('home-section').style.display = 'none';  // Hide Home section
    document.getElementById('info-section').style.display = 'none';  // Hide Info section
    document.getElementById('book-room-section').style.display = 'none';  // Hide Book Room section
}

// Event Listeners for navigation links
document.getElementById('home-link').addEventListener('click', function (event) {
    event.preventDefault();  // Prevent default anchor click behavior
    showHome();  // Show Home Section
});

document.getElementById('book-room-link').addEventListener('click', function (event) {
    event.preventDefault();  // Prevent default anchor click behavior
    showBookRoom();  // Show Book Room Section
});

document.getElementById('view-rooms-link').addEventListener('click', function (event) {
    event.preventDefault();  // Prevent default anchor click behavior
    showHome();  // Show Home Section
});

// Set the default section to show (Home) when the page loads
window.onload = showHome;
