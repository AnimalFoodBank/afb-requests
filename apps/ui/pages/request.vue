<script setup lang="ts">
import type { NavItem } from '@nuxt/content/dist/runtime/types';

const navigation = inject<Ref<NavItem[]>>('navigation', ref([]))

const links = computed(() => navigation.value.find((item) => item._path === '/docs')?.children ?? [])
</script>

<template>
  <UContainer>
    <UPage>
      <h1 class="text-3xl font-bold">Make a request</h1>
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
