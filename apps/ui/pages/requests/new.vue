<script setup lang="ts">
import type { FoodDeliveryFormState } from '@/types/index';

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: true,
  },
})

const links = [[
  {
    label: 'Request History',
    icon: 'i-heroicons-calendar',
    to: '/requests',
    exact: true
  },
  {
    label: 'New Request',
    icon: 'i-ph-plus-square-light',
    to: '/requests/new',
  }
]]

const googleAPIKey = 'AIzaSyC_UvqrTnimc1Pc7LDYCqdqUiGMMUgMCWg'
const autocompleteInput = ref<HTMLInputElement | null>(null);

const state: Ref<FoodDeliveryFormState | null> = ref(null)
let autocomplete: google.maps.places.Autocomplete | null = null;
const googleMapsIsReady = ref(false)

import { Loader } from "@googlemaps/js-api-loader";

const centerV = { lat: 49.282, lng: -123.12 };
const centerMH = { lat: 50.04, lng: -110.667, zoom: 12};
// const center = centerMH;

const loader = new Loader({
  apiKey: googleAPIKey,
  version: 'weekly',
  libraries: ['places'],
});

const apiPromise = loader.load();


onMounted(() => {
  console.log('requests/new.vue onMounted')

  // const loader = new Loader({
  //   apiKey: googleAPIKey,
  //   version: 'weekly',
  //   libraries: ['places'],
  // });

  if (window.google) {
    console.log('requests/new.vue onMounted - window.google exists')
    googleMapsIsReady.value = true;
  } else {
    console.log('requests/new.vue onMounted - window.google does not exist')
    loader.load().then(() => {
      initAutocomplete();
      googleMapsIsReady.value = true;
    });
  }


  state.value = {
    delivery_address: {
      branch_location: 'Medicine Hat',
      location: {
        address_line1: 'Addr line 1',
        city: 'Cccityy',
        divisions_level1: 'BC',
        postcode: 'M4C 1B5',
        country: 'CA',
      },
      // provider_location: '',
      building_type: 'Townhouse',
    },
    delivery_contact: {
      contact_number: '250-777-2171',
      contact_name: 'Pearl',
      preferred_method: "Email",
    },
    your_pets: {
      pet_name: 'Buddy',
      pet_breed: 'Labrador Retriever',
      pet_age: '3 years',
      pet_weight: '50 lbs',
    },
    safe_drop: {
      safe_drop: true,
      safe_drop_instructions: 'Leave at the door',
    },
    confirmation: {
      confirm_correct: false,
      accept_terms: false,
    },
  }

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

</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow>
      <UDashboardNavbar title="New Food Request" />

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto md:block lg:hidden">
        <UHorizontalNavigation :links="links" class="" />
      </UDashboardToolbar>

      <UDashboardPanelContent class="pb-12 pr-16 mr-16">

        <RequestsFoodDeliveryForm v-if="state" :state="state" />

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>
