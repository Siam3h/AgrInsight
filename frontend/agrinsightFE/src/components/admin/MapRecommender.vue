<template>
  <div>
    <h2 class="text-xl font-semibold">Recommended Crop & Yield</h2>
    <div id="map" class="w-full h-full map-container"></div>
  </div>
</template>

<script>
import L from "leaflet";
import "leaflet/dist/leaflet.css";

export default {
  name: "MapRecommender",
  data() {
    return {
      map: null,
      locations: [
        {
          lat: -1.286389,
          lng: 36.817223,
          recommendedCrop: "Maize",
          predictedYield: "3.2 tons/acre",
          region: "Nairobi",
        },
        {
          lat: -0.091702,
          lng: 34.767956,
          recommendedCrop: "Sorghum",
          predictedYield: "2.9 tons/acre",
          region: "Kisumu",
        },
        {
          lat: -0.716667,
          lng: 36.433333,
          recommendedCrop: "Potatoes",
          predictedYield: "4.1 tons/acre",
          region: "Nyeri",
        },
        {
          lat: 0.0525,
          lng: 37.646667,
          recommendedCrop: "Coffee",
          predictedYield: "1.5 tons/acre",
          region: "Meru",
        },
        {
          lat: -3.38,
          lng: 39.720833,
          recommendedCrop: "Cassava",
          predictedYield: "5.0 tons/acre",
          region: "Mombasa",
        },
        {
          lat: 0.516667,
          lng: 35.283333,
          recommendedCrop: "Tea",
          predictedYield: "2.8 tons/acre",
          region: "Kericho",
        },
        {
          lat: 0.3727,
          lng: 37.8084,
          recommendedCrop: "Mangoes",
          predictedYield: "6.0 tons/acre",
          region: "Embu",
        },
        {
          lat: -2.529844,
          lng: 37.459313,
          recommendedCrop: "Tomatoes",
          predictedYield: "20.0 tons/acre",
          region: "Kitui",
        },
        {
          lat: 0.4783,
          lng: 34.7398,
          recommendedCrop: "Millet",
          predictedYield: "2.5 tons/acre",
          region: "Busia",
        },
        {
          lat: -0.2833,
          lng: 36.0667,
          recommendedCrop: "Barley",
          predictedYield: "3.8 tons/acre",
          region: "Nakuru",
        },
        {
          lat: -1.2921,
          lng: 36.8219,
          recommendedCrop: "Cabbage",
          predictedYield: "6.5 tons/acre",
          region: "Kiambu",
        },
        {
          lat: -0.4569,
          lng: 39.6461,
          recommendedCrop: "Rice",
          predictedYield: "4.2 tons/acre",
          region: "Tana River",
        },
        {
          lat: 1.2193,
          lng: 34.8707,
          recommendedCrop: "Groundnuts",
          predictedYield: "1.8 tons/acre",
          region: "Siaya",
        },
        {
          lat: -0.4167,
          lng: 37.8667,
          recommendedCrop: "Avocados",
          predictedYield: "4.5 tons/acre",
          region: "Murang'a",
        },
        {
          lat: 1.2921,
          lng: 36.8219,
          recommendedCrop: "Bananas",
          predictedYield: "10.0 tons/acre",
          region: "Kakamega",
        },
        {
          lat: -1.4667,
          lng: 36.9825,
          recommendedCrop: "Wheat",
          predictedYield: "2.7 tons/acre",
          region: "Narok",
        },
      ],
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      // Initialize the map centered on Kenya with a specific zoom level
      this.map = L.map("map").setView([-1.286389, 36.817223], 7);

      // Set up the Stamen Terrain layer
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(this.map);

      // Add markers with tooltips for each location in Kenya
      this.locations.forEach((location) => {
        const marker = L.marker([location.lat, location.lng]).addTo(this.map);
        marker.bindTooltip(
          `
          <div>
            <strong>Region:</strong> ${location.region}<br />
            <strong>Recommended Crop:</strong> ${location.recommendedCrop}<br />
            <strong>Predicted Yield:</strong> ${location.predictedYield}
          </div>
        `,
          { permanent: false, direction: "top" }
        );
      });
    },
  },
};
</script>

<style scoped>
#map {
  height: 450px;
  width: 100%;
  border: 2px solid #ccc; /* Adds a light gray border */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Adds a subtle shadow */
  border-radius: 8px; /* Optional: Adds rounded corners */
}
</style>
