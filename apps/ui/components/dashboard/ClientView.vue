<script setup lang="ts">
defineProps<{
	requests: never[];
}>()
</script>

<template>
	<UDashboardPanelContent>

    <UDashboardSection
      icon="i-heroicons-user"
      title="Client Portal"
      description="Your delivery address, pet info, requests history and more. "
      />

    <UDashboardCard class="mx-9 mb-9 max-w-prose">
      <UDashboardSection class="mb-2 text-md italic">
        Please note that creating an account does not automaticaly create a request for food for you.
        If you've just created your account, please click the "Request Pet Food" button. You will need to complete this form each time you need food.
      </UDashboardSection>
    </UDashboardCard>

    <!-- <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight"></h2> -->

    <RequestsList title="Request History" description="" :cta="true" :requests="requests" />

  </UDashboardPanelContent>
</template>
