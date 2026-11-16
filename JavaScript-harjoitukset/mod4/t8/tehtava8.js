document.querySelector('#calculate').addEventListener('click', () => {
  const a = Number(document.querySelector('#num1').value);
  const b = Number(document.querySelector('#num2').value);
  const operation = document.querySelector('#operation').value;
  let result;
  switch (operation) {
    case 'add': result = a + b; break;
    case 'sub': result = a - b; break;
    case 'multi': result = a * b; break;
    case 'div': result = b === 0 ? 'Ei voi jakaa nollalla' : a / b; break;
  }
  document.querySelector('#result').textContent = result;
});
