<script setup lang="ts">
import { useRoute } from 'vue-router';

useSeoMeta({
  title: "Volunteer Agreement",
})

definePageMeta({
  auth: false,
});

const route = useRoute()

</script>

<template>
  <div>
    <h1>Volunteer Agreement</h1>
  </div>
</template>
