const apiKey ='pk.eyJ1IjoianNsZWltYW4iLCJhIjoiY2t5cWd0bjBsMGpuMDJubzd4aGc4ZHdwciJ9.UPLSgF0sRx8FezL36QqwSQ';

const mymap = L.map('map').setView([34.241974, -118.526484], 17);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: apiKey
}).addTo(mymap);

// Adding Sol Marker

const sol_marker = L.marker([34.240038, -118.527068]).addTo(mymap);

// Add popup message to marker

let template = `
<h3>Sol Center</h3>
<div style="text-align:center">
    <img width="150" height="150"src="static/styles/sol_center.jpg"/>
</div>
`
sol_marker.bindPopup(template);

// Sol center outline 

const polygon = L.polygon([
   
    [34.240249, -118.527229],
    [34.239839, -118.527232],
    [34.239836, -118.527015],
    [34.239952, -118.527023],
    [34.239954, -118.526956],
    [34.240056, -118.526795],
    [34.240251, -118.5268],
    [34.240249, -118.527229],
], {
    color:'red',
    fillColor:'red',
    fillOpacity:0.2
}).addTo(mymap).bindPopup('Sol Center')


// Adding Oasis Marker

const Oasis_marker = L.marker([34.239318, -118.525974]).addTo(mymap); 

// Add popup message to marker

let template2 = `
<h3>The Oasis</h3>
<div style="text-align:center">
    <img width="150" height="150"src="static/styles/outside_oasis.jpg"/>
</div>
`
Oasis_marker.bindPopup(template2);

// Oasis outline 

const polygon2 = L.polygon([
   
    [34.239535, -118.526374],
    [34.239249, -118.526403],
    [34.239273, -118.525639],
    [34.239397, -118.525644],
    [34.2394, -118.525918],
    [34.239533, -118.525926],
    [34.239537, -118.526379],

], {
    color:'blue',
    fillColor:'blue',
    fillOpacity:0.2
}).addTo(mymap).bindPopup('The Oasis')

// Adding SRC Marker

const src_marker = L.marker([34.24002, -118.524923]).addTo(mymap); 

// Add popup message to marker

let template3 = `
<h3>The Student Recreation Center</h3>
<div style="text-align:center">
    <img width="150" height="150"src="static/styles/outside_src.png"/>
</div>
`
src_marker.bindPopup(template3);

// SRC outline 

const polygon3 = L.polygon([
   
    [34.239433, -118.525169],
    [34.239433, -118.525113],
    [34.239329, -118.525113],
    [34.239324, -118.524708],
    [34.239433, -118.524705],
    [34.239431, -118.52466],
    [34.240491, -118.52466],
    [34.240495, -118.524711],
    [34.240597, -118.524713],
    [34.240601, -118.525068],
    [34.240621, -118.525073],
    [34.240621, -118.525137],
    [34.240493, -118.525137],
    [34.240495, -118.525172],
    [34.239431, -118.525164],


], {
    color:'green',
    fillColor:'green',
    fillOpacity:0.2
}).addTo(mymap).bindPopup('The Student Recreation Center')


/* Add circle 

const circle = L.circle([34.240038, -118.527068], {
    radius:25, 
    color: 'red', 
    fillColor: 'red',
    fillOpacity:0.2
}).addTo(mymap).bindPopup('Sol Center') */