
//this function is to leave a message when the user click on the button//

let button = document.querySelector('.button2')

function confirm(msg) {
    alert(msg)
}

button.addEventListener('click', confirm)