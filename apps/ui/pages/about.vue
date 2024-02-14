<script setup lang="ts">
import type { NavItem } from '@nuxt/content/dist/runtime/types';

const navigation = inject<Ref<NavItem[]>>('navigation', ref([]))

</script>

<template>
  <UContainer>
    <UPage>
      <h1 class="text-3xl font-bold">About Us</h1>
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
