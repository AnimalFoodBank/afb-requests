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

/**
 *
 *
 * const {Place} = await google.maps.importLibrary("places");
 *
 */

import { Loader } from "@googlemaps/js-api-loader";

const googleAPIKey = 'AIzaSyC_UvqrTnimc1Pc7LDYCqdqUiGMMUgMCWg'
const googleMapsIsReady = ref(false)

const state: Ref<FoodDeliveryFormState | null> = ref(null)

const loader = new Loader({
  apiKey: googleAPIKey,
  version: 'beta',
  libraries: ['places'],
});


loader.load().then(async () => {
    // const { Map } = await google.maps.importLibrary("maps") as google.maps.MapsLibrary;
    // const { Place } = await google.maps.importLibrary("places") as google.maps.PlacesLibrary;
    googleMapsIsReady.value = true

    // Request needed libraries. Currently only Places API is used for selecting address.
    await Promise.all([
      google.maps.importLibrary("places"),
    ]);

    const center = { lat: 50.064192, lng: -110.605469 };
    // Create a bounding box with sides ~20km away from the center point
    const bounds = new google.maps.LatLngBounds(center);
    const boundaryDistance = 0.2;
    const defaultBounds = {
      north: center.lat + 0.2,
      south: center.lat - 0.2,
      east: center.lng + 0.2,
      west: center.lng - 0.2,
    };
    const input = document.getElementById("location.interactive_address") as HTMLInputElement;
    const options = {
      location: center,
      bounds: defaultBounds,
      componentRestrictions: { country: "ca" },
      fields: ["formatted_address", "geometry", "place_id", "plus_code"], // address_components, place_id
      // This is an option for the Google Maps Places Autocomplete API
      // It sets whether the Autocomplete predictions should be strictly biased to the bounds set via the bounds option.
      strictBounds: true
    };

    const autocomplete = new google.maps.places.Autocomplete(input, options);

  });

onMounted(() => {
  console.log('requests/new.vue onMounted')

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
      interactive_address: '',
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


</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow>
      <UDashboardNavbar title="New Food Request" />

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto md:block lg:hidden">
        <UHorizontalNavigation :links="links" class="" />
      </UDashboardToolbar>

      <UDashboardPanelContent class="pb-12 pr-16 mr-16">

        <RequestsFoodDeliveryForm v-if="state" :state="state" :googleMapsIsReady="googleMapsIsReady" />

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>
