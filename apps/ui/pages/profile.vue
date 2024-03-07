<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    authenticated: true,
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
      <UDashboardNavbar title="Profile" />

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto md:block lg:hidden">
        <UHorizontalNavigation :links="links" class="" />
      </UDashboardToolbar>

      <NuxtPage />
    </UDashboardPanel>
  </UDashboardPage>
</template>
