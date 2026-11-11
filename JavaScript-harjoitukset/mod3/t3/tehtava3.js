const koirat = [];
for (let i = 0; i < 6; i++) koirat.push(prompt(`Koiran ${i + 1} nimi:`));
koirat.sort((a, b) => b.localeCompare(a, 'fi'));
const lista = document.querySelector('#target');
for (const koira of koirat) {
  const li = document.createElement('li');
  li.textContent = koira;
  lista.appendChild(li);
}
