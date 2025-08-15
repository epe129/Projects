document.getElementById('fontInput').addEventListener('input', function() {
    document.getElementById('fontInput').style.display = 'none';
    
    const displayElements = document.getElementsByClassName('fontDisplay');
    const inputValue = this.value;
    
    for (let element of displayElements) {
        element.textContent = inputValue;
    }
});