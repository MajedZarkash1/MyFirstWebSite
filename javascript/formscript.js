// this function to submit the form if every thing in the form done well like the password is matching//

function handleSubmit(event) {

    event.preventDefault(); // Prevent form submission to see the alert

    let password = document.getElementById('password').value;
    let cpassword = document.getElementById('cpassword').value;

    if (password !== cpassword){
        alert('the password is not matching');
        return;
    } 




    alert("Thank you!");




}




