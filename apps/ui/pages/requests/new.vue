<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/login',
  },
  // colorMode: 'dark',
})

const isDeleteAccountModalOpen = ref(false)
const state = reactive({
  name: 'Poo Bear',
  email: 'poop@solutious.com',
  username: 'poobear',
  avatar: '',
  bio: '',
  password_current: '',
  password_new: ''
})


</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Dashboard">

      </UDashboardNavbar>

      <UDashboardToolbar>
      </UDashboardToolbar>

      <UDashboardPanelContent class="pb-24">
        <UDashboardSection title="Theme" description="Customize the look and feel of your dashboard.">
          <template #links>
            <UColorModeSelect color="gray" />
          </template>
        </UDashboardSection>

        <UDivider class="mb-4" />





      </UDashboardPanelContent>


    </UDashboardPanel>
  </UDashboardPage>

</template>
