import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AdminView from "../views/AdminView.vue";

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
      name: "AdminView",
      component: AdminView,
    },
    {
      path: "/admin/crop-recommendations",
      name: "CropRecommendations",
      component: () => import("../components/AdminCropRecommender.vue"),
    },
    {
      path: "/admin/yield-predictions",
      name: "YieldPredictions",
      component: () => import("../components/AdminCopYieldPredictor.vue"),
    },
    {
      path: "/admin/farming-practices",
      name: "FarmingPractices",
      component: () => import("../components/AdminInsights.vue"),
    },
    {
      path: "/admin/market-insights",
      name: "MarketInsights",
      component: () => import("../components/AdminMarketInsights.vue"),
    },
    {
      path: "/admin/chat",
      name: "Chat",
      component: () => import("../components/AdminChat.vue"),
    },
    {
      path: "/privacy-policy/",
      name: "PrivacyPolicy",
      component: () => import("../views/PrivacyPolicyView.vue"),
    },
    {
      path: "/terms-of-service/",
      name: "TermsOfService",
      component: () => import("../views/TermsView.vue"),
    },
    {
      path: "/404/",
      name: "404",
      component: () => import("../components/404.vue"),
    },
    {
      path: "/soon/",
      name: "Soon",
      component: () => import("../components/ComingSoon.vue"),
    },
    {
      path: "/contact/",
      name: "contact",
      component: () => import("../components/Contact.vue"),
    },
  ],
});

export default router;
