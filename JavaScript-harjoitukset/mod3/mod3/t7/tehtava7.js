function heitaNoppaa(tahkot) {
  return Math.floor(Math.random() * tahkot) + 1;
}
const tahkot = Number(prompt('Montako tahkoa nopassa on?'));
if (!Number.isInteger(tahkot) || tahkot < 2) {
  alert('Anna kokonaisluku, joka on vähintään 2.');
} else {
  const lista = document.querySelector('#target');
  let tulos;
  do {
    tulos = heitaNoppaa(tahkot);
    const li = document.createElement('li');
    li.textContent = tulos;
    lista.appendChild(li);
  } while (tulos !== tahkot);
}
