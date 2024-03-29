<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

const q = ref("");

const requests = [
  {
    id: "8a36e9c2-966b-4573-ad8a-ce3c01e98e26",
    date: "2024-01-01",
    address_full: "123 Maple Street, Toronto, Ontario, M5V 2T6, Canada",
    payload: "2 bags of dog food and 1 bag of cat food.",
    imageUrl: "/img/Dog-Cat-Eating-240x240-1.png",
  },
  {
    id: "9d4c52f7-1e9d-430f-b6dd-1c0a3377f290",
    date: "2024-02-02",
    address_full:
      "456 Oak Avenue, Vancouver, British Columbia, V5Z 0B3, Canada",
    payload: "3 bags of cat food.",
    imageUrl: "/img/Dog-Cat-Eating-240x240-1.png",
  },
  {
    id: "62d77fa2-4f6e-427d-8744-258d12ceae49",
    date: "2024-03-03",
    address_full: "789 Pine Road, Calgary, Alberta, T2P 2M5, Canada",
    payload: "1 bag of dog food and 2 cans of cat food.",
    imageUrl: "/img/Dog-Cat-Eating-240x240-1.png",
  },
];
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Requests"> </UDashboardNavbar>

      <UDashboardPanelContent class="pb-24">
        <UDashboardSection
          icon="i-streamline-shipping-truck"
          title="Request History"
          description="Your previous requests for food."
        />

        <!-- <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight"></h2> -->

        <RequestList
          title="Request History"
          description=""
          :cta="true"
          :requests="requests"
        />
      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>
</template>
