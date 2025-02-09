document.addEventListener("DOMContentLoaded", function() {
  let messageContainer = document.getElementById("checkout-message-container");
  if (messageContainer) {
    let messages = messageContainer.getElementsByClassName("alert-message");

    for (let message of messages) {
      alert(message.innerHTML);
    }
  }
});
