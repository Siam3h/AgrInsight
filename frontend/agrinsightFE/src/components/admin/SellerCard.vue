<template>
  <div class="flex items-center p-2 bg-white rounded-lg shadow">
    <img :src="seller.avatar" alt="Seller" class="h-10 w-10 rounded-full" />
    <div class="ml-4">
      <h3 class="font-semibold">{{ seller.name }}</h3>
      <p class="text-sm text-gray-500">{{ seller.sales }} plants sold</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["seller"],
};
</script>
