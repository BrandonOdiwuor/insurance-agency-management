function activateModal(elemID) {
    let elem = document.getElementById(elemID);
    elem.classList.add('is-active');
}

function deactivateModal(elemID) {
    let elem = document.getElementById(elemID);
    elem.classList.remove('is-active');
}

function updateFormInput(inputID, value) {
    let elem = document.getElementById(inputID);
    elem.value = value;
}

function updatePaymentFormModal(modalID, inputID, value) {
    activateModal(modalID);
    updateFormInput(inputID, value);
}