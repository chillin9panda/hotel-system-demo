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
