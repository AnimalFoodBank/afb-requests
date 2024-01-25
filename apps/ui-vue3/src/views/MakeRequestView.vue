<!--
  This example requires some changes to your config:

  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>


  <NewRequestForm></NewRequestForm>

</template>


<script lang="ts" setup>
// import { PhotoIcon, UserCircleIcon } from '@heroicons/vue/24/solid';
import NewRequestForm from '../components/forms/NewRequestForm.vue';

</script>
