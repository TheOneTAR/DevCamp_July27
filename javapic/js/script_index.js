// Jumbotron that automatically loops.
// Loops through some of our images every 20 seconds.
// >>>-------------------------------------------------------------->


// Gets the id jumbotron
var jumbotron = document.getElementById("jumbotron");

// Initializes the variables
var imgNum = 10;
var imgSrc = "images/pdxcg_" + imgNum + ".jpg";

// Sets the interval for the loop infinitely
setInterval(function () {changeImage();}, 20000);

// Iterates through images in the folder
function changeImage() {
  jumbotron.style.backgroundImage = "url(" + imgSrc + ")";
  console.log(imgNum);
  if (imgNum === 60) {
    imgNum = 9; // Max 60 images and restarts at image number 10
  }
  imgNum ++;
  imgSrc = "images/pdxcg_" + imgNum + ".jpg";
}

