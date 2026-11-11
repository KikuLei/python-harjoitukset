function heitaNoppaa() {
  return Math.floor(Math.random() * 6) + 1;
}
const lista = document.querySelector('#target');
let tulos;
do {
  tulos = heitaNoppaa();
  const li = document.createElement('li');
  li.textContent = tulos;
  lista.appendChild(li);
} while (tulos !== 6);
