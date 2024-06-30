<script setup lang="ts">
import { Loader } from "@googlemaps/js-api-loader";
import { defineProps, ref } from 'vue';

const config = useRuntimeConfig();

const {
  status,
  data: authData,
} = useAuth();

const {
  profileInfo,
  userInfo,
  authToken,
} = useProfile();

const googleAPIKey = config.public.googleAPIKey;
const googleMapsIsReady = ref(false)
const autocomplete = ref<google.maps.places.Autocomplete | null>(null);

const props = defineProps<{
  title?: string
  description?: string
  state?: object
  cta?: boolean
  icon?: string
}>()


const branches = ref([]);

const fetchBranches = async () => {
  const options = {
    headers: {
      'Authorization': authToken.value,
    },
    params: {
      show_hidden: false
    }
  }
  const response: Array<Branch> = await $fetch('/api/v1/branches/', options)
  branches.value = response.results;
}

const branchesMap = ref(new Map());

const parsedBranches = computed(() => {
  branchesMap.value.clear();
  return branches.value.map((branch: Branch) => {
    const parsedBranch = {
      label: branch.display_name,
      value: branch.id,
      latitude: branch.latitude,
      longitude: branch.longitude,
    };
    branchesMap.value.set(branch.id, parsedBranch);
    return parsedBranch;
  });
});


//const errors = ref<FormError[]>([])
const toast = useToast()

function validate (state: any): FormError[] {
  const errors = []
  if (!state.name) errors.push({ path: 'name', message: 'Please enter your name.' })
  if (!state.email) errors.push({ path: 'email', message: 'Please enter your email.' })
  if (!state.branch_selection) errors.push({ path: 'branch_selection', message: 'Please doublecheck branch location.' })
  return errors
}

async function onSubmit (event: FormSubmitEvent<any>) {
  // Do something with data
  console.log(event.data)

  toast.add({
    title: `${props.title} updated`,
    icon: 'i-heroicons-check-circle',
  })
}

const addressInput = ref(null);

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


  // Request needed libraries. Currently only Places API is used for selecting address.
  await Promise.all([
    google.maps.importLibrary("places"),
  ]);

  // Wait for the next DOM update cycle to ensure the input is rendered
  nextTick(() => {
    const input = addressInput?.value.$el.querySelector('input')

    if (input instanceof HTMLInputElement) {

      const mapOptions = {
        // Don't limit the scope further than the country. Unlike
        // the FoodRequestForm, we don't want to limit the scope
        // to a specific city area since the user may be in a
        // different city.
        componentRestrictions: { country: "ca" },
        fields: ["formatted_address", "geometry", "place_id", "plus_code"],
        strictBounds: true,
      };

      autocomplete.value = new google.maps.places.Autocomplete(input, mapOptions);
    } else {
      console.error('Input element not found')
    }

    googleMapsIsReady.value = true
  })
});



onMounted(() => {
  fetchBranches();

  const state = props.state;


    updateInputAddressCenterPoint(state.branch_selection)


  watch(() => autocomplete, (newValue, oldValue) => {
    console.log("Autocomplete ready", newValue);
    if (!newValue) {
      return;
    }

    newValue.addListener("place_changed", () => {
      const place = newValue.getPlace();

      state.address = place.formatted_address;

      const ext_address_details = {
        place: place,
      }
      state.ext_address_details = ext_address_details;

    });
  });

})

const updateInputAddressCenterPoint = (value: string) => {
  const branch = branchesMap.value.get(value);
  if (branch) {
    state.value.zip = branch.value;
    updateAutocomplete(branch.latitude, branch.longitude);
  }
}

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

</script>


<template>
    <div>
      <UForm :state="state" :validate="validate" :validate-on="['submit']" @submit="onSubmit" ref="form$">
        <UDashboardSection :title="title" :description="description" :icon="icon">
          <template #links v-if="cta">
            <UButton type="submit" label="Save changes" class="block rounded-md bg-primary text-white dark:text-white"/>
          </template>

          <UFormGroup
            name="branch"
            label="AFB Branch"
            description="The location that will fulfill your request."
            required
            class="grid grid-cols-2 gap-2"
            :ui="{ container: '' }"
          >

            <USelect
              v-model="state.branch_selection"
              name="branch_selection"
              :options="parsedBranches"
              placeholder="Select a branch"
              icon="i-ph-map-pin"
              size="md"
              @change="updateInputAddressCenterPoint"
            />

            <p class="text-gray-500 text-xs">
              <NuxtLink to="/requests/area/" class="text-secondary underline font-medium">See delivery area</NuxtLink>
            </p>
            <p class="text-gray-500 text-xs italic">Please contact admin@animalfoodbank.org to update your branch.</p>
          </UFormGroup>

          <UFormGroup
            name="name"
            label="Your Name"
            description="Please enter your name."
            required
            class="grid grid-cols-2 gap-2 items-center"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.name" autocomplete="off" icon="i-heroicons-user" size="md" name="name" />
          </UFormGroup>

          <UFormGroup
            name="email"
            label="Your Email"
            description="The email address you use to sign in. We also use this for co-ordinating food requests."
            class="grid grid-cols-2 gap-2 items-center"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.email" autocomplete="off" icon="i-heroicons-envelope" size="md" disabled />
          </UFormGroup>

          <UFormGroup
            name="name"
            label="Your Phone (optional)"
            description="Please enter your name."
            class="grid grid-cols-2 gap-2 items-center"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.phone_number" autocomplete="off" icon="i-heroicons-phone" size="md" name="phone_number" />
          </UFormGroup>

          <UFormGroup
            name="address"
            label="Address"
            description="The address for the pet food delivery."
            required
            class="grid grid-cols-2 gap-2"
            :ui="{ container: '' }"
          >

            <UInput v-model="state.ext_address_details" type="hidden" name="ext_address_details" />


            <UInput v-model="state.address" type="address" autocomplete="off" icon="i-heroicons-envelope" size="md" name="address" ref="addressInput">
              <template #trailing>
                <span class="text-gray-500 dark:text-gray-400 text-sm">{{ state.zip }}</span>
              </template>
            </UInput>
          </UFormGroup>

        </UDashboardSection>
      </UForm>

    </div>
  </template>
