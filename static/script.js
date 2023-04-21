
const form = document.querySelector('form');
const input = document.querySelector('#name');
const submitButton = document.querySelector('input[type="submit"]');

submitButton.addEventListener('click', function(event) {
    if (input.value.trim() === '') {
        event.preventDefault();
        input.classList.add('error');
    } else {
        input.classList.remove('error');
    }
});
