<script setup lang="ts">
import type { NavItem } from '@nuxt/content/dist/runtime/types';

const navigation = inject<Ref<NavItem[]>>('navigation', ref([]))

const links = [{
  label: 'Request',
  to: '/request'
}, {
  label: 'Dashboard',
  to: '/dashboard'
}, {
  label: 'About Us',
  to: '/about'
}]
</script>

<template>
  <UHeader :links="links">
    <template #logo>
      <!-- AFB <UBadge label="Registered Non-Profit" variant="subtle" class="mb-0.5" /> -->
      <NuxtLink to="/">
        <nuxt-img src="/img/afb_logo_horizontal_colour.png" alt="Animal Food Bank Logo" class="max-w-32 min-16"/>
      </NuxtLink>
    </template>

    <template #right>
      <!-- <UButton label="Sign in" color="gray" to="/login" /> -->
      <UButton label="Sign in" icon="i-heroicons-arrow-right-20-solid" trailing color="black" to="/login" class="hidden lg:flex" />
    </template>

    <template #panel>
      <UNavigationTree :links="mapContentNavigation(navigation)" default-open />
    </template>
  </UHeader>
</template>
