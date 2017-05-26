 var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([12.33646, 51.33194]),
    zoom: 18
  })
});



/*
$(document).ready(function () {
	view = new ol.View({
	  	center: [1373295.0134457604, 6680221.679608975],
	  	zoom: 18,
	 	maxZoom: 20,
	  	minZoom: 2,
	});

	var map = new ol.Map({
		target: 'map',
		controls: ol.control.defaults().extend([
	  		new ol.control.ScaleLine(),
	  		new ol.control.ZoomSlider()
		]),
		layers: [
	  		new ol.layer.Tile({
	    		source: new ol.source.OSM()
	  		})
		],
		view: view
	});

	var point = new ol.layer.Vector({
		source: new ol.source.Vector({
			features: [
				new ol.Feature({
					geometry: new ol.geom.Point([1373285.013457604, 6680225.679608975])
				})
			]
		})
	});

	map.addLayer(point);

});
*/
