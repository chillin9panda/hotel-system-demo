// payment table
document.addEventListener("DOMContentLoaded", function() {
  //Seect all rows  
  document.querySelectorAll(".listing-table tbody tr").forEach(row => {
    row.addEventListener("click", function() {
      let cells = this.getElementsByTagName("td");

      //Values
      let payment_for = cells[1].innerText;

      let service_name = cells[2].innerText;
      let amount = cells[3].innerText;

      const payment_status = row.cells[4].textContent.trim();


      // pass the data to span tags
      document.getElementById("amount").innerText = amount;
      document.getElementById("service-name").innerText = service_name;


      //Clear past values for hidden input 
      document.getElementById("service-payment-id").value = "";
      document.getElementById("booking-payment-id").value = "";
      document.getElementById("payment-type").value = "";
      document.getElementById("payment-id").value = ""

      // Assign the values
      if (payment_for === "Service") {
        document.getElementById("payment-id").value = this.getAttribute("data-service-payment-id");
      } else if (payment_for === "Booking") {
        document.getElementById("payment-id").value = this.getAttribute("data-booking-payment-id");
      }

      document.getElementById("payment-type").value = payment_for;
      document.getElementById("payment-amount").value = amount;

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
});

