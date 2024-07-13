<template>
  <div class="about-recommender">
    <header class="bg-green-900 text-white py-6">
      <div class="container mx-auto px-4">
        <h1 class="text-4xl font-bold">About Crop Recommender</h1>
      </div>
    </header>
    
    <section class="bg-white py-8">
      <div class="container mx-auto px-4">
        <h2 class="text-2xl font-semibold mb-4">How It Works</h2>
        <p class="text-lg mb-6">
          Our Crop Recommender uses advanced algorithms to suggest the best crops to plant based on soil quality, weather patterns, and market demand. Maximize your yield and profitability with tailored crop recommendations.
        </p>
        
        <div class="mb-8">
          <h3 class="text-xl font-semibold mb-2">Machine Learning Algorithms</h3>
          <p class="text-lg mb-4">
            The recommender uses machine learning algorithms to analyze historical data on climate and soil conditions. By understanding the patterns and correlations within the data, it can make accurate predictions on the best crops to plant in different conditions.
          </p>
        </div>
        
        <div class="mb-8">
          <h3 class="text-xl font-semibold mb-2">Data Sources</h3>
          <p class="text-lg mb-4">
            Our system gathers data from various sources, including:
            <ul class="list-disc list-inside ml-4">
              <li>Weather stations and climate models</li>
              <li>Soil testing laboratories</li>
              <li>Market demand analytics</li>
            </ul>
          </p>
        </div>
        
        <div class="mb-8">
          <h3 class="text-xl font-semibold mb-2">Flow Chart</h3>
          <p class="text-lg mb-4">
            The flow chart below illustrates the process of how the recommender works:
          </p>
          <img src="" alt="Crop Recommender Flow Chart" class="w-full h-auto mb-4">
          <p class="text-lg">
            The process starts with data collection, followed by data preprocessing, model training, prediction, and finally, recommendation. Each step is crucial in ensuring the accuracy and reliability of the recommendations.
          </p>
        </div>
        
        <div class="mb-8">
          <h3 class="text-xl font-semibold mb-2">Video Explanation</h3>
          <p class="text-lg mb-4">
            Watch the video below to see a detailed explanation of how our crop recommender works:
          </p>
          <iframe class="w-full h-64" src="https://www.youtube.com/embed/video_id" frameborder="0" allowfullscreen></iframe>
        </div>
        
        <div class="mb-8">
          <h3 class="text-xl font-semibold mb-2">Additional Benefits</h3>
          <p class="text-lg">
            In addition to crop recommendations, our system provides:
            <ul class="list-disc list-inside ml-4">
              <li>Real-time updates on weather conditions</li>
              <li>Soil health monitoring</li>
              <li>Market trends analysis</li>
              <li>Customized farming tips and best practices</li>
            </ul>
          </p>
        </div>
      </div>
    </section>
  </div>
  <Footer />
</template>

<script setup>
import { ref } from 'vue';
import Footer from "../components/Footer.vue";
</script>

<style scoped>
.about-recommender header {
  background-color: #0f5132;
}

.about-recommender section {
  background-color: #f9f9f9;
}
</style>
