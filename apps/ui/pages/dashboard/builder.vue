
<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
  },
})
</script>

<template>
  <div class="">
    <ClientOnly>
      <VueformBuilder />
    </ClientOnly>
  </div>
</template>
