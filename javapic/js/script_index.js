// Jumbotron that automatically loops.
// Loops through some of our images every 20 seconds.
// >>>-------------------------------------------------------------->

var jumbotron = document.getElementById("jumbotron");

// Initializes the variables
var imgNum = 1;
var imgMax = 35;
// var imgSrc = "images/pdxcg_" + imgNum + ".jpg";

// Sets the interval for the loop infinitely
setInterval(function () {changeImage();}, 20000);

// Iterates through images in the folder
function changeImage() {
  // Images 1 .. 9 need a different URL structure
  if (imgNum < 10) {
    jumbotron.style.backgroundImage = "url('images/pdxcg_0" + imgNum + ".jpg')";
  } else {
    // Images 10 .. imgMax need a different URL structure
    jumbotron.style.backgroundImage = "url('images/pdxcg_" + imgNum + ".jpg')";
  }
  console.log(imgNum);

  // when counter reaches imgMax, counter restarts at imgNum 0
  if (imgNum === imgMax) {
    imgNum = 0;
  }
  imgNum ++;
}

