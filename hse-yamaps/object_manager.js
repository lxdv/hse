ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [55.76, 37.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            gridSize: 32
        });
        
    myMap.geoObjects.add(objectManager);
    $.ajax({
        url: "http://localhost:8080?file=cords.txt"
    }).done(function(data) {
        objectManager.add(data);
    });
}