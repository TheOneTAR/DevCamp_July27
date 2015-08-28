// Gallery that is auto-populated with all the images in the folder.
// When an image is clicked, it should show up larger.
// Clicking anywhere on the page should remove the larger preview.
// >>>-------------------------------------------------------------->


var gallery = document.getElementById('gallery');
var images = [];
var numOfImages = 60

// makes and array of image names matching the directory of images
function produceListOfImgNamesARRAY() {

  for(var i = 1; i < numOfImages + 1; i++) {

    // Images 1 .. 9 need a different URL structure
    if (i < 10) {
      images.push("images/pdxcg_0" + i + ".jpg");
    } else {
      // Images 10 .. 60 need a different URL structure
      images.push("images/pdxcg_" + i + ".jpg");
    }
  }
  console.log(images);
}
produceListOfImgNamesARRAY();

// creates the DOM elements for manipulation
function createListItemsWithImagesDOM() {

  // Takes the images Array and creates DOM elements
  for (var i = 0; i < images.length; i++) {
    var newList = document.createElement('li');
    var newImg = document.createElement('img');
    newImg.src = images[i];
    newList.appendChild(newImg);

    gallery.appendChild(newList);
  }
}
createListItemsWithImagesDOM();

// event listener for click of an image



