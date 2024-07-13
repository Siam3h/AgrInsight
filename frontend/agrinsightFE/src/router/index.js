import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/SignUpView.vue"),
    },
    {
      path: "/signin",
      name: "signin",
      component: () => import("../views/SignInView.vue"),
    },
    {
      path: "/about/recommender/",
      name: "aboutRecommender",
      component: () => import("../views/AboutRecommenderView.vue"),
    },
    {
      path: "/about/yield/",
      name: "aboutYield",
      component: () => import("../views/AboutYieldView.vue"),
    },
    {
      path: "/about/insights",
      name: "aboutInsights",
      component: () => import("../views/AboutInsightsView.vue"),
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("../views/AdminView.vue"),
    },
  ],
});

export default router;
