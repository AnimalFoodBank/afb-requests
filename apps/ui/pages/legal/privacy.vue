<script setup lang="ts">
import { useRoute } from 'vue-router';

useSeoMeta({
  title: "Privacy Notice",
})

definePageMeta({
  auth: false,
});

const route = useRoute()

</script>

<template>
  <div>
    <h1>Privacy Notice</h1>
  </div>
</template>
