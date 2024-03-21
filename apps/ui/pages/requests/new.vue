
<script setup lang="ts">

  definePageMeta({
    layout: 'dashboard',
    auth: {
      unauthenticatedOnly: true,
    },
  })

  const links = [[{
      label: 'My Delivery Info',
      icon: 'i-heroicons-user-circle',
      to: '/profile',
      exact: true
    }, {
      label: 'My Pets',
      icon: 'i-heroicons-home',
      to: '/profile/pets',
    }, {
      label: 'Contact us',
      icon: 'i-heroicons-house',
      to: 'https://animalfoodbank.org/#contact',
      target: '_blank',
      exact: true
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

        <RequestForm />

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>
