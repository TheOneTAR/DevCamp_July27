// Gallery that is auto-populated with all the images in the folder.
// >>>-------------------------------------------------------------->

var $gallery = $('#gallery');
var $tagline = $('.tagline');
var images = [];
var imgMax = 60;

// IFFE array of image names matching the directory of images
(function produceListOfImgNamesARRAY() {
  for(var imgNum = 1; imgNum < imgMax + 1; imgNum++) {
    // Images 1 .. 9 need a different URL structure
    if (imgNum < 10) {
      images.push("../images/pdxcg_0" + imgNum + ".jpg");
    } else {
      // Images 10 .. 60 need a different URL structure
      images.push("../images/pdxcg_" + imgNum + ".jpg");
    }
  }
  // console.log(images);
})();

// IFFE creates the DOM elements for manipulation, displays gallery
var items = [];
$.each(images, function(i, item) {
  items.push('<li><img src=' + item + '></li>')
});
$gallery.append(items);

// When an image is clicked, it should show up larger.
// Clicking anywhere on the page should remove the larger preview.
$imgDiv = $('#image_show');
$imgDivChild = $imgDiv.children('img:first-child');

// show image when clicked to larger image
$gallery.on('click', function(e) {
  console.log(e.target.src);
  $imgDiv.removeClass("display_none").addClass("display_img");
  $imgDivChild.attr('src', e.target.src);
});

// stop event flow bubbling when image is clicked
$imgDivChild.on('click', function(e) {
  e.stopPropagation();
})

// hide image from the large image state
$imgDiv.on('click', function() {
  $imgDiv.addClass('display_none');
})

