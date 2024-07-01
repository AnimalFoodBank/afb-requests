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

console.log('profileInfo', profileInfo)

//const isDeleteAccountModalOpen = ref(false)
const state = ref({})

onMounted(() => {
  console.log('profile/index.vue onMounted')

  state.value = {
    profile_id: profileInfo?.id,
    user_id: userInfo.id,
    branch_selection: profileInfo?.branch, //|| '5c3549e0-a728-4510-a64a-69bcd26d52d5', // Osoyoos
    name: profileInfo.preferred_name || userInfo.name,
    email: userInfo.email,
    phone_number: profileInfo?.phone_number,
    address: profileInfo?.address,
    ext_address_details: profileInfo?.ext_address_details,
  }
})

</script>

<template>
  <UDashboardPanelContent class="pb-24">

    <DeliveryInfoForm :title="title" :description="description" :icon="icon" :cta="cta" :state="state" />

    <UDivider class="mb-16" />

    <!--<UDashboardSection title="Account Changes" description="These actions are not reversible." class="">
      <div>
        <UButton color="red" label="Delete account" size="md" @click="isDeleteAccountModalOpen = true" />
      </div>
    </UDashboardSection>-->

  </UDashboardPanelContent>

<!--<SettingsDeleteAccountModal v-model:visible="isDeleteAccountModalOpen" />-->

</template>
