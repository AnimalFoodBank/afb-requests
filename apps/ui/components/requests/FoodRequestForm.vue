<template>
  <Vueform :steps="steps"
           :schema="schema"
           :endpoint="false"
           add-class="vf-request-form"
           size="lg"
           display-errors
           display-success
           @submit="submitFoodRequest"
           @mounted="addSummaryFunctionality"
           ref="form$" />
</template>


<script setup lang="ts">
import type { FoodRequestFormState } from '@/types/index';

/**
 * WARNING! ATTENTION! ACHTUNG! ATENCIÓN! 注意! ВНИМАНИЕ! توجه!
 *
 * Never define const state = ref() outside of <script setup> or setup() function.
 * Such state will be shared across all users visiting your website and
 * can lead to memory leaks!
 * Instead use const useX = () => useState('x')
 *
 *    -- https://nuxt.com/docs/getting-started/state-management#best-practices
 *
 **/

const props = defineProps<{
  // validate: (state: any) => { path: string; message: string }[];
  // onSubmit: (state: any) => void;
  state: FoodRequestFormState;
  googleMapsIsReady?: boolean;
  user?: any;
}>();

const form$ = ref<any>(null);

const {
  profileInfo,
  userInfo,
  authToken,
} = useProfile();

// Use the form's mounted event to add custom functionality to
// the confirmation step. This is where we can add a summary
// of the form data for the user to review before submitting.
//
// We need to do this at the time of mounting so that the
// entire form is rendered and available to us. We can then
// add a function to the confirmation step that dynamically
// updates the summary based on the form data that's been
// entered. This is a good way to keep the summary in sync
// with the form data.
const addSummaryFunctionality = (form$: any) => {
  console.log("Form mounted", 'form$');

  let summaryStep = form$.steps$.steps$.step4;

  summaryStep.on("activate", (form$: any) => {
    console.log("Summary step activated", form$);

    // TODO: Generate the summary based on the form data
    // and update the summary element in the form.
  });
};


const submitFoodRequest = async (form$: any, FormData: any) => {
  // Using form$.data will INCLUDE conditional elements and it
  // will submit the form as "Content-Type: application/json".
  // console.log("submitFoodRequest data", form$)
  const foodRequestFormData = form$.data

  // Using form$.requestData will EXCLUDE conditional elements and it
  // will submit the form as "Content-Type: application/json".
  const requestData = form$.requestData

  // Show loading spinner
  form$.submitting = true

  const userId = authData?.value?.id;

  const foodRequestAPIData = {
    // Match the API field names exactly
    user: userId,  // not user_id
    address_text: requestData.delivery_address.interactive_address,
    address_google_place_id: null,
    address_canadapost_id: null,
    address_latitude: null,
    address_longitude: null,
    contact_name: requestData.delivery_contact.contact_name,
    contact_email: requestData.delivery_contact.contact_email,
    contact_phone: requestData.delivery_contact.contact_phone,
    method_of_contact: requestData.delivery_contact.preferred_method,

    // Pass complete form data as-is, by step name. See requestData vs
    // form$.data above for the differences in terms of which fields
    // are included.
    branch_location: requestData.branch_locations,
    location: requestData.location,
    delivery_contact: requestData.delivery_contact,
    client_pets: requestData.client_pets,
    confirmation: requestData.confirmation,
    safe_drop: requestData.safe_drop,
  };

  const options = {
    headers: {
      'Authorization': authToken.value,
    },
  }
  return await form$.$vueform.services.axios.post('/api/v1/requests/',
    foodRequestAPIData, options
  )
};


/**
 * ***************************************************
 *  FORM STEPS
 * ***************************************************
 *
 * The steps object organizes the form schema across multiple
 * UI steps. Each step has its own set of elements and can
 * have custom labels, buttons, and event handlers.
 *
 **/
