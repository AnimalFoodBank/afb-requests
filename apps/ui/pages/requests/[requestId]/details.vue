
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

        <UDashboardCard class="mx-9 mb-9 max-w-prose">
          <UDashboardSection class="mb-2 text-md italic">

            Please note that creating an account does not automaticaly create a request for food for you.
            If you've just created your account, please click the "Request Pet Food" button. You will need to complete this form each time you need food.
          </UDashboardSection>
        </UDashboardCard>

        <!-- <h2 class="text-2xl sm:text-xl font-bold text-gray-900 dark:text-white tracking-tight"></h2> -->

        <RequestDetails title="Request Details" description="" :cta="true" :requestDetails="requestDetails" />

      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>

</template>
