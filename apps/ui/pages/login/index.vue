<script setup lang="ts">
import { navigateTo } from '#app';
import type { FormError, FormSubmitEvent } from "#ui/types";

useSeoMeta({
  title: "Sign In",
});

const config = useRuntimeConfig();

const coolOffCTA = ref(false);

// https://evomark.co.uk/open-source-software/vue3-snackbar/
const snackbar = useSnackbar();

// Auth
//
// Note: You cannot use local protection when you turned on the global
// middleware by setting globalAppMiddleware: true in the nuxt-auth
// configuration. You will get an error along the lines of "Error: Unknown
// route middleware: 'auth'". This is because the auth middleware is then
// added globally and not available to use as a local, page-specific
// middleware.

definePageMeta({
  layout: "onboarding",
  auth: false,
});

const fields = [
  {
    name: "email",
    type: "text",
    label: "Email",
    placeholder: "Enter your email",
    icon: "i-heroicons-envelope",
    autofocus: true,
  },
];


const validateEmail = (email: string) => {
  return (/^\w+([\.-\\+]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
}

const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Email is required' })
  if (!validateEmail(state.email)) {
    errors.push({ path: 'email', message: 'Please enter a valid email address' })
  }

  return errors
}

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

  try {
    // Send post request to the API endpoint using Nuxt 3 useFetch
    const path = "/api/v1/passwordless/auth/email/";
    const { data, pending, error, refresh } = await useFetch(path, {
      onRequest({ request, options }) {
        console.log("Request:", request);
        // Set the request headers
        options.headers = options.headers || {};

        // Addresses the following TypeScript error:
        //   Element implicitly has an 'any' type because expression of type '"Content-Type"' can't be used to index type 'HeadersInit'.
        //
        // TODO: Find a better way.
        (options.headers as { [key: string]: any })["AFB"] = "rules";
      },
      onRequestError({ request, options, error }) {
        // Handle the request errors
        console.error("A request error occurred:", error);
      },
      onResponse({ request, response, options }) {
        const data = response._data;
        console.log("Response data:", data);
        // Process the response data

        // A successful response returns a friendly message for the
        // user. The next step is for the user to check their email
        // for the magic link to sign in.
        if (response.ok) {
          // Ignore data.detail bc it's not a friendly message
          // and comes straight from drfpasswordless.
          const message = "Check your email for a link to log in.";
          console.log("Message:", message);

          snackbar.add({
            type: "success",
            text: message,
          });

          coolOffCTA.value = true;
          setTimeout(() => {
            coolOffCTA.value = false;
          }, 10000); // TODO: Increase to?

          // Redirect after successful form submission
          navigateTo('/login/almost')

        } else {
          // Handle the response errors
          console.error(
            "A response error occurred:",
            "Status code:",
            response.status,
            "Status message:",
            data.detail,
          );

          snackbar.add({
            type: "error",
            text: "An error occurred. Please try again.",
          });
        }
      },
      onResponseError({ request, response, options }) {
        // Handle the response errors
        console.error(
          "A response error occurred:",
          "Status code:",
          response.status,
          "Status message:",
          response._data.detail,
        );
      },
      baseURL: config.public.apiBase,
      method: "POST",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
      },
      mode: "cors",
    });
  } catch (error) {
    console.error("An unhandled error occurred:", error);
  }


}

const branchLocations = [
  {
    name: "",
    value: "",
    // coolOffCTA: true
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
];

const defaultBranch = ref("none");
</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <NuxtSnackbar top
                left
                shadow
                :duration="10000" />
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">

    <UAuthForm :fields="fields"
               :validate="validate"
               title="Sign in"
               description="Enter your email to access your account."
               align="top"
               icon="i-ph-paw-print-fill"
               :ui="{ base: 'text-center', footer: 'text-center' }"
               :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
               :loading="false"
               @submit="onSubmit">
      <template #description>
        We'll send a magic link to complete your sign in.
      </template>

      <template #footer>
        By signing in, you agree to our
        <NuxtLink to="/legal/terms"
                  class="text-primary font-medium">Terms of Service</NuxtLink>.
      </template>
    </UAuthForm>
  </UCard>
</template>
