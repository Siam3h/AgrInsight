<template>
  <div class="p-8 mx-100">
    <h2 class="text-2xl font-bold mb-6">Frequently asked questions</h2>
    <div class="border-t border-b divide-y">
      <div
        v-for="(faq, index) in faqs"
        :key="index"
        class="py-4 flex justify-between items-center cursor-pointer"
        @click="toggleFaq(index)"
      >
        <span>{{ faq.question }}</span>
        <span class="text-xl">+</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      faqs: [
        { question: "What's the best thing about Switzerland?" },
        { question: "How do you make holy water?" },
        { question: "What do you call someone with no body and no nose?" },
        { question: "Why do you never see elephants hiding in trees?" },
        { question: "Why can't you hear a pterodactyl go to the bathroom?" },
        { question: "Why did the invisible man turn down the job offer?" },
      ],
    };
  },
  methods: {
    toggleFaq(index) {
      // Handle FAQ item click event (for future use if needed)
      console.log(`Toggled FAQ ${index}`);
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>
