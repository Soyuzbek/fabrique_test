django.jQuery(document).ready(() => {
    let kinds = document.getElementsByClassName('field-kind')
    let options = document.getElementsByClassName('field-options')
    Array.from(kinds).forEach((kind) => {
        if (kind.querySelector('select').value === 'text') {
            kind.closest('.form-row').querySelector('.field-options').classList.add('opacity')
        }
        kind.addEventListener('change', (event) => {
            if (kind.querySelector('select').value === 'text') {
                kind.closest('.form-row').querySelector('.field-options').classList.add('opacity')
            } else {
                kind.closest('.form-row').querySelector('.field-options').classList.remove('opacity')
            }
        })
    });
})