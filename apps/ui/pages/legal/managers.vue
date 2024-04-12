<script setup lang="ts">
import { useRoute } from 'vue-router';

useSeoMeta({
  title: "Branch Managers Agreement",
})

definePageMeta({
  auth: false,
});

const route = useRoute()

</script>

<template>
  <div>
    <h1>Branch Managers Agreement</h1>
  </div>
</template>
