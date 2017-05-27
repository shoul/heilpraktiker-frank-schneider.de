
var pointer = new ol.layer.Vector({
	source: new ol.source.Vector({
		features: [
			new ol.Feature({
				geometry: new ol.geom.Point([1373285.013457604, 6680225.679608975]),
				name: 'Therapieraum im Feng Shui Haus.',
				population: 4000,
				rainfall: 500
			})
		]
	}),
	style: new ol.style.Style({
		image: new ol.style.Icon({
			anchor: [0.5, 1],
			src: '/static/img/Marker.svg.png',
		})
	})
});

var map = new ol.Map({
  target: 'map',
  controls: ol.control.defaults().extend([
  	new ol.control.FullScreen()
  ]),
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    }),
  	pointer
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([12.33646, 51.33194]),
    zoom: 18
  })
});
