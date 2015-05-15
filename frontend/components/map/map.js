app.controller("MapController", function($http) {

  var map = L.map('map').setView([41.89, 12.53], 6);

  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // MAP ENVIRONMENT
  $http.get('http://localhost:5000/geo/supplier/').success(function(data) {
    suppliers = data._items;
    for ( var x in suppliers ) {
      s = suppliers[x];
      L.marker(s.coords.reverse()).addTo(map)
        .bindPopup("<b>" + s.name + "</b><br>" +
          s.address + "<br>" +
          (s.webSite? '<a href="' + s.webSite + '">' + s.webSite + '</a>': ''));
    }
  });
});
