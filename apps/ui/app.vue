<script setup lang="ts">

// https://www.npmjs.com/package/@googlemaps/js-api-loader

const googleAPIKey = 'AIzaSyC_UvqrTnimc1Pc7LDYCqdqUiGMMUgMCWg'
let autocomplete: google.maps.places.Autocomplete | null = null;
const googleMapsIsReady = ref(false)


onMounted(() => {
  console.log('app.vue onMounted')
})

// TODO: Revisit this earl dark mode cruft. May not be needed anymore.
const colorMode = useColorMode()
const color = computed(() => colorMode.value === 'dark' ? '#111827' : 'white')

useHead({
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    { key: 'theme-color', name: 'theme-color', content: color }
  ],
  link: [
    { rel: 'icon', href: '/favicon.ico' }
  ],
  script: [
    {
      // src: `https://maps.googleapis.com/maps/api/js?key=${ googleAPIKey }&libraries=places&callback=initMap`,
      // async: true,
      // defer: true,
    },
  ],
  htmlAttrs: {
    lang: 'en'
  }
})

useSeoMeta({
  title: "Welcome",
  titleTemplate: '%s | AFB - Animal Food Bank',
  ogImage: '/img/afb_logo_vertical_colour.png',
})

</script>

<template>
  <div>
    <NuxtLoadingIndicator />

    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>

    <UNotifications />
  </div>
</template>
