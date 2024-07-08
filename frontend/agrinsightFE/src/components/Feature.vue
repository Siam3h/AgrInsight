<template>
  <section class="bg-gray-900 text-white py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <p class="text-indigo-500 font-semibold mb-2">Deploy faster</p>
      <h2 class="text-3xl md:text-4xl font-extrabold mb-4">
        Everything you need to deploy your app
      </h2>
      <p class="text-lg max-w-3xl mx-auto mb-12">
        Quis tellus eget adipiscing convallis sit sit eget aliquet quis.
        Suspendisse eget egestas a elementum pulvinar et feugiat blandit at. In
        mi viverra elit nunc.
      </p>
    </div>
    <div
      class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-3 gap-8 text-left"
    >
      <div class="feature-card">
        <div class="flex items-center mb-4">
          <i class="fas fa-cloud-upload-alt text-indigo-500 text-2xl"></i>
          <h3 class="ml-2 text-lg font-semibold">Push to deploy</h3>
        </div>
        <p class="text-gray-400 mb-4">
          Commodo nec sagittis tortor mauris sed. Turpis tortor quis scelerisque
          diam id accumsan nullam tempus. Pulvinar etiam lacus volutpat eu.
          Phasellus praesent ligula sit faucibus.
        </p>
        <a href="#" class="text-indigo-500 hover:text-indigo-400"
          >Learn more &rarr;</a
        >
      </div>
      <div class="feature-card">
        <div class="flex items-center mb-4">
          <i class="fas fa-lock text-indigo-500 text-2xl"></i>
          <h3 class="ml-2 text-lg font-semibold">SSL certificates</h3>
        </div>
        <p class="text-gray-400 mb-4">
          Pellentesque enim a commodo malesuada turpis eleifend risus. Facilisis
          donec placerat sapien consequat tempor fermentum nibh.
        </p>
        <a href="#" class="text-indigo-500 hover:text-indigo-400"
          >Learn more &rarr;</a
        >
      </div>
      <div class="feature-card">
        <div class="flex items-center mb-4">
          <i class="fas fa-sync-alt text-indigo-500 text-2xl"></i>
          <h3 class="ml-2 text-lg font-semibold">Simple queues</h3>
        </div>
        <p class="text-gray-400 mb-4">
          Pellentesque sit elit congue ante nec amet. Dolor aenean curabitur
          viverra suspendisse iaculis eget. Nec mollis placerat ultricies
          euismod ut condimentum.
        </p>
        <a href="#" class="text-indigo-500 hover:text-indigo-400"
          >Learn more &rarr;</a
        >
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Feature",
};
</script>

<style scoped>
.feature-card {
  background-color: #1a1a2e;
  padding: 20px;
  border-radius: 8px;
}
</style>
