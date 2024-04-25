<template>
  <Vueform :state="state"
           :schema="schema"
           add-class="vf-request-form"
           size="lg"
           display-errors
           display-success
           ref="form$" />
</template>

<script setup lang="ts">
// import type { PetFormState } from '@/types/forms/index';
import clientPetsSchema from '@/modules/requests/clientPetsSchema';

const props = defineProps<{
  title?: String
  description?: String
  state?: Object
  cta?: Boolean
}>()


const toast = useToast()


const schema = ref({})
onMounted(() => {
  // console.log("FoodRequestFormState has been mounted");

  const state = props.state;

  schema.value = {
    client_pets: clientPetsSchema,
  }

});
</script>

<style>
  .dark:vf-request-form *,
  .dark:vf-request-form *:before,
  .dark:vf-request-form *:after,
  .dark:vf-request-form:root {
    /**
        * Creating this namespace is enough to allow the existing
        * CSS variables to be used in the dark mode.
        **/
    --vf-bg-input: #ffffff;
  }

  .vf-request-form *,
  .vf-request-form *:before,
  .vf-request-form *:after,
  .vf-request-form:root {
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
