<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types';

const config = useRuntimeConfig();

const disabled = ref(false);

// https://evomark.co.uk/open-source-software/vue3-snackbar/
const snackbar = useSnackbar();

definePageMeta({
  layout: 'auth',
  auth: {
    unauthenticatedOnly: false,
  },
  // colorMode: 'dark',
})

useSeoMeta({
  title: 'Login'
})

const fields = [{
  name: 'email',
  type: 'text',
  label: 'Email',
  placeholder: 'Enter your email',
}]

const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Email is required' })
  return errors
}

const providers = [
  {
    label: 'Continue with Google',
    icon: 'i-simple-icons-google',
    color: 'white' as const,
    click: () => {
      console.log('Redirect to Google')
    }
  },
  {
    label: 'Continue with Facebook',
    icon: 'i-simple-icons-facebook',
    color: 'white' as const,
    click: () => {
      console.log('Redirect to Facebook')
    }
  },
  {
    label: 'Continue with Apple',
    icon: 'i-simple-icons-apple',
    color: 'white' as const,
    click: () => {
      console.log('Redirect to Apple')
    }
  },
]

let timeoutId: number | undefined


onUnmounted(() => {
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
});

async function onSubmit (event: FormSubmitEvent<{ email: string }>) {
  console.log('Submitted', event);

  if (disabled.value) {
    snackbar.add({
      type: 'warning',
      text: "If you haven't received an email, please wait a few minutes and try again.",
    })
    return;
  } else {
    disabled.value = true;
    setTimeout(() => {
      disabled.value = false;
    }, 60000);

  }


  // Prepare the payload
  const payload = {
    email: event.email,
  }
  console.log('Payload:', payload)

  try {
    // Send post request to the API endpoint using Nuxt 3 useFetch
    const path = '/api/passwordless/auth/email/'
    await $fetch(path, {
      onRequest({ request, options }) {
        console.log('Request:', request)
        // Set the request headers
        options.headers = options.headers || {}
        // options.headers = options.headers || { any: '' }
        options.headers['AFB'] = 'rules'
        options.headers['Content-Type'] = 'application/json'

      },
      onRequestError({ request, options, error }) {
        // Handle the request errors
        console.error('A request error occurred:', error)
      },
      onResponse({ request, response, options }) {
        const data = response._data
        console.log('Response data:', data)
        // Process the response data

        // A successful response returns a friendly message for the
        // user. The next step is for the user to check their email
        // for the magic link to sign in.
        if (response.ok) {
          // Ignore data.detail bc it's not a friendly message
          // and comes straight from drfpasswordless.
          const message = 'Check your email for a link to log in.'
          console.log('Message:', message)

          snackbar.add({
            type: 'success',
            text: message,
          })
        } else {
          // Handle the response errors
          console.error('A response error occurred:', error)

          snackbar.add({
            type: 'error',
            text: 'An error occurred. Please try again.',
          })
        }

      },
      onResponseError({ request, response, options }) {
        // Handle the response errors
        console.error('A response error occurred:', error)
      },
      baseURL: config.public.apiBase,
      method: 'POST',
      body: JSON.stringify(payload),
      headers: {
        'Content-Type': 'application/json'
      },
      mode: 'cors',

    })

  } catch (error) {
    console.error('An unhandled error occurred:', error)
  }

}

</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <NuxtSnackbar top left shadow :duration="10000" />
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <!-- https://ui.nuxt.com/pro/components/auth-form -->
    <UAuthForm
        :fields="fields"
        :validate="validate"
        :providers="providers"
        title="Sign in to AFB Requests"
        description="Enter your email to access your account."
        align="top"
        icon="i-heroicons-lock-closed"
        :ui="{ base: 'text-center', footer: 'text-center' }"
        :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
        :loading="false"
        @submit="onSubmit"
      >

      <template #description>
        Submit the form to get a magic link sent to your email.
      </template>

      <template #footer>
        By signing in, you agree to our <NuxtLink to="/" class="text-primary font-medium">Terms of Service</NuxtLink>.
      </template>
    </UAuthForm>

  </UCard>
</template>
