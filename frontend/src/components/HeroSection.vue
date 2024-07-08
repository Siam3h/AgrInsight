<template>
  <v-container fluid class="hero-section">
    <v-row>
      <v-col class="text-center">
        <img
          src="https://images.app.goo.gl/46z98U74KJd7WmMVA"
          alt="Hero Background"
          class="hero-bg"
        />
        <div class="hero-content">
          <h1>Empowering Agriculture for a Sustainable Future</h1>
          <p>
            Honor the traditions of farming while embracing modern innovations.
            Our platform offers a balanced approach combining time-tested
            methods with cutting-edge technology to help you achieve optimal
            results.
          </p>
          <v-btn color="primary" class="mr-4">Join Now</v-btn>
          <v-btn outlined>Learn More</v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Hero-Section",
};
</script>

<style scoped>
.hero-section {
  position: relative;
}
.hero-bg {
  width: 100%;
  height: auto;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
.hero-content {
  margin-top: 20vh;
}
</style>
