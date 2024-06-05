<script setup lang="ts">

const title = 'Address & Delivery Info'
const description = 'Update your delivery information.'
const icon = 'i-heroicons-home'
const cta = true

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
const state = ref({})


onMounted(() => {
  console.log('profile/index.vue onMounted')

  const userInfo = authData?.value || {}
  const profile = userInfo.profiles?.[0] || {}

  console.log('authData', userInfo)
  console.log('profile', profile)

  state.value = {
    branch_selection: profile?.branch_selection || 'Medicine Hat',
    name: userInfo.name,
    email: userInfo.email,
    phone_number: profile?.phone_number,
    address: profile?.address || '1234 Southview Drive SE',
    city: profile?.city || 'Medicine Hat',
    state: profile?.state || 'AB',
    zip: profile?.zip || 'T1A 8E1',
  }

  console.log('state', state.value)
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
