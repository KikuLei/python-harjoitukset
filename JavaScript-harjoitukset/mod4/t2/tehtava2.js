const target = document.querySelector('#target');
for (const text of ['First item', 'Second item', 'Third item']) {
  const li = document.createElement('li');
  li.textContent = text;
  target.appendChild(li);
}
target.children[1].classList.add('my-item');
