<!--
  This is a Vue page for the magic login functionality.
  It uses the 'definePageMeta' function to set the page metadata.
-->
<script setup lang="ts">
import type { FormError } from '#ui/types';
import { useRoute } from 'vue-router';

const colorMode = useColorMode()
const isDark = computed({
  get () {
    return colorMode.value === 'dark'
  },
  set () {
    colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'
  }
})

const {
  status,
  data,
  token,
  lastRefreshedAt,
  getSession,
  signUp,
  signIn,
  signOut,
} = useAuth()

useSeoMeta({
  title: "Sign In",
})

const config = useRuntimeConfig();
const snackbar = useSnackbar();

definePageMeta({
  layout: 'onboarding',
  auth: false,
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
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Required' })
  if (!state.code) errors.push({ path: 'code', message: 'Required' })
  return errors
}

const fields = [
  {
    name: "email",
    type: "text",
    label: "Email",
    placeholder: "Your email address",
    icon: "i-heroicons-envelope",
  },
]

async function authHandler() {

  // Prepare the credentials expected by the DRF Passwordless view:
  // drfpasswordless.views.ObtainAuthTokenFromCallbackToken. Annoyingly
  // the code is referred to as 'token' here in the request payload.
  // The term "token" is used in the response payload to refer to
  // the widely-recognized Authentication/Bearer token that is used
  // to authenticate requests to the API.
  //
  const credentials = {
    email: state.email,
    token: state.code,
  }

  try {
    const response = await signIn(credentials, { callbackUrl: '/dashboard' })

  } catch (error) {
    console.error('An unhandled error occurred:', error);

    const toast = useToast()
    toast.add({
      title: 'Login Error',
      description: 'An error occurred on our end. Please try logging in again.',
    })

    return navigateTo('/login')
  }
}

</script>

<template>
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <img :src="isDark ? '/img/afb_icon_white.png' : '/img/afb_icon_black.png'" alt="Logo" class="mx-auto w-24 h-24 rounded-full" />

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
      @submit="authHandler"
    >
      <div class="w-full max-w-sm space-y-6">
        <h2 class="text-2xl text-gray-900 dark:text-white font-bold text-center">Complete Sign In</h2>
        <p class="text-gray-500 dark:text-gray-400 text-center">Don't have an account? <NuxtLink to="/login" class="text-primary font-medium">Sign up</NuxtLink>.</p>

        <UInput v-model="email" name="email" type="hidden" label="Email" required />
        <UInput v-model="code" name="code" type="text" color="primary" variant="outline" disabled placeholder="Code" label="Code" size="xl" class="w-32 mx-auto" required />

        <p class="text-sm text-gray-500 dark:text-gray-400 mt-2 text-center">
          By signing in, you agree to our
          <NuxtLink to="/legal/terms"
                    class="text-primary font-medium">Terms of Service</NuxtLink> and
          <NuxtLink to="/legal/privacy"
                    class="text-primary font-medium">Privacy Notice</NuxtLink>.
        </p>

        <UButton type="submit" class="focus:outline-none disabled:cursor-not-allowed disabled:opacity-75 flex-shrink-0 font-medium rounded-full text-sm gap-x-2 px-3 py-2 shadow-sm text-white dark:text-gray-900 bg-primary-500 hover:bg-primary-600 disabled:bg-primary-500 dark:bg-primary-400 dark:hover:bg-primary-500 dark:disabled:bg-primary-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-500 dark:focus-visible:outline-primary-400 w-full flex justify-center items-center">
          <span class="">Continue</span>
          <span class="i-heroicons-arrow-right-20-solid flex-shrink-0 h-5 w-5" aria-hidden="true"></span>
        </UButton>

      </div>
    </UForm>
  </UCard>
</template>
