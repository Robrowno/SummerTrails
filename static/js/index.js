mapboxgl.accessToken =
    "pk.eyJ1IjoiY2FsbHVtZGVubmlzaWUiLCJhIjoiY2xrM3gyNmtrMDZsMzNvcnlkcDA1OGlyNSJ9.JPGtfXiSJF5qipCkDbQuyg";
const geojson = {
    type: "FeatureCollection",
    features: [
        {
            type: "Feature",
            properties: {
                message: "This is image number 1",
                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlmkYJl-s0c3jHK2vxyfGrJhZhhfadefAqr0iRJlYhzg&s",
                iconSize: [60, 60]
            },
            geometry: {
                type: "Point",
                coordinates: [-66.324462, -16.024695]
            }
        },
        {
            type: "Feature",
            properties: {
                message: "This is image number 2",
                image: "https://cf-images.us-east-1.prod.boltdns.net/v1/static/3281700261001/2683dfb6-47e9-44f9-a1b5-78315738a1f6/23ed0ed9-9cef-4d4a-921c-146a282d9105/1280x720/match/image.jpg",
                iconSize: [50, 50]
            },
            geometry: {
                type: "Point",
                coordinates: [-61.21582, -15.971891]
            }
        },
        {
            type: "Feature",
            properties: {
                message: "This is image number 3",
                image: "https://www.planetware.com/wpimages/2020/01/india-in-pictures-beautiful-places-to-photograph-gateway-of-india-mumbai.jpg",
                iconSize: [40, 40]
            },
            geometry: {
                type: "Point",
                coordinates: [-63.292236, -18.281518]
            }
        }
    ]
};

const map = new mapboxgl.Map({
    container: "map",
    // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    style: "mapbox://styles/mapbox/streets-v12",
    center: [-65.017, -16.457],
    zoom: 5
});

// Add markers to the map.
for (const marker of geojson.features) {
    // Create a DOM element for each marker.
    const el = document.createElement("div");
    const width = marker.properties.iconSize[0];
    const height = marker.properties.iconSize[1];
    const image = marker.properties.image;
    el.className = "marker";
    el.style.backgroundImage = `url(${image})`;
    el.style.width = `${width}px`;
    el.style.height = `${height}px`;
    el.style.backgroundSize = "100%";

    el.addEventListener("click", () => {
        myModal.show()
    });

    // Add markers to the map.
    new mapboxgl.Marker(el).setLngLat(marker.geometry.coordinates).addTo(map);
}

var myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {
    keyboard: false
})