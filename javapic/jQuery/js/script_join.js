// A login form that won’t let users continue to the gallery until validation passes
// >>>-------------------------------------------------------------->

var $form = $('#signup');
var $nameInput = $('[name=name]');
var $username = $('[name=username]');
var $email = $('[type=email]');

// preventDefault submit button behavior
// otherwise route to the gallery.html
$form.on('submit', function(e) {
  e.preventDefault();
  if (checkValidation()) {

    // redirect to gallery upon clicking submit button
    window.location.href = "gallery.html";

    // Make tagline .. {name} on gallery.html
    if (window.sessionStorage) {
      sessionStorage.setItem('txtName', $nameInput.val());
      console.log($nameInput.val());
    }
  }
})

// check validation for each input on blur
$('input').on('blur', function() {
  checkValidation();
})

function checkValidation() {
  // check name
  if ($nameInput.val().length < 2) {

    alert('Please provide a name of two or more characters.');
    $nameInput.focus;
    return false
  }
  // check username
  if ($username.val().length < 2) {
    alert('Please provide a username of two or more characters.');
    $username.focus;
    return false
  }
  // check email
  var valid = /[^@]+@[^@].+/;
  if (!valid.test($email.val())) {
    alert('Please provide a valid email address.\n' +
      'yourEmail@place.com');
    $email.focus;
    return false
  }
  return true
}

