$(document).foundation()

$(document).ready(function() {
  var mappings = {
    "layers": [new ol.layer.Tile({
        source: new ol.source.OSM()
      }),
      new ol.layer.Vector({
        source: new ol.source.Vector({
          features: [
            new ol.Feature({
              geometry: new ol.geom.Point([1373285.013457604, 6680225.679608975]),
              name: 'Therapieraum im Feng Shui Haus.'
            })
          ]
        }),
        style: new ol.style.Style({
          image: new ol.style.Icon({
            anchor: [0.5, 1],
            src: '/static/img/Marker.svg.png',
          })
        })
      })
    ],
    "controls": ol.control.defaults().extend([
      new ol.control.FullScreen()
    ]),
    "view": new ol.View({
      center: ol.proj.fromLonLat([12.33646, 51.33194]),
      zoom: 18
    })
  }

  map = new ol.Map({
    target: 'map',
    controls: mappings.controls,
    layers: mappings.layers,
    view: mappings.view
  });
})