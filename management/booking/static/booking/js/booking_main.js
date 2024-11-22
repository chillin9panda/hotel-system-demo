//show the Home section
function showHome() {
    hideAllSections(); 
    document.getElementById('home-section').style.display = 'block';
    document.getElementById('info-section').style.display = 'block';
}

// show the Book Room section
function showBookRoom() {
    hideAllSections(); 
    document.getElementById('book-room-section').style.display = 'block';
}

//show view rooms section
function showViewRooms() {
	hideAllSections();
	document.getElementById('view-rooms-section').style.display = 'block';
}

// Function to hide all sections
function hideAllSections() {
    document.getElementById('home-section').style.display = 'none';  // Hide Home section
    document.getElementById('info-section').style.display = 'none';  // Hide Info section
    document.getElementById('book-room-section').style.display = 'none';  // Hide Book Room section
    document.getElementById('view-rooms-section').style.display = 'none'; // Hide View Rooms section
}

// Event Listeners for navigation links
document.getElementById('home-link').addEventListener('click', function (event) {
    event.preventDefault();
    showHome();
});

document.getElementById('book-room-link').addEventListener('click', function (event) {
    event.preventDefault();
    showBookRoom();
});

document.getElementById('view-rooms-link').addEventListener('click', function (event) {
    event.preventDefault();
    showViewRooms();
});

//Dynamic section for mobile banking payment method
document.getElementById("payment-method").addEventListener("change", function() {
	const paymentMethod = this.value;
	const mobileBankingFields = document.getElementById("mobile-banking-fields");
	
	if ("mobile-banking" === paymentMethod){
		mobileBankingFields.style.display = "block";
	} else {
		mobileBankingFields.style.display = "none";
	}

	document.getElementById("bank-name").value = ""; 
	document.getElementById("transaction-id").value = "";
});

// Set the default section to show (Home) when the page loads
window.onload = showHome;
