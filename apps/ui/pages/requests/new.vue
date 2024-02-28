<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/login',
  },
  // colorMode: 'dark',
})

</script>


<template>
  <UContainer>
    <UPage>
      <h1 class="text-3xl font-bold">Make a request</h1>
      <p class="mt-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>

      <template #left>
        <UAside>
          <template #top>


          </template>
        </UAside>
      </template>

      <NuxtPage />
    </UPage>
  </UContainer>
</template>
