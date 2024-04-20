<script setup lang="ts">

const isDeleteAccountModalOpen = ref(false)
const state = reactive({
  name: 'Delbo Baggins',
  branch_selection: 'Xanadu',
  email: 'delbo@solutious.com',
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

    <DeliveryInfoForm title="My Delivery Info" description="Update your delivery information." icon="i-game-icons-cardboard-box-closed" :cta="true" :state="state" />

    <UDivider class="mb-16" />

    <UDashboardSection title="Account Changes" description="These actions are not reversible." class="">
      <div>
        <UButton color="red" label="Delete account" size="md" @click="isDeleteAccountModalOpen = true" />
      </div>
    </UDashboardSection>

  </UDashboardPanelContent>
  <SettingsDeleteAccountModal v-model="isDeleteAccountModalOpen" />
</template>
