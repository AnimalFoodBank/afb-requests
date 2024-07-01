<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

const q = ref("");


const links = [[
  {
    label: 'New Request',
    icon: 'i-ph-plus-square-light',
    to: '/requests/new',
  },
  {
    label: 'Request History',
    icon: 'i-heroicons-calendar',
    to: '/requests',
    exact: true
  },
]]

const {
  status: authStatus,
  data: userInfo,
  token: authToken,
} = useAuth();



const requests = ref([]);


const fetchRequests = async () => {
  const options = {
    headers: {
      'Authorization': authToken.value,
    },
  }

  const response: Array<FoodRequest>[any] = await $fetch('/api/v1/requests/', options)

  requests.value = response.results;

  console.log(requests);
}

onMounted(() => {
  fetchRequests();
});

</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Requests">
      </UDashboardNavbar>

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto md:block">
        <UHorizontalNavigation :links="links" class="" />
      </UDashboardToolbar>

      <UDashboardPanelContent class="pb-24">
        <UDashboardSection
          icon="i-streamline-shipping-truck"
          title="Request History"
          description="Your previous requests for food."
        />

        <!-- <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight"></h2> -->

        <RequestsList
          title="Request History"
          description=""
          :cta="true"
          :requests="requests"
        />

      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>
</template>
