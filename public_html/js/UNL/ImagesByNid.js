
var imageCollection = null;
var currentImageKey = null;
var currentImageNum = null;
var currentImage = null;

$(document).ready(function() {
    /*********************************************************************/
    $.ajaxSetup({
        beforeSend: function() {
            // show gif here, eg:
            //$('#loading').show();
            $('body').addClass('loading');
        },
        complete: function() {// hide gif here, eg:
            $('body').removeClass('loading');
            displayUNLImage();
        }
    });
    /*********************************************************************/

        var arr = null;
        $.ajax({
            'async': false,
            'global': false,
            'url': '/files/json/unl/ImagesByNid.json',

            'dataType': 'json',
            'success': function (data) {
                imageCollection = data;
                currentImageNum = 0
                currentImageKey = Object.keys(imageCollection)[currentImageNum];
                currentImage = currentImageKey;
                console.log('Current imagekey:\n' + currentImageKey);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert('Status: ' + textStatus); alert('Error: ' + errorThrown);
            }
        });

});




function displayUNLImage() {

    displayimage = 'https://nematode.unl.edu/' + currentImage
    var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

    var image = '<div class="col-md-6"> <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]" alt="" style="width: 500px" /></a></div>';
    image = image.replace('[ReplaceImage]', displayimage);
    image = image.replace('[ReplaceImage]', displayimage);
    $('#displayDiv').empty();
    $('#displayDiv').append(image);

    //currentImage = imageCollection[currentImageKey];

    return false;
}
function resetImages() {
    count =1;
    location.reload();
}
function nextImage() {
    currentImageNum = currentImageNum + 1;
    currentImageKey = Object.keys(imageCollection)[currentImageNum];
    currentImage = currentImageKey;
    console.log('imageCollection:\n' + imageCollection);
    console.log('Current image key:\n' + currentImageKey);
    console.log('Current image :\n' + currentImage);
    displayUNLImage();
}

function previousImage() {
    currentImageNum = currentImageNum - 1;
    if (currentImageNum < 1) {
       currentImageNum = 0; 
    }

    
    currentImageKey = Object.keys(imageCollection)[currentImageNum];
    currentImage = currentImageKey;
    console.log('imageCollection:\n' + imageCollection);
    console.log('Current image key:\n' + currentImageKey);
    console.log('Current image :\n' + currentImage);
    displayUNLImage();
}

