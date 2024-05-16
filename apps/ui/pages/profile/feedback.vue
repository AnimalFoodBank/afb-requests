<script setup lang="ts">



</script>

<template>
  <UDashboardPanelContent class="pb-24">



    <UDivider class="mb-16" />

    <UDashboardSection title="Account Changes" description="These actions are not reversible." class="hidden">
      <div>
        <UButton color="red" label="Delete account" size="md" @click="isDeleteAccountModalOpen = true" />
      </div>
    </UDashboardSection>

  </UDashboardPanelContent>
</template>
s
