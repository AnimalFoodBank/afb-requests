<script setup lang="ts">
import { useRoute } from 'vue-router';

const route = useRoute()

const { data: page } = await useAsyncData('index', () => queryContent('/').findOne())
console.log(`${route.path}: `, page.value)
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
</script>

<template>
  <div>
    <ULandingHero v-if="page.hero" v-bind="page.hero">

      <template #links>
        <UButton v-for="(link, index) in page.links" :key="index" v-bind="link" @click="link.click" />
      </template>

    </ULandingHero>

    <!-- Renders nothing by default -->
    <ULandingSection v-if="page.features" :title="page.features.title" :links="page.features.links">
      <UPageGrid>
        <ULandingCard v-for="(item, index) of page.features.items" :key="index" v-bind="item" />
      </UPageGrid>
    </ULandingSection>
  </div>
</template>
