<template>
  <UDashboardPage>
    <UDashboardPanel grow>
      <UDashboardNavbar title="New Food Request" />

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto md:block lg:hidden">
        <UHorizontalNavigation :links="links"
                               class="" />
      </UDashboardToolbar>

      <UDashboardPanelContent class="pb-12 pr-16 mr-16">

        <RequestsFoodRequestForm v-if="state"
                                 :state="state"
                                 :googleMapsIsReady="googleMapsIsReady"
                                 :user="userInfo"
                                 :autocomplete="autocomplete"
                                 :updateAutocomplete="updateAutocomplete"
                                 :addressSelected="addressSelected" />

      </UDashboardPanelContent>

    </UDashboardPanel>
  </UDashboardPage>
</template>


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
  profileInfo,
  userInfo,
  authToken,
} = useProfile();

/**
 *
 *
 * const {Place} = await google.maps.importLibrary("places");
 *
 */

import { Loader } from "@googlemaps/js-api-loader";

const googleAPIKey = config.public.googleAPIKey;
const googleMapsIsReady = ref(false)
const autocomplete = ref<google.maps.places.Autocomplete | null>(null);

const state: Ref<FoodRequestFormState | null> = ref(null)

const loader = new Loader({
  apiKey: googleAPIKey,
  version: 'beta',
  libraries: ['places'],
});

// Get the currently select branch from branch_locations and
// extract the center lat lon to use as the default location.
const defaultCenter = { lat: 50.064192, lng: -110.605469 };

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
  const center = defaultCenter;
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

  autocomplete.value = new google.maps.places.Autocomplete(input, mapOptions);

});

const addressSelected = ref(false);
const updateAutocomplete = (latitude: number, longitude: number) => {
  if (autocomplete.value) {
    const center = new google.maps.LatLng(latitude, longitude);
    const bounds = new google.maps.LatLngBounds(center);
    const boundaryDistance = 0.2;
    const newBounds = {
      north: center.lat() + boundaryDistance,
      south: center.lat() - boundaryDistance,
      east: center.lng() + boundaryDistance,
      west: center.lng() - boundaryDistance,
    };

    autocomplete.value.setBounds(newBounds);
    autocomplete.value.setOptions({
      strictBounds: true,
      location: center,
    });


  }
};

onMounted(() => {
  console.log('requests/new.vue onMounted')
  state.value = {} as FoodRequestFormState;
});

</script>
