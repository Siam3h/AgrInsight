<template>
  <aside class="bg-green-100 h-screen p-4">
    <div class="flex items-center justify-center mb-6">
      <img src="@/assets/images/logo.png" alt="AgrInsight" class="h-8" />
    </div>
    <ul>
      <li v-for="item in menuItems" :key="item.name" class="mb-4">
        <router-link
          :to="item.link"
          class="flex items-center text-green-800 hover:bg-green-200 p-2 rounded-lg"
        >
          <component :is="item.icon" class="mr-3 h-5 w-5" />
          <span>{{ item.name }}</span>
        </router-link>
      </li>
    </ul>
  </aside>
</template>

<script>
import {
  ComputerDesktopIcon,
  ShoppingBagIcon,
  UserGroupIcon,
  ShoppingCartIcon,
  ReceiptPercentIcon,
} from "@heroicons/vue/24/outline";

export default {
  data() {
    return {
      menuItems: [
        {
          name: "Recommender",
          link: "/admin/crop-recommendations",
          icon: ComputerDesktopIcon,
        },
        {
          name: "Yield Predictor",
          link: "/admin/yield-predictions",
          icon: ShoppingCartIcon,
        },
        {
          name: "Farming Practices",
          link: "/admin/farming-practices",
          icon: UserGroupIcon,
        },
        {
          name: "Market Place",
          link: "/admin/market-insights",
          icon: ShoppingBagIcon,
        },
        { name: "Chat", link: "/admin/chat", icon: ReceiptPercentIcon },
        {
          name: "Contact Us",
          link: "/contact/",
          icon: ShoppingBagIcon,
        },
      ],
    };
  },
};
</script>

<style scoped>
/* Additional styling here */
</style>
