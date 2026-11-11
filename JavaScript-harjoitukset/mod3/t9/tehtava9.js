function even(taulukko) {
  const parilliset = [];
  for (const luku of taulukko) if (luku % 2 === 0) parilliset.push(luku);
  return parilliset;
}
const alkuperainen = [2, 7, 4, 9, 12, 3];
const parilliset = even(alkuperainen);
console.log('Alkuperäinen:', alkuperainen);
console.log('Parilliset:', parilliset);
