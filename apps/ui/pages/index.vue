<script setup lang="ts">
const { data: page } = await useAsyncData('index', () => queryContent('/').findOne())
if (!page.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
}

useSeoMeta({
  titleTemplate: '',
  title: page.value.title,
  ogTitle: page.value.title,
  description: page.value.description,
  ogDescription: page.value.description
})

definePageMeta({
})

defineOgImage({
  component: 'Saas',
  title: page.value.title,
  description: page.value.description,
})
</script>

<template>
  <div v-if="page">
    <ULandingHero :title="page.hero.title" :description="page.hero.description" :links="page.hero.links">
      <div class="absolute inset-0 landing-grid z-[-1] [mask-image:radial-gradient(100%_100%_at_top_right,white,transparent)]" />
    </ULandingHero>

  </div>
</template>

<style scoped>
/**
*   background-size: 100px 100px;
*   background-image:
*     linear-gradient(to right, rgb(var(--color-gray-200)) 1px, transparent 1px),
*     linear-gradient(to bottom, rgb(var(--color-gray-200)) 1px, transparent 1px);
* }
* .dark {
*   .landing-grid {
*     background-image:
*       linear-gradient(to right, rgb(var(--color-gray-800)) 1px, transparent 1px),
*       linear-gradient(to bottom, rgb(var(--color-gray-800)) 1px, transparent 1px);
*   }
* }
**/
</style>
