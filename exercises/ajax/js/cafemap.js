window.onload = loadScript;
function initialize() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(-34.397, 150.644),
    mapTypeId: google.maps.MapTypeId.HYBRID

  };
  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  };
  var markerA = new google.maps.Marker({
    map: map,
    position: new google.maps.LatLng(-34.397, 150.644),
    customInfo: "Marker A"
  });

function loadScript() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' +
      'callback=initialize';
  document.body.appendChild(script);
}

// $(document).ready(function() {   
//  $.ajax(
//    {
//      url: "https://maps.googleapis.com/maps/api/js?key=AIzaSyBKLU9CN4S7MB74EO9vIh97OQwZZ7wGL9w&sensor=false",
//      type: 'POST',
//      dataType: 'json',
//      data: {
//        fname: firstname,
//        lname: lastname,
//        date: (new Date())
//      },
//      success: function(json) {
//        console.log(json);
//        // DO SOMETHING HERE

//      }
//    }
//  );  
//  return false;
// });