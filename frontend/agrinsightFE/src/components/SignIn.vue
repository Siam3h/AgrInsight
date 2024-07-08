<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md bg-white p-8 rounded-lg shadow-lg">
      <h2 class="text-2xl font-bold mb-6 text-center">Sign In</h2>
      <form @submit.prevent="handleSignIn">
        <div class="mb-4">
          <label for="email" class="block text-gray-700 mb-2">Email</label>
          <input
            v-model="email"
            type="email"
            id="email"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-indigo-500"
            required
          />
        </div>
        <div class="mb-4">
          <label for="password" class="block text-gray-700 mb-2"
            >Password</label
          >
          <input
            v-model="password"
            type="password"
            id="password"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-indigo-500"
            required
          />
        </div>
        <div class="flex items-center justify-between mb-6">
          <div>
            <input
              type="checkbox"
              id="remember_me"
              class="mr-2"
              v-model="rememberMe"
            />
            <label for="remember_me" class="text-gray-700">Remember me</label>
          </div>
          <a href="#" class="text-indigo-500 hover:text-indigo-700"
            >Forgot password?</a
          >
        </div>
        <button
          type="submit"
          class="w-full bg-indigo-500 text-white py-2 rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring focus:border-indigo-500 mb-4"
        >
          Sign In
        </button>
      </form>
      <p class="text-center text-gray-600 mb-4">or sign in with</p>
      <div class="flex justify-center space-x-4 mb-4">
        <button
          @click="handleGmailSignIn"
          class="flex items-center bg-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-700 focus:outline-none focus:ring"
        >
          <i class="fab fa-google mr-2"></i> Gmail
        </button>
        <button
          @click="handleFacebookSignIn"
          class="flex items-center bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-800 focus:outline-none focus:ring"
        >
          <i class="fab fa-facebook-f mr-2"></i> Facebook
        </button>
      </div>
      <p class="text-center text-gray-600">
        Don't have an account?
        <a href="/signup" class="text-indigo-500 hover:text-indigo-700"
          >Sign up</a
        >
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      rememberMe: false,
    };
  },
  methods: {
    handleSignIn() {
      // Handle the sign-in process
      console.log("Sign-In Attempt", {
        email: this.email,
        password: this.password,
        rememberMe: this.rememberMe,
      });
      // Add your sign-in logic here
    },
    handleGmailSignIn() {
      // Handle Gmail sign-in process
      console.log("Gmail Sign-In Attempt");
      // Add your Gmail sign-in logic here
    },
    handleFacebookSignIn() {
      // Handle Facebook sign-in process
      console.log("Facebook Sign-In Attempt");
      // Add your Facebook sign-in logic here
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>
