<script setup lang="ts">

useSeoMeta({
  title: "Profile",
})

definePageMeta({
  layout: 'dashboard',
})

const links = [[
  {
    label: 'Delivery Information',
    icon: 'i-heroicons-user-circle',
    to: '/profile',
    exact: true
  },
  {
    label: 'My Pets',
    icon: 'i-heroicons-home',
    to: '/profile/pets',
  }
]]

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
