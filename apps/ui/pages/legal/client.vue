<script setup lang="ts">
import { useRoute } from 'vue-router';

useSeoMeta({
  title: "Client Agreeement",
})

definePageMeta({
  auth: false,
});

const route = useRoute()

</script>

<template>
  <div>
    <h1>Client Agreement</h1>
  </div>
</template>
