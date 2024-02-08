<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types';

const config = useRuntimeConfig();

// https://evomark.co.uk/open-source-software/vue3-snackbar/
const snackbar = useSnackbar();

definePageMeta({
  layout: 'auth',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/protected',
  },
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

async function onSubmit (event: FormSubmitEvent<any>) {
  console.log('Submitted', event);

  // Prepare the payload
  const payload = {
    email: event.email
  }
  console.log('Payload:', payload)

  // Send post request to the API endpoint using Nuxt 3 useFetch
  //
  // data - RefImpl, the response data. The value is null until
  //    the request is successful. “RefImpl is commonly a reference
  //    implementation used by Vue.js.”
  // pending - boolean, true if the request is still pending
  // error - ObjectRefImpl, when error.value is called, returns the error
  //    object or null. When null, the request was successful.
  // refresh - function, to manually trigger a new request.
  //
  // https://medium.com/@enestalayy/data-fetching-with-nuxt-3-ede89fb0509f
  //
  const path = '/api/passwordless/auth/email/'
  const { data, pending, error, refresh } = useFetch(path, {
    baseURL: config.public.apiBase,
    method: 'POST',
    body: JSON.stringify(payload),
    headers: {
      'Content-Type': 'application/json'
    },
    mode: 'cors',
  })

  // ObjectRefImpl is implemented by the Vue.js reactivity system.
  // https://github.com/vuejs/core/blob/75e02b5099a0/packages/reactivity/src/ref.ts#L357
  if (error.value) {
    console.error('An error occurred:', error.value)
    return
  }

  // A successful repsonse returns a friendly message for the
  // user. The next step is for the user to check their email
  // for the magic link to sign in.
  if (await data.value) {
    const message = data.value.detail
    console.log('Message:', message)

    snackbar.add({
        type: 'success',
        text: message,
    })
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
