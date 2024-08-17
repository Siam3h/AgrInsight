<template>
  <div
    class="flex items-center justify-between bg-white p-4 rounded-lg shadow mb-4"
  >
    <div class="flex items-center">
      <div class="bg-green-100 p-2 rounded-lg">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 text-green-600"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 10h4l3 6 4-8 3 4h4M14 10h7m-7 0l-7 8m-7-4v-6m0 0L5 4m2 6h.01M13 10h.01"
          />
        </svg>
      </div>
      <div class="ml-4">
        <h3 class="font-semibold">{{ transaction.name }}</h3>
        <p class="text-sm text-gray-500">{{ transaction.date }}</p>
      </div>
    </div>
    <p class="text-green-700 font-semibold">{{ transaction.amount }}</p>
  </div>
</template>

<script>
export default {
  props: {
    transaction: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
/* Additional styling if needed */
</style>
