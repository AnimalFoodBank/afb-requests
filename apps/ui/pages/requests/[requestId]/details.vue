
<script setup lang="ts">

const route = useRoute();
let requestDetail = ref(null)


definePageMeta({
  layout: 'dashboard',
})

const q = ref('')
const requestId = route.params.requestId;

const {
  status: authStatus,
  data: authData,
  token: authToken,
} = useAuth();



const requestDetails = ref([]);


const fetchRequest = async () => {
  const options = {
    headers: {
      'Authorization': authToken.value,
    },
  }
  const requestURI = `/api/v1/requests/${requestId}/`
  const response: FoodRequest = await $fetch(requestURI, options)

  requestDetails.value = response;

  console.log(requestDetails);
}

onMounted(() => {
  fetchRequest();
});

</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Requests">

      </UDashboardNavbar>


      <UDashboardPanelContent>

        <UDashboardSection
          icon="i-heroicons-user"
          title="Request Details"
          description=""
          />

        <!-- <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight"></h2> -->

        <RequestsDetails title="Request Details" description="" :cta="true" :requestDetails="requestDetails" />

      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>

</template>
