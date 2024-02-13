<script setup lang="ts">

const { data: navigation } = await useAsyncData('navigation', () => fetchContentNavigation(), { default: () => [] })
provide('navigation', navigation)

</script>

<template>
  <div>
    <Header />

    <UMain>
      <slot />
    </UMain>

    <Footer />
  </div>
</template>
