
<script setup lang="ts">

definePageMeta({
  layout: 'dashboard',
})
</script>

<template>
  <div class="">
    <ClientOnly>
      <VueformBuilder />
    </ClientOnly>
  </div>
</template>
