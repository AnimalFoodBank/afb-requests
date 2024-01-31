<script setup lang="ts">
const config = useRuntimeConfig();

definePageMeta({
  layout: 'auth'
})

useSeoMeta({
  title: 'Login'
})

const fields = [{
  name: 'email',
  type: 'text',
  label: 'Email',
  placeholder: 'Enter your email'
}, {
  name: 'password',
  label: 'Password',
  type: 'password',
  placeholder: 'Enter your password'
}]

const validate = (state: any) => {
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Email is required' })
  if (!state.password) errors.push({ path: 'password', message: 'Password is required' })
  return errors
}

const providers = [{
  label: 'Continue with Gmail',
  icon: 'i-simple-icons-gmail',
  color: 'white' as const,
  click: () => {
    console.log('Redirect to Google')
  }
},{
  label: 'Continue with Apple',
  icon: 'i-simple-icons-apple',
  color: 'white' as const,
  click: () => {
    console.log('Redirect to Apple')
  }
}]

async function onSubmit (formData: any) {
  console.log('Submitted', formData);

  // Prepare the payload
  const payload = {
    username: formData.email,
    password: formData.password
  }
  console.log('Payload:', payload)

  // Send post request to the API endpoint using Nuxt 3 useFetch
  const { data, pending, error, refresh } = useFetch('/auth-token/', {
    baseURL: config.public.apiBase,
    method: 'POST',
    body: JSON.stringify(payload),
    headers: {
      'Content-Type': 'application/json'
    },
    mode: 'cors',
    credentials: 'include',

  })

  if (error) {
    debugger
    console.error('An error occurred:', error)
    console.log(error)
    return
  }

  // The response should contain the token if the login was successful
  const token = data.token
  console.log('Token:', token)
}
</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <UAuthForm
      :fields="fields"
      :validate="validate"
      :providers="providers"
      title="Welcome back"
      align="top"
      icon="i-heroicons-lock-closed"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
      @submit="onSubmit"
    >
      <template #description>
        Don't have an account? <NuxtLink to="/signup" class="text-primary font-medium">Sign up</NuxtLink>.
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
