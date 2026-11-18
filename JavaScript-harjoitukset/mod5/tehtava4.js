'use strict';

const form = document.querySelector('form');
const results = document.querySelector('#results');

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const query = document.querySelector('#query').value;

    results.innerHTML = '';

    try {
        const response = await fetch(
            `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`
        );

        const data = await response.json();

        for (const item of data) {
            const show = item.show;

            const article = document.createElement('article');

            const title = document.createElement('h2');
            title.textContent = show.name;

            const link = document.createElement('a');
            link.href = show.url;
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
            link.textContent = 'Lisätietoja';

            const image = document.createElement('img');

            image.src = show.image
                ? show.image.medium
                : 'https://placehold.co/210x295?text=Not%20Found';

            image.alt = show.name;

            const summary = document.createElement('div');
            summary.innerHTML = show.summary || '';

            article.appendChild(title);
            article.appendChild(link);
            article.appendChild(image);
            article.appendChild(summary);

            results.appendChild(article);
        }

    } catch (error) {
        console.log(error);
    }
});