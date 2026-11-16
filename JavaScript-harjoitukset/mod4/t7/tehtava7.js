const trigger = document.querySelector('#trigger');
const target = document.querySelector('#target');
trigger.addEventListener('mouseenter', () => target.src = '../assets/pic2-medium.svg');
trigger.addEventListener('mouseleave', () => target.src = '../assets/pic1-medium.svg');
