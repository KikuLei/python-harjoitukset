const nopat = Number(prompt("Kuinka monta noppaa heitetään?"));

const tavoite = Number(prompt("Mikä silmälukujen summa halutaan?"));

let onnistumiset = 0;

const heitot = 10000;

for (let i = 0; i < heitot; i++) {

    let summa = 0;

    for (let j = 0; j < nopat; j++) {

        const noppa = Math.floor(Math.random() * 6) + 1;

        summa += noppa;

    }

    if (summa === tavoite) {

        onnistumiset++;

    }

}

const todennakoisyys = (onnistumiset / heitot) * 100;

document.querySelector("#tulos").textContent =

    "Todennäköisyys saada summa " + tavoite +

    " on " + todennakoisyys.toFixed(2) + "%.";