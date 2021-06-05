function httpGet(theUrl)
{
    var xhr = new XMLHttpRequest();
    xhr.open( "GET", theUrl, false ); // false for synchronous request
    xhr.send( null );

    if (xhr.status === 200) {
        return xhr.responseText;
    } else {
        return "";
    }
}
