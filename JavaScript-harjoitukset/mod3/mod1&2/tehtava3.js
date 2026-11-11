const luku1 = Number(prompt("Anna ensimmäinen kokonaisluku:"));

const luku2 = Number(prompt("Anna toinen kokonaisluku:"));

const luku3 = Number(prompt("Anna kolmas kokonaisluku:"));

const summa = luku1 + luku2 + luku3;

const tulo = luku1 * luku2 * luku3;

const keskiarvo = summa / 3;

document.querySelector("h1").textContent =

    "Summa: " + summa +

    ", Tulo: " + tulo +

    ", Keskiarvo: " + keskiarvo;