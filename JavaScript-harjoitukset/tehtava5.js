const vuosi = Number(prompt("Anna vuosiluku:"));

if (vuosi % 4 === 0 && (vuosi % 100 !== 0 || vuosi % 400 === 0)) {

    document.querySelector("h1").textContent =

        vuosi + " on karkausvuosi.";

} else {

    document.querySelector("h1").textContent =

        vuosi + " ei ole karkausvuosi.";

}