<template>
  <div class="bg-green-10">
    <header class="absolute inset-x-0 top-0 z-50">
      <nav
        class="flex items-center justify-between p-6 lg:px-8"
        aria-label="Global"
      >
        <div class="flex lg:flex-1">
          <a href="/" class="-m-1.5 p-1.5 flex items-center">
            <span
              class="block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
            >
              Agr<span class="font-bold sr-m">Insight Inc</span>
            </span>
          </a>
        </div>
        <div class="flex lg:hidden">
          <button
            type="button"
            class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
            @click="mobileMenuOpen = true"
          >
            <span class="sr-only">Open main menu</span>
            <Bars3Icon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="hidden lg:flex lg:gap-x-12">
          <a
            v-for="item in navigation"
            :key="item.name"
            :href="item.href"
            class="text-sm font-semibold leading-6 text-gray-900"
            >{{ item.name }}</a
          >
          <div class="relative" @mouseleave="dropdownOpen = false">
            <button
              @mouseenter="dropdownOpen = true"
              @click="dropdownOpen = !dropdownOpen"
              class="flex items-center text-sm font-semibold leading-6 text-gray-900"
            >
              Features
              <ChevronDownIcon class="ml-1 h-5 w-2" aria-hidden="true" />
            </button>
            <div
              v-if="dropdownOpen"
              class="absolute z-10 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
            >
              <a
                v-for="feature in features"
                :key="feature.name"
                :href="feature.href"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                @click="dropdownOpen = false"
                >{{ feature.name }}</a
              >
            </div>
          </div>
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end">
          <a
            href="/signin"
            class="text-sm font-semibold leading-6 text-gray-900"
            >Log in <span aria-hidden="true">&rarr;</span></a
          >
        </div>
      </nav>
      <Dialog
        class="lg:hidden"
        @close="mobileMenuOpen = false"
        :open="mobileMenuOpen"
      >
        <div class="fixed inset-0 z-50" />
        <DialogPanel
          class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10"
        >
          <div class="flex items-center justify-between">
            <a href="/" class="-m-1.5 p-1.5">
              <span class="sr-only">Agri Insight Inc</span>
              <img
                class="h-18 w-auto"
                src="@/assets/images/logo_title.png"
                alt=""
              />
            </a>
            <button
              type="button"
              class="-m-2.5 rounded-md p-2.5 text-gray-700"
              @click="mobileMenuOpen = false"
            >
              <span class="sr-only">Close menu</span>
              <XMarkIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div class="mt-6 flow-root">
            <div class="-my-6 divide-y divide-gray-500/10">
              <div class="space-y-2 py-6">
                <a
                  v-for="item in navigation"
                  :key="item.name"
                  :href="item.href"
                  class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >{{ item.name }}</a
                >
                <div class="relative">
                  <button
                    @click="mobileDropdownOpen = !mobileDropdownOpen"
                    class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >
                    Features
                    <ChevronDownIcon class="ml-1 h-5 w-5" aria-hidden="true" />
                  </button>
                  <div
                    v-if="mobileDropdownOpen"
                    class="mt-2 w-full rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
                  >
                    <a
                      v-for="feature in features"
                      :key="feature.name"
                      :href="feature.href"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      @click="mobileDropdownOpen = false"
                      >{{ feature.name }}</a
                    >
                  </div>
                </div>
              </div>
              <div class="py-6">
                <a
                  href="/signin"
                  class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >Log in</a
                >
              </div>
            </div>
          </div>
        </DialogPanel>
      </Dialog>
    </header>

    <div class="relative isolate px-6 pt-14 lg:px-8">
      <div
        class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
        aria-hidden="true"
      >
        <div
          class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
          style="
            clip-path: polygon(
              74.1% 44.1%,
              100% 61.6%,
              97.5% 26.9%,
              85.5% 0.1%,
              80.7% 2%,
              72.5% 32.5%,
              60.2% 62.4%,
              52.4% 68.1%,
              47.5% 58.3%,
              45.2% 34.5%,
              27.5% 76.7%,
              0.1% 64.9%,
              17.9% 100%,
              27.6% 76.8%,
              76.1% 97.7%,
              74.1% 44.1%
            );
          "
        />
      </div>
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="hidden sm:mb-8 sm:flex sm:justify-center">
          <div
            class="relative rounded-full px-3 py-1 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20"
          >
            <span>Unlocking the Future of Agriculture</span>
          </div>
        </div>
        <div class="text-center">
          <h1
            class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl"
          >
            Enhance Your Farming Experience
          </h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">
            Discover insights to boost crop yield, receive personalized crop
            recommendations, and adopt best farming practices. Empower your
            farming decisions with data-driven solutions.
          </p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <a
              href="/signup"
              class="rounded-md bg-green-900 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >Get started</a
            >
            <a
              href="/about"
              class="text-sm font-semibold leading-6 text-gray-900"
              >Learn more <span aria-hidden="true">→</span></a
            >
          </div>
        </div>
      </div>
      <div
        class="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
        aria-hidden="true"
      >
        <div
          class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]"
          style="
            clip-path: polygon(
              74.1% 44.1%,
              100% 61.6%,
              97.5% 26.9%,
              85.5% 0.1%,
              80.7% 2%,
              72.5% 32.5%,
              60.2% 62.4%,
              52.4% 68.1%,
              47.5% 58.3%,
              45.2% 34.5%,
              27.5% 76.7%,
              0.1% 64.9%,
              17.9% 100%,
              27.6% 76.8%,
              76.1% 97.7%,
              74.1% 44.1%
            );
          "
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { Dialog, DialogPanel } from "@headlessui/vue";
import {
  Bars3Icon,
  XMarkIcon,
  ChevronDownIcon,
} from "@heroicons/vue/24/outline";

const navigation = [
  { name: "Home", href: "/" },
  { name: "About", href: "/about" },
];

const features = [
  { name: "Crop Recommendation", href: "/about/recommender/" },
  { name: "Crop Yield", href: "/about/yield/" },
  { name: "Farming Practices", href: "/about/insights/" },
];

const mobileMenuOpen = ref(false);
const dropdownOpen = ref(false);
const mobileDropdownOpen = ref(false);
</script>

<style scoped>
.logo {
  height: 80%;
  width: auto;
  max-height: 50px;
}
</style>
