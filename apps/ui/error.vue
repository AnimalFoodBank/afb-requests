<script setup lang="ts">
import type { NuxtError } from '#app';

useSeoMeta({
  title: 'Page not found',
  description: 'We are sorry but this page could not be found.'
})

defineProps<{
  error: NuxtError
}>()

useHead({
  htmlAttrs: {
    lang: 'en'
  }
})

</script>

<template>
  <div>
    <Header />

    <UMain>
      <UContainer>
        <UPage>
          <UPageError :error="error" />
        </UPage>
      </UContainer>
    </UMain>

    <Footer />

    <UNotifications />
  </div>
</template>
