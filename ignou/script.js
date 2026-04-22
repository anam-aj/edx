    document.getElementById('admissionForm').addEventListener('submit', function(event) {
    // 1. Get all the values from the form inputs
    const name = document.getElementById('candidateName').value.trim();
    const motherName = document.getElementById('motherName').value.trim();
    const subject = document.getElementById('subject').value;
    const fee = document.getElementById('fee').value.trim();
    const background = document.getElementById('background').value.trim();

    // Check if either the Yes or No radio button is selected
    const regYes = document.getElementById('regYes').checked;
    const regNo = document.getElementById('regNo').checked;

    // 2. Validate that none of the fields are empty
    if (name === "" || motherName === "" || subject === "" || fee === "" || background === "" || (!regYes && !regNo)) {

        // Alert the user and stop the form from submitting
        alert("Validation Error: Please fill out all fields before submitting.");
        event.preventDefault();

    } else {
        // If everything is filled out, show a success message
        alert("Form successfully completed!");

        // Note: For demonstration purposes in your viva, I am preventing the default submission
        // so the page doesn't instantly refresh, allowing the examiner to see your completed form.
        event.preventDefault();
    }
});
