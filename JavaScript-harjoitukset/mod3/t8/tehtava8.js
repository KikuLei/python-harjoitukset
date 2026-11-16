function concat(taulukko) {
  let tulos = '';
  for (const sana of taulukko) tulos += sana;
  return tulos;
}
const nimet = ['Johnny', 'DeeDee', 'Joey', 'Marky'];
document.querySelector('#target').textContent = concat(nimet);
