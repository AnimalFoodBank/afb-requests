<!--
  Based on https://vue3-google-map.com/advanced-usage/#loading-the-google-maps-api-script-externally
 -->

<script setup lang="ts">
import { Circle, GoogleMap } from "vue3-google-map";

definePageMeta({
  layout: 'dashboard',
})


// Get the google api Key from nuxt config
const config = useRuntimeConfig()

const googleAPIKey = config.public.googleAPIKey;

// Get the query params name lat and lng
const route = useRoute();
const lat = (route.query.lat || '49.282') as string;
const lng = (route.query.lng || '-123.12') as string;
const zoom = (route.query.zoom || '12') as string;
const center = {
  lat: Math.max(-90, Math.min(90, parseFloat(lat))),
  lng: Math.max(-180, Math.min(180, parseFloat(lng))),
  zoom: Math.max(1, Math.min(20, parseInt(zoom))),
}
console.log('center', center)

let apiPromise: Promise<typeof window.google> | undefined = undefined;


const colour = '#00FF00';
type City = {
  center: { lat: number, lng: number },
  population: number,
  radius?: number,
  strokeColor?: string,
  strokeOpacity?: number,
  strokeWeight?: number,
  fillColor?: string,
  fillOpacity?: number,
};

const cities: Record<string, City> = {
  vancouver: {
    center: { lat: 49.25, lng: -123.1 },
    population: 603502,
  },
  medicinehat: {
    center: { lat: 50.04, lng: -110.667 },
    population: 63138,
  },
  toronto: {
    center: { lat: 43.7, lng: -79.42 },
    population: 2731571,
  },
  winnipeg: {
    center: { lat: 49.9, lng: -97.13 },
    population: 632063,
  },
  saskatoon: {
    center: { lat: 52.13, lng: -106.67 },
    population: 202340,
  },
  edmonton: {
    center: { lat: 53.55, lng: -113.5 },
    population: 1159869,
  },
}

const circles: Record<string, City> = {}

for (const key in cities) {
  circles[key] = {
    center: cities[key].center,
    population: cities[key].population,
    radius: Math.sqrt(cities[key].population) * 10,
    strokeColor: colour,
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: colour,
    fillOpacity: 0.15,
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
