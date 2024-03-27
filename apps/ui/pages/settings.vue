<!-- <UColorModeButton size="sm" name="darkModeToggle" /> -->

<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});
</script>


<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Portal Settings">

      </UDashboardNavbar>

      <!-- <UDashboardToolbar>
      </UDashboardToolbar> -->

      <UDashboardPanelContent class="max-w-full">

        <UDashboardSection
          icon="i-heroicons-cog"
          title="Site Settings"
          description="Update the settings for your portal experience."
          />

        <UDivider class="mb-4" />

        <UDashboardSection title="Theme" description="Customize the look and feel of your dashboard." >
          <template #links>
            <UColorModeSelect color="gray" />
          </template>
        </UDashboardSection>

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>
