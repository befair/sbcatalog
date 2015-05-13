var map = L.map('map').setView([41.89, 12.53], 6);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([41, 12]).addTo(map)
    .bindPopup('A pretty CSS3 popup. <br> Easily customizable.')
