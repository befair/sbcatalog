// map controller for sbcatalog frontend
app.controller("MapController", function($http) {

    // create the map (map container must be loaded in dom)
    var map = L.map('map').setView([41.89, 12.53], 6);

    // return index of a marker in markers that match coordinates
    var getMarkerFromCoords = function(coords, markers) {
        for (x in markers) {
            if (markers[x][0] == coords[0] &&
                markers[x][1] == coords[1])
                return x;
        }
    }

    // add open street map layer to map
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">' +
                     'OpenStreetMap</a> contributors'
    }).addTo(map);

    // get the supplier data and add to the map
    $http.get('http://localhost:5000/geo/supplier/').success(function(data) {
        suppliers = data._items;
        markers = [];

        for ( var x in suppliers ) {
            s = suppliers[x];
            c = s.coords.reverse();

            // this will move the point of a 
            // random offset if there is duplicate
            while(getMarkerFromCoords(c, markers) !== undefined) {
                c[0] += Math.random()/1000.0;
                c[0] -= Math.random()/1000.0;
                c[1] -= Math.random()/1000.0;
                c[1] += Math.random()/1000.0;
            }

            // push into the markers array
            markers.push(c);

            // add to map
            L.marker(c).addTo(map)
                .bindPopup("<b>" + s.name + "</b><br>" + s.address + "<br>" +
                           (s.webSite? '<a href="' + s.webSite + '">' +
                            s.webSite + '</a>': ''));
        }
    });
});
