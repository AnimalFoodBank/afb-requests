<!--
  Based on https://vue3-google-map.com/advanced-usage/#loading-the-google-maps-api-script-externally
 -->

<script setup lang="ts">
import { Circle, GoogleMap } from "vue3-google-map";

const googleAPIKey = "AIzaSyC_UvqrTnimc1Pc7LDYCqdqUiGMMUgMCWg";

const centerV = { lat: 49.282, lng: -123.12 };
const centerMH = { lat: 50.04, lng: -110.667, zoom: 12};
// const center = centerMH;

let apiPromise: Promise<typeof window.google> | undefined = undefined;


const center = { lat: 37.09, lng: -95.712 }
const cities = {
  chicago: {
    center: { lat: 41.878, lng: -87.629 },
    population: 2714856,
  },
  newyork: {
    center: { lat: 40.714, lng: -74.005 },
    population: 8405837,
  },
  losangeles: {
    center: { lat: 34.052, lng: -118.243 },
    population: 3857799,
  },
  vancouver: {
    center: { lat: 49.25, lng: -123.1 },
    population: 603502,
  },
}

const circles = {}

for (const key in cities) {
  circles[key] = {
    center: cities[key].center,
    radius: Math.sqrt(cities[key].population) * 100,
    strokeColor: '#FF0000',
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: '#FF0000',
    fillOpacity: 0.35,
  }
}

onMounted(() => {

});


</script>

<template>
  <GoogleMap
    :api-promise="apiPromise"
    :api-key="googleAPIKey"
    mapTypeId="terrain"
    style="width: 100%; height: 500px"
    :center="center"
    :zoom="center.zoom || 4"
  >
    <!-- <Marker :options="{ position: center }" /> -->
    <Circle v-for="circle in circles" :options="circle" />
  </GoogleMap>
</template>
