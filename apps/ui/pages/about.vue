<script setup lang="ts">
import { useRoute } from 'vue-router';

useSeoMeta({
  title: "About Us",
})

definePageMeta({
  auth: false,
});

const route = useRoute()

</script>

<template>
  <div>
    <h1>About Us</h1>
  </div>
</template>
