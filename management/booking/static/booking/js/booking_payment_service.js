document.addEventListener("DOMContentLoaded", function() {
  function toggleMenu(event, bookingId) {
    event.preventDefault();
    let menu = document.getElementById("menu_" + bookingId);

    document.querySelectorAll('.booking-menu').forEach(m => {
      if (m !== menu)
        m.style.display = 'none';
    });

    menu.style.display = menu.style.display === "block" ? "none" : "block"
  }

  document.querySelectorAll(".edit-booking-link").forEach(link => {
    link.addEventListener("click", function(event) {
      let bookingId = this.getAttribute("data-booking-id");
      toggleMenu(event, bookingId);
    });
  });

  document.addEventListener("click", function(event) {
    let isClickInside = event.target.closest(".edit-booking-link, .booking-menu");

    if (!isClickInside) {
      document.querySelectorAll(".booking-menu").forEach(menu => {
        menu.style.display = "none";
      });
    }
  });
});
