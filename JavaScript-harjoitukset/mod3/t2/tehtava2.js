const maara = Number(prompt('Osallistujien määrä:'));
const nimet = [];
for (let i = 0; i < maara; i++) nimet.push(prompt(`Osallistujan ${i + 1} nimi:`));
nimet.sort((a, b) => a.localeCompare(b, 'fi'));
const lista = document.querySelector('#target');
for (const nimi of nimet) {
  const li = document.createElement('li');
  li.textContent = nimi;
  lista.appendChild(li);
}
