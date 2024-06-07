<script setup lang="ts">
defineProps<{
	requests: never[];
}>()
</script>

<template>
	<UDashboardPanelContent>

    <UDashboardSection
      icon="i-heroicons-user"
      title="Volunteer Portal"
      description="Delivery list, your delivery area, and history."
      />

    <UDashboardCard class="mx-9 mb-9 max-w-prose">
      <UDashboardSection class="mb-2 text-md italic">
        Below is the list of available deliveries in or near your delivery areas. Please click on the "Accept" button to claim a delivery.
        Remember that you are not obligated to accept any delivery. You may choose to accept or decline any delivery based on your availability.
      </UDashboardSection>
    </UDashboardCard>

    <!-- <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight"></h2> -->

    <!-- <RequestsList title="Request History" description="" :cta="true" :requests="requests" /> -->

  </UDashboardPanelContent>
</template>
