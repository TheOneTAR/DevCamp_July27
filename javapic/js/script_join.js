// A login form that won’t let users continue until their inputs are correct
// Make tagline Develop something beautiful, {name}

var form = document.getElementById("signup");
var inputs = document.getElementsByTagName("input");
var nameInput = document.querySelector("input[name=name]")
var username = document.querySelector("input[name=username]")
var email = document.querySelector("input[type=email]")

nameInput.addEventListener("blur", function(){ checkName(); });
username.addEventListener("blur", function(){ checkUsername(); });
email.addEventListener("blur", function(){ checkEmail(); });

function checkName() {
  if (nameInput.value.length < 2) {
    alert('Please provide a name of two or more characters.')
    nameInput.focus;
  }
}

function checkUsername() {
  if (username.value.length < 2) {
    alert('Please provide a username of two or more characters.')
  username.focus;
  }
}

function checkEmail() {
  var valid = /[^@]+@[^@].+/;
  if (!valid.test(email.value)) {
    alert('Please provide a valid email address.\n' +
      'yourEmail@place.com');
    email.focus;
  }
}

