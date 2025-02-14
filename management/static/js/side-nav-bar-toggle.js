document.addEventListener("DOMContentLoaded", function() {
  const menuToggle = document.getElementById("side-menu-toggle");
  const sideNav = document.getElementById("side-nav");

  menuToggle.addEventListener("click", function() {
    sideNav.classList.toggle("open");
  });

  document.addEventListener("click", function(event) {
    if (!sideNav.contains(event.target) && event.target !== menuToggle) {
      sideNav.classList.remove("open");
    }
  });
});
