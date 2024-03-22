<script setup lang="ts">

// https://www.npmjs.com/package/@googlemaps/js-api-loader

const googleAPIKey = 'AIzaSyC_UvqrTnimc1Pc7LDYCqdqUiGMMUgMCWg'

const googleMapsIsReady = ref(false)

import { Loader } from '@googlemaps/js-api-loader';
// import { GoogleMap, Marker } from 'vue3-google-map';

const loader = new Loader({
  apiKey: googleAPIKey,
  version: 'weekly',
  libraries: ['places'],
});



// Using importLibrary method to load the places library
// returns a promise that resolves to the specific
// google.maps.Library object instead of simply
// the google.maps object.
//
// In short, leaving it as-is with loader.load()
// while waiting for vue3-google-map to update.
//
onMounted(() => {
  console.log('app.vue onMounted')
  loader.load().then(() => {
  console.log('google maps loaded')
})
  // console.log('app.vue onMounted')
  // console.log('BEFORE window.google', window.google)
  // if (window.google) {
  //   console.log('AFTER window.google', window.google)
  //   googleMapsIsReady.value = true
  //   return
  // }


  // const loader = new Loader({
  //   apiKey: googleAPIKey,
  //   version: 'weekly',
  //   libraries: ['places'],
  // });
  // const googlePromise = loader.load();
  // console.log('window.google', window.google)
  // window.google = Promise.resolve(googlePromise)
  // console.log('window.google', window.google)
  // googleMapsIsReady.value = true

  // loader
  //   .load()
  //   .then((google) => {
  //     console.log('google', google)
  //     window.google = google;
  //   })
  //   .catch(e => {
  //     console.error(e)
  //   });
})



// declare global {
//   interface Window {
//     google: any;
//   }
// }

// onMounted(() => {
//   console.log('app.vue onMounted')


//   window.google = {
//       maps: { Map: function() {} }
//   }
// })

// onMounted(() => {
//   console.log('app.vue onMounted')
//   initMap()
// })
// const initMap = () => {

//   const loader = new Loader({
//     apiKey: 'AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg',
//     version: 'weekly'
//   })

//   loader
//     .importLibrary('places')
//     .then((google) => {
//       window.google = google;
//     })
//     .catch(e => {
//       // do something
//     });

//   console.log(window.google)
// }

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
