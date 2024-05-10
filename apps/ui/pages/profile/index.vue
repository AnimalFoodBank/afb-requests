<script setup lang="ts">

const title = 'Address & Delivery Info'
const description = 'Update your delivery information.'
const icon = 'i-heroicons-home'
const cta = true

useHead({
  title: 'New Food Request',
})

definePageMeta({
  layout: 'dashboard',
})


/**
 * Retrieves the authentication status, data, and token using the useAuth() function.
 *
 * @returns {{
 *   status: string,
 *   data: any,
 *   token: string
 * }} The authentication status, data, and token.
 */
 const {
  status: authStatus,
  data: authData,
  token: authToken,
} = useAuth();


const isDeleteAccountModalOpen = ref(false)
const state = reactive({
  name: authData?.name || 'Delbo Baggins',
  branch_selection: 'Medicine Hat',
  email: authData?.email || 'delbo@solutious.com',
  phone: '123-456-7890',
  address: '1234 Southview Drive SE, Medicine Hat, AB, Canada',
})

onMounted(() => {
  console.log('profile/index.vue onMounted')

  console.log('authData', authData)
  // state.value.email = authData?.email || 'delbo2@solutious.com'
})

</script>

<template>
  <UDashboardPanelContent class="pb-24">

    <DeliveryInfoForm :title="title" :description="description" :icon="icon" :cta="cta" :state="state" />

    <UDivider class="mb-16" />

    <UDashboardSection title="Account Changes" description="These actions are not reversible." class="">
      <div>
        <UButton color="red" label="Delete account" size="md" @click="isDeleteAccountModalOpen = true" />
      </div>
    </UDashboardSection>

  </UDashboardPanelContent>
  <SettingsDeleteAccountModal v-model="isDeleteAccountModalOpen" />
</template>
