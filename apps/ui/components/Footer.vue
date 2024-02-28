<script setup lang="ts">
const links = [{
  label: 'Resources',
  children: [{
    label: 'Help center'
  },]
}, {
  label: 'Partners',
  children: []
}, {
  label: 'Company',
  children: [{
    label: 'About'
  }, {
    label: 'Store'
  }, {
    label: 'Volunteer'
  }, {
    label: 'Blog'
  }]
}]

const toast = useToast()

</script>

<template>
  <UFooter>
    <template #top>
      <UFooterColumns :links="links">
      </UFooterColumns>
    </template>

    <template #left>
      <p class="text-gray-500 dark:text-gray-400 text-sm">
        Animal Food Bank © {{ new Date().getFullYear() }}.
      </p>
    </template>

    <template #right>
      <UColorModeButton size="sm" />

      <UButton to="https://github.com/nuxt-ui-pro/saas" target="_blank" icon="i-simple-icons-github" aria-label="GitHub" color="gray" variant="ghost" />
    </template>
  </UFooter>
</template>
