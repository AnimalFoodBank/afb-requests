<script setup lang="ts">

const state = reactive({
  name: 'Delbo Baggins',
  branch: 'Waldorf',
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

    <PetsForm title="My Pets" description="View your pet information." :cta="true" :state="state" />


    <UDivider class="mb-4" />

    <UDashboardSection class="italic">
      Pet information cannot be updated/changed without contacting us at admin@animalfoodbank.org
    </UDashboardSection>

  </UDashboardPanelContent>
</template>
