<template>
  <v-app>
    <AppNavbar />
    <HeroSection />
    <v-container>
      <OurPartners />
      <OurStory />
      <CustomerTestimonial />
    </v-container>
    <AppFooter />
  </v-app>
</template>

<script>
import AppNavbar from "@/components/AppNavbar.vue";
import HeroSection from "@/components/HeroSection.vue";
import OurPartners from "@/components/OurPartners.vue";
import OurStory from "@/components/OurStory.vue";
import CustomerTestimonial from "@/components/CustomerTestimonial.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  components: {
    AppNavbar,
    HeroSection,
    OurPartners,
    OurStory,
    CustomerTestimonial,
    AppFooter,
  },
};
</script>

<style scoped>
/* Home styles */
</style>
