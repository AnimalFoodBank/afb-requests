<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types';
import { useRoute } from 'vue-router';

definePageMeta({
  layout: 'auth',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/protected',
  },
})


const route = useRoute()
// Create a computed property that returns the route parameter
const routeParam = computed(() => route.query.email)

const state = {
  email: route.query.email as string,
  code: route.query.code as string,
}
console.log('state', state)

const fields = [{
  name: 'email',
  type: 'text',
  value: state.email,
  label: 'Email',
}, {
  name: 'code',
  type: 'text',
  value: state.code,
  label: 'Code',
}]

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

const validate = (state: any): FormError[] => {
  console.log('statevalidate', state)
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Required' })
  if (!state.code) errors.push({ path: 'code', message: 'Required' })
  return errors
}

async function onSubmit (event: FormSubmitEvent<any>) {
  // Do something with data
  console.log("event", event)
}
</script>

<template>
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <img src="/img/afb_icon_black.png" alt="Logo" class="mx-auto w-24 h-24 rounded-full" />

    <!-- https://ui.nuxt.com/components/form -->
    <!-- https://ui.nuxt.com/pro/components/auth-form -->
    <UAuthForm
      :fields="fields"
      :validate="validate"
      :providers="providers"
      :state="state"
      title="Sign in to AFB Requests"
      description="Click 'Sign in' to complete process."
      align="top"
      icon="i-heroicons-lock-closed"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
      :loading="false"
      @submit="onSubmit"
    >
      <template #description>
        Don't have an account? <NuxtLink to="/login" class="text-primary font-medium">Sign up</NuxtLink>.
      </template>

      <template #password-hint>
        <NuxtLink to="/" class="text-primary font-medium">Forgot password?</NuxtLink>
      </template>

      <template #footer>
        By signing in, you agree to our <NuxtLink to="/" class="text-primary font-medium">Terms of Service</NuxtLink>.
      </template>

    </UAuthForm>
  </UCard>
</template>
