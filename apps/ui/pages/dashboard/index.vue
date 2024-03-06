<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: false,
  },
})

const columns = [{
  key: 'id',
  label: 'ID'
}, {
  key: 'name',
  label: 'Name',
  sortable: true
}, {
  key: 'title',
  label: 'Title',
  sortable: true
}, {
  key: 'email',
  label: 'Email',
  sortable: true,
  direction: 'desc' as const
}, {
  key: 'role',
  label: 'Role'
}]

const requests = [{
  id: 1,
  date: '2024-01-01',
  address_full: '123 Maple Street, Toronto, Ontario, M5V 2T6, Canada',
  payload: '2 bags of dog food and 1 bag of cat food.',
  imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}, {
  id: 2,
  date: '2024-02-02',
  address_full: '456 Oak Avenue, Vancouver, British Columbia, V5Z 0B3, Canada',
  payload: '3 bags of cat food.',
  imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}, {
  id: 3,
  date: '2024-03-03',
  address_full: '789 Pine Road, Calgary, Alberta, T2P 2M5, Canada',
  payload: '1 bag of dog food and 2 cans of cat food.',
  imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}]

</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Dashboard">

      </UDashboardNavbar>

      <!-- <UDashboardToolbar>
      </UDashboardToolbar> -->

      <UDashboardPanelContent>
        <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight">Request History</h2>


        <RequestList title="" description="" :cta="true" :requests="requests" />

      </UDashboardPanelContent>



    </UDashboardPanel>
  </UDashboardPage>
</template>
