<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types';
import { useRoute } from 'vue-router';

const config = useRuntimeConfig();
const snackbar = useSnackbar();

definePageMeta({
  layout: 'auth',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/protected',
  },
  // colorMode: 'dark',
})

const route = useRoute()
const email = route.query.email as string
const code = route.query.code as string

const state = reactive({
  email,
  code,
})

// re: issues with autopopulating values and Chrome not updating the DOM
// see: https://github.com/vuejs/vue/issues/7058#issuecomment-1366489524
const validate = (state: any): FormError[] => {
  console.log('statevalidate', state)
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Required' })
  if (!state.code) errors.push({ path: 'code', message: 'Required' })
  return errors
}

async function onSubmit(event: FormSubmitEvent<{ email: string }>) {
  console.log('Submitted', event);

  // Prepare the payload
  const payload = {
    email: state.email,
    token: state.code,
  }
  console.log('Payload:', payload)

  try {
    // Send post request to the API endpoint using Nuxt 3 useFetch
    const path = '/api/passwordless/auth/token/'
    const { data, pending, error, refresh } = await useFetch(path, {
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
        console.log('Response:', response)
        const data = response._data

        // After a successful response the next step is for the
        // user to be directed to their dashboard.
        if (response.ok) {
          const message = 'Your now signed in. Redirecting to your dashboard.'
          console.log('Message:', message)

          // Save the bearer token to local storage
          const token = response.headers.get('Authorization')
          if (token) {
            window.localStorage.setItem('auth._token.local', token)
          }

          navigateTo('/dashboard')


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

<template>
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <img src="/img/afb_icon_black.png" alt="Logo" class="mx-auto w-24 h-24 rounded-full" />

    <!-- https://ui.nuxt.com/components/form -->
    <!-- https://ui.nuxt.com/pro/components/auth-form -->
    <!-- UForm implementation is a workaround for UAuthForm autopopulate+validation issue. -->
    <UForm
      :validate="validate"
      :state="state"
      title="Sign in to AFB Requests"
      description="Click 'Sign in' to complete process."
      align="top"
      icon="i-heroicons-lock-closed"
      @submit="onSubmit"
    >
      <div class="w-full max-w-sm space-y-6">
        <h2 class="text-2xl text-gray-900 dark:text-white font-bold text-center">Sign in to AFB Requests</h2>
        <p class="text-gray-500 dark:text-gray-400 mt-1 text-center">Don't have an account? <NuxtLink to="/login" class="text-primary font-medium">Sign up</NuxtLink>.</p>

        <UInput v-model="email" name="email" type="hidden" label="Email" required />
        <UInput v-model="code" name="code" type="hidden" label="Code" required />

        <UButton type="submit" class="focus:outline-none disabled:cursor-not-allowed disabled:opacity-75 flex-shrink-0 font-medium rounded-full text-sm gap-x-2 px-3 py-2 shadow-sm text-white dark:text-gray-900 bg-primary-500 hover:bg-primary-600 disabled:bg-primary-500 dark:bg-primary-400 dark:hover:bg-primary-500 dark:disabled:bg-primary-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-500 dark:focus-visible:outline-primary-400 w-full flex justify-center items-center">
          <span class="">Continue</span>
          <span class="i-heroicons-arrow-right-20-solid flex-shrink-0 h-5 w-5" aria-hidden="true"></span>
        </UButton>

        <p class="text-sm text-gray-500 dark:text-gray-400 mt-2 text-center">
          By signing in, you agree to our <NuxtLink to="/" class="text-primary font-medium">Terms of Service</NuxtLink>.
        </p>
      </div>
    </UForm>
  </UCard>
</template>
