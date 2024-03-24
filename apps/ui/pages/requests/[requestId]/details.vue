
<script setup lang="ts">

const route = useRoute();
let requestDetail = ref(null)


definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/login',
  },
})

const q = ref('')
const requestId = route.params.requestId;

const requests = [{
  id: '8a36e9c2-966b-4573-ad8a-ce3c01e98e26',
  date: '2024-01-01',
  address_full: '123 Maple Street, Toronto, Ontario, M5V 2T6, Canada',
  payload: '2 bags of dog food and 1 bag of cat food.',
  imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}, {
  id: '9d4c52f7-1e9d-430f-b6dd-1c0a3377f290',
  date: '2024-02-02',
  address_full: '456 Oak Avenue, Vancouver, British Columbia, V5Z 0B3, Canada',
  payload: '3 bags of cat food.',
  imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}, {
  id: '62d77fa2-4f6e-427d-8744-258d12ceae49',
  date: '2024-03-03',
  address_full: '789 Pine Road, Calgary, Alberta, T2P 2M5, Canada',
  payload: '1 bag of dog food and 2 cans of cat food.',
  imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}]



onMounted(() => {

  requestDetail = requests.find(request => request.id === requestId);

  if (requestDetail) {
    console.log(requestDetail);
  } else {
    console.log('Request not found');
  }
})


//
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

        <RequestDetails title="Request History" description="" :cta="true" :requestDetail="requestDetail" />

      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>

</template>
