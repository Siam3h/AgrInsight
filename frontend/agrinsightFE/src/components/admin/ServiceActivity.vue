<template>
  <div class="bg-white p-4 rounded-lg shadow">
    <h2 class="text-xl font-semibold mb-4">Services Activity</h2>
    <ul>
      <li v-for="activity in activities" :key="activity.name" class="mb-2">
        <div class="flex items-center">
          <activity.icon class="h-6 w-6 text-green-700 mr-2" />
          <span>{{ activity.name }}</span>
        </div>
        <p class="text-sm text-gray-500">{{ activity.time }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import { LanguageIcon } from "@heroicons/vue/24/outline";

export default {
  data() {
    return {
      activities: [
        { name: "Available Labs", time: "1 min ago", icon: LanguageIcon },
        { name: "Available Drones", time: "2 min ago", icon: LanguageIcon },
        { name: "Expert Consult", time: "3 min ago", icon: LanguageIcon },
        { name: "Renting and bookings", time: "4 min ago", icon: LanguageIcon },
      ],
    };
  },
};
</script>
