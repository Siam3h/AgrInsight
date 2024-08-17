<template>
  <div class="bg-white p-4 rounded-lg shadow">
    <h2 class="text-xl font-semibold mb-4">Recent Activity</h2>
    <ul>
      <li v-for="activity in activities" :key="activity.user" class="mb-2">
        <div class="flex items-center">
          <img
            :src="activity.avatar"
            alt="User"
            class="h-8 w-8 rounded-full mr-2"
          />
          <div>
            <p class="font-semibold">{{ activity.user }}</p>
            <p class="text-sm text-gray-500">{{ activity.action }}</p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activities: [
        {
          user: "Siddharth Ram",
          action: "Ordered a new product",
          avatar: "@/assets/images/black_logo.png",
        },
        {
          user: "Isiah Reddy",
          action: "Ordered a new product",
          avatar: "@/assets/images/black_logo.png",
        },
      ],
    };
  },
};
</script>
