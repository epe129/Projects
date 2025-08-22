function move() {
    const button = document.getElementById('btn');
    const randomX = Math.floor(Math.random() * (window.innerWidth - button.offsetWidth));
    const randomY = Math.floor(Math.random() * (window.innerHeight - button.offsetHeight));
    
    button.style.position = 'absolute';
    button.style.left = `${randomX}px`;
    button.style.top = `${randomY}px`;
}

