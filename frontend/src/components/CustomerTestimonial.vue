<template>
  <div class="testimonial-section">
    <h2>What Our Customers Are Saying</h2>
    <v-carousel
      cycle
      interval="4000"
      hide-delimiters
      show-arrows-on-hover
      class="testimonial-carousel"
    >
      <v-carousel-item
        v-for="(testimonial, index) in testimonials"
        :key="index"
      >
        <div class="testimonial-item">
          <v-avatar size="64" class="testimonial-avatar">
            <img :src="testimonial.image" alt="Customer Avatar" />
          </v-avatar>
          <p class="testimonial-quote">"{{ testimonial.quote }}"</p>
          <p class="testimonial-name">{{ testimonial.name }}</p>
        </div>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
export default {
  name: "CustomerTestimonial",
  data() {
    return {
      testimonials: [
        {
          image: "https://images.app.goo.gl/46z98U74KJd7WmMVA",
          quote:
            "I'm hooked on Oliq's high-quality oil - it's now a staple in my kitchen. It made my homemade pasta taste like I was back in Italy",
          name: "Jennifer Austin",
        },
        {
          image: "https://images.app.goo.gl/46z98U74KJd7WmMVA",
          quote:
            "The tools and resources provided by AgriVista have significantly improved our crop yields and overall farm efficiency.",
          name: "Mark Johnson",
        },
        {
          image: "https://images.app.goo.gl/46z98U74KJd7WmMVA",
          quote:
            "AgriVista's platform is user-friendly and incredibly helpful for new farmers like me. I highly recommend it!",
          name: "Samantha Lee",
        },
      ],
    };
  },
};
</script>

<style scoped>
.testimonial-section {
  text-align: center;
  padding: 2rem 0;
  background-color: #f8f9fa;
}

.testimonial-carousel {
  max-width: 800px;
  margin: 0 auto;
}

.testimonial-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.testimonial-avatar {
  margin-bottom: 1rem;
}

.testimonial-quote {
  font-size: 1.2rem;
  font-style: italic;
  margin-bottom: 0.5rem;
}

.testimonial-name {
  font-weight: bold;
  color: #333;
}
</style>
