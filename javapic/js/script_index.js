//change the jumbotron image every 20sec for set amt images

var jumbotron = document.getElementById("jumbotron");

// var galleryArray = new Array();
// galleryArray[0]='images/pdxcg_01.jpg'
// galleryArray[1]='images/pdxcg_02.jpg'
// galleryArray[2]='images/pdxcg_03.jpg'

var imageNum = 10;
var imageStr = "images/pdxcg_" + imageNum + ".jpg";

setInterval(function () {changeImage();}, 20000);

function changeImage() {
  jumbotron.style.backgroundImage = "url(" + imageStr + ")";
  console.log(imageNum);
  if (imageNum === 60) {
    imageNum = 9;
  }
  imageNum ++;
  imageStr = "images/pdxcg_" + imageNum + ".jpg";
}

