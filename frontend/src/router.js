import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "./components/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  // Add other routes here
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
