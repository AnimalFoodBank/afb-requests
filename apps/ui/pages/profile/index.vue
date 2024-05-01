<script setup lang="ts">

const title = 'Address & Delivery Info'
const description = 'Update your delivery information.'
const icon = 'i-heroicons-home'
const cta = true

const isDeleteAccountModalOpen = ref(false)
const state = reactive({
  name: 'Delbo Baggins',
  branch_selection: 'Xanadu',
  email: 'delbo@solutious.com',
  phone: '123-456-7890',
  address: '123 Main St, Toronto, ON, Canada',
  pets: [
    { id: '', type: 'dog', name: 'Doggo', details: 'Birthdate: 2023-11-01\nUsual Food Brands: Kibbles \nWeight Ibs (Dogs only): 5 \nPetAllergies: Pork' },
    { id: '', type: 'cat', name: 'Cato', details: 'Birthdate: 2022-11-01\nUsual Food Brands: Whiskas \nWeight Ibs (Dogs only):  \nPetAllergies: none' },
  ],
  password_current: '',
  password_new: ''
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
