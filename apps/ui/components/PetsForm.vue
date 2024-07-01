<template>
  <Vueform :state="state"
           :schema="schema"
           add-class="vf-profile-form"
           size="lg"
           display-errors
           display-success
           :endpoint="false"
           @submit="onSubmit"
           ref="form$" />
</template>

<script setup lang="ts">
// import type { PetFormState } from '@/types/forms/index';
import type { FormSubmitEvent } from "#ui/types";
import clientPetsSchema from '@/modules/requests/clientPetsSchema';
import type { PetInfo } from '@/types/index';

const toast = useToast()

const {
  profileInfo,
  userInfo,
  authToken,
} = useProfile();


const props = defineProps<{
  title?: String
  description?: String
  state?: Object
  cta?: Boolean
  icon?: String
  user?: Object
  profile?: Object
}>()

const schema = ref({})

const defaultPetExample: PetInfo = {
  id: "3ef6ef2a-fd22-4082-a096-8bc95efa5a75",
  pet_type: "Dog",
  pet_name: "Buddy",
  pet_dob: "2018",
  food_details: {
    allergies: "Chicken",
    general_notes: "Loves to play fetch",
    foodtype: "Dry"
  },
  dog_details: {
    size: "20-50 lbs (Medium)"
  },
  spay_or_neutered: "Yes"
};


function validate(state: any): FormError[] {
  const errors = []
  if (!state.pets) errors.push({ path: 'name', message: 'Please enter at least one pet.' })
  return errors
}


async function onSubmit(event: FormSubmitEvent<any>) {

try {
  // Prepare the data to be sent
  const profileData = {
    id: props.profile.id,
    user_id: props.user.id,
    pets: event.data.pets,
  }

  const petsPath = `/api/v1/pets/`

  // Make the API call
  const response = await $fetch(petsPath, {
    method: 'PUT',
    body: JSON.stringify(profileData),
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `${authToken.value}`
    }
  })

  // Handle successful response
  console.log('Profile updated:', response)

  toast.add({
    title: `${props.title} updated`,
    icon: 'i-heroicons-check-circle',
  })
} catch (error) {
  console.error('Error updating profile:', error)

  toast.add({
    title: 'Error updating profile',
    description: 'Please try again later.',
    icon: 'i-heroicons-exclamation-circle',
    color: 'red'
  })
}
}

onMounted(() => {
  // console.log("FoodRequestFormState has been mounted");

  const state = props.state;
  const profilePets = props.profile?.pets || [defaultPetExample];

  schema.value = {
    client_pets: clientPetsSchema(profilePets),
    save: {
      type: 'button',
      submits: true,
      buttonLabel: 'Update Pets',
      full: true,
      size: 'lg',
      loading: false,
      ui: {
        variant: 'secondary',
        icon: 'i-heroicons-check-circle',
      },
      onClick: (event: FormSubmitEvent<any>) => {
        //event.form.setLoading('save', true);
        //onSubmit(event);

      },
    },
  }

});
</script>

<style>
  .dark:vf-profile-form *,
  .dark:vf-profile-form *:before,
  .dark:vf-profile-form *:after,
  .dark:vf-profile-form:root {
    /**
        * Creating this namespace is enough to allow the existing
        * CSS variables to be used in the dark mode.
        **/
    --vf-bg-input: #ffffff;
  }

  .vf-profile-form *,
  .vf-profile-form *:before,
  .vf-profile-form *:after,
  .vf-profile-form:root {
    --vf-primary: #07bf9b;
    --vf-primary-darker: #06ac8b;
    --vf-color-on-primary: #ffffff;
    --vf-danger: #ef4444;
    --vf-danger-lighter: #fee2e2;
    --vf-success: #10b981;
    --vf-success-lighter: #d1fae5;
    --vf-gray-50: #f9fafb;
    --vf-gray-100: #f3f4f6;
    --vf-gray-200: #e5e7eb;
    --vf-gray-300: #d1d5db; /* Without this, the steps timeline is plain white and invisible in light mode.  */
    --vf-gray-400: #9ca3af;
    --vf-gray-500: #6b7280;
    --vf-gray-600: #4b5563;
    --vf-gray-700: #374151;
    --vf-gray-800: #1f2937;
    --vf-gray-900: #111827;
    --vf-dark-50: #efefef;
    --vf-dark-100: #dcdcdc;
    --vf-dark-200: #bdbdbd;
    --vf-dark-300: #a0a0a0;
    --vf-dark-400: #848484;
    --vf-dark-500: #737373;
    --vf-dark-600: #393939;
    --vf-dark-700: #323232;
    --vf-dark-800: #262626;
    --vf-dark-900: #191919;
    --vf-ring-width: 2px;
    --vf-ring-color: #07bf9b66;
    --vf-link-color: var(--vf-primary);
    --vf-link-decoration: inherit;
  }
</style>
