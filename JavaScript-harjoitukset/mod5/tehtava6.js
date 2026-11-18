'use strict';

const form = document.querySelector('form');
const results = document.querySelector('#results');

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const query = document.querySelector('#query').value;

    results.innerHTML = '';

    try {
        const response = await fetch(
            `https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(query)}`
        );

        const data = await response.json();

        for (const joke of data.result) {
            const article = document.createElement('article');
            const paragraph = document.createElement('p');

            paragraph.textContent = joke.value;

            article.appendChild(paragraph);
            results.appendChild(article);
        }

    } catch (error) {
        console.log(error);
    }
});