const steps = {

  step0: {
    label: "Address",
    elements: [
      "step0_title",
      "delivery_address",
    ],
    buttons: {
      previous: false,
    },
    labels: {
      next: "Next: Contact",
    },
    on: (form$: any, el: any) => {
      console.log("Step 0 on", form$, el);
    },
    conditions: [
      // ["step0.delivery_address", "in", ["CA"]]  // element disappears if doesn't pass
    ],
  },

  step1: {
    active: true,
    label: "Contact",
    elements: [
      "step1_title",
      "delivery_contact",
    ],
    labels: {
      previous: "← Back",
      next: "Next: Your Pets",
    },
    onActivate: (form$: any) => {
      console.log("Step 1 activated", form$);
    },
    onComplete: (form$: any) => {
      console.log("Step 1 completed", form$);
    },
    conditions: [
      // ["step0.delivery_address", "in", ["CA"]]  // element disappears if doesn't pass
    ],
  },

  step2: {
    label: "Pets",
    elements: [
      "step2_title",
      "client_pets",
    ],
    labels: {
      previous: "← Back",
      next: "Next: Safe Drop",
    },
  },

  step3: {
    label: "Safe Drop",
    elements: [
      "step3_title",
      "safe_drop",
    ],
    labels: {
      previous: "← Back",
      next: "Next: Confirmation",
    },
    onActivate: (form$: any) => {
      console.log("Step 1 activated", form$);
    },
    onComplete: (form$: any) => {
      console.log("Step 1 completed", form$);
    },
  },

  step4: {
    label: "Confirmation",
    elements: [
      "step4_title",
      "summary",
      "divider_2",
      "confirmation",
      "divider_1",
    ],
    buttons: {
      previous: true,
    },
    labels: {
      previous: "← Back",
      finish: "Submit Request",
    },
    onActivate: (form$: any) => {
      console.log("Step 4 onActivate", form$, this);
    },
  },
};

/**
 * ***************************************************
 *  VUEFORM SCHEMA
 * ***************************************************
 *
 * The vueform schema is a JSON object that defines the
 * structure of the form fields. It includes the elements that
 * make up the form, the order in which they appear, and
 * any additional configuration options.
 *
 * Unlike the steps object which is defined entirely start time
 * the schema object is defined only after this component has
 * been mounted. This is because the schema object is dependent
 * on the props that are passed to the component.
 *
 **/
const schema = ref<any>({})

// Define the schema for the client pets section of the form.
import clientPetsSchema from '@/modules/requests/clientPetsSchema';

