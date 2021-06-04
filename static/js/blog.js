function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}


document.addEventListener('DOMContentLoaded', function() {
    let b = window.location.origin
    var theUrl = new URL('/prev_next_post_api', b);
    data = httpGet(theUrl)
    document.getElementById("prev_next_post").innerHTML += data;
}, false);


document.addEventListener('DOMContentLoaded', function() {
    let b = window.location.origin
    var theUrl = new URL('/related_post_api', b);
    data = httpGet(theUrl)
    document.getElementById("related_post").innerHTML += data;

    var elem = document.querySelector('.nav-slider-hover');
    var flkty = new Flickity( elem, {
        // options
        cellAlign: 'left',
        contain: true
    });

}, false);

