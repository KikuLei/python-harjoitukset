document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault();
  const first = document.querySelector('input[name="firstname"]').value;
  const last = document.querySelector('input[name="lastname"]').value;
  document.querySelector('#target').textContent = `Your name is ${first} ${last}`;
});
