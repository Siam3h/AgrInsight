<template>
  <div class="bg-white py-6 sm:py-8 lg:py-12">
    <div class="mx-auto max-w-screen-lg px-4 md:px-8">
      <h2 class="mb-4 text-2xl font-bold text-gray-800 md:mb-6 lg:text-3xl">
        How It Works
      </h2>
      <div class="flex flex-wrap justify-between items-start py-5">
        <AboutVideoEmbed />
      </div>
      <p class="max-w-screen-md text-gray-500 md:text-lg mt-45">
        Our platform uses advanced machine learning algorithms to analyze data
        from various sources including soil sensors, weather stations, and
        market data. This data is processed to provide accurate crop
        recommendations, predict yields, and offer tailored best farming
        practices. Our system continuously learns and improves, ensuring you get
        the best advice for your farming needs.
      </p>
    </div>
  </div>
</template>

<script>
import AboutVideoEmbed from "./AboutVideoEmbed.vue";
export default {
  name: "HowItWorks",
  components: {
    AboutVideoEmbed,
  },
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>
