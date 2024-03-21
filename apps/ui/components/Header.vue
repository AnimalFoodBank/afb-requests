<script setup lang="ts">


const links = [{
  label: 'Dashboard',
  to: '/dashboard'
}, {
  label: 'Request Food',
  to: '/requests/new'
}, {
  label: 'About Us',
  to: '/about'
}]

const { header } = useAppConfig()
</script>

<template>
  <!-- For larger screens (desktop included) the top nav is the main nav (i.e. no hamburger menu) -->
  <UHeader :links="links">
    <template #logo>
      <template v-if="header?.logo?.dark || header?.logo?.light">
        <UColorModeImage v-bind="{ class: 'h-6 w-auto', ...header?.logo }" />
      </template>
      <template v-else>
        <Logo />
      </template>
    </template>

    <template #right>
      <UButton label="Sign in" icon="i-heroicons-arrow-right-20-solid" trailing color="primary" to="/login" class="lg:flex" />
    </template>

    <!-- On smaller screens, the top nav moves to this hamburger menu. -->
    <template #panel>
      <UNavigationTree :links="links" default-open />
    </template>
  </UHeader>
</template>
