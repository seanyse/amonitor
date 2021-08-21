
document.addEventListener('DOMContentLoaded', function() {
    
    window.resizeTo(1025, 525);
}, false);

eel.expose(authenticate)
function authenticate() {
    setButton("Validating")
    key = document.getElementById("key").value;
    eel.auth(key)
}

eel.expose(print)
function printnow(print){
    eel.printnow(print);
}

eel.expose(setButton)
function setButton(status) {
    var element = document.getElementById("submit");
    element.innerHTML = status;
}
eel.expose(create)
function create() {
    window.location.href = 'index.html';
}



// function startApp(){

// }