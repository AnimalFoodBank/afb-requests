<script setup lang="ts">
import type { FormError, FormSubmitEvent } from "#ui/types";

useSeoMeta({
  title: "Become a Volunteer",
});

const config = useRuntimeConfig();

const coolOffCTA = ref(false);

// https://evomark.co.uk/open-source-software/vue3-snackbar/
const snackbar = useSnackbar();


definePageMeta({
  layout: "onboarding",
  auth: false,
});

const branchLocations = ref([
  {
    name: "",
    value: "",
  },
  {
    name: "Xanadu Branch",
    value: "x",
  },
  {
    name: "Yale Branch",
    value: "y",
  },
  {
    name: "Zulu Branch",
    value: "z",
  },
]);

const fields = [
  {
    name: "name",
    type: "text",
    label: "Name",
    placeholder: "Can be your full name, your first name or a nickname",
    icon: "i-heroicons-user-circle",
    autofocus: true,
  },
  {
    name: "location",
    type: "select",
    search: true,
     native: false,
    inputType: "search",
    label: "Branch/Location",
    placeholder: "(Optional) Choose a branch",
    icon: "i-ph-map-pin-area",
    autocomplete: "disabled",
    items: '/json/branch-locations.json',
    required: false,
  },

  {
    name: "intro",
    type: "textarea",
    label: "Favourite animal",
    placeholder: "What is your favourite animal?",
    icon: "i-ph-pencil-circle-fill",
    autofocus: false,
  },
  {
    name: "email",
    type: "text",
    label: "Email",
    placeholder: "Enter your email",
    icon: "i-heroicons-envelope",
    autofocus: false,
  },
];

const validate = (state: any): FormError[] => {
  const errors = [];
  if (!state.name)
    errors.push({ path: "name", message: "Name is required" });

  if (!state.email)
      errors.push({ path: "email", message: "Email is required" });

  if (!state.intro)
      errors.push({ path: "intro", message: "Intro is required" });

  return errors;
};

let timeoutId: number | undefined;

onUnmounted(() => {
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
});

async function onSubmit(
  event: FormSubmitEvent<{
    email: string;
  }>,
) {
  console.log("Submitted", event);

  if (coolOffCTA.value) {
    snackbar.add({
      type: "warning",
      text: "If you haven't received an email, please wait a few minutes and try again.",
    });
    return;
  }

  // Prepare the payload
  const payload = {
    email: event.email,
  };
  console.log("Payload:", payload);

}

const schema = {
      size: 'md',
      displayErrors: false,
      schema: {
        page_title: {
          type: 'static',
          content: 'Create account',
          tag: 'h1',
        },
        divider: {
          type: 'static',
          tag: 'hr',
        },
        container: {
          type: 'group',
          schema: {
            first_name: {
              type: 'text',
              placeholder: 'First name',
              columns: {
                container: 6,
                label: 12,
                wrapper: 12,
              },
              fieldName: 'First name',
              rules: [
                'required',
                'max:255',
              ],
            },
            last_name: {
              type: 'text',
              placeholder: 'Last name',
              columns: {
                container: 6,
                label: 12,
                wrapper: 12,
              },
              fieldName: 'Last name',
              rules: [
                'required',
                'max:255',
              ],
            },
          },
          description: 'Make sure it matches your legal name',
        },
        birthday: {
          type: 'date',
          placeholder: 'Birthday',
          fieldName: 'Birthday',
          rules: [
            'required',
          ],
          description: 'Your birthday is not visible others.',
          displayFormat: 'MMMM Do, YYYY',
        },
        location: {
          type: 'select',
          search: true,
          native: false,
          inputType: 'search',
          autocomplete: 'disabled',
          placeholder: 'Branch/Location',
          items: '/json/branch_locations.json',
        },
        state: {
          type: 'select',
          search: true,
          native: false,
          inputType: 'search',
          autocomplete: 'disabled',
          placeholder: 'State',
          items: '/json/states.json',
          conditions: [
            [
              'country',
              'in',
              [
                'US',
              ],
            ],
          ],
        },
        phone: {
          type: 'text',
          inputType: 'tel',
          placeholder: 'Phone',
          rules: [
            'required',
          ],
          fieldName: 'Phone',
        },
        email: {
          type: 'text',
          inputType: 'email',
          rules: [
            'required',
            'max:255',
            'email',
          ],
          placeholder: 'Email',
          fieldName: 'Email',
          description: 'You will receive a confirmation letter to this email.',
        },
        password: {
          type: 'text',
          inputType: 'password',
          rules: [
            'required',
            'min:8',
            'same:password_confirmation',
          ],
          fieldName: 'Password',
          placeholder: 'Password',
        },
        password_confirmation: {
          type: 'text',
          inputType: 'password',
          rules: [
            'required',
          ],
          fieldName: 'Password confirmation',
          placeholder: 'Password again',
        },
        terms: {
          type: 'checkbox',
          text: 'I accept the Terms & Conditions & Privacy Policy',
        },
        marketing_emails: {
          type: 'checkbox',
          text: 'I want to recieve marketing emails',
        },
        divider_1: {
          type: 'static',
          tag: 'hr',
        },
        register: {
          type: 'button',
          submits: true,
          buttonLabel: 'Create account',
          full: true,
          size: 'lg',
        },
      },
    };

const defaultBranch = ref("none");
</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <NuxtSnackbar top left shadow :duration="10000" />
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <!-- https://ui.nuxt.com/pro/components/auth-form -->
    <UAuthForm
      :schema="schema"
      :fields="fields"
      :validate="validate"
      title="Become a Volunteer"
      description="Enter a few details to get started."
      align="top"
      icon="i-ph-hand-heart-fill"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
      :loading="false"
      @submit="onSubmit"
    >
      <template #description>
        Let's create an account for you to get started. We'll send you an email to confirm your account.

      </template>

      <template #footer>
        By signing in, you agree to our
        <NuxtLink to="/legal/terms" class="text-primary font-medium"
          >Terms of Service</NuxtLink
        >.
      </template>
    </UAuthForm>
  </UCard>
</template>
