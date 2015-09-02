// A login form that won’t let users continue to the gallery until validation passes
// >>>-------------------------------------------------------------->


var $form = $('#signup');
var $nameInput = $('[name=name]');
var $username = $('[name=username]');
var $email = $('[type=email]');
var $this = $(this);

$('input').on('blur', function() {
  // alert("hi");
})

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

function checkValidation() {
  return false
}

