<template>
  <div>
    <NavBar />
    <PlatformOverview />
    <HowItWorks />
    <UserTestimonials />
    <LogoClouds />
    <Team />
    <div class="border-t border-gray-300"></div>
    <Contact />
    <Footer />
  </div>
</template>

<script>
import LogoClouds from "../components/LogoClouds.vue";
import Footer from "../components/Footer.vue";
import AboutVideoEmbed from "@/components/AboutVideoEmbed.vue";
import PlatformOverview from "@/components/PlatformOverview.vue";
import HowItWorks from "@/components/HowItWorks.vue";
import UserTestimonials from "@/components/UserTestimonials.vue";
import Team from "@/components/Team.vue";
import Contact from "@/components/Contact.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "AboutView",
  components: {
    NavBar,
    PlatformOverview,
    AboutVideoEmbed,
    HowItWorks,
    UserTestimonials,
    Team,
    Contact,
    Footer,
    LogoClouds,
  },
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>
