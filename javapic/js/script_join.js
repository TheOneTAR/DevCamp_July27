// A login form that won’t let users continue until their inputs are correct

var form = document.getElementById("signup");
var nameInput = document.querySelector("[name=name]");
var username = document.querySelector("[name=username]");
var email = document.querySelector("[type=email]");

nameInput.addEventListener("blur", function(){ checkName(); });
username.addEventListener("blur", function(){ checkUsername(); });
email.addEventListener("blur", function(){ checkEmail(); });

function checkName() {
  if (nameInput.value.length < 2) {
    alert('Please provide a name of two or more characters.');
    nameInput.focus;
    return false
  }
  return true
}
function checkUsername() {
  if (username.value.length < 2) {
    alert('Please provide a username of two or more characters.');querySelector("span[class=tagline]");
    username.focus;
    return false
  }
  return true
}
function checkEmail() {
  var valid = /[^@]+@[^@].+/;
  if (!valid.test(email.value)) {
    alert('Please provide a valid email address.\n' +
      'yourEmail@place.com');
    email.focus;
    return false
  }
  return true
}

// prevent the submit button from resetting the page
// var submit = document.getElementById("submit");
form.addEventListener("submit", function(){ checkFormValidation(); });

function checkFormValidation() {
  if (checkName() === true && checkUsername() === true && checkEmail() === true) {
    form.setAttribute("action", "gallery.html");

    // Make tagline Develop something beautiful, {name} on gallery.html
    if (window.sessionStorage) {
      sessionStorage.setItem('txtName', nameInput.value);
      console.log(nameInput.value);
    }
  }
  else {
    preventSubmit(event);
  }
}

function preventSubmit(e) {
  e.preventDefault();
}



