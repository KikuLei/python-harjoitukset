document.querySelector('#calculate').addEventListener('click', () => {
  const expression = document.querySelector('#calculation').value.replace(/\s/g, '');
  const match = expression.match(/^(-?\d+)([+*/-])(-?\d+)$/);
  const output = document.querySelector('#result');
  if (!match) { output.textContent = 'Virheellinen lasku'; return; }
  const a = Number(match[1]);
  const operator = match[2];
  const b = Number(match[3]);
  let result;
  if (operator === '+') result = a + b;
  else if (operator === '-') result = a - b;
  else if (operator === '*') result = a * b;
  else result = b === 0 ? 'Ei voi jakaa nollalla' : a / b;
  output.textContent = result;
});
