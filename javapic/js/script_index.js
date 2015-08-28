// Jumbotron that automatically loops.
// Loops through some of our images every 20 seconds.
// >>>-------------------------------------------------------------->


// Gets the id jumbotron
var jumbotron = document.getElementById("jumbotron");

// Initializes the variables
var imageNum = 10;
var imageStr = "images/pdxcg_" + imageNum + ".jpg";

// Sets the interval for the loop infinitely
setInterval(function () {changeImage();}, 20000);

// Iterates through images in the folder
function changeImage() {
  jumbotron.style.backgroundImage = "url(" + imageStr + ")";
  console.log(imageNum);
  if (imageNum === 60) {
    imageNum = 9; // Max 60 images and restarts at image number 10
  }
  imageNum ++;
  imageStr = "images/pdxcg_" + imageNum + ".jpg";
}

