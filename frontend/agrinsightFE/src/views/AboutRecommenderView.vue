<template>
    <AboutHeroRecommend />
    <LogoClouds />
    <section class="bg-white py-8">
  <div class="container mx-auto px-4">
    <h2 class="text-2xl font-semibold mb-4">How It Works</h2>
    <p class="text-lg mb-6">
      The Crop Yield Predictor leverages machine learning to analyze historical data, weather forecasts, and soil conditions. Get accurate predictions on your crop yields and plan your farming activities with confidence.
    </p>

    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Machine Learning Algorithms</h3>
      <p class="text-lg mb-4">
        The predictor uses advanced machine learning algorithms to evaluate past crop yield data, current weather forecasts, and soil health conditions. This analysis helps in generating reliable yield predictions.
      </p>
    </div>

    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Data Sources</h3>
      <p class="text-lg mb-4">
        Our system utilizes data from:
        <ul class="list-disc list-inside ml-4">
          <li>Historical crop yield records</li>
          <li>Weather forecast models</li>
          <li>Soil health reports</li>
        </ul>
      </p>
    </div>

    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Flow Chart</h3>
      <p class="text-lg mb-4">
        The flow chart below illustrates the workflow of the yield predictor:
      </p>
      <img src="/src/assets/images/yieldPredictor.png" alt="Crop Yield Predictor Flow Chart" class="w-full h-auto mb-4">
      <p class="text-lg">
        The workflow begins with data collection, followed by data preprocessing, model training, prediction generation, and finally, yield estimation. Each step is essential for ensuring accurate predictions.
      </p>
    </div>

    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Video Explanation</h3>
      <p class="text-lg mb-4">
        Watch the video below for a detailed explanation of our crop yield predictor:
      </p>
      <iframe class="w-full h-64" src="https://www.youtube.com/embed/video_id" frameborder="0" allowfullscreen></iframe>
    </div>

    <div class="mb-8">
      <h3 class="text-xl font-semibold mb-2">Additional Benefits</h3>
      <p class="text-lg">
        In addition to yield predictions, our system provides:
        <ul class="list-disc list-inside ml-4">
          <li>Real-time weather updates</li>
          <li>Soil health monitoring</li>
          <li>Market trends analysis</li>
          <li>Customized farming tips and best practices</li>
        </ul>
      </p>
    </div>
  </div>
</section>

   <Footer />
</template>

<script setup>
import { ref } from 'vue';
import Footer from "../components/Footer.vue";
import AboutHeroRecommend from "../components/AboutHeroRecommend.vue";
import LogoClouds from "../components/LogoClouds.vue";
</script>

<style scoped>
.about-yield-predictor header {
  background-color: #0f5132;
}

.about-yield-predictor section {
  background-color: #f9f9f9;
}
</style>


