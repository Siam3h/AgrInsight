<template>
  <section class="bg-gray-900 text-white py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <p class="text-indigo-500 font-semibold mb-2">Empower Your Farming</p>
      <h2 class="text-3xl md:text-4xl font-extrabold mb-4">
        Innovative Solutions for Modern Agriculture
      </h2>
      <p class="text-lg max-w-3xl mx-auto mb-12">
        Our platform provides advanced tools to enhance your farming efficiency
        and productivity. From recommending the best crops to predicting yields
        and offering the best farming practices, we help you make informed
        decisions for better outcomes.
      </p>
    </div>
    <div
      class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-3 gap-8 text-left"
    >
      <div class="feature-card">
        <div class="flex items-center mb-4">
          <i class="fas fa-seedling text-indigo-500 text-2xl"></i>
          <h3 class="ml-2 text-lg font-semibold">Crop Recommender</h3>
        </div>
        <p class="text-gray-400 mb-4">
          Our Crop Recommender uses advanced algorithms to suggest the best
          crops to plant based on soil quality, weather patterns, and market
          demand. Maximize your yield and profitability with tailored crop
          recommendations.
        </p>
        <a href="#" class="text-indigo-500 hover:text-indigo-400"
          >Learn more &rarr;</a
        >
      </div>

      <div class="feature-card">
        <div class="flex items-center mb-4">
          <i class="fas fa-chart-line text-indigo-500 text-2xl"></i>
          <h3 class="ml-2 text-lg font-semibold">Crop Yield Predictor</h3>
        </div>
        <p class="text-gray-400 mb-4">
          The Crop Yield Predictor leverages machine learning to analyze
          historical data, weather forecasts, and soil conditions. Get accurate
          predictions on your crop yields and plan your farming activities with
          confidence.
        </p>
        <a href="#" class="text-indigo-500 hover:text-indigo-400"
          >Learn more &rarr;</a
        >
      </div>

      <div class="feature-card">
        <div class="flex items-center mb-4">
          <i class="fas fa-hand-holding-water text-indigo-500 text-2xl"></i>
          <h3 class="ml-2 text-lg font-semibold">Best Farming Practices</h3>
        </div>
        <p class="text-gray-400 mb-4">
          Discover the best farming practices to enhance your crop yield and
          soil health. Our platform provides tips and techniques on irrigation,
          fertilization, and pest management based on the latest agricultural
          research.
        </p>
        <a href="#" class="text-indigo-500 hover:text-indigo-400"
          >Learn more &rarr;</a
        >
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Feature",
};
</script>

<style scoped>
.feature-card {
  background-color: #1a1a2e;
  padding: 20px;
  border-radius: 8px;
}
</style>
