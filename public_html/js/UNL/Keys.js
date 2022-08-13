
var keyObject = null;
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
        }
    });
    /*********************************************************************/

        var arr = null;
        $.ajax({
            'async': false,
            'global': false,
            'url': '/files/json/unl/UNL_Keys.json',
            
            'dataType': 'json',
            'success': function (data) {
                keyObject = data;
                console.log(keyObject);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert('Status: ' + textStatus); alert('Error: ' + errorThrown);
            }
        });


});



function displayImages(value, object) {
    console.log("displayImages");
    console.log("value");
//    console.log(value);
    console.log("object");
    console.log(object);
    console.log("object class className");
    console.log(object.className);
    //if object == 
    //var view = document.getElementById('View');
    "collapsed"
    var val = value.replace('-image-target','')
    var zz = keyObject[val];
    console.log("Target");
    console.log(val);
    if (object.className == "accordion-button collapsed") {
        rmm = '#' + val + " img";
        $(rmm).remove();
    }
    for (let i = 0; i < zz.length; i++) {
        //console.log(zz[i]);
        displayimage =  zz[i];
        //nid = zz[i];
        //var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

        var image = '<img  src="[ReplaceImage]" alt="blank">';
        image = image.replace('[ReplaceImage]', displayimage);
        //image = image.replace('[ReplaceImage]', displayimage);
        //image = image.replace('[ReplaceImage]', displayimage);
        //$('#accordioncollapseOne001').append(image);
        var targetDivZId = '#' + value
        $(targetDivZId).append(image);

    }

    return false;
}
function resetImages() {
    count =1;
    location.reload();
}


