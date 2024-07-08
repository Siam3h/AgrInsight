<template>
  <div class="features-section">
    <h2>Why Should You Choose AgriVista</h2>
    <v-container>
      <v-row>
        <v-col
          v-for="(feature, index) in features"
          :key="index"
          cols="12"
          md="6"
        >
          <v-card class="feature-card">
            <v-card-title>
              <v-icon class="feature-icon">{{ feature.icon }}</v-icon>
              <span>{{ feature.title }}</span>
            </v-card-title>
            <v-card-text>{{ feature.description }}</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "AppFeatures",
  data() {
    return {
      features: [
        {
          icon: "mdi-weather-sunny",
          title: "Weather Forecast Tool",
          description:
            "Understand the effects of climate change on agriculture and how farmers can adapt to ensure their crops thrive in changing conditions. Get expert tips on mitigating risks and maximizing yields.",
        },
        {
          icon: "mdi-calendar-check",
          title: "Crop Planning Calculator",
          description:
            "Understand the effects of climate change on agriculture and how farmers can adapt to ensure their crops thrive in changing conditions. Get expert tips on mitigating risks and maximizing yields.",
        },
        {
          icon: "mdi-flask",
          title: "Soil Testing Guide",
          description:
            "Understand the effects of climate change on agriculture and how farmers can adapt to ensure their crops thrive in changing conditions. Get expert tips on mitigating risks and maximizing yields.",
        },
        {
          icon: "mdi-currency-usd",
          title: "Market Price Tracker",
          description:
            "Understand the effects of climate change on agriculture and how farmers can adapt to ensure their crops thrive in changing conditions. Get expert tips on mitigating risks and maximizing yields.",
        },
      ],
    };
  },
};
</script>

<style scoped>
.features-section {
  text-align: center;
  padding: 2rem 0;
  background-color: #fff;
}

.features-section h2 {
  margin-bottom: 2rem;
}

.feature-card {
  padding: 1rem;
  margin: 1rem 0;
}

.feature-icon {
  font-size: 2rem;
  margin-right: 1rem;
}

.v-card-title {
  display: flex;
  align-items: center;
}

.v-card-text {
  text-align: left;
}
</style>
