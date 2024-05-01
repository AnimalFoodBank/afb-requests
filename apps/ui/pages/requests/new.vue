<script setup lang="ts">
import type { FoodRequestFormState } from '@/types/index';

const config = useRuntimeConfig();

useHead({
  title: 'New Food Request',
})

definePageMeta({
  layout: 'dashboard',
})

const links = [[
  {
    label: 'New Request',
    icon: 'i-ph-plus-square-light',
    to: '/requests/new',
  },
  {
    label: 'Request History',
    icon: 'i-heroicons-calendar',
    to: '/requests',
    exact: true
  },
]]

const {
  status,
  data: authData,
} = useAuth();

/**
 *
 *
 * const {Place} = await google.maps.importLibrary("places");
 *
 */

import { Loader } from "@googlemaps/js-api-loader";

const googleAPIKey = config.public.googleAPIKey;
const googleMapsIsReady = ref(false)

const state: Ref<FoodRequestFormState | null> = ref(null)

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

  const input = document.getElementById("delivery_address.interactive_address") as HTMLInputElement;


// Create a bounding box with sides ~20km away from the center point
const center = { lat: 50.064192, lng: -110.605469 };
const bounds = new google.maps.LatLngBounds(center);
const boundaryDistance = 0.2;
const defaultBounds = {
  north: center.lat + 0.2,
  south: center.lat - 0.2,
  east: center.lng + 0.2,
  west: center.lng - 0.2,
};

const mapOptions = {
      location: center,
      bounds: defaultBounds,
      componentRestrictions: { country: "ca" },
      fields: ["formatted_address", "geometry", "place_id", "plus_code"], // address_components, place_id
      // This is an option for the Google Maps Places Autocomplete API
      // It sets whether the Autocomplete predictions should be strictly biased to the bounds set via the bounds option.
      strictBounds: true,
    };

  const autocomplete = new google.maps.places.Autocomplete(input, mapOptions);

});

onMounted(() => {
  console.log('requests/new.vue onMounted')

  state.value = {
    id: '8d3a9c7-4b93-44f1-bf6a-f5b0a2e2c54',
    user_id: '76f7f43-dfca-41ae-a5ee-cdb1d7e8af9',
    delivery_address: {
      branch_location: 'Medicine Hat',
      location: {
        address_line1: 'Addr line 1',
        city: 'Slurpee',
        prov_or_state: 'BC',
        postcode: 'M4C 1B5',
      },
      country: 'CA',
      interactive_address: '1201 Kingsway, Med Hat',
      building_type: 'Townhouse',
    },
    delivery_contact: {
      contact_name: 'Delbo Baggins',
      contact_email: 'delbo@afb.pet',
      contact_phone: '250-777-2171',
      preferred_method: "Any",
    },
    client_pets: {
      pets: [
        {
          pet_type: 'Dog',
          pet_name: 'Bella',
          pet_dob: '5',
          food_details: {
            usual_brands: 'Purina',
            foodtype: 'dry',
          },
          dog_details: {
            size: '10',
          }
        },
      ],
    },
    safe_drop: {
      safe_drop: true,
      safe_drop_instructions: 'Leave at the door',
    },
    confirmation: {
      confirm_correct: true,
      accept_terms: true,
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

        <RequestsFoodRequestForm v-if="state" :state="state" :googleMapsIsReady="googleMapsIsReady" :user="authData" />

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>
