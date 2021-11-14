window.onload = function (ev) {

    if (document.location.pathname === '/account/register/') {
        let slide = 1;
        let firstStep = document.querySelector('.register_form_first_step');
        let secondStep = document.querySelector('.register_form_second_step');
        let thirdStep = document.querySelector('.register_form_third_step');
        let stepBlock = document.querySelector('.form-title_step');

        let nextButtons = document.querySelectorAll('.button_next_step');
        let backButtons = document.querySelectorAll('.button_back_step');
        let registerButton = document.querySelector('.button_register');
        nextButtons.forEach(function (nextButton) {
            nextButton.addEventListener('click', function (ev) {
                if (firstStep.classList.contains('dis_block') && secondStep.classList.contains('dis_none') && thirdStep.classList.contains('dis_none')) {
                    firstStep.classList.remove('dis_block');
                    firstStep.classList.add('dis_none');
                    secondStep.classList.remove('dis_none');
                    secondStep.classList.add('dis_block');
                    stepBlock.innerText = '2/3';
                } else if (firstStep.classList.contains('dis_none') && secondStep.classList.contains('dis_block') && thirdStep.classList.contains('dis_none')) {
                    secondStep.classList.remove('dis_block');
                    secondStep.classList.add('dis_none');
                    thirdStep.classList.remove('dis_none');
                    thirdStep.classList.add('dis_block');
                    stepBlock.innerText = '3/3';
                }
            });
        });
        backButtons.forEach(function (backButton) {
            backButton.addEventListener('click', function (ev) {
                if (firstStep.classList.contains('dis_none') && secondStep.classList.contains('dis_block') && thirdStep.classList.contains('dis_none')) {
                    firstStep.classList.remove('dis_none');
                    firstStep.classList.add('dis_block');
                    secondStep.classList.remove('dis_block');
                    secondStep.classList.add('dis_none');
                    stepBlock.innerText = '1/3';
                } else if (firstStep.classList.contains('dis_none') && secondStep.classList.contains('dis_none') && thirdStep.classList.contains('dis_block')) {
                    secondStep.classList.remove('dis_none');
                    secondStep.classList.add('dis_block');
                    thirdStep.classList.remove('dis_block');
                    thirdStep.classList.add('dis_none');
                    stepBlock.innerText = '2/3';
                }
            });
        });


        registerButton.addEventListener('click', function (ev) {
            document.querySelector('.true_button_register').click();
        });
    }
    if (document.location.pathname === '/account/login/') {
        let registerButton = document.querySelector('.button_register');
        registerButton.addEventListener('click', function (ev) {
            document.querySelector('.true_button_register').click();
        });
    }

};
$(document).ready(function () {
    $('select[name="users_volonter"]').select2({
        placeholder: 'Выберите...',
        maximumSelectionLength: 7,
    });
    if ($('input[name="username"]')) {

    }
});