const luku = Number(prompt("Anna kokonaisluku:"));

let alkuluku = true;

if (luku < 2) {

    alkuluku = false;

}

for (let i = 2; i < luku; i++) {

    if (luku % i === 0) {

        alkuluku = false;

        break;

    }

}

if (alkuluku) {

    document.querySelector("#tulos").textContent =

        luku + " on alkuluku.";

} else {

    document.querySelector("#tulos").textContent =

        luku + " ei ole alkuluku.";

}