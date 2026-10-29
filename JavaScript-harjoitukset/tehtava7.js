const maara = Number(prompt("Kuinka monta noppaa heitetään?"));

let summa = 0;

for (let i = 0; i < maara; i++) {

    const noppa = Math.floor(Math.random() * 6) + 1;

    summa = summa + noppa;

}

document.querySelector("h1").textContent =

    "Noppien silmälukujen summa on " + summa;