//Dynamic date
const currentDate = new Date();

const formattedDate = currentDate.toLocaleDateString('en-US', {
  weekday: 'long',
  year: 'numeric',
  month: 'long',
  day: 'numeric'
});

document.getElementById('current-date').textContent = formattedDate;

//show the Home section
function showHome() {
  hideAllSections();
  document.getElementById('home-section').style.display = 'block';
  document.getElementById('info-section').style.display = 'block';
}

//show bookings section
function showBookings() {
  hideAllSections();
  document.getElementById('bookings-section').style.display = 'block';
}

// show the Book Room section
function showBookRoom() {
  hideAllSections();
  document.getElementById('book-room-section').style.display = 'block';
}

//shoe payments section
function showPayment() {
  hideAllSections();
  document.getElementById('payments-section').style.display = 'block';
}

//show view rooms section
function showViewRooms() {
  hideAllSections();
  document.getElementById('view-rooms-section').style.display = 'block';
}


// clear form
function resetForm() {
  const createBookingForm = document.querySelector('#book-room-section form');
  if (createBookingForm) createBookingForm.reset();
}

// Function to hide all sections
function hideAllSections() {
  document.getElementById('home-section').style.display = 'none';  // Hide Home section
  document.getElementById('info-section').style.display = 'none';  // Hide Info section
  document.getElementById('book-room-section').style.display = 'none';  // Hide Book Room section
  document.getElementById('view-rooms-section').style.display = 'none'; // Hide View Rooms section
  document.getElementById('bookings-section').style.display = 'none';
  document.getElementById('payments-section').style.display = 'none';


  resetForm();
}

// Event Listeners for navigation links
const home_link = 'home-link';
document.getElementById(home_link).addEventListener('click', function(event) {
  event.preventDefault();
  showHome();
  highlightActiveLink(home_link);
  saveActiveSection(home_link);
});

const book_room_link = 'book-room-link';
document.getElementById(book_room_link).addEventListener('click', function(event) {
  event.preventDefault();
  showBookRoom();
  highlightActiveLink(book_room_link);
  saveActiveSection(book_room_link);
});

const view_rooms_link = 'view-rooms-link';
document.getElementById(view_rooms_link).addEventListener('click', function(event) {
  event.preventDefault();
  showViewRooms();
  highlightActiveLink(view_rooms_link);
  saveActiveSection(view_rooms_link);
});

const bookings_link = 'bookings-link';
document.getElementById(bookings_link).addEventListener('click', function(event) {
  event.preventDefault();
  showBookings();
  highlightActiveLink(bookings_link);
  saveActiveSection(bookings_link);
});

const payments_link = 'payments-link';
document.getElementById(payments_link).addEventListener('click', function(event) {
  event.preventDefault();
  showPayment();
  highlightActiveLink(payments_link);
  saveActiveSection(payments_link);
});


//Dynamic section for mobile banking payment method
document.getElementById("payment-method").addEventListener("change", function() {
  const paymentMethod = this.value;
  const mobileBankingFields = document.getElementById("mobile-banking-fields");

  if ("mobile-banking" === paymentMethod) {
    mobileBankingFields.style.display = "block";
  } else {
    mobileBankingFields.style.display = "none";
  }

  document.getElementById("bank-name").value = "";
  document.getElementById("transaction-id").value = "";
});

//Highlight Active tab
function highlightActiveLink(linkId) {
  document.querySelectorAll('.nav-links li a').forEach(link => link.classList.remove('active'));
  document.getElementById(linkId).classList.add('active');
}

//Save active section for reload
function saveActiveSection(section) {
  localStorage.setItem('activeSection', section);
}

//Logout btn event listner
document.querySelector('.logout-btn').addEventListener('click', function(event) {
  localStorage.clear();
});

//resore saved
window.onload = function() {
  const activeSection = localStorage.getItem('activeSection') || home_link;
  if (activeSection === home_link) showHome();
  else if (activeSection === bookings_link) showBookings();
  else if (activeSection === book_room_link) showBookRoom();
  else if (activeSection === payments_link) showPayment();
  else if (activeSection === view_rooms_link) showViewRooms();
};


