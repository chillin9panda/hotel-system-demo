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

//show view rooms section
function showViewRooms() {
  hideAllSections();
  document.getElementById('view-rooms-section').style.display = 'block';
}


function showSearchResults() {
  hideAllSections();
  document.getElementById('search-results-section').style.display = 'block';
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
  document.getElementById('search-results-section').style.display = 'none';

  resetForm();
}

//Highlight Active tab
function highlightActiveLink(linkId) {
  document.querySelectorAll('.nav-links li a').forEach(link => link.classList.remove('active'));
  document.getElementById(linkId).classList.add('active');
}

//Save active section for reload
function saveActiveSection(section) {
  localStorage.setItem('activeSection', section);
}

// switch tabs
const search = 'search';
document.getElementById('search').addEventListener('click', function(event) {
  event.preventDefault();
  showSearchResults();
  saveActiveSection(search);
});

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
  else if (activeSection === view_rooms_link) showViewRooms();
  else if (activeSection == search) showSearchResults();
};

// Submit search with icon 
function validateAndSubmitSearch(icon) {

  let form = icon.closest('form');
  let input = form.querySelector('input[name="phone_number"]');

  if (input.value.trim() === "") {
    alert("Enter a phone number to search.");
    return;
  }

  form.submit();
}


// returning home after searching 
document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", function(event) {
      if (link.classList.contains("logout-btn")) {
        return;
      }

      event.preventDefault();

      if (window.location.pathname !== "/booking/") {
        window.location.href = "/booking/";
      }
    });
  });
});
