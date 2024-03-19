<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/login',
  },
})

const state = reactive({
  name: 'Poo Bear',
  email: 'poop@solutious.com',
  username: 'poobear',
  avatar: '',
  bio: '',
  password_current: '',
  password_new: ''
})

const validate = (state: any) => {
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Email is required' })
  if (!state.password) errors.push({ path: 'password', message: 'Password is required' })
  return errors
}

function onSubmit (data: any) {
  console.log('Submitted', data)
}

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

        <RequestsFoodRequestForm :state="state" :validate="validate" :onSubmit="onSubmit"/>

      </UDashboardPanelContent>


    </UDashboardPanel>
  </UDashboardPage>

</template>
