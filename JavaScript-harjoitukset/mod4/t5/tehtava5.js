const picArray = [
  {title: 'Kuva 1', caption: 'Ensimmäinen kuva', description: 'Ensimmäisen kuvan kuvaus.', medium: '../assets/pic1-medium.svg', large: '../assets/pic1-large.svg'},
  {title: 'Kuva 2', caption: 'Toinen kuva', description: 'Toisen kuvan kuvaus.', medium: '../assets/pic2-medium.svg', large: '../assets/pic2-large.svg'},
  {title: 'Kuva 3', caption: 'Kolmas kuva', description: 'Kolmannen kuvan kuvaus.', medium: '../assets/pic3-medium.svg', large: '../assets/pic3-large.svg'}
];
const section = document.querySelector('#target');
for (const pic of picArray) {
  const article = document.createElement('article');
  const heading = document.createElement('h2');
  heading.textContent = pic.title;
  const figure = document.createElement('figure');
  const img = document.createElement('img');
  img.src = pic.medium;
  img.alt = pic.title;
  const caption = document.createElement('figcaption');
  caption.textContent = pic.caption;
  figure.append(img, caption);
  const description = document.createElement('p');
  description.textContent = pic.description;
  article.append(heading, figure, description);
  section.appendChild(article);
}
