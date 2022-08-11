
(function ($) { //create closure so we can safely use $ as alias for jQuery

    $(document).ready(function () {

        // initialise plugin
        var example = $('#example').superfish({
            //add options here if required
        });
        // buttons to demonstrate Superfish's public methods
        $('.destroy').on('click', function () {
            example.superfish('destroy');
        });
        $('.init').on('click', function () {
            example.superfish();
        });
        $('.open').on('click', function () {
            example.children('li:first').superfish('show');
        });
        $('.close').on('click', function () {
            example.children('li:first').superfish('hide');
        });
    });
})(jQuery);

function includeHTML() {
    var z, i, elmnt, file, xhttp;
    /* Loop through a collection of all HTML elements: */
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
        elmnt = z[i];
        /*search for elements with a certain atrribute:*/
        file = elmnt.getAttribute("w3-include-html");
        if (file) {
            /* Make an HTTP request using the attribute value as the file name: */
            xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4) {
                    if (this.status == 200) {
                        elmnt.innerHTML = this.responseText;
                    }
                    if (this.status == 404) {
                        elmnt.innerHTML = "Page not found.";
                    }
                    /* Remove the attribute, and call this function once more: */
                    elmnt.removeAttribute("w3-include-html");
                    includeHTML();
                }
            }
            xhttp.open("GET", file, true);
            xhttp.send();
            /* Exit the function: */
            return;
        }
    }
}

