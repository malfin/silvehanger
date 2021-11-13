window.onload = function (ev) {

    if (document.location.pathname === '/account/register/') {
        let firstStep = document.querySelector('.register_form_first_step');
        let secondStep = document.querySelector('.register_form_second_step');

        let nextButton = document.querySelector('.button_next_step');
        nextButton.addEventListener('click', function (ev) {
            if (firstStep.classList.contains('dis_block') && secondStep.classList.contains('dis_none')) {
                firstStep.classList.remove('dis_block');
                firstStep.classList.add('dis_none');
                secondStep.classList.remove('dis_none');
                secondStep.classList.add('dis_block');
            }
        });
    }
};