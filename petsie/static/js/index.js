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

function codeAddress(address, firstname, email, image, id) {

//    var sAddress = document.getElementById("inputTextAddress").value;
//    sAddress = address || sAddress;
    geocoder.geocode({'address': address},function(results, status)

    {
     if (status == google.maps.GeocoderStatus.OK) {

         map.setCenter(results[0].geometry.location);
         console.log(results);

         var pet_sitter_info = firstname + ", " + email +"<div><a href='/view_sitter/"+id +"'" + "><img style='height:100px' src='/media/" +image+"'" +"/></a></div>";

         var infowindow = new google.maps.InfoWindow({
             content: pet_sitter_info
         });
         var marker = new google.maps.Marker({
             map:map,
             position: results[0].geometry.location,
             title: "some title"
         });
//         google.maps.event.addListener(marker, 'mouseover', function(){
//             infowindow.open(map,marker);
//         });

            google.maps.event.addListener(marker, 'click', function(){
             infowindow.open(map,marker);
         });


//        google.maps.event.addListener(marker, 'mouseout', function(){
//            infowindow.close();
//        });

     }
     else
     {
    alert("Geocode was not successful for the following reason: " + status);
     }

    });
}

google.maps.event.addDomListener(window, 'load', initialize);