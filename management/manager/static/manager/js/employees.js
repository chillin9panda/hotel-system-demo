document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll("tr[data-employee-id]").forEach(row => {
    row.addEventListener("click", function() {
      const employeeId = this.getAttribute("data-employee-id");
      window.location.href = 'employee/' + employeeId + '/';
    });
  });
});
