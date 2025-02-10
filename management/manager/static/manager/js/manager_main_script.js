//reset form
function resetForm() {
  const addRoomForm = document.querySelector('#reception-section form');
  if (addRoomForm) addRoomForm.reset();
}

// Tabs switching
function hideAllSections() {
  document.getElementById('home-section').style.display = 'none';
  document.getElementById('employees-section').style.display = 'none';
  document.getElementById('reception-section').style.display = 'none';
  document.getElementById('reports-section').style.display = 'none';

  //reset form on tab switching
  resetForm();

}

function highlightActiveLink(linkId) {
  document.querySelectorAll('.nav-links li a').forEach(link => link.classList.remove('active'));
  document.getElementById(linkId).classList.add('active');
}

//show sections
function showHome() {
  hideAllSections();
  document.getElementById('home-section').style.display = 'block';
  document.getElementById('info-section').style.display = 'block';
}

function showEmployees() {
  hideAllSections();
  document.getElementById('employees-section').style.display = 'block';
}

function showReception() {
  hideAllSections();
  document.getElementById('reception-section').style.display = 'block';
}


function showReports() {
  hideAllSections();
  document.getElementById('reports-section').style.display = 'block';
}

// switching event listner
const home_link = 'home-link';
document.getElementById(home_link).addEventListener('click', function(event) {
  event.preventDefault();
  showHome();
  highlightActiveLink(home_link);
  saveActiveSection(home_link);
});

const employees_link = 'employees-link';
document.getElementById(employees_link).addEventListener('click', function(event) {
  event.preventDefault();
  showEmployees();
  highlightActiveLink(employees_link);
  saveActiveSection(employees_link);
});

const reception_link = 'reception-link';
document.getElementById(reception_link).addEventListener('click', function(event) {
  event.preventDefault();
  showReception();
  highlightActiveLink(reception_link);
  saveActiveSection(reception_link);
});

const reports_link = 'reports-link';
document.getElementById(reports_link).addEventListener('click', function(event) {
  event.preventDefault();
  showReports();
  highlightActiveLink(reports_link);
  saveActiveSection(reports_link);
});

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
  else if (activeSection === employees_link) showEmployees();
  else if (activeSection === reception_link) showReception();
  else if (activeSection === reports_link) showReports();

  //reset form on reload
  resetForm();
};
