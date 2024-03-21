
<script setup lang="ts">
  import type { FoodDeliveryFormState } from '@/types/index';


  definePageMeta({
    layout: 'dashboard',
    auth: {
      unauthenticatedOnly: true,
    },
  })

  const state = reactive<FoodDeliveryFormState>({
    delivery_address: {
      branch_location: 'Medicine Hat',
      location: {
        address_line1: 'Addr line 1',
        city: 'Cccityy',
        divisions_level1: 'BC',
        postcode: 'M4C 1B5',
        country: 'CA',
      },
      building_type: 'Townhouse',
    },
    delivery_contact:{
      contact_number: '250-777-2171',
      contact_name: 'Pearl',
      preferred_method: "Email",
    },
    your_pets: {
      pet_name: 'Buddy',
      pet_breed: 'Labrador Retriever',
      pet_age: '3 years',
      pet_weight: '50 lbs',
    },
    safe_drop: {
      safe_drop: true,
      safe_drop_instructions: 'Leave at the door',
    },
    confirmation: {
      confirm_correct: false,
      accept_terms: false,
    },
  })

  const links = [[{
      label: 'Request History',
      icon: 'i-heroicons-calendar',
      to: '/requests',
      exact: true
    }, {
      label: 'New Request',
      icon: 'i-ph-plus-square-light',
      to: '/requests/new',
    }]
  ]
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow>
      <UDashboardNavbar title="New Food Request" />

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto md:block lg:hidden">
        <UHorizontalNavigation :links="links" class="" />
      </UDashboardToolbar>

      <UDashboardPanelContent class="pb-12 pr-16 mr-16">

        <RequestsFoodDeliveryForm :state="state as any" />

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>
