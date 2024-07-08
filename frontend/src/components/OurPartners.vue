<template>
  <v-container class="partners">
    <h2>Some of Our Awesome Partners</h2>
    <v-row>
      <v-col v-for="partner in partners" :key="partner.name" cols="12" md="2">
        <img :src="partner.logo" :alt="partner.name" class="partner-logo" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "OurPartners",
  data() {
    return {
      partners: [
        { name: "Deliveroo", logo: require("@/assets/images/logo.png") },
        { name: "Tech", logo: require("@/assets/images/logo.png") },
        { name: "Logite", logo: require("@/assets/images/logo.png") },
        { name: "Delivery", logo: require("@/assets/images/logo.png") },
        { name: "Salesforce", logo: require("@/assets/images/logo.png") },
      ],
    };
  },
};
</script>

<style scoped>
.partner-logo {
  width: 100%;
  max-width: 150px;
}
</style>