onMounted(() => {
  // console.log("FoodRequestFormState has been mounted");

  const state = props.state;

  schema.value = {
    //
    // === STEP 0: Delivery Address ====
    //

    delivery_address: {
      type: "object",
      schema: {
        branch_locations: {
          type: "select",
          search: true,
          native: false,
          inputType: "search",
          autocomplete: "off",
          items: "/json/branch_locations.json",
          rules: [],  // it's for display only so not "required" when submitting the form
          label: "Your local branch",
          description: "Please contact admin@animalfoodbank.org to change your branch.",
          disabled: true,
          conditions: [
            ["delivery_address.country", "in", ["CA"]]  // element disappears if doesn't pass
          ],
          columns: {
            label: 12,
            container: 12,
            wrapper: 6,
          },
          default: state.delivery_address?.branch_location,
        },
        interactive_address: {
          type: "text",
          autocomplete: "one-time-code",
          placeholder: "e.g. 123 Yukon St. Vancouver, BC V5V 1V1",
          label: "Your address",
          description: "Please contact us if you need to change your address.",
          rules: ["required"],
          attrs: {
            autofocus: true,
          },
          columns: {
            label: 12,
            container: 12,
            wrapper: 6
          },
          floating: false,
          // Disable progressing to next step on "Enter" keypress. This
          // is a rudimentary to prevent the issue but it's not a proper
          // solution. There should be a way to handle this with either
          // Vueform or the google autocomplete library itself.
          onKeypress: (e: any) => {
            console.log("[interactive_address-debug]", e);
            if (e.key === "Enter") {
              e.preventDefault();
            }
          },
          default: state.delivery_address?.interactive_address, // || "1234 Southview Drive SE, Medicine Hat, AB, Canada",
        },
        building_type: {
          type: "radiogroup",
          view: "default",
          items: [
            "Apartment",
            "Townhouse",
            "Condo",
            "Laneway",
            "Detached house",
            "Other",
          ],
          rules: [],
          fieldName: "Building type",
          label: "Building type <i>(optional)</i>",
          columns: {
            container: 12,
            label: 12,
            wrapper: 8,
          },
          default: state.delivery_address?.building_type,
        },
        location: {
          type: "object",
        },
        country: {
          type: "hidden",
          hidden: true,
          default: "CA",
        },
      }
    },

    //
    // STEP 1 - Delivery Contact
    //
    delivery_contact: {
      type: "object",
      schema: {
        step1_intro: {
          type: "static",
          tag: "p",
          content: "Please provide a contact person for the delivery.",
        },
        choose_contact: {
          type: "checkbox",
          rules: [],
          text: "I am the contact person for this delivery.",
          default: true,
        },
        contact_name: {
          type: "text",
          rules: ["required", "max:32"],
          label: "Contact name",
          placeholder: "e.g. Jean",
          floating: false,
          disabled: true,
          columns: {
            container: 12,
            label: 12,
            wrapper: 3,
          },
          default: state.delivery_contact?.contact_name || "Delbo Baggins",
          conditions: [
            ['delivery_contact.choose_contact', true],
          ],
        },
        alt_contact_name: {
          type: "text",
          rules: ["required", "max:32"],
          label: "Contact name",
          placeholder: "e.g. Jean",
          floating: false,
          columns: {
            container: 12,
            label: 12,
            wrapper: 3,
          },
          conditions: [
            ['delivery_contact.choose_contact', false],
          ],
        },
        preferred_method: {
          type: "radiogroup",
          view: "tabs",
          items: ["Call", "Text", "Email"],
          rules: ["required"],
          description: "We do our best to accomodate your preferences whenever possible. Depending on volunteer availability, we may contact you via another method.",
          label: "Preferred method",
          default: state.delivery_contact?.preferred_method,
        },
        contact_email: {
          type: "text",
          rules: ["required", "email"],
          label: "Contact email",
          placeholder: "e.g. your email address",
          floating: false,
          disabled: true,
          columns: {
            container: 12,
            label: 12,
            wrapper: 6,
          },
          conditions: [
            ['delivery_contact.preferred_method', ['Email']],
            ['delivery_contact.choose_contact', true],
          ],
          default: state.delivery_contact?.contact_email || 'profile?.email',
        },
        alt_contact_email: {
          type: "text",
          rules: ["required", "email"],
          label: "Contact email",
          placeholder: "e.g. alternate email address",
          floating: false,
          columns: {
            container: 12,
            label: 12,
            wrapper: 6,
          },
          conditions: [
            ['delivery_contact.preferred_method', ['Email']],
            ['delivery_contact.choose_contact', false],
          ],
        },
        contact_phone: {
          type: "text",
          rules: ["required", "max:16"],
          label: "Contact phone",
          placeholder: "(123) 456-7890",
          floating: false,
          mask: "(000) 000-0000",
          disabled: true,
          columns: {
            container: 12,
            label: 12,
            wrapper: 6,
          },
          conditions: [
            ['delivery_contact.preferred_method', ['Call', 'Text']],
            ['delivery_contact.choose_contact', true],
          ],
          default: state.delivery_contact?.contact_phone || '123-456-7890',
        },
        alt_contact_phone: {
          type: "text",
          rules: ["max:16"],
          label: "Alternate phone number",
          placeholder: "e.g. phone number of a friend",
          floating: false,
          mask: "(000) 000-0000",
          description: "If you want to co-ordinate this delivery using a different phone number.",
          columns: {
            container: 12,
            label: 12,
            wrapper: 6,
          },
          conditions: [
            ['delivery_contact.preferred_method', ['Call', 'Text']],
            ['delivery_contact.choose_contact', false],
          ],
        },
      },
    },

    //
    // STEP 2 - Your Pets
    //
    client_pets: clientPetsSchema,

    //
    // STEP 3 - Safe Drop
    //
    safe_drop: {
      type: "object",
      schema: {
        policy: {
          type: "static",
          tag: "p",
          content:
            "Our Safe Drop policy allows our drivers to leave your order at your door, lobby, or another safe location. By checking the box below, you agree to the Safe Drop policy.",
        },
        confirm: {
          type: "checkbox",
          text: "<strong>I understand and agree to the Safe Drop policy.</strong>",
          fieldName: "Safe Drop Policy",
          rules: ["accepted"],
          default: state.safe_drop?.safe_drop,
        },
        instructions: {
          type: "textarea",
          rules: ["max:255"],
          label: "Safe Drop Instructions (optional)",
          placeholder: "e.g. Leave at the front door.",
          default: state.safe_drop?.safe_drop_instructions,
          columns: {
            container: 6,
            label: 12,
            wrapper: 12,
          },
        },
      },
    },

    //
    // STEP 4 - Confirmation
    //
    summary: {
      type: "object",
      schema:{
        summary: {
          type: "static",
          tag: "p",
          content: "Please review the information below and confirm that it is correct.",
        },
        location: {
          type: "static",
          tag: "p",
          columns: {
            container: 12,
            label: 6,
            wrapper: 6,
          },
          content: "<strong>Address:</strong> " + state.delivery_address?.interactive_address,
        },
        contact: {
          type: "static",
          tag: "p",
          columns: {
            container: 12,
            label: 6,
            wrapper: 6,
          },
          content: "<strong>Contact:</strong> " + state.delivery_contact?.contact_name + " (" + state.delivery_contact?.contact_phone + ")",
        },
        pets: {
          type: "static",
          tag: "p",
          columns: {
            container: 12,
            label: 6,
            wrapper: 6,
          },
          content: "<strong>Pets:</strong> ",
        },
        safe_drop: {
          type: "static",
          tag: "p",
          columns: {
            container: 12,
            label: 6,
            wrapper: 6,
          },
          content: "<strong>Safe Drop:</strong> " + (state.safe_drop?.safe_drop ? "Yes" : "No") + " - " + state.safe_drop?.safe_drop_instructions,
        },
      },
    },

    confirmation: {
      type: "object",
      schema: {
        confirm_info: {
          type: "checkbox",
          text: "I confirm that the information provided is correct.",
          fieldName: "Confirmation",
          rules: ["accepted"],
          default: state.confirmation?.confirm_correct,
        },
        accept_terms: {
          type: "checkbox",
          text: "I have read, accepted, and agreed to the Terms and Conditions and Privacy Notice.",
          fieldName: "Terms",
          rules: ["accepted"],
          default: state.confirmation?.accept_terms,
        },
      },
    },

    //
    // === SHARED ELEMENTS ===
    //
    divider: {
      type: "static",
      tag: "hr",
    },
    divider_1: {
      type: "static",
      tag: "hr",
      top: "1",
      bottom: "1",
    },
    divider_2: {
      type: "static",
      tag: "hr",
      top: "2",
      bottom: "2",
    },

    //
    // === STATIC ELEMENTS ===
    //
    step0_title: {
      type: "static",
      content: "Delivery Address",
      tag: "h3",
      top: "1",
    },
    step1_title: {
      type: "static",
      content: "Delivery Contact",
      tag: "h3",
      top: "1",
    },
    step2_title: {
      type: "static",
      content: "Your Pets",
      tag: "h3",
      top: 1,
    },
    step3_title: {
      type: "static",
      content: "Safe Drop",
      tag: "h3",
      top: 1,
    },
    step4_title: {
      type: "static",
      content: "Confirmation",
      tag: "h3",
      top: 2,
    },
  };


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
