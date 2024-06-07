<script setup lang="ts">

const title = 'Address & Delivery Info'
const description = 'Update your delivery information.'
const icon = 'i-heroicons-home'
const cta = true

definePageMeta({
  layout: 'dashboard',
})


const {
  userInfo,
  profileInfo,
} = useProfile();

const isDeleteAccountModalOpen = ref(false)
const state = ref({})

onMounted(() => {
  console.log('profile/index.vue onMounted')

  state.value = {
    branch_selection: profileInfo?.branch_selection || 'Medicine Hat',
    name: userInfo.name,
    email: userInfo.email,
    phone_number: profileInfo?.phone_number,
    address: profileInfo?.address || '1234 Southview Drive SE',
    city: profileInfo?.city || 'Medicine Hat',
    state: profileInfo?.state || 'AB',
    zip: profileInfo?.zip || 'T1A 8E1',
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
