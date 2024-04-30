<script setup lang="ts">
const config = useRuntimeConfig();

// https://www.npmjs.com/package/@googlemaps/js-api-loader

const googleAPIKey = config.public.googleAPIKey;
let autocomplete: google.maps.places.Autocomplete | null = null;
const googleMapsIsReady = ref(false)


onMounted(() => {
  console.log('app.vue onMounted')
})

// Set the suggested toolbar color based on the color mode.
// Please note that not all browsers support this feature,
// and even those that do may interpret it in different ways.
// For example, Chrome for Android uses the color to tint
// the tab bar, while Safari on iOS doesn't use it at all.
const colorMode = useColorMode()
const color = computed(() => colorMode.value === 'dark' ? '#111827' : 'white')

useHead({
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    // { name: 'theme-color', content: color }
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
