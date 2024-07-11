<template>
  <div class="bg-white py-6 sm:py-8 lg:py-12">
    <div class="mx-auto max-w-screen-2xl px-4 md:px-8">
      <p class="mb-2 font-semibold text-indigo-500 md:mb-3 lg:text-lg">
        Introducing
      </p>

      <h2 class="mb-4 text-2xl font-bold text-gray-800 md:mb-6 lg:text-3xl">
        Revolutionary way to build the web
      </h2>

      <p class="max-w-screen-md text-gray-500 md:text-lg">
        This is a section of some simple filler text, also known as placeholder
        text. It shares some characteristics of a real written text but is
        random or otherwise generated.
      </p>
    </div>
  </div>
  <div class="flex flex-wrap justify-between items-start p-5">
    <div class="w-full lg:w-1/2 mb-5 lg:mb-0">
      <h2 class="text-green-900 text-lg font-semibold mb-2">
        Enhance Your Farming
      </h2>
      <h1 class="text-3xl font-bold mb-4">Smart Agriculture Solutions</h1>
      <p class="mb-6">
        Discover the power of machine learning in agriculture. Optimize your
        crop yield, get the best crop recommendations, and follow best farming
        practices with our cutting-edge platform.
      </p>
      <div class="flex items-start mb-6">
        <div class="text-2xl mr-4">🌾</div>
        <div>
          <h3 class="text-xl font-semibold">Crop Recommendation</h3>
          <p>
            Get the best crop recommendations based on your soil type, weather
            conditions, and market trends to maximize your yield and
            profitability.
          </p>
        </div>
      </div>
      <div class="flex items-start mb-6">
        <div class="text-2xl mr-4">📈</div>
        <div>
          <h3 class="text-xl font-semibold">Yield Prediction</h3>
          <p>
            Use our advanced machine learning models to predict crop yields with
            high accuracy, helping you make informed decisions and plan ahead.
          </p>
        </div>
      </div>
      <div class="flex items-start">
        <div class="text-2xl mr-4">🌍</div>
        <div>
          <h3 class="text-xl font-semibold">Best Farming Practices</h3>
          <p>
            Access a wealth of knowledge and best practices tailored to your
            specific crops and conditions, ensuring sustainable and efficient
            farming.
          </p>
        </div>
      </div>
    </div>
    <div class="w-full lg:w-1/2">
      <div class="aspect-w-16 aspect-h-9">
        <iframe
          class="w-full h-full"
          src="https://www.youtube.com/embed/o_AIw9bGogo"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Video",
};
</script>

<style>
/* Add any additional styles if needed */
</style>
