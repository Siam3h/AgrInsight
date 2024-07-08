<template>
  <div class="our-story-section">
    <v-container>
      <v-row>
        <v-col cols="12" md="6">
          <h2>Our Story</h2>
          <p>
            Agriculture is the backbone of our world, providing essential
            resources and sustaining communities. At <strong>AgriVista</strong>,
            we are passionate about supporting farmers and agricultural
            professionals by offering innovative tools, comprehensive resources,
            and a vibrant community. Founded in <strong>[Year]</strong>, our
            mission is to empower agriculture through knowledge, technology, and
            collaboration.
          </p>
        </v-col>
        <v-col cols="12" md="6">
          <v-img
            src="https://images.app.goo.gl/46z98U74KJd7WmMVA"
            alt="Agriculture"
            class="our-story-image"
          ></v-img>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "OurStory",
};
</script>

<style scoped>
.our-story-section {
  padding: 2rem 0;
  background-color: #f8f9fa;
  text-align: left;
}

.our-story-section h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.our-story-section p {
  font-size: 1.1rem;
  line-height: 1.6;
}

.our-story-image {
  border-radius: 8px;
}
</style>
