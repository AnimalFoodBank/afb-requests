<script setup lang="ts">
const { data: page } = await useAsyncData('index', () => queryContent('/').findOne())

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
