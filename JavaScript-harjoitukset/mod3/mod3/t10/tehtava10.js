const ehdokkaidenMaara = Number(prompt('Ehdokkaiden määrä:'));
const ehdokkaat = [];
for (let i = 0; i < ehdokkaidenMaara; i++) {
  ehdokkaat.push({name: prompt(`Ehdokkaan ${i + 1} nimi:`), votes: 0});
}
const aanestajienMaara = Number(prompt('Äänestäjien määrä:'));
for (let i = 0; i < aanestajienMaara; i++) {
  const nimi = prompt(`Äänestäjä ${i + 1}: ketä äänestät? (tyhjä = tyhjä ääni)`);
  if (!nimi) continue;
  const ehdokas = ehdokkaat.find(e => e.name.toLowerCase() === nimi.trim().toLowerCase());
  if (ehdokas) ehdokas.votes++;
  else console.log(`Tuntematon ehdokas: ${nimi}`);
}
ehdokkaat.sort((a, b) => b.votes - a.votes);
if (ehdokkaat.length) console.log(`The winner is ${ehdokkaat[0].name} with ${ehdokkaat[0].votes} votes.`);
console.log('results:');
for (const e of ehdokkaat) console.log(`${e.name}: ${e.votes} votes`);
