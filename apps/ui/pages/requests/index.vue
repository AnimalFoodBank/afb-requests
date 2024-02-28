
<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/login',
  },
})

const q = ref('')


</script>

<template>
  <UDashboardPanelContent class="pb-24">
    <UDashboardSection title="Make a new request" description="Send a food request to your local AFB branch." orientation="horizontal" :ui="{ container: 'lg:sticky top-2' }">
      <template #links>
      </template>

      <UCard :ui="{ header: { padding: 'p-4 sm:px-6' }, body: { padding: '' } }" class="min-w-0">
        <template #header>
          <UInput v-model="q" icon="i-heroicons-magnifying-glass" placeholder="Search members" autofocus />
        </template>
      </UCard>
    </UDashboardSection>

  </UDashboardPanelContent>
</template>
