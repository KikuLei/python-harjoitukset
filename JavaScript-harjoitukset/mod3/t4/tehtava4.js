const luvut = [];
while (true) {
  const luku = Number(prompt('Anna luku (0 lopettaa):'));
  if (luku === 0) break;
  luvut.push(luku);
}
luvut.sort((a, b) => b - a);
console.log(luvut);
