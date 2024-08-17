<template>
  <aside class="bg-green-100 h-screen p-4">
    <div class="flex items-center justify-center mb-6">
      <img src="@/assets/images/black_logo.png" alt="Agrobee" class="h-8" />
    </div>
    <ul>
      <li v-for="item in menuItems" :key="item.name" class="mb-4">
        <router-link
          :to="item.link"
          class="flex items-center text-green-800 hover:bg-green-200 p-2 rounded-lg"
        >
          <item.icon class="mr-3" />
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
        { name: "Dashboard", link: "/", icon: ComputerDesktopIcon },
        { name: "Shop", link: "/shop", icon: ShoppingCartIcon },
        { name: "Community", link: "/community", icon: UserGroupIcon },
        { name: "Orders", link: "/orders", icon: ShoppingBagIcon },
        { name: "Report", link: "/report", icon: ReceiptPercentIcon },
      ],
    };
  },
};
</script>

<style scoped>
/* Additional styling here */
</style>
