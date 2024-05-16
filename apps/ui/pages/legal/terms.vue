<script setup lang="ts">
import { useRoute } from 'vue-router';

useSeoMeta({
  title: "Terms of Use",
})

definePageMeta({
  auth: false,
});

const route = useRoute()

</script>

<template>
  <div>
    <h1>Terms of Use</h1>
  </div>
</template>
