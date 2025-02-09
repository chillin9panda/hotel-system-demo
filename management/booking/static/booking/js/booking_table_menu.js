document.addEventListener("DOMContentLoaded", function() {
  function toggleMenu(event, menuId) {
    event.preventDefault();
    let menu = document.getElementById(menuId);

    document.querySelectorAll('.booking-menu').forEach(m => {
      if (m !== menu) {
        m.style.display = "none";
      }
    });

    menu.style.display = (menu.style.display === "block") ? "none" : "block";
  }


  function addMenuToggleListener(selector, menuPrefix) {
    document.querySelectorAll(selector).forEach(link => {
      link.addEventListener("click", function(event) {
        let bookingId = this.getAttribute("data-booking-id");
        toggleMenu(event, `${menuPrefix}${bookingId}`);
      });
    });
  }

  addMenuToggleListener(".edit-booking-link", "booking-menu_");
  addMenuToggleListener(".booking-status-link", "status-menu_");



  document.addEventListener("click", function(event) {
    if (!event.target.closest(".edit-booking-link, .booking-status-link, .booking-menu")) {
      document.querySelectorAll(".booking-menu").forEach(menu => {
        menu.style.display = "none";
      });
    }
  });
});

