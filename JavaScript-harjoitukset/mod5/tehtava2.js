'use strict';

const form = document.querySelector('form');

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const query = document.querySelector('#query').value;

    try {
        const response = await fetch(
            `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`
        );

        const data = await response.json();

        console.log(data);

    } catch (error) {
        console.log(error);
    }
});