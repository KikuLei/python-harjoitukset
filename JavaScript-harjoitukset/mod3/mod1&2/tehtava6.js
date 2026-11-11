const vastaus = confirm("Haluatko laskeaneliöjuuren?");
if (vastaus) {
    const luku = Number(prompt("Anna luku:"));
    if (luku < 0) {
        document.querySelector("h1").textContent =
        "Negatiivisen luvun neliöjuurta ei voida laskea.";
    } else {
        const neliöjuuri = Math.sqrt(luku);
        document.querySelector("h1").textContent =
        "Luvun " + luku + " neliöjuuri on " + neliöjuuri;
    }
}