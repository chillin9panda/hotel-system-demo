const currentDate = new Date();

const formattedDate = currentDate.toLocaleDateString('en-US', {
  weekday: 'long',
  year: 'numeric',
  month: 'long',
  day: 'numeric'
});

document.getElementById('current-date').textContent = formattedDate;
