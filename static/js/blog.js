

document.addEventListener('DOMContentLoaded', function() {
    let b = window.location.origin
    var theUrl = new URL(path, b);
    data = httpGet(theUrl)
    document.getElementById("prev_next_post").innerHTML += data;
}, false);


document.addEventListener('DOMContentLoaded', function() {
    let b = window.location.origin
    var theUrl = new URL('/api/related/test', b);
    data = httpGet(theUrl)
    document.getElementById("related_post").innerHTML += data;

    var elem = document.querySelector('.nav-slider-hover');
    var flkty = new Flickity( elem, {
        // options
        cellAlign: 'left',
        contain: true
    });

}, false);


document.addEventListener('DOMContentLoaded', function() {
    let b = window.location.origin
    var theUrl = new URL('/api/latest/test', b);
    data = httpGet(theUrl)
    document.getElementById("latest_post").innerHTML += data;
}, false);


document.addEventListener('DOMContentLoaded', function() {
    let b = window.location.origin
    var theUrl = new URL('/api/advertisement/test', b);
    data = httpGet(theUrl)
    document.getElementById("advertisement_post").innerHTML += data;
}, false);


document.addEventListener('DOMContentLoaded', function() {
    let b = window.location.origin
    var theUrl = new URL('/api/author_info/test', b);
    data = httpGet(theUrl)
    document.getElementById("author_box").innerHTML += data;
}, false);
