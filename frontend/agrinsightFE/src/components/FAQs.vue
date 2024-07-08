<template>
  <div class="p-8 mx-100">
    <h2 class="text-2xl font-bold mb-6">Frequently Asked Questions</h2>
    <p class="mb-6">
      If you have any other questions, please feel free to
      <router-link to="/contact" class="text-blue-500">contact us</router-link>.
    </p>
    <div class="border-t border-b divide-y">
      <div
        v-for="(faq, index) in faqs"
        :key="index"
        class="py-4 cursor-pointer"
        @click="toggleFaq(index)"
      >
        <div class="flex justify-between items-center">
          <span>{{ faq.question }}</span>
          <span class="text-xl">{{ faq.isOpen ? "-" : "+" }}</span>
        </div>
        <div v-if="faq.isOpen" class="mt-2 text-gray-700">
          {{ faq.answer }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      faqs: [
        {
          question: "How does your platform predict crop yields?",
          answer:
            "Our platform uses advanced machine learning algorithms that analyze historical data, weather patterns, soil conditions, and other factors to predict crop yields accurately. The models are continuously updated to ensure the most accurate predictions.",
          isOpen: false,
        },
        {
          question: "How do crop recommendations work?",
          answer:
            "Our platform analyzes the data provided and suggests the best crops to plant based on factors like soil quality, weather patterns, market demand, and historical performance. The recommendations aim to maximize yield and profitability.",
          isOpen: false,
        },
        {
          question: "Can your platform help with pest and disease management?",
          answer:
            "Yes, our platform includes features that help identify potential pest and disease threats based on current conditions and historical data. It also provides recommendations for preventative measures and treatments.",
          isOpen: false,
        },
        {
          question: "How secure is my data on your platform?",
          answer:
            "Data security is our top priority. We use industry-standard encryption and security measures to protect your data. Only authorized personnel have access to your information, and it is never shared with third parties without your consent.",
          isOpen: false,
        },
        {
          question:
            "Can I integrate your platform with my existing farm management software?",
          answer:
            "Yes, our platform is designed to be compatible with most farm management software. We provide APIs and support to help you integrate our solution seamlessly into your existing workflow.",
          isOpen: false,
        },
      ],
    };
  },
  methods: {
    toggleFaq(index) {
      this.faqs[index].isOpen = !this.faqs[index].isOpen;
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>
