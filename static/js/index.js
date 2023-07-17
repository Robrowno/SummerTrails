mapboxgl.accessToken =
    "pk.eyJ1IjoiY2FsbHVtZGVubmlzaWUiLCJhIjoiY2xrM3gyNmtrMDZsMzNvcnlkcDA1OGlyNSJ9.JPGtfXiSJF5qipCkDbQuyg";
const geojson = {
    type: "FeatureCollection",
    features: []
};

const map = new mapboxgl.Map({
    container: "map",
    // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    style: "mapbox://styles/mapbox/streets-v12",
    center: [5.6484, 30.2268],
    zoom: 2
});

map.on("load", () => {
    map.addSource("markers", {
        type: "geojson",
        data: {
            type: "FeatureCollection",
            features: []
        }
    });

    function updateMarkers() {
        // Clear existing markers from the map
        map.getSource("markers").setData(geojson);

        // Add markers to the map.
        for (const marker of geojson.features) {
            // Create a DOM element for each marker.
            const el = document.createElement("div");
            const width = marker.properties.iconSize[0];
            const height = marker.properties.iconSize[1];
            const image = marker.properties.image;
            const title = marker.properties.title;
            const content = marker.properties.content;
            const user = marker.properties.user;

            el.className = "marker";
            el.style.backgroundImage = `url(${image})`;
            el.style.width = `${width}px`;
            el.style.height = `${height}px`;
            el.style.backgroundSize = "100%";

            el.addEventListener("click", () => {
                openLightbox(image, title, content, user);
            });

            // Add markers to the map.
            new mapboxgl.Marker(el)
            .setLngLat(marker.geometry.coordinates)
            .addTo(map);
        }
    }

    function openLightbox(imageUrl, title, content, user) {
        const lightbox = document.createElement("div");
        lightbox.className = "lightbox";
        lightbox.innerHTML = `
          <div class="lightbox-content">
            <img src="${imageUrl}" alt="Image" class="lightbox-image" />
            <div class="image-details">
              <h4>${title}</h4>
              <p>${content}</p>
              <p>Uploaded by: ${user}</p>
            </div>
          </div>
        `;
        document.body.appendChild(lightbox);
      
        lightbox.addEventListener("click", () => {
          lightbox.remove();
        });
      }

    // Make an AJAX request to fetch the photo information
    const baseUrl = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:8000" : "https://summertrails-heroku-dd7388a15196.herokuapp.com";
    const url = `${baseUrl}/api/users/posts/`;
    
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            // Update the geojson.features array with the photo information
            data.forEach((photo) => {
                const feature = {
                    type: "Feature",
                    properties: {
                        title: photo.title,
                        image: photo.image,
                        content: photo.content,
                        user: photo.user,
                        iconSize: [40, 40],
                        icon: "marker"
                    },
                    geometry: {
                        type: "Point",
                        coordinates: [photo.longitude, photo.latitude]
                    }
                };

                geojson.features.push(feature);
            });

            // Update the map with the new markers
            updateMarkers();
        })
        .catch((error) => {
            console.log("Error:", error);
        });
});

var myModal = new bootstrap.Modal(document.getElementById("exampleModal"), {
    keyboard: false
});
