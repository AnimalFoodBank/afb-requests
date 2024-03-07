
<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/login',
  },
})

const q = ref('')

// $route.params.requestId
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Requests">

      </UDashboardNavbar>


      <UDashboardPanelContent class="pb-24">
        <UDashboardSection title="Make a new request" description="Send a food request to your local AFB branch." orientation="horizontal" :ui="{ container: 'lg:sticky top-2' }">

        </UDashboardSection>

      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>

</template>
