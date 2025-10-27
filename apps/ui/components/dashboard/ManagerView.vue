<script setup lang="ts">
defineProps<{
	requests: never[];
}>()
</script>

<template>
	<UDashboardPanelContent>

    <UDashboardSection
      icon="i-heroicons-user"
      title="Branch Dashboard"
      description="Everything."
      />

    <UDashboardCard class="mx-9 mb-9 max-w-prose">
      <UDashboardSection class="mb-2 text-md italic">
        You are a branch manager. You have access to all the features of the system.
      </UDashboardSection>
    </UDashboardCard>

    <!-- <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight"></h2> -->

    <!-- <RequestsList title="Request History" description="" :cta="true" :requests="requests" /> -->

  </UDashboardPanelContent>
</template>
