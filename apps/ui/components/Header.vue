<script setup lang="ts">


const links = [{
  label: 'New Request',
  to: '/requests/new'
}, {
  label: 'About Us',
  to: '/about'
}]
</script>

<template>
  <!-- For larger screens (desktop included) the top nav is the main nav (i.e. no hamburger menu) -->
  <UHeader :links="links">
    <template #logo>
      <Logo />
    </template>

    <template #right>
      <UButton label="Sign in" icon="i-heroicons-arrow-right-20-solid" trailing color="black" to="/login" class="lg:flex" />
    </template>

    <!-- On smaller screens, the top nav moves to this hamburger menu. -->
    <template #panel>
      <UNavigationTree :links="links" default-open />
    </template>
  </UHeader>
</template>
