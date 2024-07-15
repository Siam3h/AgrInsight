<template>
  <footer class="bg-gray-900 text-white py-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row md:space-y-0 md:justify-between">
        <div class="flex flex-col items-center md:items-start">
          <img
            src="@/assets/images/black_logo.png"
            alt="Logo"
            class="h-20 mb-4"
          />
          <p class="text-center md:text-left">
            Making the world a better place by <br />
            data-driven and precision Agriculture
          </p>
          <div class="mt-4 flex space-x-4">
            <a href="#" class="text-gray-400 hover:text-white"
              ><i class="fab fa-facebook-f"></i
            ></a>
            <a href="#" class="text-gray-400 hover:text-white"
              ><i class="fab fa-instagram"></i
            ></a>
            <a href="#" class="text-gray-400 hover:text-white"
              ><i class="fab fa-twitter"></i
            ></a>
            <a href="#" class="text-gray-400 hover:text-white"
              ><i class="fab fa-github"></i
            ></a>
            <a href="#" class="text-gray-400 hover:text-white"
              ><i class="fab fa-youtube"></i
            ></a>
          </div>
        </div>
        <div
          class="mt-8 md:mt-0 flex flex-col md:flex-row md:space-x-16 w-full md:w-auto"
        >
          <div class="mb-8 md:mb-0">
            <h4 class="font-bold mb-4">Solutions</h4>
            <ul class="space-y-2">
              <li>
                <a
                  href="/about/recommender/"
                  class="text-gray-400 hover:text-white"
                  >Crop Recommender</a
                >
              </li>
              <li>
                <a href="/about/yield/" class="text-gray-400 hover:text-white"
                  >Yield Predictor</a
                >
              </li>
              <li>
                <a
                  href="/about/insights/"
                  class="text-gray-400 hover:text-white"
                  >Best Practices</a
                >
              </li>
            </ul>
          </div>
          <div class="mb-8 md:mb-0">
            <h4 class="font-bold mb-4">Support</h4>
            <ul class="space-y-2">
              <li>
                <a href="/soon/" class="text-gray-400 hover:text-white"
                  >Documentation</a
                >
              </li>
              <li>
                <a href="/soon/" class="text-gray-400 hover:text-white"
                  >API Status</a
                >
              </li>
            </ul>
          </div>
          <div class="mb-8 md:mb-0">
            <h4 class="font-bold mb-4">Company</h4>
            <ul class="space-y-2">
              <li>
                <a href="/about/" class="text-gray-400 hover:text-white"
                  >About</a
                >
              </li>
              <li>
                <a href="/soon/" class="text-gray-400 hover:text-white">Blog</a>
              </li>
              <li>
                <a href="/soon/" class="text-gray-400 hover:text-white"
                  >Careers</a
                >
              </li>
              <li>
                <a href="/contact/" class="text-gray-400 hover:text-white"
                  >Contact</a
                >
              </li>
            </ul>
          </div>
          <div>
            <h4 class="font-bold mb-4">Legal</h4>
            <ul class="space-y-2">
              <li>
                <a
                  href="/privacy-policy/"
                  class="text-gray-400 hover:text-white"
                  >Privacy Policy</a
                >
              </li>
              <li>
                <a
                  href="/terms-of-service/"
                  class="text-gray-400 hover:text-white"
                  >Terms of Service</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="border-t border-gray-800 mt-8"></div>
      <div class="mt-4 text-center text-gray-500">
        &copy; {{ currentYear }} Agricultural Insights, Inc. <br />
        All rights reserved.
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      currentYear: new Date().getFullYear(),
    };
  },
};
</script>
