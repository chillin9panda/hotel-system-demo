document.addEventListener("DOMContentLoaded", function() {
  //Seect all rows  
  document.querySelectorAll(".listing-table tbody tr").forEach(row => {
    row.addEventListener("click", function() {
      let cells = this.getElementsByTagName("td");

      //Values
      let type = cells[1].innerText;
      let service = cells[2].innerText;
      let amount = cells[3].innerText;

      document.getElementById("process-service-name").innerText = service;
      document.getElementById("process-amount").innerText = amount;

      const payment_status = row.cells[4].textContent.trim();

      if (payment_status === "Paid") {
        alert("This Service/Booking is already paid for!");
      } else {
        const payments_section = document.getElementById("payments-section");
        payments_section.style.display = "block";
      }

    });
  });
});




//Dynamic loading section for mobile banking payment method
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

