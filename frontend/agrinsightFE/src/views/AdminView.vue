<template>
  <div class="min-h-screen flex flex-col dark:bg-gray-900 dark:text-white">
    <header
      class="bg-green-600 dark:bg-green-800 text-white p-4 flex justify-between items-center"
    >
      <h1 class="text-xl font-bold">Agri-Tech Admin Dashboard</h1>
      <DarkModeToggle />
    </header>
    <div class="flex flex-1">
      <aside class="w-64 bg-gray-100 dark:bg-gray-800 p-4">
        <nav>
          <ul>
            <li class="mb-4">
              <router-link
                to="admin/crop-recommendations"
                class="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700"
                >Crop Recommendations</router-link
              >
            </li>
            <li class="mb-4">
              <router-link
                to="/admin/yield-predictions"
                class="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700"
                >Yield Predictions</router-link
              >
            </li>
            <li class="mb-4">
              <router-link
                to="/admin/farming-practices"
                class="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700"
                >Farming Practices</router-link
              >
            </li>
            <li class="mb-4">
              <router-link
                to="/admin/market-insights"
                class="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700"
                >Market Insights</router-link
              >
            </li>
            <li class="mb-4">
              <router-link
                to="/admin/chat"
                class="block p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700"
                >Chat</router-link
              >
            </li>
          </ul>
        </nav>
      </aside>
      <main class="flex-1 p-6">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
import DarkModeToggle from "../components/DarkModeToggle.vue";

export default {
  name: "AdminView",
  components: {
    DarkModeToggle,
  },
};
</script>

<style scoped>
body {
  @apply dark:bg-gray-900 dark:text-white;
}
</style>
