<script setup lang="ts">

definePageMeta({
  layout: 'default',
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
      <h1 class="text-3xl font-bold">Your Dashboard</h1>
      <p class="mt-4">We are a company that does things.</p>

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
