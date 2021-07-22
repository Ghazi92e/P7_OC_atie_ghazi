$(document).ready(function(ajax) {
     // Request AJAX to get address map from back end
     $('form').on('submit', function(event) {
        oneLoop();
       $.ajax({
          data : {
             address : $('#address').val(),
                 },
             type : 'POST',
             url : '/ajaxtest'
            })
        .done(function(data) {
          $('#output').text(data.output).show();
            dataApi = JSON.stringify(data.output);
            console.log(dataApi);
            setTimeout(function() {
                bot(data.output);
            }, 1000);
              $('#wikioutput').text(data.wikidata).show();
                wikiapi = JSON.stringify(data.wikidata);
                setTimeout(function() {
                    wikiresponse(data.wikidata);
            }, 2000);
                console.log(wikiapi);
                // Display a google maps map from a defined address
          (function (geocode){
            let mapElement = 'map';
            let address = dataApi;
            geocoder = new google.maps.Geocoder();
           geocoder.geocode({ 'address': address }, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
              var mapOptions = {
                  zoom: 14,
                  center: results[0].geometry.location,
                  disableDefaultUI: true
              };
              var map = new google.maps.Map(document.getElementById(mapElement), mapOptions);
              var marker = new google.maps.Marker({
                  map: map,
                  position: results[0].geometry.location
              });
            } else {
                alert("Geocode was not successful for the following reason: " + status);
            }
          });
        })();

      });
      event.preventDefault();
      });
});