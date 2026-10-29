const alku = Number(prompt("Anna aloitusvuosi:"));

const loppu = Number(prompt("Anna lopetusvuosi:"));

const lista = document.querySelector("#vuodet");

for (let vuosi = alku; vuosi <= loppu; vuosi++) {

    if (vuosi % 4 === 0 && (vuosi % 100 !== 0 || vuosi % 400 === 0)) {

        const li = document.createElement("li");

        li.textContent = vuosi;

        lista.appendChild(li);

    }

}