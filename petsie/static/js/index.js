/**
 * Created by golrizrad on 7/25/14.
 */

var geocoder;
var map;
//function initialize() {
//
//    var mapOptions = {
//        zoom: 16,
//        center: new google.maps.LatLng(37.7833, -122.4167)
//    };
//    geocoder = new google.maps.Geocoder();
//
//    map = new google.maps.Map(document.getElementById('map-canvas'),
//        mapOptions);
//    codeAddress('1407 Golden Gate Ave, San Francisco');
//    codeAddress('225 Bush Street, San Francisco');
//}

function codeAddress(address) {

    var sAddress = document.getElementById("inputTextAddress").value;
    sAddress = address || sAddress;
    geocoder.geocode({'address': sAddress},function(results, status)

    {
     if (status == google.maps.GeocoderStatus.OK) {

         map.setCenter(results[0].geometry.location)
         console.log(results)

         var marker = new google.maps.Marker({
             map:map,
             position: results[0].geometry.location});

     }
     else
     {
    alert("Geocode was not successful for the following reason: " + status);
     }

    });
}





google.maps.event.addDomListener(window, 'load', initialize);