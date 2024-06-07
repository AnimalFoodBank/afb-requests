<!--
  This is a Vue page for the login functionality.
  It uses the 'definePageMeta' function to set the page metadata.
  -->

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
    placeholder: "Your email address",
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

        // TODO
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
          navigateTo('/login/check')

        }
      },
      onResponseError({ request, response, options }) {
        // Handle the response errors
        console.error(
          "A response error occurred:",
          "Status code:",
          response.status,
          "Status message:",
          response._data,
        );

        // Check for a non field error and that the value has at least
        // one message.
        if (response._data?.non_field_errors && response._data.non_field_errors.length > 0) {
          snackbar.add({
            type: "info",
            text: "Please create an account.",
          });

          // Nuxt redirect to welcome/clients page, including the email address
          // in the query string.
          console.log('Directing to welcome/clients')
          navigateTo({
            path: '/welcome/clients',
            query: {
              email: event.email,
            }
          });


        } else {
          // Display error message
          snackbar.add({
            type: "error",
            text: "An error occurred. Please try again.",
          });
        }
        // debugger

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
               class=""
               :ui="{ base: 'text-center', footer: 'text-center' }"
               :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
               :loading="false"
               @submit="onSubmit">

      <template #description>
        <p class="text-sm italic mb-4">(Don't have an account? <NuxtLink to="/welcome/clients" class="text-secondary underline font-medium">Sign up</NuxtLink>)</p>

        <p>Enter the email address associated with your account and we'll send a magic link to your inbox.</p>
      </template>

      <template #validation>
        <p class="ui.validation">
          By signing in, you agree to our
          <NuxtLink to="/legal/terms"
                    class="text-secondary underline font-medium">Terms of Service</NuxtLink> and
          <NuxtLink to="/legal/privacy"
                    class="text-secondary underline font-medium">Privacy Notice</NuxtLink>.
        </p>
      </template>
    </UAuthForm>
  </UCard>
</template>
