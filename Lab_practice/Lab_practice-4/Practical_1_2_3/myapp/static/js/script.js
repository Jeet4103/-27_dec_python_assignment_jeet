function validateForm() {
    const inputs = document.querySelectorAll('input, select, textarea');
    let valid = true;

    for (let input of inputs) {
        if (input.type !== 'submit' && input.type !== 'radio' && input.value.trim() === '') {
            alert("Please fill all the fields.");
            input.focus();
            return false;
        }
    }

    const email = document.querySelector('input[type="text"][size="50"]');
    const mobile = document.querySelector('input[type="text"][value="+91"]').nextElementSibling;

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email.value.trim())) {
        alert("Please enter a valid email.");
        email.focus();
        return false;
    }

    const mobilePattern = /^\d{10}$/;
    if (!mobilePattern.test(mobile.value.trim())) {
        alert("Please enter a valid 10-digit mobile number.");
        mobile.focus();
        return false;
    }

    return true;
}