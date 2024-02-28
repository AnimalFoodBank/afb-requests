
<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/login',
  },
  // colorMode: 'dark',
})

const q = ref('')
const isInviteModalOpen = ref(false)

</script>

<template>
  <UDashboardPanelContent class="pb-24">
    <UDashboardSection title="Manage access" description="Invite new members by email address." orientation="horizontal" :ui="{ container: 'lg:sticky top-2' }">
      <template #links>
        <UButton label="Invite people" color="black" @click="isInviteModalOpen = true" />
      </template>

      <UCard :ui="{ header: { padding: 'p-4 sm:px-6' }, body: { padding: '' } }" class="min-w-0">
        <template #header>
          <UInput v-model="q" icon="i-heroicons-magnifying-glass" placeholder="Search members" autofocus />
        </template>
      </UCard>
    </UDashboardSection>

    <UDashboardModal v-model="isInviteModalOpen" title="Invite people" description="Invite new members by email address" :ui="{ width: 'sm:max-w-md' }">
      <!-- ~/components/settings/MembersForm.vue -->
      <SettingsMembersForm @close="isInviteModalOpen = false" />
    </UDashboardModal>
  </UDashboardPanelContent>
</template>
