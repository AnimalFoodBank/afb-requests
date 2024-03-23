<script setup lang="ts">

// https://www.npmjs.com/package/@googlemaps/js-api-loader

const googleAPIKey = 'AIzaSyC_UvqrTnimc1Pc7LDYCqdqUiGMMUgMCWg'
const autocompleteInput = ref<HTMLInputElement | null>(null);


let autocomplete: google.maps.places.Autocomplete | null = null;
const googleMapsIsReady = ref(false)

import { Loader } from '@googlemaps/js-api-loader';
// import { GoogleMap, Marker } from 'vue3-google-map';

// const loader = new Loader({
//   apiKey: googleAPIKey,
//   version: 'weekly',
//   libraries: ['places'],
// });

// if (window.google) {
//   googleMapsIsReady.value = true;
// } else {

//   loader.load().then(() => {
//     initAutocomplete();
//   });
// }



onMounted(() => {
  console.log('app.vue onMounted')

  // re: deprecation warning for loader.load()
  //
  // Using importLibrary method to load the places library
  // returns a promise that resolves to the specific
  // google.maps.Library object instead of simply
  // the google.maps object.
  //
  // In short, leaving it as-is with loader.load() while
  // waiting for vue3-google-map to update. The warning
  // suggests that google will give a headsup at last
  // 12 months before the method is removed.
  //


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
const initAutocomplete = () => {
  console.log('initAutocomplete')
  if (autocompleteInput.value) {
    console.log('initAutocomplete - input exists')

    autocomplete = new google.maps.places.Autocomplete(autocompleteInput.value, {});
    autocomplete.addListener('place_changed', handlePlaceChanged);
  }
};

const handlePlaceChanged = () => {
  if (autocomplete) {
    console.log('handlePlaceChanged')
    const place = autocomplete.getPlace();
    // Handle the selected place here
    console.log(place);
  }
};

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
