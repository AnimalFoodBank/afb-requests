<script setup lang="ts">

useSeoMeta({
  title: "Dashboard",
})

definePageMeta({
  layout: 'dashboard',
})

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

/**
 * Retrieves the authentication status, data, and token using the useAuth() function.
 *
 * @returns {{
 *   status: string,
 *   data: any,
 *   token: string
 * }} The authentication status, data, and token.
 */
const {
  status: authStatus,
  data: userInfo,
  token: authToken,
} = useAuth();

const requests = ref([]);
const role = computed(() => userInfo.value?.profiles?.[0]?.role || 'unknown');

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

const isClient = computed(() => role.value === 'client');
const isVolunteer = computed(() => role.value === 'volunteer');
const isManager = computed(() => role.value === 'manager');

onMounted(() => {
  fetchRequests();

  const userInfo = userInfo?.value || {}
  const profile = userInfo.profiles?.[0] || {}
  role.value = profile?.role || 'unknown';
});


</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Dashboard">

      </UDashboardNavbar>

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto md:block lg:hidden">
        <UHorizontalNavigation :links="links" class="" />
      </UDashboardToolbar>

      <DashboardClientView :requests="requests" v-if="isClient" />
      <DashboardVolunteerView :requests="requests" v-if="isVolunteer" />
      <DashboardManagerView :requests="requests" v-if="isManager" />
      <div v-if="role === 'unknown'">
        <p>Loading dashboard content...</p>
      </div>

    </UDashboardPanel>
  </UDashboardPage>
</template>
