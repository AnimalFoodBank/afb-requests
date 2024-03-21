
<script setup lang="ts">

  definePageMeta({
    layout: 'dashboard',
    auth: {
      unauthenticatedOnly: true,
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

        <RequestForm />

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>
