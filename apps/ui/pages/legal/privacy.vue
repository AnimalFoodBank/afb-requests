<script setup lang="ts">
import { useRoute } from 'vue-router';

useSeoMeta({
  title: "Privacy Policy",
})

definePageMeta({
  auth: false,
});

const route = useRoute()

</script>

<template>
  <div>
    <h1>Privacy Policy</h1>
  </div>
</template>
