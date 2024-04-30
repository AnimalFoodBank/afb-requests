<script setup lang="ts">

const state = reactive({})

const title = 'My Pets'
const description = 'Manage your pet information. '
const icon = 'i-heroicons-home'
const cta = false

</script>

<template>
  <UDashboardPanelContent class="pb-24">

    <UDashboardSection :title="title" :description="description" :icon="icon">
      <template #links v-if="cta">
        <UButton type="submit" label="Save changes" color="black" />
      </template>
    </UDashboardSection>

    <!-- <UDashboardCard class="mx-9 mb-1 max-w-prose">
      <UDashboardSection class="mb-2 text-md italic">

      </UDashboardSection>
    </UDashboardCard> -->

    <UDashboardSection>
      <PetsForm :cta="false" :state="state" />
    </UDashboardSection>

    <UDivider class="mb-4" />

    <UDashboardSection class="italic">
      Please note that we review pet details and may follow-up for verification.
    </UDashboardSection>

  </UDashboardPanelContent>
</template>
