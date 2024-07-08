<template>
  <div>
    <v-footer app>
      <v-container>
        <v-row>
          <v-col cols="12" md="3">
            <h3>AgriVista.</h3>
            <p>
              Our platform is dedicated to helping farmers and agricultural
              professionals thrive by providing access to valuable resources,
              expert advice, and a supportive community.
            </p>
          </v-col>
          <v-col cols="12" md="3">
            <h4>Navigate</h4>
            <v-list>
              <v-list-item
                v-for="(link, index) in navigationLinks"
                :key="index"
              >
                <v-list-item-content>
                  <v-list-item-title>
                    <a :href="link.href">{{ link.text }}</a>
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-col>
          <v-col cols="12" md="3">
            <h4>Support Us</h4>
            <v-list>
              <v-list-item v-for="(link, index) in supportLinks" :key="index">
                <v-list-item-content>
                  <v-list-item-title>
                    <a :href="link.href">{{ link.text }}</a>
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-col>
          <v-col cols="12" md="3">
            <h4>Contact Us</h4>
            <p>
              Email:
              <a href="mailto:alma.lawson@example.com"
                >alma.lawson@example.com</a
              >
            </p>
            <p>Phone: <a href="tel:+12075550119">(207) 555-0119</a></p>
          </v-col>
        </v-row>
      </v-container>
      <v-divider></v-divider>
      <v-container>
        <v-row>
          <v-col cols="12">
            <p class="text-center">
              &copy; 2023 Grodxon. We love our users! |
              <a href="#">Terms & Conditions</a> |
              <a href="#">Privacy Policy</a> | <a href="#">Sitemap</a>
            </p>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: "AppFooter",
  data() {
    return {
      navigationLinks: [
        { text: "Home", href: "#" },
        { text: "Pricing", href: "#" },
        { text: "Blog", href: "#" },
        { text: "About", href: "#" },
      ],
      supportLinks: [
        { text: "FAQs", href: "#" },
        { text: "Contact Us", href: "#" },
        { text: "Support", href: "#" },
        { text: "Security", href: "#" },
        { text: "Center", href: "#" },
      ],
    };
  },
};
</script>

<style scoped>
h3 {
  font-weight: bold;
  margin-bottom: 1rem;
}

h4 {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

v-list-item a {
  color: inherit;
  text-decoration: none;
}

.text-center {
  text-align: center;
}

v-footer {
  padding: 2rem 0;
  background-color: #f8f9fa;
}

v-container {
  max-width: 1140px;
  margin: 0 auto;
}

v-divider {
  margin: 2rem 0;
}
</style>
