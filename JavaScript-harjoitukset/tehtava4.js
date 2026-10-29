const nimi = prompt("Mikä sinun nimesi on?");

const tupa = Math.floor(Math.random() * 4) + 1;

let tuvanNimi;

if (tupa === 1) {

    tuvanNimi = "Gryffindor";

} else if (tupa === 2) {

    tuvanNimi = "Slytherin";

} else if (tupa === 3) {

    tuvanNimi = "Hufflepuff";

} else {

    tuvanNimi = "Ravenclaw";

}

document.querySelector("h1").textContent =

    nimi + ", you are " + tuvanNimi + ".";