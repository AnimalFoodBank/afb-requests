
<!-- https://vuejs.org/guide/essentials/component-basics.html#dynamic-components -->
<template>
  <component :is="$route.meta.layout || 'div'">
    <router-view />
  </component>
</template>

<script setup lang="ts">
/**
 * In SFC, the code inside is compiled as the content of the component's
 * setup() function. This means that unlike normal <script>, which
 * only executes once when the component is first imported, code
 * inside <script setup> will execute every time an instance of
 * the component is created. -- https://vuejs.org/api/sfc-script-setup.html#basic-syntax
**/

import { onMounted } from 'vue';

onMounted(async () => {
  // Example of using environment variables in a Vue component.
  console.log('import.meta.env.VITE_BASE_URL=' + import.meta.env.VITE_BASE_URL)
});

</script>

<style>
</style>
