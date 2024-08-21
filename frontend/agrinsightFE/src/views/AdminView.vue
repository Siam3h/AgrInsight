<template>
  <div>
    <div class="flex">
      <Sidebar />

      <main class="flex-1 p-6 bg-gray-100">
        <section
          class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-6"
        >
          <MapRecommender className="sm:col-span-2 lg:col-span-1" />
          <StatusCard className="sm:col-span-1 lg:col-span-1" />
        </section>

        <section class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <ActivityChart />
          <ServiceActivity />
          <RecentActivity />
        </section>

        <section class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6 pt-6">
          <div>
            <h2 class="text-xl font-semibold mb-4">Top Sellers</h2>
            <SellerCard
              class="mt-6"
              v-for="seller in topSellers"
              :key="seller.id"
              :seller="seller"
            />
          </div>

          <div>
            <h2 class="text-xl font-semibold mb-4">Recent Transactions</h2>
            <TransactionCard
              v-for="transaction in recentTransactions"
              :key="transaction.id"
              :transaction="transaction"
            />
          </div>
        </section>
      </main>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import Sidebar from "@/components/admin/SideBar.vue";
import Header from "@/components/admin/Header.vue";
import StatusCard from "@/components/admin/StatusCard.vue";
import ActivityChart from "@/components/admin/ActivityChart.vue";
import ServiceActivity from "@/components/admin/ServiceActivity.vue";
import SellerCard from "@/components/admin/SellerCard.vue";
import TransactionCard from "@/components/admin/TransactionCard.vue";
import RecentActivity from "@/components/admin/RecentActivity.vue";
import MapRecommender from "@/components/admin/MapRecommender.vue";

export default {
  components: {
    Sidebar,
    Header,
    StatusCard,
    ActivityChart,
    ServiceActivity,
    SellerCard,
    TransactionCard,
    RecentActivity,
    Footer,
    MapRecommender,
  },
  data() {
    return {
      topSellers: [
        {
          id: 1,
          name: "John Doe",
          sales: 1542,
          avatar: "@/assets/images/logo.png",
        },
        {
          id: 2,
          name: "Jane Smith",
          sales: 1300,
          avatar: "@/assets/images/logo.png",
        },
      ],
      recentTransactions: [
        { id: 1, name: "Order #1234", amount: "$230.00", date: "2024-08-16" },
        { id: 2, name: "Order #1235", amount: "$120.00", date: "2024-08-16" },
      ],
    };
  },
};
</script>

<style scoped>
/* Additional styling here */
</style>
