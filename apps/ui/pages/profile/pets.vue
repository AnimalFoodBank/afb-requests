<script setup lang="ts">

const state = reactive({})

const title = 'Your Pets'
const description = 'Manage your pet information. '
const icon = 'i-ph-paw-print'
const cta = false

definePageMeta({
  layout: 'dashboard',
})


</script>

<template>
  <UDashboardPanelContent class="pb-24">

    <UDashboardSection :title="title" :description="description" :icon="icon">
      <template #links v-if="cta">
        <UButton type="submit" label="Save changes" color="black" />
      </template>
    </UDashboardSection>

    <UDashboardSection>
      <PetsForm :cta="false" :state="state" />
    </UDashboardSection>

    <UDashboardSection class="mb-8 text-md italic">
      Please note we may follow-up with you if we need more information.
    </UDashboardSection>

    <UDashboardSection class="">
      <p class="text-xl font-bold text-gray-900 dark:text-gray-50">Pet History</p>
    </UDashboardSection>

    <UDashboardCard class="mx-9 mb-1 max-w-prose">
      <UDashboardSection class="mb-2 text-md text-base text-gray-500">
      No changes to display yet.
      </UDashboardSection>
    </UDashboardCard>

    <!-- <UDivider class="mb-4" />
 -->

  </UDashboardPanelContent>
</template>
