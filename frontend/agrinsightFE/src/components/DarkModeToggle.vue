<template>
  <button
    @click="toggleDarkMode"
    class="p-2 bg-gray-200 dark:bg-gray-700 rounded"
  >
    Toggle Dark Mode
  </button>
</template>

<script>
export default {
  name: "DarkModeToggle",
  methods: {
    toggleDarkMode() {
      document.documentElement.classList.toggle("dark");
    },
  },
};
</script>
