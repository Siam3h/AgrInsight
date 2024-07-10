<template>
  <div
    class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2
        class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900"
      >
        Sign up for an account
      </h2>
      <p class="mt-2 text-center text-sm leading-5 text-gray-600">
        Or
        <a
          href="/signin"
          class="font-medium text-indigo-600 hover:text-indigo-500 transition duration-150 ease-in-out"
        >
          sign in to your existing account
        </a>
      </p>
    </div>
    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <form class="space-y-6" @submit.prevent="handleSubmit">
          <div>
            <label
              for="name"
              class="block text-sm font-medium leading-5 text-gray-700"
            >
              Full Name
            </label>
            <div class="mt-1 rounded-md shadow-sm">
              <input
                id="name"
                name="name"
                type="text"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5"
              />
            </div>
          </div>
          <div>
            <label
              for="email"
              class="block text-sm font-medium leading-5 text-gray-700"
            >
              Email address
            </label>
            <div class="mt-1 rounded-md shadow-sm">
              <input
                id="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5"
              />
            </div>
          </div>
          <div>
            <label
              for="password"
              class="block text-sm font-medium leading-5 text-gray-700"
            >
              Password
            </label>
            <div class="mt-1 rounded-md shadow-sm">
              <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5"
              />
            </div>
          </div>
          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input
                id="terms"
                name="terms"
                type="checkbox"
                required
                class="form-checkbox h-4 w-4 text-indigo-600 transition duration-150 ease-in-out"
              />
              <label
                for="terms"
                class="ml-2 block text-sm leading-5 text-gray-900"
              >
                I agree to the
                <a
                  href="#"
                  class="font-medium text-indigo-600 hover:text-indigo-500 transition duration-150 ease-in-out"
                >
                  Terms and Conditions
                </a>
              </label>
            </div>
          </div>
          <div>
            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out"
            >
              Sign up
            </button>
          </div>
        </form>
        <div class="mt-6">
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-gray-300"></div>
            </div>
            <div class="relative flex justify-center text-sm leading-5">
              <span class="px-2 bg-white text-gray-500">
                Or continue with
              </span>
            </div>
          </div>
          <div class="mt-6 grid grid-cols-2 gap-3">
            <div>
              <button
                @click="handleGoogleSignIn"
                class="w-full inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white text-sm leading-5 font-medium text-gray-500 hover:bg-gray-50 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-gray-50 active:text-gray-800 transition duration-150 ease-in-out"
              >
                <svg
                  class="w-5 h-5 mr-2"
                  aria-hidden="true"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    d="M21.35 11.1H12v2.8h5.3c-.2 1.2-1 2.3-2.1 2.9v2.4h3.5c2-1.8 3.1-4.4 3.1-7.1 0-.8-.1-1.5-.2-2.2z"
                    fill="#4285F4"
                  />
                  <path
                    d="M12 22c2.7 0 5-1 6.6-2.6l-3.5-2.4c-.8.5-1.7.8-2.8.8-2.2 0-4-1.5-4.6-3.5H4.1v2.5C5.7 19.7 8.6 22 12 22z"
                    fill="#34A853"
                  />
                  <path
                    d="M7.4 13.3c-.2-.8-.2-1.7 0-2.5V8.3H4.1c-1 2-1 4.2 0 6.2l3.3-1.2z"
                    fill="#FBBC05"
                  />
                  <path
                    d="M12 5.4c1.3 0 2.4.5 3.3 1.3l2.4-2.4C16.9 2.6 14.6 2 12 2 8.6 2 5.7 4.3 4.1 7.3l3.3 2.5c.7-2 2.5-3.4 4.6-3.4z"
                    fill="#EA4335"
                  />
                  <path fill="none" d="M0 0h24v24H0z" />
                </svg>
                Google
              </button>
            </div>
            <div>
              <button
                @click="handleFacebookSignIn"
                class="w-full inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm bg-white text-sm leading-5 font-medium text-gray-500 hover:bg-gray-50 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-gray-50 active:text-gray-800 transition duration-150 ease-in-out"
              >
                <svg
                  class="w-5 h-5 mr-2"
                  aria-hidden="true"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    d="M22.675 0h-21.35C.595 0 0 .595 0 1.325v21.351c0 .73.595 1.325 1.325 1.325H12.82v-9.3H9.692V10.5h3.127v-2.8c0-3.1 1.894-4.793 4.66-4.793 1.325 0 2.462.1 2.793.143v3.24h-1.914c-1.504 0-1.794.714-1.794 1.762V10.5h3.588l-.467 3.2h-3.121v9.3h6.121c.73 0 1.325-.595 1.325-1.325V1.325C24 .595 23.405 0 22.675 0z"
                  />
                  <path fill="none" d="M0 0h24v24H0z" />
                </svg>
                Facebook
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Signup",
  methods: {
    handleSubmit() {
      // Handle form submission
    },
    handleGoogleSignIn() {
      // Handle Google sign-in
    },
    handleFacebookSignIn() {
      // Handle Facebook sign-in
    },
  },
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
