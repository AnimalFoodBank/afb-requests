<script setup lang="ts">

useSeoMeta({
  title: "Dashboard",
})

definePageMeta({
  layout: 'dashboard',
})


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
  data: authData,
  token: authToken,
} = useAuth();

const requests = ref([]);
const role = ref('unknown');

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

  const userInfo = authData?.value || {}
  const profile = userInfo.profiles?.[0] || {}
  role.value = profile?.role || 'unknown';
});


</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Dashboard">

      </UDashboardNavbar>

      <!-- <UDashboardToolbar>
      </UDashboardToolbar> -->

      <DashboardClientView :requests="requests" v-if="isClient" />
      <DashboardVolunteerView :requests="requests" v-if="isVolunteer" />
      <DashboardManagerView :requests="requests" v-if="isManager" />
      <div v-if="role === 'unknown'">
        <p>Loading dashboard content...</p>
      </div>

    </UDashboardPanel>
  </UDashboardPage>
</template>
