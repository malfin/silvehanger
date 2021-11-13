window.onload = function (ev) {

    if (document.location.pathname === '/account/register/') {
        let firstStep = document.querySelector('.register_form_first_step');
        let secondStep = document.querySelector('.register_form_second_step');

        let nextButton = document.querySelector('.button_next_step');
        nextButton.addEventListener('click', function (ev) {
            firstStep.setAttribute('hidden', 'true');
            secondStep.removeAttribute('hidden');
        });
    }
};