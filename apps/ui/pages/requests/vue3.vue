<!--
  Based on https://vue3-google-map.com/advanced-usage/#loading-the-google-maps-api-script-externally
 -->

<script setup lang="ts">
import { GoogleMap, Marker } from 'vue3-google-map';

const center = { lat: 40.689247, lng: -74.044502 };
let apiPromise: Promise<typeof window.google> | undefined = undefined;

onMounted(() => {
  console.log('vue3.vue onMounted')
  console.log('window.google', window.google)
  apiPromise = Promise.resolve(window.google);
})


</script>

<template>
  <GoogleMap
    :api-promise="apiPromise"
    style="width: 100%; height: 500px"
    :center="center"
    :zoom="15"
  >
    <Marker :options="{ position: center }" />
  </GoogleMap>
</template>
